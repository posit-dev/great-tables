// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import { NotebookApp } from '@jupyter-notebook/application';

// The webpack public path needs to be set before loading the CSS assets.
import { PageConfig } from '@jupyterlab/coreutils';

import { PluginRegistry } from '@lumino/coreutils';

import './style.js';

// custom list of disabled plugins
const disabled = [
  "@jupyterlab/application-extension:dirty",
  "@jupyterlab/application-extension:info",
  "@jupyterlab/application-extension:layout",
  "@jupyterlab/application-extension:logo",
  "@jupyterlab/application-extension:main",
  "@jupyterlab/application-extension:move-widget",
  "@jupyterlab/application-extension:notfound",
  "@jupyterlab/application-extension:paths",
  "@jupyterlab/application-extension:property-inspector",
  "@jupyterlab/application-extension:shell",
  "@jupyterlab/application-extension:status",
  "@jupyterlab/application-extension:tree-resolver",
  "@jupyterlab/apputils-extension:announcements",
  "@jupyterlab/apputils-extension:kernel-status",
  "@jupyterlab/apputils-extension:palette-restorer",
  "@jupyterlab/apputils-extension:print",
  "@jupyterlab/apputils-extension:resolver",
  "@jupyterlab/apputils-extension:running-sessions-status",
  "@jupyterlab/apputils-extension:splash",
  "@jupyterlab/apputils-extension:workspaces",
  "@jupyterlab/console-extension:kernel-status",
  "@jupyterlab/docmanager-extension:download",
  "@jupyterlab/docmanager-extension:opener",
  "@jupyterlab/docmanager-extension:path-status",
  "@jupyterlab/docmanager-extension:saving-status",
  "@jupyterlab/documentsearch-extension:labShellWidgetListener",
  "@jupyterlab/filebrowser-extension:browser",
  "@jupyterlab/filebrowser-extension:download",
  "@jupyterlab/filebrowser-extension:file-upload-status",
  "@jupyterlab/filebrowser-extension:open-with",
  "@jupyterlab/filebrowser-extension:share-file",
  "@jupyterlab/filebrowser-extension:widget",
  "@jupyterlab/fileeditor-extension:editor-syntax-status",
  "@jupyterlab/fileeditor-extension:language-server",
  "@jupyterlab/fileeditor-extension:search",
  "@jupyterlab/help-extension:about",
  "@jupyterlab/help-extension:open",
  "@jupyterlab/lsp-extension:plugin",
  "@jupyterlab/notebook-extension:execution-indicator",
  "@jupyterlab/notebook-extension:kernel-status",
  "@jupyterlab/services-extension:config-section-manager",
  "@jupyterlab/services-extension:connection-status",
  "@jupyterlab/services-extension:default-drive",
  "@jupyterlab/services-extension:event-manager",
  "@jupyterlab/services-extension:kernel-manager",
  "@jupyterlab/services-extension:kernel-spec-manager",
  "@jupyterlab/services-extension:nbconvert-manager",
  "@jupyterlab/services-extension:session-manager",
  "@jupyterlab/services-extension:setting-manager",
  "@jupyterlab/services-extension:user-manager",
  "@jupyterlab/services-extension:workspace-manager",
  "@jupyter-notebook/application-extension:logo",
  "@jupyter-notebook/application-extension:opener",
  "@jupyter-notebook/application-extension:path-opener",
  "@jupyter-notebook/help-extension:about",
];

async function createModule(scope, module) {
  try {
    const factory = await window._JUPYTERLAB[scope].get(module);
    const instance = factory();
    instance.__scope__ = scope;
    return instance;
  } catch (e) {
    console.warn(`Failed to create module: package: ${scope}; module: ${module}`);
    throw e;
  }
}

/**
 * The main entry point for the application.
 */
