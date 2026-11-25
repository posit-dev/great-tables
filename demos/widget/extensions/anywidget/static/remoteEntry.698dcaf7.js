var _JUPYTERLAB;
(() => {
"use strict";
var __webpack_modules__ = ({
846(__unused_rspack_module, exports, __webpack_require__) {

var moduleMap = {
  "./extension": () => {
return Promise.all([__webpack_require__.e("2"), __webpack_require__.e("528")]).then(() => (() => (__webpack_require__(59))));
},
};
var get = function(module, getScope) {
  __webpack_require__.R = getScope;
  getScope = (
    __webpack_require__.o(moduleMap, module)
      ? moduleMap[module]()
      : Promise.resolve().then(() => {
throw new Error('Module "' + module + '" does not exist in container.');
})
  );
  __webpack_require__.R = undefined;
  return getScope;
}
var init = function(shareScope, initScope) {
  if (!__webpack_require__.S) return;
  var name = "default";
  var oldScope = __webpack_require__.S[name];
  if(oldScope && oldScope !== shareScope) throw new Error("Container initialization failed as it has already been initialized with a different share scope");
  __webpack_require__.S[name] = shareScope;
  return __webpack_require__.I(name, initScope);
}
__webpack_require__.d(exports, {
	get: () => (get),
	init: () => (init)
});

},

});
// The module cache
var __webpack_module_cache__ = {};

// The require function
function __webpack_require__(moduleId) {

// Check if module is in cache
var cachedModule = __webpack_module_cache__[moduleId];
if (cachedModule !== undefined) {
return cachedModule.exports;
}
// Create a new module (and put it into the cache)
var module = (__webpack_module_cache__[moduleId] = {
exports: {}
});
// Execute the module function
__webpack_modules__[moduleId](module, module.exports, __webpack_require__);

// Return the exports of the module
return module.exports;

}

// expose the modules object (__webpack_modules__)
__webpack_require__.m = __webpack_modules__;

// expose the module cache
__webpack_require__.c = __webpack_module_cache__;

// webpack/runtime/define_property_getters
(() => {
__webpack_require__.d = (exports, definition) => {
	for(var key in definition) {
        if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
            Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
        }
    }
};
})();
// webpack/runtime/ensure_chunk
(() => {
__webpack_require__.f = {};
// This file contains only the entry chunk.
// The chunk loading function for additional chunks
__webpack_require__.e = (chunkId) => {
	return Promise.all(
		Object.keys(__webpack_require__.f).reduce((promises, key) => {
			__webpack_require__.f[key](chunkId, promises);
			return promises;
		}, [])
	);
};
})();
// webpack/runtime/get javascript chunk filename
(() => {
// This function allow to reference chunks
__webpack_require__.u = (chunkId) => {
  // return url for filenames not based on template
  
  // return url for filenames based on template
  return "" + chunkId + "." + {"2": "3dbf81c0","528": "d9f5934c",}[chunkId] + ".js"
}
})();
// webpack/runtime/global
(() => {
__webpack_require__.g = (() => {
	if (typeof globalThis === 'object') return globalThis;
	try {
		return this || new Function('return this')();
	} catch (e) {
		if (typeof window === 'object') return window;
	}
})();
})();
// webpack/runtime/has_own_property
(() => {
__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
})();
// webpack/runtime/load_script
(() => {
var inProgress = {};

var uniqueName = "@anywidget/monorepo:";
// loadScript function to load a script via script tag
__webpack_require__.l = function (url, done, key, chunkId) {
	if (inProgress[url]) {
		inProgress[url].push(done);
		return;
	}
	var script, needAttach;
	if (key !== undefined) {
		var scripts = document.getElementsByTagName("script");
		for (var i = 0; i < scripts.length; i++) {
			var s = scripts[i];
			if (s.getAttribute("src") == url || s.getAttribute("data-rspack") == uniqueName + key) {
				script = s;
				break;
			}
		}
	}
	if (!script) {
		needAttach = true;
		script = document.createElement('script');


script.timeout = 120;
if (__webpack_require__.nc) {
  script.setAttribute("nonce", __webpack_require__.nc);
}

script.setAttribute("data-rspack", uniqueName + key);



script.src = url;


	}
	inProgress[url] = [done];
	var onScriptComplete = function (prev, event) {
		script.onerror = script.onload = null;
		clearTimeout(timeout);
		var doneFns = inProgress[url];
		delete inProgress[url];
		script.parentNode && script.parentNode.removeChild(script);
		doneFns &&
			doneFns.forEach(function (fn) {
				return fn(event);
			});
		if (prev) return prev(event);
	};
	var timeout = setTimeout(
		onScriptComplete.bind(null, undefined, {
			type: 'timeout',
			target: script
		}),
		120000
	);
	script.onerror = onScriptComplete.bind(null, script.onerror);
	script.onload = onScriptComplete.bind(null, script.onload);
	needAttach && document.head.appendChild(script);
};

})();
// webpack/runtime/make_namespace_object
(() => {
// define __esModule on exports
__webpack_require__.r = (exports) => {
	if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
		Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
	}
	Object.defineProperty(exports, '__esModule', { value: true });
};
})();
// webpack/runtime/rspack_version
(() => {
__webpack_require__.rv = () => ("1.7.11")
})();
// webpack/runtime/sharing
(() => {

__webpack_require__.S = {};
__webpack_require__.initializeSharingData = { scopeToSharingDataMapping: {  }, uniqueName: "@anywidget/monorepo" };
var initPromises = {};
var initTokens = {};
__webpack_require__.I = function(name, initScope) {
	if (!initScope) initScope = [];
	// handling circular init calls
	var initToken = initTokens[name];
	if (!initToken) initToken = initTokens[name] = {};
	if (initScope.indexOf(initToken) >= 0) return;
	initScope.push(initToken);
	// only runs once
	if (initPromises[name]) return initPromises[name];
	// creates a new share scope if needed
	if (!__webpack_require__.o(__webpack_require__.S, name))
		__webpack_require__.S[name] = {};
	// runs all init snippets from all modules reachable
	var scope = __webpack_require__.S[name];
	var warn = function (msg) {
		if (typeof console !== "undefined" && console.warn) console.warn(msg);
	};
	var uniqueName = __webpack_require__.initializeSharingData.uniqueName;
	var register = function (name, version, factory, eager) {
		var versions = (scope[name] = scope[name] || {});
		var activeVersion = versions[version];
		if (
			!activeVersion ||
			(!activeVersion.loaded &&
				(!eager != !activeVersion.eager
					? eager
					: uniqueName > activeVersion.from))
		)
			versions[version] = { get: factory, from: uniqueName, eager: !!eager };
	};
	var initExternal = function (id) {
		var handleError = function (err) {
			warn("Initialization of sharing external failed: " + err);
		};
		try {
			var module = __webpack_require__(id);
			if (!module) return;
			var initFn = function (module) {
				return (
					module &&
					module.init &&
					module.init(__webpack_require__.S[name], initScope)
				);
			};
			if (module.then) return promises.push(module.then(initFn, handleError));
			var initResult = initFn(module);
			if (initResult && initResult.then)
				return promises.push(initResult["catch"](handleError));
		} catch (err) {
			handleError(err);
		}
	};
	var promises = [];
	var scopeToSharingDataMapping = __webpack_require__.initializeSharingData.scopeToSharingDataMapping;
	if (scopeToSharingDataMapping[name]) {
		scopeToSharingDataMapping[name].forEach(function (stage) {
			if (typeof stage === "object") register(stage.name, stage.version, stage.factory, stage.eager);
			else initExternal(stage)
		});
	}
	if (!promises.length) return (initPromises[name] = 1);
	return (initPromises[name] = Promise.all(promises).then(function () {
		return (initPromises[name] = 1);
	}));
};


})();
// webpack/runtime/auto_public_path
(() => {
var scriptUrl;

if (__webpack_require__.g.importScripts) scriptUrl = __webpack_require__.g.location + "";
var document = __webpack_require__.g.document;
if (!scriptUrl && document) {
  // Technically we could use `document.currentScript instanceof window.HTMLScriptElement`,
  // but an attacker could try to inject `<script>HTMLScriptElement = HTMLImageElement</script>`
  // and use `<img name="currentScript" src="https://attacker.controlled.server/"></img>`
  if (document.currentScript && document.currentScript.tagName.toUpperCase() === 'SCRIPT') scriptUrl = document.currentScript.src;
  if (!scriptUrl) {
    var scripts = document.getElementsByTagName("script");
    if (scripts.length) {
      var i = scripts.length - 1;
      while (i > -1 && (!scriptUrl || !/^http(s?):/.test(scriptUrl))) scriptUrl = scripts[i--].src;
    }
  }
}

// When supporting browsers where an automatic publicPath is not supported you must specify an output.publicPath manually via configuration",
// or pass an empty string ("") and set the __webpack_public_path__ variable from your code to use your own logic.',
if (!scriptUrl) throw new Error("Automatic publicPath is not supported in this browser");
scriptUrl = scriptUrl.replace(/^blob:/, "").replace(/#.*$/, "").replace(/\?.*$/, "").replace(/\/[^\/]+$/, "/");

__webpack_require__.p = scriptUrl;

})();
// webpack/runtime/consumes_loading
(() => {

__webpack_require__.consumesLoadingData = { chunkMapping: {"528":["319"]}, moduleIdToConsumeDataMapping: {"319": { shareScope: "default", shareKey: "@jupyter-widgets/base", import: null, requiredVersion: "^6", strictVersion: false, singleton: true, eager: false, fallback: undefined }}, initialConsumes: [] };
var splitAndConvert = function(str) {
  return str.split(".").map(function(item) {
    return +item == item ? +item : item;
  });
};
var parseRange = function(str) {
  // see https://docs.npmjs.com/misc/semver#range-grammar for grammar
  var parsePartial = function(str) {
    var match = /^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(str);
    var ver = match[1] ? [0].concat(splitAndConvert(match[1])) : [0];
    if (match[2]) {
      ver.length++;
      ver.push.apply(ver, splitAndConvert(match[2]));
    }

    // remove trailing any matchers
    let last = ver[ver.length - 1];
    while (
      ver.length &&
      (last === undefined || /^[*xX]$/.test(/** @type {string} */ (last)))
    ) {
      ver.pop();
      last = ver[ver.length - 1];
    }

    return ver;
  };
  var toFixed = function(range) {
    if (range.length === 1) {
      // Special case for "*" is "x.x.x" instead of "="
      return [0];
    } else if (range.length === 2) {
      // Special case for "1" is "1.x.x" instead of "=1"
      return [1].concat(range.slice(1));
    } else if (range.length === 3) {
      // Special case for "1.2" is "1.2.x" instead of "=1.2"
      return [2].concat(range.slice(1));
    } else {
      return [range.length].concat(range.slice(1));
    }
  };
  var negate = function(range) {
    return [-range[0] - 1].concat(range.slice(1));
  };
  var parseSimple = function(str) {
    // simple       ::= primitive | partial | tilde | caret
    // primitive    ::= ( '<' | '>' | '>=' | '<=' | '=' | '!' ) ( ' ' ) * partial
    // tilde        ::= '~' ( ' ' ) * partial
    // caret        ::= '^' ( ' ' ) * partial
    const match = /^(\^|~|<=|<|>=|>|=|v|!)/.exec(str);
    const start = match ? match[0] : "";
    const remainder = parsePartial(
      start.length ? str.slice(start.length).trim() : str.trim()
    );
    switch (start) {
      case "^":
        if (remainder.length > 1 && remainder[1] === 0) {
          if (remainder.length > 2 && remainder[2] === 0) {
            return [3].concat(remainder.slice(1));
          }
          return [2].concat(remainder.slice(1));
        }
        return [1].concat(remainder.slice(1));
      case "~":
        return [2].concat(remainder.slice(1));
      case ">=":
        return remainder;
      case "=":
      case "v":
      case "":
        return toFixed(remainder);
      case "<":
        return negate(remainder);
      case ">": {
        // and( >=, not( = ) ) => >=, =, not, and
        const fixed = toFixed(remainder);
        return [, fixed, 0, remainder, 2];
      }
      case "<=":
        // or( <, = ) => <, =, or
        return [, toFixed(remainder), negate(remainder), 1];
      case "!": {
        // not =
        const fixed = toFixed(remainder);
        return [, fixed, 0];
      }
      default:
        throw new Error("Unexpected start value");
    }
  };
  var combine = function(items, fn) {
    if (items.length === 1) return items[0];
    const arr = [];
    for (const item of items.slice().reverse()) {
      if (0 in item) {
        arr.push(item);
      } else {
        arr.push.apply(arr, item.slice(1));
      }
    }
    return [,].concat(arr, items.slice(1).map(() => fn));
  };
  var parseRange = function(str) {
    // range      ::= hyphen | simple ( ' ' ( ' ' ) * simple ) * | ''
    // hyphen     ::= partial ( ' ' ) * ' - ' ( ' ' ) * partial
    const items = str.split(/\s+-\s+/);
    if (items.length === 1) {
			str = str.trim();
			const items = [];
			const r = /[-0-9A-Za-z]\s+/g;
			var start = 0;
			var match;
			while ((match = r.exec(str))) {
				const end = match.index + 1;
				items.push(parseSimple(str.slice(start, end).trim()));
				start = end;
			}
			items.push(parseSimple(str.slice(start).trim()));
      return combine(items, 2);
    }
    const a = parsePartial(items[0]);
    const b = parsePartial(items[1]);
    // >=a <=b => and( >=a, or( <b, =b ) ) => >=a, <b, =b, or, and
    return [, toFixed(b), negate(b), 1, a, 2];
  };
  var parseLogicalOr = function(str) {
    // range-set  ::= range ( logical-or range ) *
    // logical-or ::= ( ' ' ) * '||' ( ' ' ) *
    const items = str.split(/\s*\|\|\s*/).map(parseRange);
    return combine(items, 1);
  };
  return parseLogicalOr(str);
};
var parseVersion = function(str) {
	var match = /^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(str);
	/** @type {(string|number|undefined|[])[]} */
	var ver = match[1] ? splitAndConvert(match[1]) : [];
	if (match[2]) {
		ver.length++;
		ver.push.apply(ver, splitAndConvert(match[2]));
	}
	if (match[3]) {
		ver.push([]);
		ver.push.apply(ver, splitAndConvert(match[3]));
	}
	return ver;
}
var versionLt = function(a, b) {
	a = parseVersion(a);
	b = parseVersion(b);
	var i = 0;
	for (;;) {
		// a       b  EOA     object  undefined  number  string
		// EOA        a == b  a < b   b < a      a < b   a < b
		// object     b < a   (0)     b < a      a < b   a < b
		// undefined  a < b   a < b   (0)        a < b   a < b
		// number     b < a   b < a   b < a      (1)     a < b
		// string     b < a   b < a   b < a      b < a   (1)
		// EOA end of array
		// (0) continue on
		// (1) compare them via "<"

		// Handles first row in table
		if (i >= a.length) return i < b.length && (typeof b[i])[0] != "u";

		var aValue = a[i];
		var aType = (typeof aValue)[0];

		// Handles first column in table
		if (i >= b.length) return aType == "u";

		var bValue = b[i];
		var bType = (typeof bValue)[0];

		if (aType == bType) {
			if (aType != "o" && aType != "u" && aValue != bValue) {
				return aValue < bValue;
			}
			i++;
		} else {
			// Handles remaining cases
			if (aType == "o" && bType == "n") return true;
			return bType == "s" || aType == "u";
		}
	}
}
var rangeToString = function(range) {
	var fixCount = range[0];
	var str = "";
	if (range.length === 1) {
		return "*";
	} else if (fixCount + 0.5) {
		str +=
			fixCount == 0
				? ">="
				: fixCount == -1
				? "<"
				: fixCount == 1
				? "^"
				: fixCount == 2
				? "~"
				: fixCount > 0
				? "="
				: "!=";
		var needDot = 1;
		for (var i = 1; i < range.length; i++) {
			var item = range[i];
			var t = (typeof item)[0];
			needDot--;
			str +=
				t == "u"
					? // undefined: prerelease marker, add an "-"
					  "-"
					: // number or string: add the item, set flag to add an "." between two of them
					  (needDot > 0 ? "." : "") + ((needDot = 2), item);
		}
		return str;
	} else {
		var stack = [];
		for (var i = 1; i < range.length; i++) {
			var item = range[i];
			stack.push(
				item === 0
					? "not(" + pop() + ")"
					: item === 1
					? "(" + pop() + " || " + pop() + ")"
					: item === 2
					? stack.pop() + " " + stack.pop()
					: rangeToString(item)
			);
		}
		return pop();
	}
	function pop() {
		return stack.pop().replace(/^\((.+)\)$/, "$1");
	}
}
var satisfy = function(range, version) {
	if (0 in range) {
		version = parseVersion(version);
		var fixCount = /** @type {number} */ (range[0]);
		// when negated is set it swill set for < instead of >=
		var negated = fixCount < 0;
		if (negated) fixCount = -fixCount - 1;
		for (var i = 0, j = 1, isEqual = true; ; j++, i++) {
			// cspell:word nequal nequ

			// when isEqual = true:
			// range         version: EOA/object  undefined  number    string
			// EOA                    equal       block      big-ver   big-ver
			// undefined              bigger      next       big-ver   big-ver
			// number                 smaller     block      cmp       big-cmp
			// fixed number           smaller     block      cmp-fix   differ
			// string                 smaller     block      differ    cmp
			// fixed string           smaller     block      small-cmp cmp-fix

			// when isEqual = false:
			// range         version: EOA/object  undefined  number    string
			// EOA                    nequal      block      next-ver  next-ver
			// undefined              nequal      block      next-ver  next-ver
			// number                 nequal      block      next      next
			// fixed number           nequal      block      next      next   (this never happens)
			// string                 nequal      block      next      next
			// fixed string           nequal      block      next      next   (this never happens)

			// EOA end of array
			// equal (version is equal range):
			//   when !negated: return true,
			//   when negated: return false
			// bigger (version is bigger as range):
			//   when fixed: return false,
			//   when !negated: return true,
			//   when negated: return false,
			// smaller (version is smaller as range):
			//   when !negated: return false,
			//   when negated: return true
			// nequal (version is not equal range (> resp <)): return true
			// block (version is in different prerelease area): return false
			// differ (version is different from fixed range (string vs. number)): return false
			// next: continues to the next items
			// next-ver: when fixed: return false, continues to the next item only for the version, sets isEqual=false
			// big-ver: when fixed || negated: return false, continues to the next item only for the version, sets isEqual=false
			// next-nequ: continues to the next items, sets isEqual=false
			// cmp (negated === false): version < range => return false, version > range => next-nequ, else => next
			// cmp (negated === true): version > range => return false, version < range => next-nequ, else => next
			// cmp-fix: version == range => next, else => return false
			// big-cmp: when negated => return false, else => next-nequ
			// small-cmp: when negated => next-nequ, else => return false

			var rangeType = j < range.length ? (typeof range[j])[0] : "";

			var versionValue;
			var versionType;

			// Handles first column in both tables (end of version or object)
			if (
				i >= version.length ||
				((versionValue = version[i]),
				(versionType = (typeof versionValue)[0]) == "o")
			) {
				// Handles nequal
				if (!isEqual) return true;
				// Handles bigger
				if (rangeType == "u") return j > fixCount && !negated;
				// Handles equal and smaller: (range === EOA) XOR negated
				return (rangeType == "") != negated; // equal + smaller
			}

			// Handles second column in both tables (version = undefined)
			if (versionType == "u") {
				if (!isEqual || rangeType != "u") {
					return false;
				}
			}

			// switch between first and second table
			else if (isEqual) {
				// Handle diagonal
				if (rangeType == versionType) {
					if (j <= fixCount) {
						// Handles "cmp-fix" cases
						if (versionValue != range[j]) {
							return false;
						}
					} else {
						// Handles "cmp" cases
						if (negated ? versionValue > range[j] : versionValue < range[j]) {
							return false;
						}
						if (versionValue != range[j]) isEqual = false;
					}
				}

				// Handle big-ver
				else if (rangeType != "s" && rangeType != "n") {
					if (negated || j <= fixCount) return false;
					isEqual = false;
					j--;
				}

				// Handle differ, big-cmp and small-cmp
				else if (j <= fixCount || versionType < rangeType != negated) {
					return false;
				} else {
					isEqual = false;
				}
			} else {
				// Handles all "next-ver" cases in the second table
				if (rangeType != "s" && rangeType != "n") {
					isEqual = false;
					j--;
				}

				// next is applied by default
			}
		}
	}
	/** @type {(boolean | number)[]} */
	var stack = [];
	var p = stack.pop.bind(stack);
	for (var i = 1; i < range.length; i++) {
		var item = /** @type {SemVerRange | 0 | 1 | 2} */ (range[i]);
		stack.push(
			item == 1
				? p() | p()
				: item == 2
				? p() & p()
				: item
				? satisfy(item, version)
				: !p()
		);
	}
	return !!p();
}
var ensureExistence = function(scopeName, key) {
	var scope = __webpack_require__.S[scopeName];
	if(!scope || !__webpack_require__.o(scope, key)) throw new Error("Shared module " + key + " doesn't exist in shared scope " + scopeName);
	return scope;
};
var findVersion = function(scope, key) {
	var versions = scope[key];
	var key = Object.keys(versions).reduce(function(a, b) {
		return !a || versionLt(a, b) ? b : a;
	}, 0);
	return key && versions[key]
};
var findSingletonVersionKey = function(scope, key) {
	var versions = scope[key];
	return Object.keys(versions).reduce(function(a, b) {
		return !a || (!versions[a].loaded && versionLt(a, b)) ? b : a;
	}, 0);
};
var getInvalidSingletonVersionMessage = function(scope, key, version, requiredVersion) {
	return "Unsatisfied version " + version + " from " + (version && scope[key][version].from) + " of shared singleton module " + key + " (required " + rangeToString(requiredVersion) + ")"
};
var getSingleton = function(scope, scopeName, key, requiredVersion) {
	var version = findSingletonVersionKey(scope, key);
	return get(scope[key][version]);
};
var getSingletonVersion = function(scope, scopeName, key, requiredVersion) {
	var version = findSingletonVersionKey(scope, key);
	if (!satisfy(requiredVersion, version)) warn(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));
	return get(scope[key][version]);
};
var getStrictSingletonVersion = function(scope, scopeName, key, requiredVersion) {
	var version = findSingletonVersionKey(scope, key);
	if (!satisfy(requiredVersion, version)) throw new Error(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));
	return get(scope[key][version]);
};
var findValidVersion = function(scope, key, requiredVersion) {
	var versions = scope[key];
	var key = Object.keys(versions).reduce(function(a, b) {
		if (!satisfy(requiredVersion, b)) return a;
		return !a || versionLt(a, b) ? b : a;
	}, 0);
	return key && versions[key]
};
var getInvalidVersionMessage = function(scope, scopeName, key, requiredVersion) {
	var versions = scope[key];
	return "No satisfying version (" + rangeToString(requiredVersion) + ") of shared module " + key + " found in shared scope " + scopeName + ".\n" +
		"Available versions: " + Object.keys(versions).map(function(key) {
		return key + " from " + versions[key].from;
	}).join(", ");
};
var getValidVersion = function(scope, scopeName, key, requiredVersion) {
	var entry = findValidVersion(scope, key, requiredVersion);
	if(entry) return get(entry);
	throw new Error(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));
};
var warn = function(msg) {
	if (typeof console !== "undefined" && console.warn) console.warn(msg);
};
var warnInvalidVersion = function(scope, scopeName, key, requiredVersion) {
	warn(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));
};
var get = function(entry) {
	entry.loaded = 1;
	return entry.get()
};
var init = function(fn) { return function(scopeName, a, b, c) {
	var promise = __webpack_require__.I(scopeName);
	if (promise && promise.then) return promise.then(fn.bind(fn, scopeName, __webpack_require__.S[scopeName], a, b, c));
	return fn(scopeName, __webpack_require__.S[scopeName], a, b, c);
}; };

var load = /*#__PURE__*/ init(function(scopeName, scope, key) {
	ensureExistence(scopeName, key);
	return get(findVersion(scope, key));
});
var loadFallback = /*#__PURE__*/ init(function(scopeName, scope, key, fallback) {
	return scope && __webpack_require__.o(scope, key) ? get(findVersion(scope, key)) : fallback();
});
var loadVersionCheck = /*#__PURE__*/ init(function(scopeName, scope, key, version) {
	ensureExistence(scopeName, key);
	return get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));
});
var loadSingleton = /*#__PURE__*/ init(function(scopeName, scope, key) {
	ensureExistence(scopeName, key);
	return getSingleton(scope, scopeName, key);
});
var loadSingletonVersionCheck = /*#__PURE__*/ init(function(scopeName, scope, key, version) {
	ensureExistence(scopeName, key);
	return getSingletonVersion(scope, scopeName, key, version);
});
var loadStrictVersionCheck = /*#__PURE__*/ init(function(scopeName, scope, key, version) {
	ensureExistence(scopeName, key);
	return getValidVersion(scope, scopeName, key, version);
});
var loadStrictSingletonVersionCheck = /*#__PURE__*/ init(function(scopeName, scope, key, version) {
	ensureExistence(scopeName, key);
	return getStrictSingletonVersion(scope, scopeName, key, version);
});
var loadVersionCheckFallback = /*#__PURE__*/ init(function(scopeName, scope, key, version, fallback) {
	if(!scope || !__webpack_require__.o(scope, key)) return fallback();
	return get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));
});
var loadSingletonFallback = /*#__PURE__*/ init(function(scopeName, scope, key, fallback) {
	if(!scope || !__webpack_require__.o(scope, key)) return fallback();
	return getSingleton(scope, scopeName, key);
});
var loadSingletonVersionCheckFallback = /*#__PURE__*/ init(function(scopeName, scope, key, version, fallback) {
	if(!scope || !__webpack_require__.o(scope, key)) return fallback();
	return getSingletonVersion(scope, scopeName, key, version);
});
var loadStrictVersionCheckFallback = /*#__PURE__*/ init(function(scopeName, scope, key, version, fallback) {
	var entry = scope && __webpack_require__.o(scope, key) && findValidVersion(scope, key, version);
	return entry ? get(entry) : fallback();
});
var loadStrictSingletonVersionCheckFallback = /*#__PURE__*/ init(function(scopeName, scope, key, version, fallback) {
	if(!scope || !__webpack_require__.o(scope, key)) return fallback();
	return getStrictSingletonVersion(scope, scopeName, key, version);
});
var resolveHandler = function(data) {
	var strict = false
	var singleton = false
	var versionCheck = false
	var fallback = false
	var args = [data.shareScope, data.shareKey];
	if (data.requiredVersion) {
		if (data.strictVersion) strict = true;
		if (data.singleton) singleton = true;
		args.push(parseRange(data.requiredVersion));
		versionCheck = true
	} else if (data.singleton) singleton = true;
	if (data.fallback) {
		fallback = true;
		args.push(data.fallback);
	}
	if (strict && singleton && versionCheck && fallback) return function() { return loadStrictSingletonVersionCheckFallback.apply(null, args); }
	if (strict && versionCheck && fallback) return function() { return loadStrictVersionCheckFallback.apply(null, args); }
	if (singleton && versionCheck && fallback) return function() { return loadSingletonVersionCheckFallback.apply(null, args); }
	if (strict && singleton && versionCheck) return function() { return loadStrictSingletonVersionCheck.apply(null, args); }
	if (singleton && fallback) return function() { return loadSingletonFallback.apply(null, args); }
	if (versionCheck && fallback) return function() { return loadVersionCheckFallback.apply(null, args); }
	if (strict && versionCheck) return function() { return loadStrictVersionCheck.apply(null, args); }
	if (singleton && versionCheck) return function() { return loadSingletonVersionCheck.apply(null, args); }
	if (singleton) return function() { return loadSingleton.apply(null, args); }
	if (versionCheck) return function() { return loadVersionCheck.apply(null, args); }
	if (fallback) return function() { return loadFallback.apply(null, args); }
	return function() { return load.apply(null, args); }
};
var installedModules = {};
__webpack_require__.f.consumes = function(chunkId, promises) {
	var moduleIdToConsumeDataMapping = __webpack_require__.consumesLoadingData.moduleIdToConsumeDataMapping
	var chunkMapping = __webpack_require__.consumesLoadingData.chunkMapping;
	if(__webpack_require__.o(chunkMapping, chunkId)) {
		chunkMapping[chunkId].forEach(function(id) {
			if(__webpack_require__.o(installedModules, id)) return promises.push(installedModules[id]);
			var onFactory = function(factory) {
				installedModules[id] = 0;
				__webpack_require__.m[id] = function(module) {
					delete __webpack_require__.c[id];
					module.exports = factory();
				}
			};
			var onError = function(error) {
				delete installedModules[id];
				__webpack_require__.m[id] = function(module) {
					delete __webpack_require__.c[id];
					throw error;
				}
			};
			try {
				var promise = resolveHandler(moduleIdToConsumeDataMapping[id])();
				if(promise.then) {
					promises.push(installedModules[id] = promise.then(onFactory)['catch'](onError));
				} else onFactory(promise);
			} catch(e) { onError(e); }
		});
	}
}

})();
// webpack/runtime/jsonp_chunk_loading
(() => {

      // object to store loaded and loading chunks
      // undefined = chunk not loaded, null = chunk preloaded/prefetched
      // [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
      var installedChunks = {"180": 0,};
      
        __webpack_require__.f.j = function (chunkId, promises) {
          // JSONP chunk loading for javascript
var installedChunkData = __webpack_require__.o(installedChunks, chunkId)
	? installedChunks[chunkId]
	: undefined;
if (installedChunkData !== 0) {
	// 0 means "already installed".

	// a Promise means "currently loading".
	if (installedChunkData) {
		promises.push(installedChunkData[2]);
	} else {
		if (true) {
			// setup Promise in chunk cache
			var promise = new Promise((resolve, reject) => (installedChunkData = installedChunks[chunkId] = [resolve, reject]));
			promises.push((installedChunkData[2] = promise));

			// start chunk loading
			var url = __webpack_require__.p + __webpack_require__.u(chunkId);
			// create error before stack unwound to get useful stacktrace later
			var error = new Error();
			var loadingEnded = function (event) {
				if (__webpack_require__.o(installedChunks, chunkId)) {
					installedChunkData = installedChunks[chunkId];
					if (installedChunkData !== 0) installedChunks[chunkId] = undefined;
					if (installedChunkData) {
						var errorType =
							event && (event.type === 'load' ? 'missing' : event.type);
						var realSrc = event && event.target && event.target.src;
						error.message =
							'Loading chunk ' +
							chunkId +
							' failed.\n(' +
							errorType +
							': ' +
							realSrc +
							')';
						error.name = 'ChunkLoadError';
						error.type = errorType;
						error.request = realSrc;
						installedChunkData[1](error);
					}
				}
			};
			__webpack_require__.l(url, loadingEnded, "chunk-" + chunkId, chunkId);
		} 
	}
}

        }
        // install a JSONP callback for chunk loading
var __rspack_jsonp = (parentChunkLoadingFunction, data) => {
	var [chunkIds, moreModules, runtime] = data;
	// add "moreModules" to the modules object,
	// then flag all "chunkIds" as loaded and fire callback
	var moduleId, chunkId, i = 0;
	if (chunkIds.some((id) => (installedChunks[id] !== 0))) {
		for (moduleId in moreModules) {
			if (__webpack_require__.o(moreModules, moduleId)) {
				__webpack_require__.m[moduleId] = moreModules[moduleId];
			}
		}
		if (runtime) var result = runtime(__webpack_require__);
	}
	if (parentChunkLoadingFunction) parentChunkLoadingFunction(data);
	for (; i < chunkIds.length; i++) {
		chunkId = chunkIds[i];
		if (
			__webpack_require__.o(installedChunks, chunkId) &&
			installedChunks[chunkId]
		) {
			installedChunks[chunkId][0]();
		}
		installedChunks[chunkId] = 0;
	}
	
};

var chunkLoadingGlobal = self["webpackChunk_anywidget_monorepo"] = self["webpackChunk_anywidget_monorepo"] || [];
chunkLoadingGlobal.forEach(__rspack_jsonp.bind(null, 0));
chunkLoadingGlobal.push = __rspack_jsonp.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));

})();
// webpack/runtime/rspack_unique_id
(() => {
__webpack_require__.ruid = "bundler=rspack@1.7.11";
})();
// module cache are used so entry inlining is disabled
// startup
// Load entry module and return exports
var __webpack_exports__ = __webpack_require__(846);
(_JUPYTERLAB = typeof _JUPYTERLAB === 'undefined' ? {} : _JUPYTERLAB).anywidget = __webpack_exports__;
})()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicmVtb3RlRW50cnkuYTNhZTIwNjkuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvL3dlYnBhY2svcnVudGltZS9kZWZpbmVfcHJvcGVydHlfZ2V0dGVycyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvL3dlYnBhY2svcnVudGltZS9lbnN1cmVfY2h1bmsiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvZ2V0IGphdmFzY3JpcHQgY2h1bmsgZmlsZW5hbWUiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvZ2xvYmFsIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL2hhc19vd25fcHJvcGVydHkiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvbG9hZF9zY3JpcHQiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvbWFrZV9uYW1lc3BhY2Vfb2JqZWN0Iiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL3JzcGFja192ZXJzaW9uIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL3NoYXJpbmciLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvYXV0b19wdWJsaWNfcGF0aCIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvL3dlYnBhY2svcnVudGltZS9jb25zdW1lc19sb2FkaW5nIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL2pzb25wX2NodW5rX2xvYWRpbmciLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvcnNwYWNrX3VuaXF1ZV9pZCJdLCJzb3VyY2VzQ29udGVudCI6WyJfX3dlYnBhY2tfcmVxdWlyZV9fLmQgPSAoZXhwb3J0cywgZGVmaW5pdGlvbikgPT4ge1xuXHRmb3IodmFyIGtleSBpbiBkZWZpbml0aW9uKSB7XG4gICAgICAgIGlmKF9fd2VicGFja19yZXF1aXJlX18ubyhkZWZpbml0aW9uLCBrZXkpICYmICFfX3dlYnBhY2tfcmVxdWlyZV9fLm8oZXhwb3J0cywga2V5KSkge1xuICAgICAgICAgICAgT2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsIGtleSwgeyBlbnVtZXJhYmxlOiB0cnVlLCBnZXQ6IGRlZmluaXRpb25ba2V5XSB9KTtcbiAgICAgICAgfVxuICAgIH1cbn07IiwiX193ZWJwYWNrX3JlcXVpcmVfXy5mID0ge307XG4vLyBUaGlzIGZpbGUgY29udGFpbnMgb25seSB0aGUgZW50cnkgY2h1bmsuXG4vLyBUaGUgY2h1bmsgbG9hZGluZyBmdW5jdGlvbiBmb3IgYWRkaXRpb25hbCBjaHVua3Ncbl9fd2VicGFja19yZXF1aXJlX18uZSA9IChjaHVua0lkKSA9PiB7XG5cdHJldHVybiBQcm9taXNlLmFsbChcblx0XHRPYmplY3Qua2V5cyhfX3dlYnBhY2tfcmVxdWlyZV9fLmYpLnJlZHVjZSgocHJvbWlzZXMsIGtleSkgPT4ge1xuXHRcdFx0X193ZWJwYWNrX3JlcXVpcmVfXy5mW2tleV0oY2h1bmtJZCwgcHJvbWlzZXMpO1xuXHRcdFx0cmV0dXJuIHByb21pc2VzO1xuXHRcdH0sIFtdKVxuXHQpO1xufTsiLCIvLyBUaGlzIGZ1bmN0aW9uIGFsbG93IHRvIHJlZmVyZW5jZSBjaHVua3Ncbl9fd2VicGFja19yZXF1aXJlX18udSA9IChjaHVua0lkKSA9PiB7XG4gIC8vIHJldHVybiB1cmwgZm9yIGZpbGVuYW1lcyBub3QgYmFzZWQgb24gdGVtcGxhdGVcbiAgXG4gIC8vIHJldHVybiB1cmwgZm9yIGZpbGVuYW1lcyBiYXNlZCBvbiB0ZW1wbGF0ZVxuICByZXR1cm4gXCJcIiArIGNodW5rSWQgKyBcIi5cIiArIHtcIjJcIjogXCIwZmI1ZGRlM1wiLFwiNTI4XCI6IFwiYjA2ZjY1NTlcIix9W2NodW5rSWRdICsgXCIuanNcIlxufSIsIl9fd2VicGFja19yZXF1aXJlX18uZyA9ICgoKSA9PiB7XG5cdGlmICh0eXBlb2YgZ2xvYmFsVGhpcyA9PT0gJ29iamVjdCcpIHJldHVybiBnbG9iYWxUaGlzO1xuXHR0cnkge1xuXHRcdHJldHVybiB0aGlzIHx8IG5ldyBGdW5jdGlvbigncmV0dXJuIHRoaXMnKSgpO1xuXHR9IGNhdGNoIChlKSB7XG5cdFx0aWYgKHR5cGVvZiB3aW5kb3cgPT09ICdvYmplY3QnKSByZXR1cm4gd2luZG93O1xuXHR9XG59KSgpOyIsIl9fd2VicGFja19yZXF1aXJlX18ubyA9IChvYmosIHByb3ApID0+IChPYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5LmNhbGwob2JqLCBwcm9wKSkiLCJ2YXIgaW5Qcm9ncmVzcyA9IHt9O1xuXG52YXIgdW5pcXVlTmFtZSA9IFwiQGFueXdpZGdldC9tb25vcmVwbzpcIjtcbi8vIGxvYWRTY3JpcHQgZnVuY3Rpb24gdG8gbG9hZCBhIHNjcmlwdCB2aWEgc2NyaXB0IHRhZ1xuX193ZWJwYWNrX3JlcXVpcmVfXy5sID0gZnVuY3Rpb24gKHVybCwgZG9uZSwga2V5LCBjaHVua0lkKSB7XG5cdGlmIChpblByb2dyZXNzW3VybF0pIHtcblx0XHRpblByb2dyZXNzW3VybF0ucHVzaChkb25lKTtcblx0XHRyZXR1cm47XG5cdH1cblx0dmFyIHNjcmlwdCwgbmVlZEF0dGFjaDtcblx0aWYgKGtleSAhPT0gdW5kZWZpbmVkKSB7XG5cdFx0dmFyIHNjcmlwdHMgPSBkb2N1bWVudC5nZXRFbGVtZW50c0J5VGFnTmFtZShcInNjcmlwdFwiKTtcblx0XHRmb3IgKHZhciBpID0gMDsgaSA8IHNjcmlwdHMubGVuZ3RoOyBpKyspIHtcblx0XHRcdHZhciBzID0gc2NyaXB0c1tpXTtcblx0XHRcdGlmIChzLmdldEF0dHJpYnV0ZShcInNyY1wiKSA9PSB1cmwgfHwgcy5nZXRBdHRyaWJ1dGUoXCJkYXRhLXJzcGFja1wiKSA9PSB1bmlxdWVOYW1lICsga2V5KSB7XG5cdFx0XHRcdHNjcmlwdCA9IHM7XG5cdFx0XHRcdGJyZWFrO1xuXHRcdFx0fVxuXHRcdH1cblx0fVxuXHRpZiAoIXNjcmlwdCkge1xuXHRcdG5lZWRBdHRhY2ggPSB0cnVlO1xuXHRcdHNjcmlwdCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NjcmlwdCcpO1xuXG5cbnNjcmlwdC50aW1lb3V0ID0gMTIwO1xuaWYgKF9fd2VicGFja19yZXF1aXJlX18ubmMpIHtcbiAgc2NyaXB0LnNldEF0dHJpYnV0ZShcIm5vbmNlXCIsIF9fd2VicGFja19yZXF1aXJlX18ubmMpO1xufVxuXG5zY3JpcHQuc2V0QXR0cmlidXRlKFwiZGF0YS1yc3BhY2tcIiwgdW5pcXVlTmFtZSArIGtleSk7XG5cblxuXG5zY3JpcHQuc3JjID0gdXJsO1xuXG5cblx0fVxuXHRpblByb2dyZXNzW3VybF0gPSBbZG9uZV07XG5cdHZhciBvblNjcmlwdENvbXBsZXRlID0gZnVuY3Rpb24gKHByZXYsIGV2ZW50KSB7XG5cdFx0c2NyaXB0Lm9uZXJyb3IgPSBzY3JpcHQub25sb2FkID0gbnVsbDtcblx0XHRjbGVhclRpbWVvdXQodGltZW91dCk7XG5cdFx0dmFyIGRvbmVGbnMgPSBpblByb2dyZXNzW3VybF07XG5cdFx0ZGVsZXRlIGluUHJvZ3Jlc3NbdXJsXTtcblx0XHRzY3JpcHQucGFyZW50Tm9kZSAmJiBzY3JpcHQucGFyZW50Tm9kZS5yZW1vdmVDaGlsZChzY3JpcHQpO1xuXHRcdGRvbmVGbnMgJiZcblx0XHRcdGRvbmVGbnMuZm9yRWFjaChmdW5jdGlvbiAoZm4pIHtcblx0XHRcdFx0cmV0dXJuIGZuKGV2ZW50KTtcblx0XHRcdH0pO1xuXHRcdGlmIChwcmV2KSByZXR1cm4gcHJldihldmVudCk7XG5cdH07XG5cdHZhciB0aW1lb3V0ID0gc2V0VGltZW91dChcblx0XHRvblNjcmlwdENvbXBsZXRlLmJpbmQobnVsbCwgdW5kZWZpbmVkLCB7XG5cdFx0XHR0eXBlOiAndGltZW91dCcsXG5cdFx0XHR0YXJnZXQ6IHNjcmlwdFxuXHRcdH0pLFxuXHRcdDEyMDAwMFxuXHQpO1xuXHRzY3JpcHQub25lcnJvciA9IG9uU2NyaXB0Q29tcGxldGUuYmluZChudWxsLCBzY3JpcHQub25lcnJvcik7XG5cdHNjcmlwdC5vbmxvYWQgPSBvblNjcmlwdENvbXBsZXRlLmJpbmQobnVsbCwgc2NyaXB0Lm9ubG9hZCk7XG5cdG5lZWRBdHRhY2ggJiYgZG9jdW1lbnQuaGVhZC5hcHBlbmRDaGlsZChzY3JpcHQpO1xufTtcbiIsIi8vIGRlZmluZSBfX2VzTW9kdWxlIG9uIGV4cG9ydHNcbl9fd2VicGFja19yZXF1aXJlX18uciA9IChleHBvcnRzKSA9PiB7XG5cdGlmKHR5cGVvZiBTeW1ib2wgIT09ICd1bmRlZmluZWQnICYmIFN5bWJvbC50b1N0cmluZ1RhZykge1xuXHRcdE9iamVjdC5kZWZpbmVQcm9wZXJ0eShleHBvcnRzLCBTeW1ib2wudG9TdHJpbmdUYWcsIHsgdmFsdWU6ICdNb2R1bGUnIH0pO1xuXHR9XG5cdE9iamVjdC5kZWZpbmVQcm9wZXJ0eShleHBvcnRzLCAnX19lc01vZHVsZScsIHsgdmFsdWU6IHRydWUgfSk7XG59OyIsIl9fd2VicGFja19yZXF1aXJlX18ucnYgPSAoKSA9PiAoXCIxLjcuMTFcIikiLCJcbl9fd2VicGFja19yZXF1aXJlX18uUyA9IHt9O1xuX193ZWJwYWNrX3JlcXVpcmVfXy5pbml0aWFsaXplU2hhcmluZ0RhdGEgPSB7IHNjb3BlVG9TaGFyaW5nRGF0YU1hcHBpbmc6IHsgIH0sIHVuaXF1ZU5hbWU6IFwiQGFueXdpZGdldC9tb25vcmVwb1wiIH07XG52YXIgaW5pdFByb21pc2VzID0ge307XG52YXIgaW5pdFRva2VucyA9IHt9O1xuX193ZWJwYWNrX3JlcXVpcmVfXy5JID0gZnVuY3Rpb24obmFtZSwgaW5pdFNjb3BlKSB7XG5cdGlmICghaW5pdFNjb3BlKSBpbml0U2NvcGUgPSBbXTtcblx0Ly8gaGFuZGxpbmcgY2lyY3VsYXIgaW5pdCBjYWxsc1xuXHR2YXIgaW5pdFRva2VuID0gaW5pdFRva2Vuc1tuYW1lXTtcblx0aWYgKCFpbml0VG9rZW4pIGluaXRUb2tlbiA9IGluaXRUb2tlbnNbbmFtZV0gPSB7fTtcblx0aWYgKGluaXRTY29wZS5pbmRleE9mKGluaXRUb2tlbikgPj0gMCkgcmV0dXJuO1xuXHRpbml0U2NvcGUucHVzaChpbml0VG9rZW4pO1xuXHQvLyBvbmx5IHJ1bnMgb25jZVxuXHRpZiAoaW5pdFByb21pc2VzW25hbWVdKSByZXR1cm4gaW5pdFByb21pc2VzW25hbWVdO1xuXHQvLyBjcmVhdGVzIGEgbmV3IHNoYXJlIHNjb3BlIGlmIG5lZWRlZFxuXHRpZiAoIV9fd2VicGFja19yZXF1aXJlX18ubyhfX3dlYnBhY2tfcmVxdWlyZV9fLlMsIG5hbWUpKVxuXHRcdF9fd2VicGFja19yZXF1aXJlX18uU1tuYW1lXSA9IHt9O1xuXHQvLyBydW5zIGFsbCBpbml0IHNuaXBwZXRzIGZyb20gYWxsIG1vZHVsZXMgcmVhY2hhYmxlXG5cdHZhciBzY29wZSA9IF9fd2VicGFja19yZXF1aXJlX18uU1tuYW1lXTtcblx0dmFyIHdhcm4gPSBmdW5jdGlvbiAobXNnKSB7XG5cdFx0aWYgKHR5cGVvZiBjb25zb2xlICE9PSBcInVuZGVmaW5lZFwiICYmIGNvbnNvbGUud2FybikgY29uc29sZS53YXJuKG1zZyk7XG5cdH07XG5cdHZhciB1bmlxdWVOYW1lID0gX193ZWJwYWNrX3JlcXVpcmVfXy5pbml0aWFsaXplU2hhcmluZ0RhdGEudW5pcXVlTmFtZTtcblx0dmFyIHJlZ2lzdGVyID0gZnVuY3Rpb24gKG5hbWUsIHZlcnNpb24sIGZhY3RvcnksIGVhZ2VyKSB7XG5cdFx0dmFyIHZlcnNpb25zID0gKHNjb3BlW25hbWVdID0gc2NvcGVbbmFtZV0gfHwge30pO1xuXHRcdHZhciBhY3RpdmVWZXJzaW9uID0gdmVyc2lvbnNbdmVyc2lvbl07XG5cdFx0aWYgKFxuXHRcdFx0IWFjdGl2ZVZlcnNpb24gfHxcblx0XHRcdCghYWN0aXZlVmVyc2lvbi5sb2FkZWQgJiZcblx0XHRcdFx0KCFlYWdlciAhPSAhYWN0aXZlVmVyc2lvbi5lYWdlclxuXHRcdFx0XHRcdD8gZWFnZXJcblx0XHRcdFx0XHQ6IHVuaXF1ZU5hbWUgPiBhY3RpdmVWZXJzaW9uLmZyb20pKVxuXHRcdClcblx0XHRcdHZlcnNpb25zW3ZlcnNpb25dID0geyBnZXQ6IGZhY3RvcnksIGZyb206IHVuaXF1ZU5hbWUsIGVhZ2VyOiAhIWVhZ2VyIH07XG5cdH07XG5cdHZhciBpbml0RXh0ZXJuYWwgPSBmdW5jdGlvbiAoaWQpIHtcblx0XHR2YXIgaGFuZGxlRXJyb3IgPSBmdW5jdGlvbiAoZXJyKSB7XG5cdFx0XHR3YXJuKFwiSW5pdGlhbGl6YXRpb24gb2Ygc2hhcmluZyBleHRlcm5hbCBmYWlsZWQ6IFwiICsgZXJyKTtcblx0XHR9O1xuXHRcdHRyeSB7XG5cdFx0XHR2YXIgbW9kdWxlID0gX193ZWJwYWNrX3JlcXVpcmVfXyhpZCk7XG5cdFx0XHRpZiAoIW1vZHVsZSkgcmV0dXJuO1xuXHRcdFx0dmFyIGluaXRGbiA9IGZ1bmN0aW9uIChtb2R1bGUpIHtcblx0XHRcdFx0cmV0dXJuIChcblx0XHRcdFx0XHRtb2R1bGUgJiZcblx0XHRcdFx0XHRtb2R1bGUuaW5pdCAmJlxuXHRcdFx0XHRcdG1vZHVsZS5pbml0KF9fd2VicGFja19yZXF1aXJlX18uU1tuYW1lXSwgaW5pdFNjb3BlKVxuXHRcdFx0XHQpO1xuXHRcdFx0fTtcblx0XHRcdGlmIChtb2R1bGUudGhlbikgcmV0dXJuIHByb21pc2VzLnB1c2gobW9kdWxlLnRoZW4oaW5pdEZuLCBoYW5kbGVFcnJvcikpO1xuXHRcdFx0dmFyIGluaXRSZXN1bHQgPSBpbml0Rm4obW9kdWxlKTtcblx0XHRcdGlmIChpbml0UmVzdWx0ICYmIGluaXRSZXN1bHQudGhlbilcblx0XHRcdFx0cmV0dXJuIHByb21pc2VzLnB1c2goaW5pdFJlc3VsdFtcImNhdGNoXCJdKGhhbmRsZUVycm9yKSk7XG5cdFx0fSBjYXRjaCAoZXJyKSB7XG5cdFx0XHRoYW5kbGVFcnJvcihlcnIpO1xuXHRcdH1cblx0fTtcblx0dmFyIHByb21pc2VzID0gW107XG5cdHZhciBzY29wZVRvU2hhcmluZ0RhdGFNYXBwaW5nID0gX193ZWJwYWNrX3JlcXVpcmVfXy5pbml0aWFsaXplU2hhcmluZ0RhdGEuc2NvcGVUb1NoYXJpbmdEYXRhTWFwcGluZztcblx0aWYgKHNjb3BlVG9TaGFyaW5nRGF0YU1hcHBpbmdbbmFtZV0pIHtcblx0XHRzY29wZVRvU2hhcmluZ0RhdGFNYXBwaW5nW25hbWVdLmZvckVhY2goZnVuY3Rpb24gKHN0YWdlKSB7XG5cdFx0XHRpZiAodHlwZW9mIHN0YWdlID09PSBcIm9iamVjdFwiKSByZWdpc3RlcihzdGFnZS5uYW1lLCBzdGFnZS52ZXJzaW9uLCBzdGFnZS5mYWN0b3J5LCBzdGFnZS5lYWdlcik7XG5cdFx0XHRlbHNlIGluaXRFeHRlcm5hbChzdGFnZSlcblx0XHR9KTtcblx0fVxuXHRpZiAoIXByb21pc2VzLmxlbmd0aCkgcmV0dXJuIChpbml0UHJvbWlzZXNbbmFtZV0gPSAxKTtcblx0cmV0dXJuIChpbml0UHJvbWlzZXNbbmFtZV0gPSBQcm9taXNlLmFsbChwcm9taXNlcykudGhlbihmdW5jdGlvbiAoKSB7XG5cdFx0cmV0dXJuIChpbml0UHJvbWlzZXNbbmFtZV0gPSAxKTtcblx0fSkpO1xufTtcblxuIiwidmFyIHNjcmlwdFVybDtcblxuaWYgKF9fd2VicGFja19yZXF1aXJlX18uZy5pbXBvcnRTY3JpcHRzKSBzY3JpcHRVcmwgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLmcubG9jYXRpb24gKyBcIlwiO1xudmFyIGRvY3VtZW50ID0gX193ZWJwYWNrX3JlcXVpcmVfXy5nLmRvY3VtZW50O1xuaWYgKCFzY3JpcHRVcmwgJiYgZG9jdW1lbnQpIHtcbiAgLy8gVGVjaG5pY2FsbHkgd2UgY291bGQgdXNlIGBkb2N1bWVudC5jdXJyZW50U2NyaXB0IGluc3RhbmNlb2Ygd2luZG93LkhUTUxTY3JpcHRFbGVtZW50YCxcbiAgLy8gYnV0IGFuIGF0dGFja2VyIGNvdWxkIHRyeSB0byBpbmplY3QgYDxzY3JpcHQ+SFRNTFNjcmlwdEVsZW1lbnQgPSBIVE1MSW1hZ2VFbGVtZW50PC9zY3JpcHQ+YFxuICAvLyBhbmQgdXNlIGA8aW1nIG5hbWU9XCJjdXJyZW50U2NyaXB0XCIgc3JjPVwiaHR0cHM6Ly9hdHRhY2tlci5jb250cm9sbGVkLnNlcnZlci9cIj48L2ltZz5gXG4gIGlmIChkb2N1bWVudC5jdXJyZW50U2NyaXB0ICYmIGRvY3VtZW50LmN1cnJlbnRTY3JpcHQudGFnTmFtZS50b1VwcGVyQ2FzZSgpID09PSAnU0NSSVBUJykgc2NyaXB0VXJsID0gZG9jdW1lbnQuY3VycmVudFNjcmlwdC5zcmM7XG4gIGlmICghc2NyaXB0VXJsKSB7XG4gICAgdmFyIHNjcmlwdHMgPSBkb2N1bWVudC5nZXRFbGVtZW50c0J5VGFnTmFtZShcInNjcmlwdFwiKTtcbiAgICBpZiAoc2NyaXB0cy5sZW5ndGgpIHtcbiAgICAgIHZhciBpID0gc2NyaXB0cy5sZW5ndGggLSAxO1xuICAgICAgd2hpbGUgKGkgPiAtMSAmJiAoIXNjcmlwdFVybCB8fCAhL15odHRwKHM/KTovLnRlc3Qoc2NyaXB0VXJsKSkpIHNjcmlwdFVybCA9IHNjcmlwdHNbaS0tXS5zcmM7XG4gICAgfVxuICB9XG59XG5cbi8vIFdoZW4gc3VwcG9ydGluZyBicm93c2VycyB3aGVyZSBhbiBhdXRvbWF0aWMgcHVibGljUGF0aCBpcyBub3Qgc3VwcG9ydGVkIHlvdSBtdXN0IHNwZWNpZnkgYW4gb3V0cHV0LnB1YmxpY1BhdGggbWFudWFsbHkgdmlhIGNvbmZpZ3VyYXRpb25cIixcbi8vIG9yIHBhc3MgYW4gZW1wdHkgc3RyaW5nIChcIlwiKSBhbmQgc2V0IHRoZSBfX3dlYnBhY2tfcHVibGljX3BhdGhfXyB2YXJpYWJsZSBmcm9tIHlvdXIgY29kZSB0byB1c2UgeW91ciBvd24gbG9naWMuJyxcbmlmICghc2NyaXB0VXJsKSB0aHJvdyBuZXcgRXJyb3IoXCJBdXRvbWF0aWMgcHVibGljUGF0aCBpcyBub3Qgc3VwcG9ydGVkIGluIHRoaXMgYnJvd3NlclwiKTtcbnNjcmlwdFVybCA9IHNjcmlwdFVybC5yZXBsYWNlKC9eYmxvYjovLCBcIlwiKS5yZXBsYWNlKC8jLiokLywgXCJcIikucmVwbGFjZSgvXFw/LiokLywgXCJcIikucmVwbGFjZSgvXFwvW15cXC9dKyQvLCBcIi9cIik7XG5cbl9fd2VicGFja19yZXF1aXJlX18ucCA9IHNjcmlwdFVybDtcbiIsIlxuX193ZWJwYWNrX3JlcXVpcmVfXy5jb25zdW1lc0xvYWRpbmdEYXRhID0geyBjaHVua01hcHBpbmc6IHtcIjUyOFwiOltcIjMxOVwiXX0sIG1vZHVsZUlkVG9Db25zdW1lRGF0YU1hcHBpbmc6IHtcIjMxOVwiOiB7IHNoYXJlU2NvcGU6IFwiZGVmYXVsdFwiLCBzaGFyZUtleTogXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIiwgaW1wb3J0OiBudWxsLCByZXF1aXJlZFZlcnNpb246IFwiXjZcIiwgc3RyaWN0VmVyc2lvbjogZmFsc2UsIHNpbmdsZXRvbjogdHJ1ZSwgZWFnZXI6IGZhbHNlLCBmYWxsYmFjazogdW5kZWZpbmVkIH19LCBpbml0aWFsQ29uc3VtZXM6IFtdIH07XG52YXIgc3BsaXRBbmRDb252ZXJ0ID0gZnVuY3Rpb24oc3RyKSB7XG4gIHJldHVybiBzdHIuc3BsaXQoXCIuXCIpLm1hcChmdW5jdGlvbihpdGVtKSB7XG4gICAgcmV0dXJuICtpdGVtID09IGl0ZW0gPyAraXRlbSA6IGl0ZW07XG4gIH0pO1xufTtcbnZhciBwYXJzZVJhbmdlID0gZnVuY3Rpb24oc3RyKSB7XG4gIC8vIHNlZSBodHRwczovL2RvY3MubnBtanMuY29tL21pc2Mvc2VtdmVyI3JhbmdlLWdyYW1tYXIgZm9yIGdyYW1tYXJcbiAgdmFyIHBhcnNlUGFydGlhbCA9IGZ1bmN0aW9uKHN0cikge1xuICAgIHZhciBtYXRjaCA9IC9eKFteLStdKyk/KD86LShbXitdKykpPyg/OlxcKyguKykpPyQvLmV4ZWMoc3RyKTtcbiAgICB2YXIgdmVyID0gbWF0Y2hbMV0gPyBbMF0uY29uY2F0KHNwbGl0QW5kQ29udmVydChtYXRjaFsxXSkpIDogWzBdO1xuICAgIGlmIChtYXRjaFsyXSkge1xuICAgICAgdmVyLmxlbmd0aCsrO1xuICAgICAgdmVyLnB1c2guYXBwbHkodmVyLCBzcGxpdEFuZENvbnZlcnQobWF0Y2hbMl0pKTtcbiAgICB9XG5cbiAgICAvLyByZW1vdmUgdHJhaWxpbmcgYW55IG1hdGNoZXJzXG4gICAgbGV0IGxhc3QgPSB2ZXJbdmVyLmxlbmd0aCAtIDFdO1xuICAgIHdoaWxlIChcbiAgICAgIHZlci5sZW5ndGggJiZcbiAgICAgIChsYXN0ID09PSB1bmRlZmluZWQgfHwgL15bKnhYXSQvLnRlc3QoLyoqIEB0eXBlIHtzdHJpbmd9ICovIChsYXN0KSkpXG4gICAgKSB7XG4gICAgICB2ZXIucG9wKCk7XG4gICAgICBsYXN0ID0gdmVyW3Zlci5sZW5ndGggLSAxXTtcbiAgICB9XG5cbiAgICByZXR1cm4gdmVyO1xuICB9O1xuICB2YXIgdG9GaXhlZCA9IGZ1bmN0aW9uKHJhbmdlKSB7XG4gICAgaWYgKHJhbmdlLmxlbmd0aCA9PT0gMSkge1xuICAgICAgLy8gU3BlY2lhbCBjYXNlIGZvciBcIipcIiBpcyBcIngueC54XCIgaW5zdGVhZCBvZiBcIj1cIlxuICAgICAgcmV0dXJuIFswXTtcbiAgICB9IGVsc2UgaWYgKHJhbmdlLmxlbmd0aCA9PT0gMikge1xuICAgICAgLy8gU3BlY2lhbCBjYXNlIGZvciBcIjFcIiBpcyBcIjEueC54XCIgaW5zdGVhZCBvZiBcIj0xXCJcbiAgICAgIHJldHVybiBbMV0uY29uY2F0KHJhbmdlLnNsaWNlKDEpKTtcbiAgICB9IGVsc2UgaWYgKHJhbmdlLmxlbmd0aCA9PT0gMykge1xuICAgICAgLy8gU3BlY2lhbCBjYXNlIGZvciBcIjEuMlwiIGlzIFwiMS4yLnhcIiBpbnN0ZWFkIG9mIFwiPTEuMlwiXG4gICAgICByZXR1cm4gWzJdLmNvbmNhdChyYW5nZS5zbGljZSgxKSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJldHVybiBbcmFuZ2UubGVuZ3RoXS5jb25jYXQocmFuZ2Uuc2xpY2UoMSkpO1xuICAgIH1cbiAgfTtcbiAgdmFyIG5lZ2F0ZSA9IGZ1bmN0aW9uKHJhbmdlKSB7XG4gICAgcmV0dXJuIFstcmFuZ2VbMF0gLSAxXS5jb25jYXQocmFuZ2Uuc2xpY2UoMSkpO1xuICB9O1xuICB2YXIgcGFyc2VTaW1wbGUgPSBmdW5jdGlvbihzdHIpIHtcbiAgICAvLyBzaW1wbGUgICAgICAgOjo9IHByaW1pdGl2ZSB8IHBhcnRpYWwgfCB0aWxkZSB8IGNhcmV0XG4gICAgLy8gcHJpbWl0aXZlICAgIDo6PSAoICc8JyB8ICc+JyB8ICc+PScgfCAnPD0nIHwgJz0nIHwgJyEnICkgKCAnICcgKSAqIHBhcnRpYWxcbiAgICAvLyB0aWxkZSAgICAgICAgOjo9ICd+JyAoICcgJyApICogcGFydGlhbFxuICAgIC8vIGNhcmV0ICAgICAgICA6Oj0gJ14nICggJyAnICkgKiBwYXJ0aWFsXG4gICAgY29uc3QgbWF0Y2ggPSAvXihcXF58fnw8PXw8fD49fD58PXx2fCEpLy5leGVjKHN0cik7XG4gICAgY29uc3Qgc3RhcnQgPSBtYXRjaCA/IG1hdGNoWzBdIDogXCJcIjtcbiAgICBjb25zdCByZW1haW5kZXIgPSBwYXJzZVBhcnRpYWwoXG4gICAgICBzdGFydC5sZW5ndGggPyBzdHIuc2xpY2Uoc3RhcnQubGVuZ3RoKS50cmltKCkgOiBzdHIudHJpbSgpXG4gICAgKTtcbiAgICBzd2l0Y2ggKHN0YXJ0KSB7XG4gICAgICBjYXNlIFwiXlwiOlxuICAgICAgICBpZiAocmVtYWluZGVyLmxlbmd0aCA+IDEgJiYgcmVtYWluZGVyWzFdID09PSAwKSB7XG4gICAgICAgICAgaWYgKHJlbWFpbmRlci5sZW5ndGggPiAyICYmIHJlbWFpbmRlclsyXSA9PT0gMCkge1xuICAgICAgICAgICAgcmV0dXJuIFszXS5jb25jYXQocmVtYWluZGVyLnNsaWNlKDEpKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmV0dXJuIFsyXS5jb25jYXQocmVtYWluZGVyLnNsaWNlKDEpKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gWzFdLmNvbmNhdChyZW1haW5kZXIuc2xpY2UoMSkpO1xuICAgICAgY2FzZSBcIn5cIjpcbiAgICAgICAgcmV0dXJuIFsyXS5jb25jYXQocmVtYWluZGVyLnNsaWNlKDEpKTtcbiAgICAgIGNhc2UgXCI+PVwiOlxuICAgICAgICByZXR1cm4gcmVtYWluZGVyO1xuICAgICAgY2FzZSBcIj1cIjpcbiAgICAgIGNhc2UgXCJ2XCI6XG4gICAgICBjYXNlIFwiXCI6XG4gICAgICAgIHJldHVybiB0b0ZpeGVkKHJlbWFpbmRlcik7XG4gICAgICBjYXNlIFwiPFwiOlxuICAgICAgICByZXR1cm4gbmVnYXRlKHJlbWFpbmRlcik7XG4gICAgICBjYXNlIFwiPlwiOiB7XG4gICAgICAgIC8vIGFuZCggPj0sIG5vdCggPSApICkgPT4gPj0sID0sIG5vdCwgYW5kXG4gICAgICAgIGNvbnN0IGZpeGVkID0gdG9GaXhlZChyZW1haW5kZXIpO1xuICAgICAgICByZXR1cm4gWywgZml4ZWQsIDAsIHJlbWFpbmRlciwgMl07XG4gICAgICB9XG4gICAgICBjYXNlIFwiPD1cIjpcbiAgICAgICAgLy8gb3IoIDwsID0gKSA9PiA8LCA9LCBvclxuICAgICAgICByZXR1cm4gWywgdG9GaXhlZChyZW1haW5kZXIpLCBuZWdhdGUocmVtYWluZGVyKSwgMV07XG4gICAgICBjYXNlIFwiIVwiOiB7XG4gICAgICAgIC8vIG5vdCA9XG4gICAgICAgIGNvbnN0IGZpeGVkID0gdG9GaXhlZChyZW1haW5kZXIpO1xuICAgICAgICByZXR1cm4gWywgZml4ZWQsIDBdO1xuICAgICAgfVxuICAgICAgZGVmYXVsdDpcbiAgICAgICAgdGhyb3cgbmV3IEVycm9yKFwiVW5leHBlY3RlZCBzdGFydCB2YWx1ZVwiKTtcbiAgICB9XG4gIH07XG4gIHZhciBjb21iaW5lID0gZnVuY3Rpb24oaXRlbXMsIGZuKSB7XG4gICAgaWYgKGl0ZW1zLmxlbmd0aCA9PT0gMSkgcmV0dXJuIGl0ZW1zWzBdO1xuICAgIGNvbnN0IGFyciA9IFtdO1xuICAgIGZvciAoY29uc3QgaXRlbSBvZiBpdGVtcy5zbGljZSgpLnJldmVyc2UoKSkge1xuICAgICAgaWYgKDAgaW4gaXRlbSkge1xuICAgICAgICBhcnIucHVzaChpdGVtKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGFyci5wdXNoLmFwcGx5KGFyciwgaXRlbS5zbGljZSgxKSk7XG4gICAgICB9XG4gICAgfVxuICAgIHJldHVybiBbLF0uY29uY2F0KGFyciwgaXRlbXMuc2xpY2UoMSkubWFwKCgpID0+IGZuKSk7XG4gIH07XG4gIHZhciBwYXJzZVJhbmdlID0gZnVuY3Rpb24oc3RyKSB7XG4gICAgLy8gcmFuZ2UgICAgICA6Oj0gaHlwaGVuIHwgc2ltcGxlICggJyAnICggJyAnICkgKiBzaW1wbGUgKSAqIHwgJydcbiAgICAvLyBoeXBoZW4gICAgIDo6PSBwYXJ0aWFsICggJyAnICkgKiAnIC0gJyAoICcgJyApICogcGFydGlhbFxuICAgIGNvbnN0IGl0ZW1zID0gc3RyLnNwbGl0KC9cXHMrLVxccysvKTtcbiAgICBpZiAoaXRlbXMubGVuZ3RoID09PSAxKSB7XG5cdFx0XHRzdHIgPSBzdHIudHJpbSgpO1xuXHRcdFx0Y29uc3QgaXRlbXMgPSBbXTtcblx0XHRcdGNvbnN0IHIgPSAvWy0wLTlBLVphLXpdXFxzKy9nO1xuXHRcdFx0dmFyIHN0YXJ0ID0gMDtcblx0XHRcdHZhciBtYXRjaDtcblx0XHRcdHdoaWxlICgobWF0Y2ggPSByLmV4ZWMoc3RyKSkpIHtcblx0XHRcdFx0Y29uc3QgZW5kID0gbWF0Y2guaW5kZXggKyAxO1xuXHRcdFx0XHRpdGVtcy5wdXNoKHBhcnNlU2ltcGxlKHN0ci5zbGljZShzdGFydCwgZW5kKS50cmltKCkpKTtcblx0XHRcdFx0c3RhcnQgPSBlbmQ7XG5cdFx0XHR9XG5cdFx0XHRpdGVtcy5wdXNoKHBhcnNlU2ltcGxlKHN0ci5zbGljZShzdGFydCkudHJpbSgpKSk7XG4gICAgICByZXR1cm4gY29tYmluZShpdGVtcywgMik7XG4gICAgfVxuICAgIGNvbnN0IGEgPSBwYXJzZVBhcnRpYWwoaXRlbXNbMF0pO1xuICAgIGNvbnN0IGIgPSBwYXJzZVBhcnRpYWwoaXRlbXNbMV0pO1xuICAgIC8vID49YSA8PWIgPT4gYW5kKCA+PWEsIG9yKCA8YiwgPWIgKSApID0+ID49YSwgPGIsID1iLCBvciwgYW5kXG4gICAgcmV0dXJuIFssIHRvRml4ZWQoYiksIG5lZ2F0ZShiKSwgMSwgYSwgMl07XG4gIH07XG4gIHZhciBwYXJzZUxvZ2ljYWxPciA9IGZ1bmN0aW9uKHN0cikge1xuICAgIC8vIHJhbmdlLXNldCAgOjo9IHJhbmdlICggbG9naWNhbC1vciByYW5nZSApICpcbiAgICAvLyBsb2dpY2FsLW9yIDo6PSAoICcgJyApICogJ3x8JyAoICcgJyApICpcbiAgICBjb25zdCBpdGVtcyA9IHN0ci5zcGxpdCgvXFxzKlxcfFxcfFxccyovKS5tYXAocGFyc2VSYW5nZSk7XG4gICAgcmV0dXJuIGNvbWJpbmUoaXRlbXMsIDEpO1xuICB9O1xuICByZXR1cm4gcGFyc2VMb2dpY2FsT3Ioc3RyKTtcbn07XG52YXIgcGFyc2VWZXJzaW9uID0gZnVuY3Rpb24oc3RyKSB7XG5cdHZhciBtYXRjaCA9IC9eKFteLStdKyk/KD86LShbXitdKykpPyg/OlxcKyguKykpPyQvLmV4ZWMoc3RyKTtcblx0LyoqIEB0eXBlIHsoc3RyaW5nfG51bWJlcnx1bmRlZmluZWR8W10pW119ICovXG5cdHZhciB2ZXIgPSBtYXRjaFsxXSA/IHNwbGl0QW5kQ29udmVydChtYXRjaFsxXSkgOiBbXTtcblx0aWYgKG1hdGNoWzJdKSB7XG5cdFx0dmVyLmxlbmd0aCsrO1xuXHRcdHZlci5wdXNoLmFwcGx5KHZlciwgc3BsaXRBbmRDb252ZXJ0KG1hdGNoWzJdKSk7XG5cdH1cblx0aWYgKG1hdGNoWzNdKSB7XG5cdFx0dmVyLnB1c2goW10pO1xuXHRcdHZlci5wdXNoLmFwcGx5KHZlciwgc3BsaXRBbmRDb252ZXJ0KG1hdGNoWzNdKSk7XG5cdH1cblx0cmV0dXJuIHZlcjtcbn1cbnZhciB2ZXJzaW9uTHQgPSBmdW5jdGlvbihhLCBiKSB7XG5cdGEgPSBwYXJzZVZlcnNpb24oYSk7XG5cdGIgPSBwYXJzZVZlcnNpb24oYik7XG5cdHZhciBpID0gMDtcblx0Zm9yICg7Oykge1xuXHRcdC8vIGEgICAgICAgYiAgRU9BICAgICBvYmplY3QgIHVuZGVmaW5lZCAgbnVtYmVyICBzdHJpbmdcblx0XHQvLyBFT0EgICAgICAgIGEgPT0gYiAgYSA8IGIgICBiIDwgYSAgICAgIGEgPCBiICAgYSA8IGJcblx0XHQvLyBvYmplY3QgICAgIGIgPCBhICAgKDApICAgICBiIDwgYSAgICAgIGEgPCBiICAgYSA8IGJcblx0XHQvLyB1bmRlZmluZWQgIGEgPCBiICAgYSA8IGIgICAoMCkgICAgICAgIGEgPCBiICAgYSA8IGJcblx0XHQvLyBudW1iZXIgICAgIGIgPCBhICAgYiA8IGEgICBiIDwgYSAgICAgICgxKSAgICAgYSA8IGJcblx0XHQvLyBzdHJpbmcgICAgIGIgPCBhICAgYiA8IGEgICBiIDwgYSAgICAgIGIgPCBhICAgKDEpXG5cdFx0Ly8gRU9BIGVuZCBvZiBhcnJheVxuXHRcdC8vICgwKSBjb250aW51ZSBvblxuXHRcdC8vICgxKSBjb21wYXJlIHRoZW0gdmlhIFwiPFwiXG5cblx0XHQvLyBIYW5kbGVzIGZpcnN0IHJvdyBpbiB0YWJsZVxuXHRcdGlmIChpID49IGEubGVuZ3RoKSByZXR1cm4gaSA8IGIubGVuZ3RoICYmICh0eXBlb2YgYltpXSlbMF0gIT0gXCJ1XCI7XG5cblx0XHR2YXIgYVZhbHVlID0gYVtpXTtcblx0XHR2YXIgYVR5cGUgPSAodHlwZW9mIGFWYWx1ZSlbMF07XG5cblx0XHQvLyBIYW5kbGVzIGZpcnN0IGNvbHVtbiBpbiB0YWJsZVxuXHRcdGlmIChpID49IGIubGVuZ3RoKSByZXR1cm4gYVR5cGUgPT0gXCJ1XCI7XG5cblx0XHR2YXIgYlZhbHVlID0gYltpXTtcblx0XHR2YXIgYlR5cGUgPSAodHlwZW9mIGJWYWx1ZSlbMF07XG5cblx0XHRpZiAoYVR5cGUgPT0gYlR5cGUpIHtcblx0XHRcdGlmIChhVHlwZSAhPSBcIm9cIiAmJiBhVHlwZSAhPSBcInVcIiAmJiBhVmFsdWUgIT0gYlZhbHVlKSB7XG5cdFx0XHRcdHJldHVybiBhVmFsdWUgPCBiVmFsdWU7XG5cdFx0XHR9XG5cdFx0XHRpKys7XG5cdFx0fSBlbHNlIHtcblx0XHRcdC8vIEhhbmRsZXMgcmVtYWluaW5nIGNhc2VzXG5cdFx0XHRpZiAoYVR5cGUgPT0gXCJvXCIgJiYgYlR5cGUgPT0gXCJuXCIpIHJldHVybiB0cnVlO1xuXHRcdFx0cmV0dXJuIGJUeXBlID09IFwic1wiIHx8IGFUeXBlID09IFwidVwiO1xuXHRcdH1cblx0fVxufVxudmFyIHJhbmdlVG9TdHJpbmcgPSBmdW5jdGlvbihyYW5nZSkge1xuXHR2YXIgZml4Q291bnQgPSByYW5nZVswXTtcblx0dmFyIHN0ciA9IFwiXCI7XG5cdGlmIChyYW5nZS5sZW5ndGggPT09IDEpIHtcblx0XHRyZXR1cm4gXCIqXCI7XG5cdH0gZWxzZSBpZiAoZml4Q291bnQgKyAwLjUpIHtcblx0XHRzdHIgKz1cblx0XHRcdGZpeENvdW50ID09IDBcblx0XHRcdFx0PyBcIj49XCJcblx0XHRcdFx0OiBmaXhDb3VudCA9PSAtMVxuXHRcdFx0XHQ/IFwiPFwiXG5cdFx0XHRcdDogZml4Q291bnQgPT0gMVxuXHRcdFx0XHQ/IFwiXlwiXG5cdFx0XHRcdDogZml4Q291bnQgPT0gMlxuXHRcdFx0XHQ/IFwiflwiXG5cdFx0XHRcdDogZml4Q291bnQgPiAwXG5cdFx0XHRcdD8gXCI9XCJcblx0XHRcdFx0OiBcIiE9XCI7XG5cdFx0dmFyIG5lZWREb3QgPSAxO1xuXHRcdGZvciAodmFyIGkgPSAxOyBpIDwgcmFuZ2UubGVuZ3RoOyBpKyspIHtcblx0XHRcdHZhciBpdGVtID0gcmFuZ2VbaV07XG5cdFx0XHR2YXIgdCA9ICh0eXBlb2YgaXRlbSlbMF07XG5cdFx0XHRuZWVkRG90LS07XG5cdFx0XHRzdHIgKz1cblx0XHRcdFx0dCA9PSBcInVcIlxuXHRcdFx0XHRcdD8gLy8gdW5kZWZpbmVkOiBwcmVyZWxlYXNlIG1hcmtlciwgYWRkIGFuIFwiLVwiXG5cdFx0XHRcdFx0ICBcIi1cIlxuXHRcdFx0XHRcdDogLy8gbnVtYmVyIG9yIHN0cmluZzogYWRkIHRoZSBpdGVtLCBzZXQgZmxhZyB0byBhZGQgYW4gXCIuXCIgYmV0d2VlbiB0d28gb2YgdGhlbVxuXHRcdFx0XHRcdCAgKG5lZWREb3QgPiAwID8gXCIuXCIgOiBcIlwiKSArICgobmVlZERvdCA9IDIpLCBpdGVtKTtcblx0XHR9XG5cdFx0cmV0dXJuIHN0cjtcblx0fSBlbHNlIHtcblx0XHR2YXIgc3RhY2sgPSBbXTtcblx0XHRmb3IgKHZhciBpID0gMTsgaSA8IHJhbmdlLmxlbmd0aDsgaSsrKSB7XG5cdFx0XHR2YXIgaXRlbSA9IHJhbmdlW2ldO1xuXHRcdFx0c3RhY2sucHVzaChcblx0XHRcdFx0aXRlbSA9PT0gMFxuXHRcdFx0XHRcdD8gXCJub3QoXCIgKyBwb3AoKSArIFwiKVwiXG5cdFx0XHRcdFx0OiBpdGVtID09PSAxXG5cdFx0XHRcdFx0PyBcIihcIiArIHBvcCgpICsgXCIgfHwgXCIgKyBwb3AoKSArIFwiKVwiXG5cdFx0XHRcdFx0OiBpdGVtID09PSAyXG5cdFx0XHRcdFx0PyBzdGFjay5wb3AoKSArIFwiIFwiICsgc3RhY2sucG9wKClcblx0XHRcdFx0XHQ6IHJhbmdlVG9TdHJpbmcoaXRlbSlcblx0XHRcdCk7XG5cdFx0fVxuXHRcdHJldHVybiBwb3AoKTtcblx0fVxuXHRmdW5jdGlvbiBwb3AoKSB7XG5cdFx0cmV0dXJuIHN0YWNrLnBvcCgpLnJlcGxhY2UoL15cXCgoLispXFwpJC8sIFwiJDFcIik7XG5cdH1cbn1cbnZhciBzYXRpc2Z5ID0gZnVuY3Rpb24ocmFuZ2UsIHZlcnNpb24pIHtcblx0aWYgKDAgaW4gcmFuZ2UpIHtcblx0XHR2ZXJzaW9uID0gcGFyc2VWZXJzaW9uKHZlcnNpb24pO1xuXHRcdHZhciBmaXhDb3VudCA9IC8qKiBAdHlwZSB7bnVtYmVyfSAqLyAocmFuZ2VbMF0pO1xuXHRcdC8vIHdoZW4gbmVnYXRlZCBpcyBzZXQgaXQgc3dpbGwgc2V0IGZvciA8IGluc3RlYWQgb2YgPj1cblx0XHR2YXIgbmVnYXRlZCA9IGZpeENvdW50IDwgMDtcblx0XHRpZiAobmVnYXRlZCkgZml4Q291bnQgPSAtZml4Q291bnQgLSAxO1xuXHRcdGZvciAodmFyIGkgPSAwLCBqID0gMSwgaXNFcXVhbCA9IHRydWU7IDsgaisrLCBpKyspIHtcblx0XHRcdC8vIGNzcGVsbDp3b3JkIG5lcXVhbCBuZXF1XG5cblx0XHRcdC8vIHdoZW4gaXNFcXVhbCA9IHRydWU6XG5cdFx0XHQvLyByYW5nZSAgICAgICAgIHZlcnNpb246IEVPQS9vYmplY3QgIHVuZGVmaW5lZCAgbnVtYmVyICAgIHN0cmluZ1xuXHRcdFx0Ly8gRU9BICAgICAgICAgICAgICAgICAgICBlcXVhbCAgICAgICBibG9jayAgICAgIGJpZy12ZXIgICBiaWctdmVyXG5cdFx0XHQvLyB1bmRlZmluZWQgICAgICAgICAgICAgIGJpZ2dlciAgICAgIG5leHQgICAgICAgYmlnLXZlciAgIGJpZy12ZXJcblx0XHRcdC8vIG51bWJlciAgICAgICAgICAgICAgICAgc21hbGxlciAgICAgYmxvY2sgICAgICBjbXAgICAgICAgYmlnLWNtcFxuXHRcdFx0Ly8gZml4ZWQgbnVtYmVyICAgICAgICAgICBzbWFsbGVyICAgICBibG9jayAgICAgIGNtcC1maXggICBkaWZmZXJcblx0XHRcdC8vIHN0cmluZyAgICAgICAgICAgICAgICAgc21hbGxlciAgICAgYmxvY2sgICAgICBkaWZmZXIgICAgY21wXG5cdFx0XHQvLyBmaXhlZCBzdHJpbmcgICAgICAgICAgIHNtYWxsZXIgICAgIGJsb2NrICAgICAgc21hbGwtY21wIGNtcC1maXhcblxuXHRcdFx0Ly8gd2hlbiBpc0VxdWFsID0gZmFsc2U6XG5cdFx0XHQvLyByYW5nZSAgICAgICAgIHZlcnNpb246IEVPQS9vYmplY3QgIHVuZGVmaW5lZCAgbnVtYmVyICAgIHN0cmluZ1xuXHRcdFx0Ly8gRU9BICAgICAgICAgICAgICAgICAgICBuZXF1YWwgICAgICBibG9jayAgICAgIG5leHQtdmVyICBuZXh0LXZlclxuXHRcdFx0Ly8gdW5kZWZpbmVkICAgICAgICAgICAgICBuZXF1YWwgICAgICBibG9jayAgICAgIG5leHQtdmVyICBuZXh0LXZlclxuXHRcdFx0Ly8gbnVtYmVyICAgICAgICAgICAgICAgICBuZXF1YWwgICAgICBibG9jayAgICAgIG5leHQgICAgICBuZXh0XG5cdFx0XHQvLyBmaXhlZCBudW1iZXIgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dCAgICAgIG5leHQgICAodGhpcyBuZXZlciBoYXBwZW5zKVxuXHRcdFx0Ly8gc3RyaW5nICAgICAgICAgICAgICAgICBuZXF1YWwgICAgICBibG9jayAgICAgIG5leHQgICAgICBuZXh0XG5cdFx0XHQvLyBmaXhlZCBzdHJpbmcgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dCAgICAgIG5leHQgICAodGhpcyBuZXZlciBoYXBwZW5zKVxuXG5cdFx0XHQvLyBFT0EgZW5kIG9mIGFycmF5XG5cdFx0XHQvLyBlcXVhbCAodmVyc2lvbiBpcyBlcXVhbCByYW5nZSk6XG5cdFx0XHQvLyAgIHdoZW4gIW5lZ2F0ZWQ6IHJldHVybiB0cnVlLFxuXHRcdFx0Ly8gICB3aGVuIG5lZ2F0ZWQ6IHJldHVybiBmYWxzZVxuXHRcdFx0Ly8gYmlnZ2VyICh2ZXJzaW9uIGlzIGJpZ2dlciBhcyByYW5nZSk6XG5cdFx0XHQvLyAgIHdoZW4gZml4ZWQ6IHJldHVybiBmYWxzZSxcblx0XHRcdC8vICAgd2hlbiAhbmVnYXRlZDogcmV0dXJuIHRydWUsXG5cdFx0XHQvLyAgIHdoZW4gbmVnYXRlZDogcmV0dXJuIGZhbHNlLFxuXHRcdFx0Ly8gc21hbGxlciAodmVyc2lvbiBpcyBzbWFsbGVyIGFzIHJhbmdlKTpcblx0XHRcdC8vICAgd2hlbiAhbmVnYXRlZDogcmV0dXJuIGZhbHNlLFxuXHRcdFx0Ly8gICB3aGVuIG5lZ2F0ZWQ6IHJldHVybiB0cnVlXG5cdFx0XHQvLyBuZXF1YWwgKHZlcnNpb24gaXMgbm90IGVxdWFsIHJhbmdlICg+IHJlc3AgPCkpOiByZXR1cm4gdHJ1ZVxuXHRcdFx0Ly8gYmxvY2sgKHZlcnNpb24gaXMgaW4gZGlmZmVyZW50IHByZXJlbGVhc2UgYXJlYSk6IHJldHVybiBmYWxzZVxuXHRcdFx0Ly8gZGlmZmVyICh2ZXJzaW9uIGlzIGRpZmZlcmVudCBmcm9tIGZpeGVkIHJhbmdlIChzdHJpbmcgdnMuIG51bWJlcikpOiByZXR1cm4gZmFsc2Vcblx0XHRcdC8vIG5leHQ6IGNvbnRpbnVlcyB0byB0aGUgbmV4dCBpdGVtc1xuXHRcdFx0Ly8gbmV4dC12ZXI6IHdoZW4gZml4ZWQ6IHJldHVybiBmYWxzZSwgY29udGludWVzIHRvIHRoZSBuZXh0IGl0ZW0gb25seSBmb3IgdGhlIHZlcnNpb24sIHNldHMgaXNFcXVhbD1mYWxzZVxuXHRcdFx0Ly8gYmlnLXZlcjogd2hlbiBmaXhlZCB8fCBuZWdhdGVkOiByZXR1cm4gZmFsc2UsIGNvbnRpbnVlcyB0byB0aGUgbmV4dCBpdGVtIG9ubHkgZm9yIHRoZSB2ZXJzaW9uLCBzZXRzIGlzRXF1YWw9ZmFsc2Vcblx0XHRcdC8vIG5leHQtbmVxdTogY29udGludWVzIHRvIHRoZSBuZXh0IGl0ZW1zLCBzZXRzIGlzRXF1YWw9ZmFsc2Vcblx0XHRcdC8vIGNtcCAobmVnYXRlZCA9PT0gZmFsc2UpOiB2ZXJzaW9uIDwgcmFuZ2UgPT4gcmV0dXJuIGZhbHNlLCB2ZXJzaW9uID4gcmFuZ2UgPT4gbmV4dC1uZXF1LCBlbHNlID0+IG5leHRcblx0XHRcdC8vIGNtcCAobmVnYXRlZCA9PT0gdHJ1ZSk6IHZlcnNpb24gPiByYW5nZSA9PiByZXR1cm4gZmFsc2UsIHZlcnNpb24gPCByYW5nZSA9PiBuZXh0LW5lcXUsIGVsc2UgPT4gbmV4dFxuXHRcdFx0Ly8gY21wLWZpeDogdmVyc2lvbiA9PSByYW5nZSA9PiBuZXh0LCBlbHNlID0+IHJldHVybiBmYWxzZVxuXHRcdFx0Ly8gYmlnLWNtcDogd2hlbiBuZWdhdGVkID0+IHJldHVybiBmYWxzZSwgZWxzZSA9PiBuZXh0LW5lcXVcblx0XHRcdC8vIHNtYWxsLWNtcDogd2hlbiBuZWdhdGVkID0+IG5leHQtbmVxdSwgZWxzZSA9PiByZXR1cm4gZmFsc2VcblxuXHRcdFx0dmFyIHJhbmdlVHlwZSA9IGogPCByYW5nZS5sZW5ndGggPyAodHlwZW9mIHJhbmdlW2pdKVswXSA6IFwiXCI7XG5cblx0XHRcdHZhciB2ZXJzaW9uVmFsdWU7XG5cdFx0XHR2YXIgdmVyc2lvblR5cGU7XG5cblx0XHRcdC8vIEhhbmRsZXMgZmlyc3QgY29sdW1uIGluIGJvdGggdGFibGVzIChlbmQgb2YgdmVyc2lvbiBvciBvYmplY3QpXG5cdFx0XHRpZiAoXG5cdFx0XHRcdGkgPj0gdmVyc2lvbi5sZW5ndGggfHxcblx0XHRcdFx0KCh2ZXJzaW9uVmFsdWUgPSB2ZXJzaW9uW2ldKSxcblx0XHRcdFx0KHZlcnNpb25UeXBlID0gKHR5cGVvZiB2ZXJzaW9uVmFsdWUpWzBdKSA9PSBcIm9cIilcblx0XHRcdCkge1xuXHRcdFx0XHQvLyBIYW5kbGVzIG5lcXVhbFxuXHRcdFx0XHRpZiAoIWlzRXF1YWwpIHJldHVybiB0cnVlO1xuXHRcdFx0XHQvLyBIYW5kbGVzIGJpZ2dlclxuXHRcdFx0XHRpZiAocmFuZ2VUeXBlID09IFwidVwiKSByZXR1cm4gaiA+IGZpeENvdW50ICYmICFuZWdhdGVkO1xuXHRcdFx0XHQvLyBIYW5kbGVzIGVxdWFsIGFuZCBzbWFsbGVyOiAocmFuZ2UgPT09IEVPQSkgWE9SIG5lZ2F0ZWRcblx0XHRcdFx0cmV0dXJuIChyYW5nZVR5cGUgPT0gXCJcIikgIT0gbmVnYXRlZDsgLy8gZXF1YWwgKyBzbWFsbGVyXG5cdFx0XHR9XG5cblx0XHRcdC8vIEhhbmRsZXMgc2Vjb25kIGNvbHVtbiBpbiBib3RoIHRhYmxlcyAodmVyc2lvbiA9IHVuZGVmaW5lZClcblx0XHRcdGlmICh2ZXJzaW9uVHlwZSA9PSBcInVcIikge1xuXHRcdFx0XHRpZiAoIWlzRXF1YWwgfHwgcmFuZ2VUeXBlICE9IFwidVwiKSB7XG5cdFx0XHRcdFx0cmV0dXJuIGZhbHNlO1xuXHRcdFx0XHR9XG5cdFx0XHR9XG5cblx0XHRcdC8vIHN3aXRjaCBiZXR3ZWVuIGZpcnN0IGFuZCBzZWNvbmQgdGFibGVcblx0XHRcdGVsc2UgaWYgKGlzRXF1YWwpIHtcblx0XHRcdFx0Ly8gSGFuZGxlIGRpYWdvbmFsXG5cdFx0XHRcdGlmIChyYW5nZVR5cGUgPT0gdmVyc2lvblR5cGUpIHtcblx0XHRcdFx0XHRpZiAoaiA8PSBmaXhDb3VudCkge1xuXHRcdFx0XHRcdFx0Ly8gSGFuZGxlcyBcImNtcC1maXhcIiBjYXNlc1xuXHRcdFx0XHRcdFx0aWYgKHZlcnNpb25WYWx1ZSAhPSByYW5nZVtqXSkge1xuXHRcdFx0XHRcdFx0XHRyZXR1cm4gZmFsc2U7XG5cdFx0XHRcdFx0XHR9XG5cdFx0XHRcdFx0fSBlbHNlIHtcblx0XHRcdFx0XHRcdC8vIEhhbmRsZXMgXCJjbXBcIiBjYXNlc1xuXHRcdFx0XHRcdFx0aWYgKG5lZ2F0ZWQgPyB2ZXJzaW9uVmFsdWUgPiByYW5nZVtqXSA6IHZlcnNpb25WYWx1ZSA8IHJhbmdlW2pdKSB7XG5cdFx0XHRcdFx0XHRcdHJldHVybiBmYWxzZTtcblx0XHRcdFx0XHRcdH1cblx0XHRcdFx0XHRcdGlmICh2ZXJzaW9uVmFsdWUgIT0gcmFuZ2Vbal0pIGlzRXF1YWwgPSBmYWxzZTtcblx0XHRcdFx0XHR9XG5cdFx0XHRcdH1cblxuXHRcdFx0XHQvLyBIYW5kbGUgYmlnLXZlclxuXHRcdFx0XHRlbHNlIGlmIChyYW5nZVR5cGUgIT0gXCJzXCIgJiYgcmFuZ2VUeXBlICE9IFwiblwiKSB7XG5cdFx0XHRcdFx0aWYgKG5lZ2F0ZWQgfHwgaiA8PSBmaXhDb3VudCkgcmV0dXJuIGZhbHNlO1xuXHRcdFx0XHRcdGlzRXF1YWwgPSBmYWxzZTtcblx0XHRcdFx0XHRqLS07XG5cdFx0XHRcdH1cblxuXHRcdFx0XHQvLyBIYW5kbGUgZGlmZmVyLCBiaWctY21wIGFuZCBzbWFsbC1jbXBcblx0XHRcdFx0ZWxzZSBpZiAoaiA8PSBmaXhDb3VudCB8fCB2ZXJzaW9uVHlwZSA8IHJhbmdlVHlwZSAhPSBuZWdhdGVkKSB7XG5cdFx0XHRcdFx0cmV0dXJuIGZhbHNlO1xuXHRcdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHRcdGlzRXF1YWwgPSBmYWxzZTtcblx0XHRcdFx0fVxuXHRcdFx0fSBlbHNlIHtcblx0XHRcdFx0Ly8gSGFuZGxlcyBhbGwgXCJuZXh0LXZlclwiIGNhc2VzIGluIHRoZSBzZWNvbmQgdGFibGVcblx0XHRcdFx0aWYgKHJhbmdlVHlwZSAhPSBcInNcIiAmJiByYW5nZVR5cGUgIT0gXCJuXCIpIHtcblx0XHRcdFx0XHRpc0VxdWFsID0gZmFsc2U7XG5cdFx0XHRcdFx0ai0tO1xuXHRcdFx0XHR9XG5cblx0XHRcdFx0Ly8gbmV4dCBpcyBhcHBsaWVkIGJ5IGRlZmF1bHRcblx0XHRcdH1cblx0XHR9XG5cdH1cblx0LyoqIEB0eXBlIHsoYm9vbGVhbiB8IG51bWJlcilbXX0gKi9cblx0dmFyIHN0YWNrID0gW107XG5cdHZhciBwID0gc3RhY2sucG9wLmJpbmQoc3RhY2spO1xuXHRmb3IgKHZhciBpID0gMTsgaSA8IHJhbmdlLmxlbmd0aDsgaSsrKSB7XG5cdFx0dmFyIGl0ZW0gPSAvKiogQHR5cGUge1NlbVZlclJhbmdlIHwgMCB8IDEgfCAyfSAqLyAocmFuZ2VbaV0pO1xuXHRcdHN0YWNrLnB1c2goXG5cdFx0XHRpdGVtID09IDFcblx0XHRcdFx0PyBwKCkgfCBwKClcblx0XHRcdFx0OiBpdGVtID09IDJcblx0XHRcdFx0PyBwKCkgJiBwKClcblx0XHRcdFx0OiBpdGVtXG5cdFx0XHRcdD8gc2F0aXNmeShpdGVtLCB2ZXJzaW9uKVxuXHRcdFx0XHQ6ICFwKClcblx0XHQpO1xuXHR9XG5cdHJldHVybiAhIXAoKTtcbn1cbnZhciBlbnN1cmVFeGlzdGVuY2UgPSBmdW5jdGlvbihzY29wZU5hbWUsIGtleSkge1xuXHR2YXIgc2NvcGUgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLlNbc2NvcGVOYW1lXTtcblx0aWYoIXNjb3BlIHx8ICFfX3dlYnBhY2tfcmVxdWlyZV9fLm8oc2NvcGUsIGtleSkpIHRocm93IG5ldyBFcnJvcihcIlNoYXJlZCBtb2R1bGUgXCIgKyBrZXkgKyBcIiBkb2Vzbid0IGV4aXN0IGluIHNoYXJlZCBzY29wZSBcIiArIHNjb3BlTmFtZSk7XG5cdHJldHVybiBzY29wZTtcbn07XG52YXIgZmluZFZlcnNpb24gPSBmdW5jdGlvbihzY29wZSwga2V5KSB7XG5cdHZhciB2ZXJzaW9ucyA9IHNjb3BlW2tleV07XG5cdHZhciBrZXkgPSBPYmplY3Qua2V5cyh2ZXJzaW9ucykucmVkdWNlKGZ1bmN0aW9uKGEsIGIpIHtcblx0XHRyZXR1cm4gIWEgfHwgdmVyc2lvbkx0KGEsIGIpID8gYiA6IGE7XG5cdH0sIDApO1xuXHRyZXR1cm4ga2V5ICYmIHZlcnNpb25zW2tleV1cbn07XG52YXIgZmluZFNpbmdsZXRvblZlcnNpb25LZXkgPSBmdW5jdGlvbihzY29wZSwga2V5KSB7XG5cdHZhciB2ZXJzaW9ucyA9IHNjb3BlW2tleV07XG5cdHJldHVybiBPYmplY3Qua2V5cyh2ZXJzaW9ucykucmVkdWNlKGZ1bmN0aW9uKGEsIGIpIHtcblx0XHRyZXR1cm4gIWEgfHwgKCF2ZXJzaW9uc1thXS5sb2FkZWQgJiYgdmVyc2lvbkx0KGEsIGIpKSA/IGIgOiBhO1xuXHR9LCAwKTtcbn07XG52YXIgZ2V0SW52YWxpZFNpbmdsZXRvblZlcnNpb25NZXNzYWdlID0gZnVuY3Rpb24oc2NvcGUsIGtleSwgdmVyc2lvbiwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHJldHVybiBcIlVuc2F0aXNmaWVkIHZlcnNpb24gXCIgKyB2ZXJzaW9uICsgXCIgZnJvbSBcIiArICh2ZXJzaW9uICYmIHNjb3BlW2tleV1bdmVyc2lvbl0uZnJvbSkgKyBcIiBvZiBzaGFyZWQgc2luZ2xldG9uIG1vZHVsZSBcIiArIGtleSArIFwiIChyZXF1aXJlZCBcIiArIHJhbmdlVG9TdHJpbmcocmVxdWlyZWRWZXJzaW9uKSArIFwiKVwiXG59O1xudmFyIGdldFNpbmdsZXRvbiA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciB2ZXJzaW9uID0gZmluZFNpbmdsZXRvblZlcnNpb25LZXkoc2NvcGUsIGtleSk7XG5cdHJldHVybiBnZXQoc2NvcGVba2V5XVt2ZXJzaW9uXSk7XG59O1xudmFyIGdldFNpbmdsZXRvblZlcnNpb24gPSBmdW5jdGlvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR2YXIgdmVyc2lvbiA9IGZpbmRTaW5nbGV0b25WZXJzaW9uS2V5KHNjb3BlLCBrZXkpO1xuXHRpZiAoIXNhdGlzZnkocmVxdWlyZWRWZXJzaW9uLCB2ZXJzaW9uKSkgd2FybihnZXRJbnZhbGlkU2luZ2xldG9uVmVyc2lvbk1lc3NhZ2Uoc2NvcGUsIGtleSwgdmVyc2lvbiwgcmVxdWlyZWRWZXJzaW9uKSk7XG5cdHJldHVybiBnZXQoc2NvcGVba2V5XVt2ZXJzaW9uXSk7XG59O1xudmFyIGdldFN0cmljdFNpbmdsZXRvblZlcnNpb24gPSBmdW5jdGlvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR2YXIgdmVyc2lvbiA9IGZpbmRTaW5nbGV0b25WZXJzaW9uS2V5KHNjb3BlLCBrZXkpO1xuXHRpZiAoIXNhdGlzZnkocmVxdWlyZWRWZXJzaW9uLCB2ZXJzaW9uKSkgdGhyb3cgbmV3IEVycm9yKGdldEludmFsaWRTaW5nbGV0b25WZXJzaW9uTWVzc2FnZShzY29wZSwga2V5LCB2ZXJzaW9uLCByZXF1aXJlZFZlcnNpb24pKTtcblx0cmV0dXJuIGdldChzY29wZVtrZXldW3ZlcnNpb25dKTtcbn07XG52YXIgZmluZFZhbGlkVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR2YXIgdmVyc2lvbnMgPSBzY29wZVtrZXldO1xuXHR2YXIga2V5ID0gT2JqZWN0LmtleXModmVyc2lvbnMpLnJlZHVjZShmdW5jdGlvbihhLCBiKSB7XG5cdFx0aWYgKCFzYXRpc2Z5KHJlcXVpcmVkVmVyc2lvbiwgYikpIHJldHVybiBhO1xuXHRcdHJldHVybiAhYSB8fCB2ZXJzaW9uTHQoYSwgYikgPyBiIDogYTtcblx0fSwgMCk7XG5cdHJldHVybiBrZXkgJiYgdmVyc2lvbnNba2V5XVxufTtcbnZhciBnZXRJbnZhbGlkVmVyc2lvbk1lc3NhZ2UgPSBmdW5jdGlvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR2YXIgdmVyc2lvbnMgPSBzY29wZVtrZXldO1xuXHRyZXR1cm4gXCJObyBzYXRpc2Z5aW5nIHZlcnNpb24gKFwiICsgcmFuZ2VUb1N0cmluZyhyZXF1aXJlZFZlcnNpb24pICsgXCIpIG9mIHNoYXJlZCBtb2R1bGUgXCIgKyBrZXkgKyBcIiBmb3VuZCBpbiBzaGFyZWQgc2NvcGUgXCIgKyBzY29wZU5hbWUgKyBcIi5cXG5cIiArXG5cdFx0XCJBdmFpbGFibGUgdmVyc2lvbnM6IFwiICsgT2JqZWN0LmtleXModmVyc2lvbnMpLm1hcChmdW5jdGlvbihrZXkpIHtcblx0XHRyZXR1cm4ga2V5ICsgXCIgZnJvbSBcIiArIHZlcnNpb25zW2tleV0uZnJvbTtcblx0fSkuam9pbihcIiwgXCIpO1xufTtcbnZhciBnZXRWYWxpZFZlcnNpb24gPSBmdW5jdGlvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR2YXIgZW50cnkgPSBmaW5kVmFsaWRWZXJzaW9uKHNjb3BlLCBrZXksIHJlcXVpcmVkVmVyc2lvbik7XG5cdGlmKGVudHJ5KSByZXR1cm4gZ2V0KGVudHJ5KTtcblx0dGhyb3cgbmV3IEVycm9yKGdldEludmFsaWRWZXJzaW9uTWVzc2FnZShzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikpO1xufTtcbnZhciB3YXJuID0gZnVuY3Rpb24obXNnKSB7XG5cdGlmICh0eXBlb2YgY29uc29sZSAhPT0gXCJ1bmRlZmluZWRcIiAmJiBjb25zb2xlLndhcm4pIGNvbnNvbGUud2Fybihtc2cpO1xufTtcbnZhciB3YXJuSW52YWxpZFZlcnNpb24gPSBmdW5jdGlvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikge1xuXHR3YXJuKGdldEludmFsaWRWZXJzaW9uTWVzc2FnZShzY29wZSwgc2NvcGVOYW1lLCBrZXksIHJlcXVpcmVkVmVyc2lvbikpO1xufTtcbnZhciBnZXQgPSBmdW5jdGlvbihlbnRyeSkge1xuXHRlbnRyeS5sb2FkZWQgPSAxO1xuXHRyZXR1cm4gZW50cnkuZ2V0KClcbn07XG52YXIgaW5pdCA9IGZ1bmN0aW9uKGZuKSB7IHJldHVybiBmdW5jdGlvbihzY29wZU5hbWUsIGEsIGIsIGMpIHtcblx0dmFyIHByb21pc2UgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLkkoc2NvcGVOYW1lKTtcblx0aWYgKHByb21pc2UgJiYgcHJvbWlzZS50aGVuKSByZXR1cm4gcHJvbWlzZS50aGVuKGZuLmJpbmQoZm4sIHNjb3BlTmFtZSwgX193ZWJwYWNrX3JlcXVpcmVfXy5TW3Njb3BlTmFtZV0sIGEsIGIsIGMpKTtcblx0cmV0dXJuIGZuKHNjb3BlTmFtZSwgX193ZWJwYWNrX3JlcXVpcmVfXy5TW3Njb3BlTmFtZV0sIGEsIGIsIGMpO1xufTsgfTtcblxudmFyIGxvYWQgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5KSB7XG5cdGVuc3VyZUV4aXN0ZW5jZShzY29wZU5hbWUsIGtleSk7XG5cdHJldHVybiBnZXQoZmluZFZlcnNpb24oc2NvcGUsIGtleSkpO1xufSk7XG52YXIgbG9hZEZhbGxiYWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgZmFsbGJhY2spIHtcblx0cmV0dXJuIHNjb3BlICYmIF9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSA/IGdldChmaW5kVmVyc2lvbihzY29wZSwga2V5KSkgOiBmYWxsYmFjaygpO1xufSk7XG52YXIgbG9hZFZlcnNpb25DaGVjayA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXksIHZlcnNpb24pIHtcblx0ZW5zdXJlRXhpc3RlbmNlKHNjb3BlTmFtZSwga2V5KTtcblx0cmV0dXJuIGdldChmaW5kVmFsaWRWZXJzaW9uKHNjb3BlLCBrZXksIHZlcnNpb24pIHx8IHdhcm5JbnZhbGlkVmVyc2lvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHZlcnNpb24pIHx8IGZpbmRWZXJzaW9uKHNjb3BlLCBrZXkpKTtcbn0pO1xudmFyIGxvYWRTaW5nbGV0b24gPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5KSB7XG5cdGVuc3VyZUV4aXN0ZW5jZShzY29wZU5hbWUsIGtleSk7XG5cdHJldHVybiBnZXRTaW5nbGV0b24oc2NvcGUsIHNjb3BlTmFtZSwga2V5KTtcbn0pO1xudmFyIGxvYWRTaW5nbGV0b25WZXJzaW9uQ2hlY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uKSB7XG5cdGVuc3VyZUV4aXN0ZW5jZShzY29wZU5hbWUsIGtleSk7XG5cdHJldHVybiBnZXRTaW5nbGV0b25WZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbik7XG59KTtcbnZhciBsb2FkU3RyaWN0VmVyc2lvbkNoZWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgdmVyc2lvbikge1xuXHRlbnN1cmVFeGlzdGVuY2Uoc2NvcGVOYW1lLCBrZXkpO1xuXHRyZXR1cm4gZ2V0VmFsaWRWZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbik7XG59KTtcbnZhciBsb2FkU3RyaWN0U2luZ2xldG9uVmVyc2lvbkNoZWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgdmVyc2lvbikge1xuXHRlbnN1cmVFeGlzdGVuY2Uoc2NvcGVOYW1lLCBrZXkpO1xuXHRyZXR1cm4gZ2V0U3RyaWN0U2luZ2xldG9uVmVyc2lvbihzY29wZSwgc2NvcGVOYW1lLCBrZXksIHZlcnNpb24pO1xufSk7XG52YXIgbG9hZFZlcnNpb25DaGVja0ZhbGxiYWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgdmVyc2lvbiwgZmFsbGJhY2spIHtcblx0aWYoIXNjb3BlIHx8ICFfX3dlYnBhY2tfcmVxdWlyZV9fLm8oc2NvcGUsIGtleSkpIHJldHVybiBmYWxsYmFjaygpO1xuXHRyZXR1cm4gZ2V0KGZpbmRWYWxpZFZlcnNpb24oc2NvcGUsIGtleSwgdmVyc2lvbikgfHwgd2FybkludmFsaWRWZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbikgfHwgZmluZFZlcnNpb24oc2NvcGUsIGtleSkpO1xufSk7XG52YXIgbG9hZFNpbmdsZXRvbkZhbGxiYWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgZmFsbGJhY2spIHtcblx0aWYoIXNjb3BlIHx8ICFfX3dlYnBhY2tfcmVxdWlyZV9fLm8oc2NvcGUsIGtleSkpIHJldHVybiBmYWxsYmFjaygpO1xuXHRyZXR1cm4gZ2V0U2luZ2xldG9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSk7XG59KTtcbnZhciBsb2FkU2luZ2xldG9uVmVyc2lvbkNoZWNrRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uLCBmYWxsYmFjaykge1xuXHRpZighc2NvcGUgfHwgIV9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSkgcmV0dXJuIGZhbGxiYWNrKCk7XG5cdHJldHVybiBnZXRTaW5nbGV0b25WZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbik7XG59KTtcbnZhciBsb2FkU3RyaWN0VmVyc2lvbkNoZWNrRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uLCBmYWxsYmFjaykge1xuXHR2YXIgZW50cnkgPSBzY29wZSAmJiBfX3dlYnBhY2tfcmVxdWlyZV9fLm8oc2NvcGUsIGtleSkgJiYgZmluZFZhbGlkVmVyc2lvbihzY29wZSwga2V5LCB2ZXJzaW9uKTtcblx0cmV0dXJuIGVudHJ5ID8gZ2V0KGVudHJ5KSA6IGZhbGxiYWNrKCk7XG59KTtcbnZhciBsb2FkU3RyaWN0U2luZ2xldG9uVmVyc2lvbkNoZWNrRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uLCBmYWxsYmFjaykge1xuXHRpZighc2NvcGUgfHwgIV9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSkgcmV0dXJuIGZhbGxiYWNrKCk7XG5cdHJldHVybiBnZXRTdHJpY3RTaW5nbGV0b25WZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbik7XG59KTtcbnZhciByZXNvbHZlSGFuZGxlciA9IGZ1bmN0aW9uKGRhdGEpIHtcblx0dmFyIHN0cmljdCA9IGZhbHNlXG5cdHZhciBzaW5nbGV0b24gPSBmYWxzZVxuXHR2YXIgdmVyc2lvbkNoZWNrID0gZmFsc2Vcblx0dmFyIGZhbGxiYWNrID0gZmFsc2Vcblx0dmFyIGFyZ3MgPSBbZGF0YS5zaGFyZVNjb3BlLCBkYXRhLnNoYXJlS2V5XTtcblx0aWYgKGRhdGEucmVxdWlyZWRWZXJzaW9uKSB7XG5cdFx0aWYgKGRhdGEuc3RyaWN0VmVyc2lvbikgc3RyaWN0ID0gdHJ1ZTtcblx0XHRpZiAoZGF0YS5zaW5nbGV0b24pIHNpbmdsZXRvbiA9IHRydWU7XG5cdFx0YXJncy5wdXNoKHBhcnNlUmFuZ2UoZGF0YS5yZXF1aXJlZFZlcnNpb24pKTtcblx0XHR2ZXJzaW9uQ2hlY2sgPSB0cnVlXG5cdH0gZWxzZSBpZiAoZGF0YS5zaW5nbGV0b24pIHNpbmdsZXRvbiA9IHRydWU7XG5cdGlmIChkYXRhLmZhbGxiYWNrKSB7XG5cdFx0ZmFsbGJhY2sgPSB0cnVlO1xuXHRcdGFyZ3MucHVzaChkYXRhLmZhbGxiYWNrKTtcblx0fVxuXHRpZiAoc3RyaWN0ICYmIHNpbmdsZXRvbiAmJiB2ZXJzaW9uQ2hlY2sgJiYgZmFsbGJhY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTdHJpY3RTaW5nbGV0b25WZXJzaW9uQ2hlY2tGYWxsYmFjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAoc3RyaWN0ICYmIHZlcnNpb25DaGVjayAmJiBmYWxsYmFjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFN0cmljdFZlcnNpb25DaGVja0ZhbGxiYWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmIChzaW5nbGV0b24gJiYgdmVyc2lvbkNoZWNrICYmIGZhbGxiYWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkU2luZ2xldG9uVmVyc2lvbkNoZWNrRmFsbGJhY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHN0cmljdCAmJiBzaW5nbGV0b24gJiYgdmVyc2lvbkNoZWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkU3RyaWN0U2luZ2xldG9uVmVyc2lvbkNoZWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmIChzaW5nbGV0b24gJiYgZmFsbGJhY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTaW5nbGV0b25GYWxsYmFjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAodmVyc2lvbkNoZWNrICYmIGZhbGxiYWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkVmVyc2lvbkNoZWNrRmFsbGJhY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHN0cmljdCAmJiB2ZXJzaW9uQ2hlY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTdHJpY3RWZXJzaW9uQ2hlY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHNpbmdsZXRvbiAmJiB2ZXJzaW9uQ2hlY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTaW5nbGV0b25WZXJzaW9uQ2hlY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHNpbmdsZXRvbikgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFNpbmdsZXRvbi5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAodmVyc2lvbkNoZWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkVmVyc2lvbkNoZWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmIChmYWxsYmFjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZEZhbGxiYWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWQuYXBwbHkobnVsbCwgYXJncyk7IH1cbn07XG52YXIgaW5zdGFsbGVkTW9kdWxlcyA9IHt9O1xuX193ZWJwYWNrX3JlcXVpcmVfXy5mLmNvbnN1bWVzID0gZnVuY3Rpb24oY2h1bmtJZCwgcHJvbWlzZXMpIHtcblx0dmFyIG1vZHVsZUlkVG9Db25zdW1lRGF0YU1hcHBpbmcgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLmNvbnN1bWVzTG9hZGluZ0RhdGEubW9kdWxlSWRUb0NvbnN1bWVEYXRhTWFwcGluZ1xuXHR2YXIgY2h1bmtNYXBwaW5nID0gX193ZWJwYWNrX3JlcXVpcmVfXy5jb25zdW1lc0xvYWRpbmdEYXRhLmNodW5rTWFwcGluZztcblx0aWYoX193ZWJwYWNrX3JlcXVpcmVfXy5vKGNodW5rTWFwcGluZywgY2h1bmtJZCkpIHtcblx0XHRjaHVua01hcHBpbmdbY2h1bmtJZF0uZm9yRWFjaChmdW5jdGlvbihpZCkge1xuXHRcdFx0aWYoX193ZWJwYWNrX3JlcXVpcmVfXy5vKGluc3RhbGxlZE1vZHVsZXMsIGlkKSkgcmV0dXJuIHByb21pc2VzLnB1c2goaW5zdGFsbGVkTW9kdWxlc1tpZF0pO1xuXHRcdFx0dmFyIG9uRmFjdG9yeSA9IGZ1bmN0aW9uKGZhY3RvcnkpIHtcblx0XHRcdFx0aW5zdGFsbGVkTW9kdWxlc1tpZF0gPSAwO1xuXHRcdFx0XHRfX3dlYnBhY2tfcmVxdWlyZV9fLm1baWRdID0gZnVuY3Rpb24obW9kdWxlKSB7XG5cdFx0XHRcdFx0ZGVsZXRlIF9fd2VicGFja19yZXF1aXJlX18uY1tpZF07XG5cdFx0XHRcdFx0bW9kdWxlLmV4cG9ydHMgPSBmYWN0b3J5KCk7XG5cdFx0XHRcdH1cblx0XHRcdH07XG5cdFx0XHR2YXIgb25FcnJvciA9IGZ1bmN0aW9uKGVycm9yKSB7XG5cdFx0XHRcdGRlbGV0ZSBpbnN0YWxsZWRNb2R1bGVzW2lkXTtcblx0XHRcdFx0X193ZWJwYWNrX3JlcXVpcmVfXy5tW2lkXSA9IGZ1bmN0aW9uKG1vZHVsZSkge1xuXHRcdFx0XHRcdGRlbGV0ZSBfX3dlYnBhY2tfcmVxdWlyZV9fLmNbaWRdO1xuXHRcdFx0XHRcdHRocm93IGVycm9yO1xuXHRcdFx0XHR9XG5cdFx0XHR9O1xuXHRcdFx0dHJ5IHtcblx0XHRcdFx0dmFyIHByb21pc2UgPSByZXNvbHZlSGFuZGxlcihtb2R1bGVJZFRvQ29uc3VtZURhdGFNYXBwaW5nW2lkXSkoKTtcblx0XHRcdFx0aWYocHJvbWlzZS50aGVuKSB7XG5cdFx0XHRcdFx0cHJvbWlzZXMucHVzaChpbnN0YWxsZWRNb2R1bGVzW2lkXSA9IHByb21pc2UudGhlbihvbkZhY3RvcnkpWydjYXRjaCddKG9uRXJyb3IpKTtcblx0XHRcdFx0fSBlbHNlIG9uRmFjdG9yeShwcm9taXNlKTtcblx0XHRcdH0gY2F0Y2goZSkgeyBvbkVycm9yKGUpOyB9XG5cdFx0fSk7XG5cdH1cbn1cbiIsIlxuICAgICAgLy8gb2JqZWN0IHRvIHN0b3JlIGxvYWRlZCBhbmQgbG9hZGluZyBjaHVua3NcbiAgICAgIC8vIHVuZGVmaW5lZCA9IGNodW5rIG5vdCBsb2FkZWQsIG51bGwgPSBjaHVuayBwcmVsb2FkZWQvcHJlZmV0Y2hlZFxuICAgICAgLy8gW3Jlc29sdmUsIHJlamVjdCwgUHJvbWlzZV0gPSBjaHVuayBsb2FkaW5nLCAwID0gY2h1bmsgbG9hZGVkXG4gICAgICB2YXIgaW5zdGFsbGVkQ2h1bmtzID0ge1wiMTgwXCI6IDAsfTtcbiAgICAgIFxuICAgICAgICBfX3dlYnBhY2tfcmVxdWlyZV9fLmYuaiA9IGZ1bmN0aW9uIChjaHVua0lkLCBwcm9taXNlcykge1xuICAgICAgICAgIC8vIEpTT05QIGNodW5rIGxvYWRpbmcgZm9yIGphdmFzY3JpcHRcbnZhciBpbnN0YWxsZWRDaHVua0RhdGEgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLm8oaW5zdGFsbGVkQ2h1bmtzLCBjaHVua0lkKVxuXHQ/IGluc3RhbGxlZENodW5rc1tjaHVua0lkXVxuXHQ6IHVuZGVmaW5lZDtcbmlmIChpbnN0YWxsZWRDaHVua0RhdGEgIT09IDApIHtcblx0Ly8gMCBtZWFucyBcImFscmVhZHkgaW5zdGFsbGVkXCIuXG5cblx0Ly8gYSBQcm9taXNlIG1lYW5zIFwiY3VycmVudGx5IGxvYWRpbmdcIi5cblx0aWYgKGluc3RhbGxlZENodW5rRGF0YSkge1xuXHRcdHByb21pc2VzLnB1c2goaW5zdGFsbGVkQ2h1bmtEYXRhWzJdKTtcblx0fSBlbHNlIHtcblx0XHRpZiAodHJ1ZSkge1xuXHRcdFx0Ly8gc2V0dXAgUHJvbWlzZSBpbiBjaHVuayBjYWNoZVxuXHRcdFx0dmFyIHByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSwgcmVqZWN0KSA9PiAoaW5zdGFsbGVkQ2h1bmtEYXRhID0gaW5zdGFsbGVkQ2h1bmtzW2NodW5rSWRdID0gW3Jlc29sdmUsIHJlamVjdF0pKTtcblx0XHRcdHByb21pc2VzLnB1c2goKGluc3RhbGxlZENodW5rRGF0YVsyXSA9IHByb21pc2UpKTtcblxuXHRcdFx0Ly8gc3RhcnQgY2h1bmsgbG9hZGluZ1xuXHRcdFx0dmFyIHVybCA9IF9fd2VicGFja19yZXF1aXJlX18ucCArIF9fd2VicGFja19yZXF1aXJlX18udShjaHVua0lkKTtcblx0XHRcdC8vIGNyZWF0ZSBlcnJvciBiZWZvcmUgc3RhY2sgdW53b3VuZCB0byBnZXQgdXNlZnVsIHN0YWNrdHJhY2UgbGF0ZXJcblx0XHRcdHZhciBlcnJvciA9IG5ldyBFcnJvcigpO1xuXHRcdFx0dmFyIGxvYWRpbmdFbmRlZCA9IGZ1bmN0aW9uIChldmVudCkge1xuXHRcdFx0XHRpZiAoX193ZWJwYWNrX3JlcXVpcmVfXy5vKGluc3RhbGxlZENodW5rcywgY2h1bmtJZCkpIHtcblx0XHRcdFx0XHRpbnN0YWxsZWRDaHVua0RhdGEgPSBpbnN0YWxsZWRDaHVua3NbY2h1bmtJZF07XG5cdFx0XHRcdFx0aWYgKGluc3RhbGxlZENodW5rRGF0YSAhPT0gMCkgaW5zdGFsbGVkQ2h1bmtzW2NodW5rSWRdID0gdW5kZWZpbmVkO1xuXHRcdFx0XHRcdGlmIChpbnN0YWxsZWRDaHVua0RhdGEpIHtcblx0XHRcdFx0XHRcdHZhciBlcnJvclR5cGUgPVxuXHRcdFx0XHRcdFx0XHRldmVudCAmJiAoZXZlbnQudHlwZSA9PT0gJ2xvYWQnID8gJ21pc3NpbmcnIDogZXZlbnQudHlwZSk7XG5cdFx0XHRcdFx0XHR2YXIgcmVhbFNyYyA9IGV2ZW50ICYmIGV2ZW50LnRhcmdldCAmJiBldmVudC50YXJnZXQuc3JjO1xuXHRcdFx0XHRcdFx0ZXJyb3IubWVzc2FnZSA9XG5cdFx0XHRcdFx0XHRcdCdMb2FkaW5nIGNodW5rICcgK1xuXHRcdFx0XHRcdFx0XHRjaHVua0lkICtcblx0XHRcdFx0XHRcdFx0JyBmYWlsZWQuXFxuKCcgK1xuXHRcdFx0XHRcdFx0XHRlcnJvclR5cGUgK1xuXHRcdFx0XHRcdFx0XHQnOiAnICtcblx0XHRcdFx0XHRcdFx0cmVhbFNyYyArXG5cdFx0XHRcdFx0XHRcdCcpJztcblx0XHRcdFx0XHRcdGVycm9yLm5hbWUgPSAnQ2h1bmtMb2FkRXJyb3InO1xuXHRcdFx0XHRcdFx0ZXJyb3IudHlwZSA9IGVycm9yVHlwZTtcblx0XHRcdFx0XHRcdGVycm9yLnJlcXVlc3QgPSByZWFsU3JjO1xuXHRcdFx0XHRcdFx0aW5zdGFsbGVkQ2h1bmtEYXRhWzFdKGVycm9yKTtcblx0XHRcdFx0XHR9XG5cdFx0XHRcdH1cblx0XHRcdH07XG5cdFx0XHRfX3dlYnBhY2tfcmVxdWlyZV9fLmwodXJsLCBsb2FkaW5nRW5kZWQsIFwiY2h1bmstXCIgKyBjaHVua0lkLCBjaHVua0lkKTtcblx0XHR9IFxuXHR9XG59XG5cbiAgICAgICAgfVxuICAgICAgICAvLyBpbnN0YWxsIGEgSlNPTlAgY2FsbGJhY2sgZm9yIGNodW5rIGxvYWRpbmdcbnZhciBfX3JzcGFja19qc29ucCA9IChwYXJlbnRDaHVua0xvYWRpbmdGdW5jdGlvbiwgZGF0YSkgPT4ge1xuXHR2YXIgW2NodW5rSWRzLCBtb3JlTW9kdWxlcywgcnVudGltZV0gPSBkYXRhO1xuXHQvLyBhZGQgXCJtb3JlTW9kdWxlc1wiIHRvIHRoZSBtb2R1bGVzIG9iamVjdCxcblx0Ly8gdGhlbiBmbGFnIGFsbCBcImNodW5rSWRzXCIgYXMgbG9hZGVkIGFuZCBmaXJlIGNhbGxiYWNrXG5cdHZhciBtb2R1bGVJZCwgY2h1bmtJZCwgaSA9IDA7XG5cdGlmIChjaHVua0lkcy5zb21lKChpZCkgPT4gKGluc3RhbGxlZENodW5rc1tpZF0gIT09IDApKSkge1xuXHRcdGZvciAobW9kdWxlSWQgaW4gbW9yZU1vZHVsZXMpIHtcblx0XHRcdGlmIChfX3dlYnBhY2tfcmVxdWlyZV9fLm8obW9yZU1vZHVsZXMsIG1vZHVsZUlkKSkge1xuXHRcdFx0XHRfX3dlYnBhY2tfcmVxdWlyZV9fLm1bbW9kdWxlSWRdID0gbW9yZU1vZHVsZXNbbW9kdWxlSWRdO1xuXHRcdFx0fVxuXHRcdH1cblx0XHRpZiAocnVudGltZSkgdmFyIHJlc3VsdCA9IHJ1bnRpbWUoX193ZWJwYWNrX3JlcXVpcmVfXyk7XG5cdH1cblx0aWYgKHBhcmVudENodW5rTG9hZGluZ0Z1bmN0aW9uKSBwYXJlbnRDaHVua0xvYWRpbmdGdW5jdGlvbihkYXRhKTtcblx0Zm9yICg7IGkgPCBjaHVua0lkcy5sZW5ndGg7IGkrKykge1xuXHRcdGNodW5rSWQgPSBjaHVua0lkc1tpXTtcblx0XHRpZiAoXG5cdFx0XHRfX3dlYnBhY2tfcmVxdWlyZV9fLm8oaW5zdGFsbGVkQ2h1bmtzLCBjaHVua0lkKSAmJlxuXHRcdFx0aW5zdGFsbGVkQ2h1bmtzW2NodW5rSWRdXG5cdFx0KSB7XG5cdFx0XHRpbnN0YWxsZWRDaHVua3NbY2h1bmtJZF1bMF0oKTtcblx0XHR9XG5cdFx0aW5zdGFsbGVkQ2h1bmtzW2NodW5rSWRdID0gMDtcblx0fVxuXHRcbn07XG5cbnZhciBjaHVua0xvYWRpbmdHbG9iYWwgPSBzZWxmW1wid2VicGFja0NodW5rX2FueXdpZGdldF9tb25vcmVwb1wiXSA9IHNlbGZbXCJ3ZWJwYWNrQ2h1bmtfYW55d2lkZ2V0X21vbm9yZXBvXCJdIHx8IFtdO1xuY2h1bmtMb2FkaW5nR2xvYmFsLmZvckVhY2goX19yc3BhY2tfanNvbnAuYmluZChudWxsLCAwKSk7XG5jaHVua0xvYWRpbmdHbG9iYWwucHVzaCA9IF9fcnNwYWNrX2pzb25wLmJpbmQobnVsbCwgY2h1bmtMb2FkaW5nR2xvYmFsLnB1c2guYmluZChjaHVua0xvYWRpbmdHbG9iYWwpKTtcbiIsIl9fd2VicGFja19yZXF1aXJlX18ucnVpZCA9IFwiYnVuZGxlcj1yc3BhY2tAMS43LjExXCI7Il0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTtBQUNBO0FBQ0E7QUFDQSxrREFBa0Qsd0NBQXdDO0FBQzFGO0FBQ0E7QUFDQSxFOzs7O0FDTkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBLEU7Ozs7QUNWQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsK0JBQStCLG1DQUFtQztBQUNsRSxDOzs7O0FDTkE7QUFDQTtBQUNBO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBLENBQUMsSTs7OztBQ1BELHdGOzs7O0FDQUE7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxrQkFBa0Isb0JBQW9CO0FBQ3RDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOzs7QUFHQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7OztBQUlBOzs7QUFHQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7Ozs7O0FDN0RBO0FBQ0E7QUFDQTtBQUNBLHVEQUF1RCxpQkFBaUI7QUFDeEU7QUFDQSxnREFBZ0QsYUFBYTtBQUM3RCxFOzs7O0FDTkEseUM7Ozs7O0FDQ0E7QUFDQSw4Q0FBOEMsK0JBQStCO0FBQzdFO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGlEQUFpRDtBQUNqRDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EseUJBQXlCO0FBQ3pCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBLEVBQUU7QUFDRjs7Ozs7O0FDckVBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7Ozs7O0FDdEJBLDRDQUE0QyxlQUFlLGNBQWMsaUNBQWlDLFNBQVMsMEtBQTBLO0FBQzdSO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLHVEQUF1RCxRQUFRO0FBQy9EO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0EsTUFBTTtBQUNOO0FBQ0E7QUFDQSxNQUFNO0FBQ047QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFlBQVksZ0NBQWdDO0FBQzVDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxrQkFBa0Isa0JBQWtCO0FBQ3BDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQSxrQkFBa0Isa0JBQWtCO0FBQ3BDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSw0QkFBNEIsUUFBUTtBQUNwQztBQUNBO0FBQ0E7QUFDQSwyQ0FBMkM7QUFDM0M7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EseUNBQXlDO0FBQ3pDOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxPQUFPO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0EsS0FBSztBQUNMO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQSxZQUFZLHNCQUFzQjtBQUNsQztBQUNBO0FBQ0EsaUJBQWlCLGtCQUFrQjtBQUNuQyx3QkFBd0IseUJBQXlCO0FBQ2pEO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEVBQUU7QUFDRjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxFQUFFO0FBQ0Y7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEVBQUU7QUFDRjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEVBQUU7QUFDRjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDBCQUEwQjtBQUMxQjtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBLDBFQUEwRTtBQUMxRSw2REFBNkQ7QUFDN0QsZ0VBQWdFO0FBQ2hFLDhEQUE4RDtBQUM5RCxnREFBZ0Q7QUFDaEQsbURBQW1EO0FBQ25ELGlEQUFpRDtBQUNqRCxvREFBb0Q7QUFDcEQsb0NBQW9DO0FBQ3BDLHVDQUF1QztBQUN2QyxtQ0FBbUM7QUFDbkMscUJBQXFCO0FBQ3JCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxNQUFNO0FBQ04sS0FBSyxXQUFXO0FBQ2hCLEdBQUc7QUFDSDtBQUNBOzs7Ozs7QUN2aUJBO0FBQ0E7QUFDQTtBQUNBLDZCQUE2QjtBQUM3QjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVEscUJBQXFCO0FBQzdCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOzs7OztBQ3RGQSxtRCJ9