export async function main() {
  const allPlugins = [];
  const pluginsToRegister = [];
  const federatedExtensionPromises = [];
  const federatedMimeExtensionPromises = [];
  const federatedStylePromises = [];

  // This is all the data needed to load and activate plugins. This should be
  // gathered by the server and put onto the initial page template.
  const extensions = JSON.parse(
    PageConfig.getOption('federated_extensions')
  );

  // The set of federated extension names.
  const federatedExtensionNames = new Set();

  extensions.forEach(data => {
    if (data.extension) {
      federatedExtensionNames.add(data.name);
      federatedExtensionPromises.push(createModule(data.name, data.extension));
    }
    if (data.mimeExtension) {
      federatedExtensionNames.add(data.name);
      federatedMimeExtensionPromises.push(createModule(data.name, data.mimeExtension));
    }
    if (data.style) {
      federatedStylePromises.push(createModule(data.name, data.style));
    }
  });

  /**
   * Iterate over active plugins in an extension.
   */
  function* activePlugins(extension) {
    // Handle commonjs or es2015 modules
    let exports;
    if (extension.hasOwnProperty('__esModule')) {
      exports = extension.default;
    } else {
      // CommonJS exports.
      exports = extension;
    }

    let plugins = Array.isArray(exports) ? exports : [exports];
    for (let plugin of plugins) {
      if (
        PageConfig.Extension.isDisabled(plugin.id) ||
        disabled.includes(plugin.id) ||
        disabled.includes(plugin.id.split(':')[0])
      ) {
        continue;
      }
      allPlugins.push({
        ...plugin,
        extension: extension.__scope__
      });
      yield plugin;
    }
  }

  // Handle the mime extensions.
  const mimeExtensions = [];
  if (!federatedExtensionNames.has('@jupyterlab/javascript-extension')) {
    try {
      let ext = require('@jupyterlab/javascript-extension');
      ext.__scope__ = '@jupyterlab/javascript-extension';
      for (let plugin of activePlugins(ext)) {
        mimeExtensions.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/json-extension')) {
    try {
      let ext = require('@jupyterlab/json-extension');
      ext.__scope__ = '@jupyterlab/json-extension';
      for (let plugin of activePlugins(ext)) {
        mimeExtensions.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/mermaid-extension')) {
    try {
      let ext = require('@jupyterlab/mermaid-extension/lib/mime.js');
      ext.__scope__ = '@jupyterlab/mermaid-extension';
      for (let plugin of activePlugins(ext)) {
        mimeExtensions.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/vega5-extension')) {
    try {
      let ext = require('@jupyterlab/vega5-extension');
      ext.__scope__ = '@jupyterlab/vega5-extension';
      for (let plugin of activePlugins(ext)) {
        mimeExtensions.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }

  // Add the federated mime extensions.
  const federatedMimeExtensions = await Promise.allSettled(federatedMimeExtensionPromises);
  federatedMimeExtensions.forEach(p => {
    if (p.status === "fulfilled") {
      for (let plugin of activePlugins(p.value)) {
        mimeExtensions.push(plugin);
      }
    } else {
      console.error(p.reason);
    }
  });

  // Handle the standard extensions.
  if (!federatedExtensionNames.has('@jupyterlab/application-extension')) {
    try {
      let ext = require('@jupyterlab/application-extension');
      ext.__scope__ = '@jupyterlab/application-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/apputils-extension')) {
    try {
      let ext = require('@jupyterlab/apputils-extension');
      ext.__scope__ = '@jupyterlab/apputils-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/audio-extension')) {
    try {
      let ext = require('@jupyterlab/audio-extension');
      ext.__scope__ = '@jupyterlab/audio-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/cell-toolbar-extension')) {
    try {
      let ext = require('@jupyterlab/cell-toolbar-extension');
      ext.__scope__ = '@jupyterlab/cell-toolbar-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/celltags-extension')) {
    try {
      let ext = require('@jupyterlab/celltags-extension');
      ext.__scope__ = '@jupyterlab/celltags-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/codemirror-extension')) {
    try {
      let ext = require('@jupyterlab/codemirror-extension');
      ext.__scope__ = '@jupyterlab/codemirror-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/completer-extension')) {
    try {
      let ext = require('@jupyterlab/completer-extension');
      ext.__scope__ = '@jupyterlab/completer-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/console-extension')) {
    try {
      let ext = require('@jupyterlab/console-extension');
      ext.__scope__ = '@jupyterlab/console-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/docmanager-extension')) {
    try {
      let ext = require('@jupyterlab/docmanager-extension');
      ext.__scope__ = '@jupyterlab/docmanager-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/documentsearch-extension')) {
    try {
      let ext = require('@jupyterlab/documentsearch-extension');
      ext.__scope__ = '@jupyterlab/documentsearch-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/filebrowser-extension')) {
    try {
      let ext = require('@jupyterlab/filebrowser-extension');
      ext.__scope__ = '@jupyterlab/filebrowser-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/fileeditor-extension')) {
    try {
      let ext = require('@jupyterlab/fileeditor-extension');
      ext.__scope__ = '@jupyterlab/fileeditor-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/help-extension')) {
    try {
      let ext = require('@jupyterlab/help-extension');
      ext.__scope__ = '@jupyterlab/help-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/logconsole-extension')) {
    try {
      let ext = require('@jupyterlab/logconsole-extension');
      ext.__scope__ = '@jupyterlab/logconsole-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/lsp-extension')) {
    try {
      let ext = require('@jupyterlab/lsp-extension');
      ext.__scope__ = '@jupyterlab/lsp-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/mainmenu-extension')) {
    try {
      let ext = require('@jupyterlab/mainmenu-extension');
      ext.__scope__ = '@jupyterlab/mainmenu-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/markedparser-extension')) {
    try {
      let ext = require('@jupyterlab/markedparser-extension');
      ext.__scope__ = '@jupyterlab/markedparser-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/mathjax-extension')) {
    try {
      let ext = require('@jupyterlab/mathjax-extension');
      ext.__scope__ = '@jupyterlab/mathjax-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/mermaid-extension')) {
    try {
      let ext = require('@jupyterlab/mermaid-extension');
      ext.__scope__ = '@jupyterlab/mermaid-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/metadataform-extension')) {
    try {
      let ext = require('@jupyterlab/metadataform-extension');
      ext.__scope__ = '@jupyterlab/metadataform-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/notebook-extension')) {
    try {
      let ext = require('@jupyterlab/notebook-extension');
      ext.__scope__ = '@jupyterlab/notebook-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/rendermime-extension')) {
    try {
      let ext = require('@jupyterlab/rendermime-extension');
      ext.__scope__ = '@jupyterlab/rendermime-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/services-extension')) {
    try {
      let ext = require('@jupyterlab/services-extension');
      ext.__scope__ = '@jupyterlab/services-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/shortcuts-extension')) {
    try {
      let ext = require('@jupyterlab/shortcuts-extension');
      ext.__scope__ = '@jupyterlab/shortcuts-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/theme-dark-extension')) {
    try {
      let ext = require('@jupyterlab/theme-dark-extension');
      ext.__scope__ = '@jupyterlab/theme-dark-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/theme-dark-high-contrast-extension')) {
    try {
      let ext = require('@jupyterlab/theme-dark-high-contrast-extension');
      ext.__scope__ = '@jupyterlab/theme-dark-high-contrast-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/theme-light-extension')) {
    try {
      let ext = require('@jupyterlab/theme-light-extension');
      ext.__scope__ = '@jupyterlab/theme-light-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/toc-extension')) {
    try {
      let ext = require('@jupyterlab/toc-extension');
      ext.__scope__ = '@jupyterlab/toc-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/tooltip-extension')) {
    try {
      let ext = require('@jupyterlab/tooltip-extension');
      ext.__scope__ = '@jupyterlab/tooltip-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/translation-extension')) {
    try {
      let ext = require('@jupyterlab/translation-extension');
      ext.__scope__ = '@jupyterlab/translation-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/ui-components-extension')) {
    try {
      let ext = require('@jupyterlab/ui-components-extension');
      ext.__scope__ = '@jupyterlab/ui-components-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlab/video-extension')) {
    try {
      let ext = require('@jupyterlab/video-extension');
      ext.__scope__ = '@jupyterlab/video-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyter-notebook/application-extension')) {
    try {
      let ext = require('@jupyter-notebook/application-extension');
      ext.__scope__ = '@jupyter-notebook/application-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyter-notebook/console-extension')) {
    try {
      let ext = require('@jupyter-notebook/console-extension');
      ext.__scope__ = '@jupyter-notebook/console-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyter-notebook/docmanager-extension')) {
    try {
      let ext = require('@jupyter-notebook/docmanager-extension');
      ext.__scope__ = '@jupyter-notebook/docmanager-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyter-notebook/help-extension')) {
    try {
      let ext = require('@jupyter-notebook/help-extension');
      ext.__scope__ = '@jupyter-notebook/help-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyter-notebook/notebook-extension')) {
    try {
      let ext = require('@jupyter-notebook/notebook-extension');
      ext.__scope__ = '@jupyter-notebook/notebook-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlite/application-extension')) {
    try {
      let ext = require('@jupyterlite/application-extension');
      ext.__scope__ = '@jupyterlite/application-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlite/apputils-extension')) {
    try {
      let ext = require('@jupyterlite/apputils-extension');
      ext.__scope__ = '@jupyterlite/apputils-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlite/notebook-application-extension')) {
    try {
      let ext = require('@jupyterlite/notebook-application-extension');
      ext.__scope__ = '@jupyterlite/notebook-application-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }
  if (!federatedExtensionNames.has('@jupyterlite/services-extension')) {
    try {
      let ext = require('@jupyterlite/services-extension');
      ext.__scope__ = '@jupyterlite/services-extension';
      for (let plugin of activePlugins(ext)) {
        pluginsToRegister.push(plugin);
      }
    } catch (e) {
      console.error(e);
    }
  }

  // Add the federated extensions.
  const federatedExtensions = await Promise.allSettled(federatedExtensionPromises);
  federatedExtensions.forEach(p => {
    if (p.status === "fulfilled") {
      for (let plugin of activePlugins(p.value)) {
        pluginsToRegister.push(plugin);
      }
    } else {
      console.error(p.reason);
    }
  });

  // Load all federated component styles and log errors for any that do not
  (await Promise.allSettled(federatedStylePromises)).filter(({status}) => status === "rejected").forEach(({reason}) => {
     console.error(reason);
    });

  // 1. Create a plugin registry
  const pluginRegistry = new PluginRegistry();

  // 2. Register the plugins
  pluginRegistry.registerPlugins(pluginsToRegister);

  // 3. Get and resolve the service manager and connection status plugins
  const IServiceManager = require('@jupyterlab/services').IServiceManager;
  const serviceManager = await pluginRegistry.resolveRequiredService(IServiceManager);

  // create the application
  const app = new NotebookApp({
    pluginRegistry,
    mimeExtensions,
    serviceManager,
    availablePlugins: allPlugins
  });
  app.name = PageConfig.getOption('appName') || 'JupyterLite';

  // Expose global app instance when in dev mode or when toggled explicitly.
  const exposeAppInBrowser =
    (PageConfig.getOption('exposeAppInBrowser') || '').toLowerCase() === 'true';

  if (exposeAppInBrowser) {
    window.jupyterapp = app;
  }

  // 4. Start the application, which will activate the other plugins
  await app.start({ bubblingKeydown: true });
  await app.restored;
}
