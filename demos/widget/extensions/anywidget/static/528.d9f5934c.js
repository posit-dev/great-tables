"use strict";
(self["webpackChunk_anywidget_monorepo"] = self["webpackChunk_anywidget_monorepo"] || []).push([["528"], {
59(__unused_rspack___webpack_module__, __webpack_exports__, __webpack_require__) {
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXPORTS
__webpack_require__.d(__webpack_exports__, {
  "default": () => (/* binding */ src_plugin)
});

// EXTERNAL MODULE: consume shared module (default) @jupyter-widgets/base@^6 (strict)
var base_6_strict_ = __webpack_require__(319);
;// CONCATENATED MODULE: ./packages/anywidget/src/model-proxy.ts
/**
 * This is a trick so that we can cleanup event listeners added
 * by the user-defined function.
 */ var INITIALIZE_MARKER = Symbol("anywidget.initialize");
/**
 * Prunes the view down to the minimum context necessary.
 *
 * Calls to `model.get` and `model.set` automatically add the
 * `context`, so we can gracefully unsubscribe from events
 * added by user-defined hooks.
 */ function modelProxy(model, context) {
    // oxlint-disable-next-line typescript-eslint/no-unsafe-type-assertion -- DOMWidgetModel.get/set/on/off have wider signatures than AnyModel, so bound versions don't narrow cleanly; the shape is structurally compatible
    return {
        get: model.get.bind(model),
        set: model.set.bind(model),
        save_changes: model.save_changes.bind(model),
        send: model.send.bind(model),
        on: function on(name, callback) {
            model.on(name, callback, context);
        },
        off: function off(name, callback) {
            model.off(name, callback, context);
        },
        // The widget_manager type is wider than what we want to expose to
        // developers. In a future version, we will expose a more limited API but
        // that can wait for a minor version bump.
        widget_manager: model.widget_manager
    };
}

;// CONCATENATED MODULE: ./packages/anywidget/src/util.ts
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function _async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function _instanceof(left, right) {
    "@swc/helpers - instanceof";
    if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) {
        return !!right[Symbol.hasInstance](left);
    } else {
        return left instanceof right;
    }
}
function _ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}
function assert(condition, message) {
    if (!condition) throw new Error(message);
}
function safeCleanup(fn, kind) {
    return _async_to_generator(function() {
        return _ts_generator(this, function(_state) {
            return [
                2,
                Promise.resolve().then(function() {
                    return fn === null || fn === void 0 ? void 0 : fn();
                }).catch(function(e) {
                    return console.warn("[anywidget] error cleaning up ".concat(kind, "."), e);
                })
            ];
        });
    })();
}
/**
 * Cleans up the stack trace at anywidget boundary.
 * You can fully inspect the entire stack trace in the console interactively,
 * but the initial error message is cleaned up to be more user-friendly.
 */ function throwAnywidgetError(source) {
    var _ref;
    var _source_stack;
    if (!_instanceof(source, Error)) {
        // Don't know what to do with this.
        throw source;
    }
    var lines = (_ref = (_source_stack = source.stack) === null || _source_stack === void 0 ? void 0 : _source_stack.split("\n")) !== null && _ref !== void 0 ? _ref : [];
    var anywidgetIndex = lines.findIndex(function(line) {
        return line.includes("anywidget");
    });
    var cleanStack = anywidgetIndex === -1 ? lines : lines.slice(0, anywidgetIndex + 1);
    source.stack = cleanStack.join("\n");
    console.error(source);
    throw source;
}
/**
 * Polyfill for {@link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/withResolvers Promise.withResolvers}
 *
 * Trevor(2025-03-14): Should be able to remove once more stable across browsers.
 */ function promiseWithResolvers() {
    var resolve;
    var reject;
    var promise = new Promise(function(res, rej) {
        resolve = res;
        reject = rej;
    });
    return {
        promise: promise,
        resolve: resolve,
        reject: reject
    };
}

;// CONCATENATED MODULE: ./packages/anywidget/src/binding.ts
function binding_asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function binding_async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                binding_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                binding_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function _check_private_redeclaration(obj, privateCollection) {
    if (privateCollection.has(obj)) {
        throw new TypeError("Cannot initialize the same private elements twice on an object");
    }
}
function _class_apply_descriptor_get(receiver, descriptor) {
    if (descriptor.get) {
        return descriptor.get.call(receiver);
    }
    return descriptor.value;
}
function _class_apply_descriptor_set(receiver, descriptor, value) {
    if (descriptor.set) {
        descriptor.set.call(receiver, value);
    } else {
        if (!descriptor.writable) {
            throw new TypeError("attempted to set read only private field");
        }
        descriptor.value = value;
    }
}
function _class_call_check(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function");
    }
}
function _class_extract_field_descriptor(receiver, privateMap, action) {
    if (!privateMap.has(receiver)) {
        throw new TypeError("attempted to " + action + " private field on non-instance");
    }
    return privateMap.get(receiver);
}
function _class_private_field_get(receiver, privateMap) {
    var descriptor = _class_extract_field_descriptor(receiver, privateMap, "get");
    return _class_apply_descriptor_get(receiver, descriptor);
}
function _class_private_field_init(obj, privateMap, value) {
    _check_private_redeclaration(obj, privateMap);
    privateMap.set(obj, value);
}
function _class_private_field_set(receiver, privateMap, value) {
    var descriptor = _class_extract_field_descriptor(receiver, privateMap, "set");
    _class_apply_descriptor_set(receiver, descriptor, value);
    return value;
}
function _defineProperties(target, props) {
    for(var i = 0; i < props.length; i++){
        var descriptor = props[i];
        descriptor.enumerable = descriptor.enumerable || false;
        descriptor.configurable = true;
        if ("value" in descriptor) descriptor.writable = true;
        Object.defineProperty(target, descriptor.key, descriptor);
    }
}
function _create_class(Constructor, protoProps, staticProps) {
    if (protoProps) _defineProperties(Constructor.prototype, protoProps);
    if (staticProps) _defineProperties(Constructor, staticProps);
    return Constructor;
}
function _define_property(obj, key, value) {
    if (key in obj) {
        Object.defineProperty(obj, key, {
            value: value,
            enumerable: true,
            configurable: true,
            writable: true
        });
    } else {
        obj[key] = value;
    }
    return obj;
}
function _type_of(obj) {
    "@swc/helpers - typeof";
    return obj && typeof Symbol !== "undefined" && obj.constructor === Symbol ? "symbol" : typeof obj;
}
function binding_ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}


function isSafeCleanupFunction(x) {
    return typeof x === "function";
}
var binding_controller = /*#__PURE__*/ new WeakMap(), _widgetDef = /*#__PURE__*/ new WeakMap(), _exports = /*#__PURE__*/ new WeakMap(), _model = /*#__PURE__*/ new WeakMap(), _resolvers = /*#__PURE__*/ new WeakMap();
var binding_WidgetBinding = /*#__PURE__*/ function() {
    "use strict";
    function WidgetBinding(model) {
        _class_call_check(this, WidgetBinding);
        _class_private_field_init(this, binding_controller, {
            writable: true,
            value: void 0
        });
        _class_private_field_init(this, _widgetDef, {
            writable: true,
            value: void 0
        });
        _class_private_field_init(this, _exports, {
            writable: true,
            value: void 0
        });
        _class_private_field_init(this, _model, {
            writable: true,
            value: void 0
        });
        _define_property(this, "ready", void 0);
        _class_private_field_init(this, _resolvers, {
            writable: true,
            value: void 0
        });
        _class_private_field_set(this, _model, model);
        _class_private_field_set(this, _resolvers, promiseWithResolvers());
        this.ready = _class_private_field_get(this, _resolvers).promise;
    }
    _create_class(WidgetBinding, [
        {
            key: "bind",
            value: function bind(_0, _1) {
                return binding_async_to_generator(function(widgetDef, param) {
                    var experimental, _widgetDef_initialize, _$_class_private_field_get, prevResolvers, signal, model, result;
                    return binding_ts_generator(this, function(_state) {
                        switch(_state.label){
                            case 0:
                                experimental = param.experimental;
                                if (_class_private_field_get(this, _widgetDef) === widgetDef) return [
                                    2
                                ];
                                if (_class_private_field_get(this, _widgetDef) && _class_private_field_get(this, _widgetDef) !== widgetDef) {
                                    ;
                                    (_$_class_private_field_get = _class_private_field_get(this, binding_controller)) === null || _$_class_private_field_get === void 0 ? void 0 : _$_class_private_field_get.abort();
                                    // Settle the old promise so any awaiter that captured `this.ready`
                                    // (e.g. a parent's `host.getWidget` snapshot) unblocks instead of
                                    // hanging until the host's 10s timeout. No-op if already resolved.
                                    prevResolvers = _class_private_field_get(this, _resolvers);
                                    _class_private_field_set(this, _resolvers, promiseWithResolvers());
                                    this.ready = _class_private_field_get(this, _resolvers).promise;
                                    prevResolvers.promise.catch(function() {});
                                    prevResolvers.reject(new Error("[anywidget] widget bind aborted by re-bind"));
                                }
                                _class_private_field_set(this, _widgetDef, widgetDef);
                                _class_private_field_set(this, binding_controller, new AbortController());
                                signal = _class_private_field_get(this, binding_controller).signal;
                                model = _class_private_field_get(this, _model);
                                model.off(null, null, INITIALIZE_MARKER);
                                return [
                                    4,
                                    (_widgetDef_initialize = widgetDef.initialize) === null || _widgetDef_initialize === void 0 ? void 0 : _widgetDef_initialize.call(widgetDef, {
                                        model: modelProxy(model, INITIALIZE_MARKER),
                                        signal: signal,
                                        experimental: experimental
                                    })
                                ];
                            case 1:
                                result = _state.sent();
                                if (!signal.aborted) return [
                                    3,
                                    3
                                ];
                                return [
                                    4,
                                    safeCleanup(isSafeCleanupFunction(result) ? result : undefined, "esm update")
                                ];
                            case 2:
                                _state.sent();
                                return [
                                    2
                                ];
                            case 3:
                                if (isSafeCleanupFunction(result)) {
                                    signal.addEventListener("abort", function() {
                                        return safeCleanup(result, "esm update");
                                    });
                                    _class_private_field_set(this, _exports, undefined);
                                } else if ((typeof result === "undefined" ? "undefined" : _type_of(result)) === "object" && result !== null) {
                                    _class_private_field_set(this, _exports, result);
                                } else {
                                    _class_private_field_set(this, _exports, undefined);
                                }
                                _class_private_field_get(this, _resolvers).resolve(_class_private_field_get(this, _exports));
                                return [
                                    2
                                ];
                        }
                    });
                }).apply(this, arguments);
            }
        },
        {
            key: "createView",
            value: function createView(_0, _1) {
                return binding_async_to_generator(function(target, param) {
                    var signal, experimental, host, _$_class_private_field_get, controller, combined, model, cleanup, disposeView;
                    return binding_ts_generator(this, function(_state) {
                        switch(_state.label){
                            case 0:
                                signal = param.signal, experimental = param.experimental, host = param.host;
                                return [
                                    4,
                                    this.ready
                                ];
                            case 1:
                                _state.sent();
                                if (!((_$_class_private_field_get = _class_private_field_get(this, _widgetDef)) === null || _$_class_private_field_get === void 0 ? void 0 : _$_class_private_field_get.render)) return [
                                    2
                                ];
                                controller = new AbortController();
                                combined = AbortSignal.any([
                                    signal,
                                    controller.signal
                                ]);
                                model = _class_private_field_get(this, _model);
                                return [
                                    4,
                                    _class_private_field_get(this, _widgetDef).render({
                                        model: modelProxy(model, target),
                                        el: target.el,
                                        signal: combined,
                                        host: host,
                                        experimental: experimental
                                    })
                                ];
                            case 2:
                                cleanup = _state.sent();
                                disposeView = function disposeView(reason) {
                                    // Clear listeners keyed to this target. For ephemeral `{el}` targets
                                    // (host.getWidget().render), this prevents leaks across re-renders.
                                    model.off(null, null, target);
                                    void safeCleanup(cleanup, reason);
                                };
                                if (combined.aborted) {
                                    disposeView("dispose view - already aborted");
                                    return [
                                        2
                                    ];
                                }
                                combined.addEventListener("abort", function() {
                                    return disposeView("dispose view - aborted");
                                });
                                return [
                                    2
                                ];
                        }
                    });
                }).apply(this, arguments);
            }
        },
        {
            key: "exports",
            get: function get() {
                return _class_private_field_get(this, _exports);
            }
        },
        {
            key: "destroy",
            value: function destroy() {
                var _$_class_private_field_get;
                (_$_class_private_field_get = _class_private_field_get(this, binding_controller)) === null || _$_class_private_field_get === void 0 ? void 0 : _$_class_private_field_get.abort();
                _class_private_field_set(this, binding_controller, undefined);
                _class_private_field_set(this, _widgetDef, undefined);
            }
        }
    ]);
    return WidgetBinding;
}();
var _bindings = /*#__PURE__*/ new WeakMap();
var binding_BindingManager = /*#__PURE__*/ function() {
    "use strict";
    function BindingManager() {
        _class_call_check(this, BindingManager);
        _class_private_field_init(this, _bindings, {
            writable: true,
            value: new Map()
        });
    }
    _create_class(BindingManager, [
        {
            key: "getOrCreate",
            value: function getOrCreate(model) {
                var binding = _class_private_field_get(this, _bindings).get(model);
                if (!binding) {
                    binding = new binding_WidgetBinding(model);
                    _class_private_field_get(this, _bindings).set(model, binding);
                }
                return binding;
            }
        },
        {
            key: "get",
            value: function get(model) {
                return _class_private_field_get(this, _bindings).get(model);
            }
        },
        {
            key: "destroy",
            value: function destroy(model) {
                var binding = _class_private_field_get(this, _bindings).get(model);
                if (binding) {
                    binding.destroy();
                    _class_private_field_get(this, _bindings).delete(model);
                }
            }
        }
    ]);
    return BindingManager;
}();
var BINDINGS = new binding_BindingManager();

// EXTERNAL MODULE: ./node_modules/.pnpm/solid-js@1.9.12/node_modules/solid-js/dist/solid.js
var solid = __webpack_require__(621);
// EXTERNAL MODULE: ./node_modules/.pnpm/@lukeed+uuid@2.0.1/node_modules/@lukeed/uuid/dist/index.mjs
var dist = __webpack_require__(661);
;// CONCATENATED MODULE: ./packages/anywidget/src/invoke.ts

function invoke(model, name, msg) {
    var options = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
    var _options_signal;
    // crypto.randomUUID() is not available in non-secure contexts (i.e., http://)
    // so we use simple (non-secure) polyfill.
    var id = dist.v4();
    var signal = (_options_signal = options.signal) !== null && _options_signal !== void 0 ? _options_signal : AbortSignal.timeout(3000);
    return new Promise(function(resolve, reject) {
        var _options_buffers;
        if (signal.aborted) {
            reject(signal.reason);
        }
        signal.addEventListener("abort", function() {
            model.off("msg:custom", handler);
            reject(signal.reason);
        });
        function handler(msg, buffers) {
            if (!(msg.id === id)) return;
            resolve([
                msg.response,
                buffers
            ]);
            model.off("msg:custom", handler);
        }
        model.on("msg:custom", handler);
        model.send({
            id: id,
            kind: "anywidget-command",
            name: name,
            msg: msg
        }, undefined, (_options_buffers = options.buffers) !== null && _options_buffers !== void 0 ? _options_buffers : []);
    });
}

;// CONCATENATED MODULE: ./packages/anywidget/src/widget-ref.ts
var WIDGET_REF_PREFIX = "anywidget:";
function parseWidgetRef(ref) {
    if (typeof ref === "string" && ref.startsWith(WIDGET_REF_PREFIX)) {
        return ref.slice(WIDGET_REF_PREFIX.length);
    }
    throw new Error("[anywidget] Invalid widget reference: ".concat(JSON.stringify(ref)));
}

;// CONCATENATED MODULE: ./packages/anywidget/src/host.ts
function host_asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function host_async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                host_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                host_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function host_ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}




function createHost(model, param) {
    var signal = param.signal;
    var host = {
        getModel: // @ts-expect-error - modelProxy returns AnyModel; generic T is erased at runtime
        function getModel(ref) {
            return host_async_to_generator(function() {
                var modelId, childModel, context;
                return host_ts_generator(this, function(_state) {
                    switch(_state.label){
                        case 0:
                            modelId = parseWidgetRef(ref);
                            return [
                                4,
                                model.widget_manager.get_model(modelId)
                            ];
                        case 1:
                            childModel = _state.sent();
                            context = Symbol("anywidget.host.getModel");
                            signal.addEventListener("abort", function() {
                                return childModel.off(null, null, context);
                            });
                            return [
                                2,
                                modelProxy(childModel, context)
                            ];
                    }
                });
            })();
        },
        getWidget: // @ts-expect-error - generic T is erased at runtime, exports typed as unknown
        function getWidget(ref) {
            return host_async_to_generator(function() {
                var modelId, childModel, childBinding, timer, exports;
                return host_ts_generator(this, function(_state) {
                    switch(_state.label){
                        case 0:
                            modelId = parseWidgetRef(ref);
                            return [
                                4,
                                model.widget_manager.get_model(modelId)
                            ];
                        case 1:
                            childModel = _state.sent();
                            childBinding = BINDINGS.get(childModel);
                            if (!childBinding) {
                                throw new Error("[anywidget] No binding found for widget ".concat(modelId));
                            }
                            return [
                                4,
                                new Promise(function(resolve, reject) {
                                    timer = setTimeout(function() {
                                        return reject(new Error("[anywidget] Timed out waiting for widget ".concat(modelId, " to initialize")));
                                    }, 10000);
                                    childBinding.ready.then(resolve, reject);
                                }).finally(function() {
                                    return clearTimeout(timer);
                                })
                            ];
                        case 2:
                            exports = _state.sent();
                            return [
                                2,
                                {
                                    exports: exports,
                                    render: function render(_0) {
                                        return host_async_to_generator(function(param) {
                                            var el, viewSignal, childViewSignal;
                                            return host_ts_generator(this, function(_state) {
                                                switch(_state.label){
                                                    case 0:
                                                        el = param.el, viewSignal = param.signal;
                                                        childViewSignal = viewSignal !== null && viewSignal !== void 0 ? viewSignal : signal;
                                                        return [
                                                            4,
                                                            childBinding.createView({
                                                                el: el
                                                            }, {
                                                                signal: childViewSignal,
                                                                experimental: {
                                                                    // @ts-expect-error - bind isn't working
                                                                    invoke: invoke.bind(null, childModel)
                                                                },
                                                                host: host
                                                            })
                                                        ];
                                                    case 1:
                                                        _state.sent();
                                                        return [
                                                            2
                                                        ];
                                                }
                                            });
                                        }).apply(this, arguments);
                                    }
                                }
                            ];
                    }
                });
            })();
        }
    };
    return host;
}

;// CONCATENATED MODULE: ./packages/anywidget/src/load.ts
function load_asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function load_async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                load_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                load_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function load_ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}

function isHref(str) {
    return str.startsWith("http://") || str.startsWith("https://");
}
function loadCssHref(href, anywidgetId) {
    return load_async_to_generator(function() {
        var prev, newLink;
        return load_ts_generator(this, function(_state) {
            prev = document.querySelector("link[id='".concat(anywidgetId, "']"));
            // Adapted from https://github.com/vitejs/vite/blob/d59e1acc2efc0307488364e9f2fad528ec57f204/packages/vite/src/client/client.ts#L185-L201
            // Swaps out old styles with new, but avoids flash of unstyled content.
            // No need to await the load since we already have styles applied.
            if (prev) {
                // oxlint-disable-next-line typescript-eslint/no-unsafe-type-assertion -- Node.cloneNode() returns Node; we know prev is HTMLLinkElement so the clone is too
                newLink = prev.cloneNode();
                newLink.href = href;
                newLink.addEventListener("load", function() {
                    return prev === null || prev === void 0 ? void 0 : prev.remove();
                });
                newLink.addEventListener("error", function() {
                    return prev === null || prev === void 0 ? void 0 : prev.remove();
                });
                prev.after(newLink);
                return [
                    2
                ];
            }
            return [
                2,
                new Promise(function(resolve) {
                    var link = Object.assign(document.createElement("link"), {
                        rel: "stylesheet",
                        href: href,
                        onload: resolve
                    });
                    document.head.appendChild(link);
                })
            ];
        });
    })();
}
function loadCssText(cssText, anywidgetId) {
    var prev = document.querySelector("style[id='".concat(anywidgetId, "']"));
    if (prev) {
        // replace instead of creating a new DOM node
        prev.textContent = cssText;
        return;
    }
    var style = Object.assign(document.createElement("style"), {
        id: anywidgetId,
        type: "text/css"
    });
    style.appendChild(document.createTextNode(cssText));
    document.head.appendChild(style);
}
function loadCss(css, anywidgetId) {
    return load_async_to_generator(function() {
        return load_ts_generator(this, function(_state) {
            if (!css || !anywidgetId) return [
                2
            ];
            if (isHref(css)) return [
                2,
                loadCssHref(css, anywidgetId)
            ];
            return [
                2,
                loadCssText(css, anywidgetId)
            ];
        });
    })();
}
function loadEsm(esm) {
    return load_async_to_generator(function() {
        var url, mod;
        return load_ts_generator(this, function(_state) {
            switch(_state.label){
                case 0:
                    if (!isHref(esm)) return [
                        3,
                        2
                    ];
                    return [
                        4,
                        import(/* webpackIgnore: true */ /* @vite-ignore */ esm)
                    ];
                case 1:
                    return [
                        2,
                        _state.sent()
                    ];
                case 2:
                    url = URL.createObjectURL(new Blob([
                        esm
                    ], {
                        type: "text/javascript"
                    }));
                    return [
                        4,
                        import(/* webpackIgnore: true */ /* @vite-ignore */ url)
                    ];
                case 3:
                    mod = _state.sent();
                    URL.revokeObjectURL(url);
                    return [
                        2,
                        mod
                    ];
            }
        });
    })();
}
function warnRenderDeprecation(anywidgetId) {
    console.warn("[anywidget] Deprecation Warning for ".concat(anywidgetId, ": Direct export of a 'render' will likely be deprecated in the future. To migrate ...\n\nRemove the 'export' keyword from 'render'\n-----------------------------------------\n\nexport function render({ model, el }) { ... }\n^^^^^^\n\nCreate a default export that returns an object with 'render'\n------------------------------------------------------------\n\nfunction render({ model, el }) { ... }\n         ^^^^^^\nexport default { render }\n                 ^^^^^^\n\nPin to anywidget>=0.9.0 in your pyproject.toml\n----------------------------------------------\n\ndependencies = [\"anywidget>=0.9.0\"]\n\nTo learn more, please see: https://github.com/manzt/anywidget/pull/395.\n"));
}
function loadWidget(esm, anywidgetId) {
    return load_async_to_generator(function() {
        var mod, widget, _tmp;
        return load_ts_generator(this, function(_state) {
            switch(_state.label){
                case 0:
                    return [
                        4,
                        loadEsm(esm)
                    ];
                case 1:
                    mod = _state.sent();
                    if (mod.render) {
                        warnRenderDeprecation(anywidgetId);
                        return [
                            2,
                            {
                                initialize: function initialize() {
                                    return load_async_to_generator(function() {
                                        return load_ts_generator(this, function(_state) {
                                            return [
                                                2
                                            ];
                                        });
                                    })();
                                },
                                render: mod.render
                            }
                        ];
                    }
                    assert(mod.default, "[anywidget] module must export a default function or object.");
                    if (!(typeof mod.default === "function")) return [
                        3,
                        3
                    ];
                    return [
                        4,
                        mod.default()
                    ];
                case 2:
                    _tmp = _state.sent();
                    return [
                        3,
                        4
                    ];
                case 3:
                    _tmp = mod.default;
                    _state.label = 4;
                case 4:
                    widget = _tmp;
                    return [
                        2,
                        widget
                    ];
            }
        });
    })();
}

;// CONCATENATED MODULE: ./packages/anywidget/src/observe.ts
function _array_like_to_array(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for(var i = 0, arr2 = new Array(len); i < len; i++)arr2[i] = arr[i];
    return arr2;
}
function _array_with_holes(arr) {
    if (Array.isArray(arr)) return arr;
}
function _iterable_to_array_limit(arr, i) {
    var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"];
    if (_i == null) return;
    var _arr = [];
    var _n = true;
    var _d = false;
    var _s, _e;
    try {
        for(_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true){
            _arr.push(_s.value);
            if (i && _arr.length === i) break;
        }
    } catch (err) {
        _d = true;
        _e = err;
    } finally{
        try {
            if (!_n && _i["return"] != null) _i["return"]();
        } finally{
            if (_d) throw _e;
        }
    }
    return _arr;
}
function _non_iterable_rest() {
    throw new TypeError("Invalid attempt to destructure non-iterable instance.\\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}
function _sliced_to_array(arr, i) {
    return _array_with_holes(arr) || _iterable_to_array_limit(arr, i) || _unsupported_iterable_to_array(arr, i) || _non_iterable_rest();
}
function _unsupported_iterable_to_array(o, minLen) {
    if (!o) return;
    if (typeof o === "string") return _array_like_to_array(o, minLen);
    var n = Object.prototype.toString.call(o).slice(8, -1);
    if (n === "Object" && o.constructor) n = o.constructor.name;
    if (n === "Map" || n === "Set") return Array.from(n);
    if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _array_like_to_array(o, minLen);
}

function observe(model, name, param) {
    var signal = param.signal;
    var _solid_createSignal = _sliced_to_array(solid/* .createSignal */.n5(model.get(name)), 2), get = _solid_createSignal[0], set = _solid_createSignal[1];
    var update = function update() {
        return set(function() {
            return model.get(name);
        });
    };
    model.on("change:".concat(name), update);
    signal === null || signal === void 0 ? void 0 : signal.addEventListener("abort", function() {
        model.off("change:".concat(name), update);
    });
    return get;
}

;// CONCATENATED MODULE: ./packages/anywidget/src/runtime.ts
function runtime_array_like_to_array(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for(var i = 0, arr2 = new Array(len); i < len; i++)arr2[i] = arr[i];
    return arr2;
}
function runtime_array_with_holes(arr) {
    if (Array.isArray(arr)) return arr;
}
function runtime_asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function runtime_async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                runtime_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                runtime_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function runtime_check_private_redeclaration(obj, privateCollection) {
    if (privateCollection.has(obj)) {
        throw new TypeError("Cannot initialize the same private elements twice on an object");
    }
}
function runtime_class_apply_descriptor_get(receiver, descriptor) {
    if (descriptor.get) {
        return descriptor.get.call(receiver);
    }
    return descriptor.value;
}
function runtime_class_apply_descriptor_set(receiver, descriptor, value) {
    if (descriptor.set) {
        descriptor.set.call(receiver, value);
    } else {
        if (!descriptor.writable) {
            throw new TypeError("attempted to set read only private field");
        }
        descriptor.value = value;
    }
}
function runtime_class_call_check(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function");
    }
}
function runtime_class_extract_field_descriptor(receiver, privateMap, action) {
    if (!privateMap.has(receiver)) {
        throw new TypeError("attempted to " + action + " private field on non-instance");
    }
    return privateMap.get(receiver);
}
function runtime_class_private_field_get(receiver, privateMap) {
    var descriptor = runtime_class_extract_field_descriptor(receiver, privateMap, "get");
    return runtime_class_apply_descriptor_get(receiver, descriptor);
}
function runtime_class_private_field_init(obj, privateMap, value) {
    runtime_check_private_redeclaration(obj, privateMap);
    privateMap.set(obj, value);
}
function runtime_class_private_field_set(receiver, privateMap, value) {
    var descriptor = runtime_class_extract_field_descriptor(receiver, privateMap, "set");
    runtime_class_apply_descriptor_set(receiver, descriptor, value);
    return value;
}
function runtime_defineProperties(target, props) {
    for(var i = 0; i < props.length; i++){
        var descriptor = props[i];
        descriptor.enumerable = descriptor.enumerable || false;
        descriptor.configurable = true;
        if ("value" in descriptor) descriptor.writable = true;
        Object.defineProperty(target, descriptor.key, descriptor);
    }
}
function runtime_create_class(Constructor, protoProps, staticProps) {
    if (protoProps) runtime_defineProperties(Constructor.prototype, protoProps);
    if (staticProps) runtime_defineProperties(Constructor, staticProps);
    return Constructor;
}
function runtime_define_property(obj, key, value) {
    if (key in obj) {
        Object.defineProperty(obj, key, {
            value: value,
            enumerable: true,
            configurable: true,
            writable: true
        });
    } else {
        obj[key] = value;
    }
    return obj;
}
function runtime_iterable_to_array_limit(arr, i) {
    var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"];
    if (_i == null) return;
    var _arr = [];
    var _n = true;
    var _d = false;
    var _s, _e;
    try {
        for(_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true){
            _arr.push(_s.value);
            if (i && _arr.length === i) break;
        }
    } catch (err) {
        _d = true;
        _e = err;
    } finally{
        try {
            if (!_n && _i["return"] != null) _i["return"]();
        } finally{
            if (_d) throw _e;
        }
    }
    return _arr;
}
function runtime_non_iterable_rest() {
    throw new TypeError("Invalid attempt to destructure non-iterable instance.\\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}
function runtime_sliced_to_array(arr, i) {
    return runtime_array_with_holes(arr) || runtime_iterable_to_array_limit(arr, i) || runtime_unsupported_iterable_to_array(arr, i) || runtime_non_iterable_rest();
}
function runtime_unsupported_iterable_to_array(o, minLen) {
    if (!o) return;
    if (typeof o === "string") return runtime_array_like_to_array(o, minLen);
    var n = Object.prototype.toString.call(o).slice(8, -1);
    if (n === "Object" && o.constructor) n = o.constructor.name;
    if (n === "Map" || n === "Set") return Array.from(n);
    if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return runtime_array_like_to_array(o, minLen);
}
function runtime_ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}







var // @ts-expect-error - Set synchronously in constructor.
_widgetResult = /*#__PURE__*/ new WeakMap(), _signal = /*#__PURE__*/ new WeakMap();
var runtime_Runtime = /*#__PURE__*/ function() {
    "use strict";
    function Runtime(model, options) {
        var _this = this;
        runtime_class_call_check(this, Runtime);
        runtime_class_private_field_init(this, _widgetResult, {
            writable: true,
            value: void 0
        });
        runtime_class_private_field_init(this, _signal, {
            writable: true,
            value: void 0
        });
        runtime_define_property(this, "ready", void 0);
        var resolvers = promiseWithResolvers();
        this.ready = resolvers.promise;
        runtime_class_private_field_set(this, _signal, options.signal);
        runtime_class_private_field_get(this, _signal).throwIfAborted();
        runtime_class_private_field_get(this, _signal).addEventListener("abort", function() {
            return dispose();
        });
        AbortSignal.timeout(2000).addEventListener("abort", function() {
            resolvers.reject(new Error("[anywidget] Failed to initialize model."));
        });
        var binding = BINDINGS.getOrCreate(model);
        var experimental = {
            // @ts-expect-error - invoke.bind loses generic type parameter
            invoke: invoke.bind(null, model)
        };
        var dispose = solid/* .createRoot */.Hr(function(dispose) {
            // DOMWidgetModel is untyped by trait shape; we know the anywidget traits, so narrow to AnyModel<State> for type-safe `.get()` access
            // oxlint-disable-next-line typescript-eslint/no-unsafe-type-assertion -- see above
            var typedModel = model;
            var id = typedModel.get("_anywidget_id");
            var css = observe(typedModel, "_css", {
                signal: runtime_class_private_field_get(_this, _signal)
            });
            var esm = observe(typedModel, "_esm", {
                signal: runtime_class_private_field_get(_this, _signal)
            });
            var _solid_createSignal = runtime_sliced_to_array(solid/* .createSignal */.n5({
                status: "pending"
            }), 2), widgetResult = _solid_createSignal[0], setWidgetResult = _solid_createSignal[1];
            runtime_class_private_field_set(_this, _widgetResult, widgetResult);
            solid/* .createEffect */.EH(solid.on(css, function() {
                return console.debug("[anywidget] css hot updated: ".concat(id));
            }, {
                defer: true
            }));
            solid/* .createEffect */.EH(solid.on(esm, function() {
                return console.debug("[anywidget] esm hot updated: ".concat(id));
            }, {
                defer: true
            }));
            solid/* .createEffect */.EH(function() {
                return loadCss(css(), id);
            });
            solid/* .createEffect */.EH(function() {
                // Per-effect controller so a stale loadWidget resolution from a
                // previous _esm value cannot overwrite a newer one. Solid fires
                // onCleanup before re-running the effect, aborting the prior load.
                var controller = new AbortController();
                solid/* .onCleanup */.Ki(function() {
                    return controller.abort();
                });
                loadWidget(esm(), id).then(function(widget) {
                    return runtime_async_to_generator(function() {
                        return runtime_ts_generator(this, function(_state) {
                            switch(_state.label){
                                case 0:
                                    if (controller.signal.aborted) return [
                                        2
                                    ];
                                    return [
                                        4,
                                        binding.bind(widget, {
                                            experimental: experimental
                                        })
                                    ];
                                case 1:
                                    _state.sent();
                                    if (controller.signal.aborted) return [
                                        2
                                    ];
                                    setWidgetResult({
                                        status: "ready",
                                        data: widget
                                    });
                                    resolvers.resolve();
                                    return [
                                        2
                                    ];
                            }
                        });
                    })();
                }).catch(function(error) {
                    if (controller.signal.aborted) return;
                    setWidgetResult({
                        status: "error",
                        error: error
                    });
                });
            });
            return dispose;
        });
    }
    runtime_create_class(Runtime, [
        {
            key: "createView",
            value: function createView(view, options) {
                return runtime_async_to_generator(function() {
                    var _this, model, signal, binding, experimental, host, dispose;
                    return runtime_ts_generator(this, function(_state) {
                        _this = this;
                        model = view.model;
                        signal = AbortSignal.any([
                            runtime_class_private_field_get(this, _signal),
                            options.signal
                        ]); // either model or view destroyed
                        signal.throwIfAborted();
                        signal.addEventListener("abort", function() {
                            return dispose();
                        });
                        binding = BINDINGS.get(model);
                        assert(binding, "[anywidget] WidgetBinding not found.");
                        experimental = {
                            // @ts-expect-error - invoke.bind loses generic type parameter
                            invoke: invoke.bind(null, model)
                        };
                        host = createHost(model, {
                            signal: signal
                        });
                        dispose = solid/* .createRoot */.Hr(function(dispose) {
                            solid/* .createEffect */.EH(function() {
                                // Clear all previous event listeners from this hook.
                                model.off(null, null, view);
                                view.$el.empty();
                                var result = runtime_class_private_field_get(_this, _widgetResult).call(_this);
                                if (result.status === "pending") {
                                    return;
                                }
                                if (result.status === "error") {
                                    throwAnywidgetError(result.error);
                                    return;
                                }
                                var controller = new AbortController();
                                solid/* .onCleanup */.Ki(function() {
                                    return controller.abort();
                                });
                                Promise.resolve().then(function() {
                                    return binding.createView(view, {
                                        signal: AbortSignal.any([
                                            signal,
                                            controller.signal
                                        ]),
                                        experimental: experimental,
                                        host: host
                                    });
                                }).catch(function(error) {
                                    return throwAnywidgetError(error);
                                });
                            });
                            return function() {
                                return dispose();
                            };
                        });
                        return [
                            2
                        ];
                    });
                }).call(this);
            }
        }
    ]);
    return Runtime;
}();

;// CONCATENATED MODULE: ./packages/anywidget/src/widget.ts
function widget_array_like_to_array(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for(var i = 0, arr2 = new Array(len); i < len; i++)arr2[i] = arr[i];
    return arr2;
}
function _array_without_holes(arr) {
    if (Array.isArray(arr)) return widget_array_like_to_array(arr);
}
function _assert_this_initialized(self) {
    if (self === void 0) {
        throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
    }
    return self;
}
function widget_asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) {
    try {
        var info = gen[key](arg);
        var value = info.value;
    } catch (error) {
        reject(error);
        return;
    }
    if (info.done) {
        resolve(value);
    } else {
        Promise.resolve(value).then(_next, _throw);
    }
}
function widget_async_to_generator(fn) {
    return function() {
        var self = this, args = arguments;
        return new Promise(function(resolve, reject) {
            var gen = fn.apply(self, args);
            function _next(value) {
                widget_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value);
            }
            function _throw(err) {
                widget_asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err);
            }
            _next(undefined);
        });
    };
}
function _call_super(_this, derived, args) {
    derived = _get_prototype_of(derived);
    return _possible_constructor_return(_this, _is_native_reflect_construct() ? Reflect.construct(derived, args || [], _get_prototype_of(_this).constructor) : derived.apply(_this, args));
}
function widget_check_private_redeclaration(obj, privateCollection) {
    if (privateCollection.has(obj)) {
        throw new TypeError("Cannot initialize the same private elements twice on an object");
    }
}
function widget_class_apply_descriptor_get(receiver, descriptor) {
    if (descriptor.get) {
        return descriptor.get.call(receiver);
    }
    return descriptor.value;
}
function widget_class_call_check(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function");
    }
}
function widget_class_extract_field_descriptor(receiver, privateMap, action) {
    if (!privateMap.has(receiver)) {
        throw new TypeError("attempted to " + action + " private field on non-instance");
    }
    return privateMap.get(receiver);
}
function widget_class_private_field_get(receiver, privateMap) {
    var descriptor = widget_class_extract_field_descriptor(receiver, privateMap, "get");
    return widget_class_apply_descriptor_get(receiver, descriptor);
}
function widget_class_private_field_init(obj, privateMap, value) {
    widget_check_private_redeclaration(obj, privateMap);
    privateMap.set(obj, value);
}
function widget_defineProperties(target, props) {
    for(var i = 0; i < props.length; i++){
        var descriptor = props[i];
        descriptor.enumerable = descriptor.enumerable || false;
        descriptor.configurable = true;
        if ("value" in descriptor) descriptor.writable = true;
        Object.defineProperty(target, descriptor.key, descriptor);
    }
}
function widget_create_class(Constructor, protoProps, staticProps) {
    if (protoProps) widget_defineProperties(Constructor.prototype, protoProps);
    if (staticProps) widget_defineProperties(Constructor, staticProps);
    return Constructor;
}
function widget_define_property(obj, key, value) {
    if (key in obj) {
        Object.defineProperty(obj, key, {
            value: value,
            enumerable: true,
            configurable: true,
            writable: true
        });
    } else {
        obj[key] = value;
    }
    return obj;
}
function _get(target, property, receiver) {
    if (typeof Reflect !== "undefined" && Reflect.get) {
        _get = Reflect.get;
    } else {
        _get = function get(target, property, receiver) {
            var base = _super_prop_base(target, property);
            if (!base) return;
            var desc = Object.getOwnPropertyDescriptor(base, property);
            if (desc.get) {
                return desc.get.call(receiver || target);
            }
            return desc.value;
        };
    }
    return _get(target, property, receiver || target);
}
function _get_prototype_of(o) {
    _get_prototype_of = Object.setPrototypeOf ? Object.getPrototypeOf : function getPrototypeOf(o) {
        return o.__proto__ || Object.getPrototypeOf(o);
    };
    return _get_prototype_of(o);
}
function _inherits(subClass, superClass) {
    if (typeof superClass !== "function" && superClass !== null) {
        throw new TypeError("Super expression must either be null or a function");
    }
    subClass.prototype = Object.create(superClass && superClass.prototype, {
        constructor: {
            value: subClass,
            writable: true,
            configurable: true
        }
    });
    if (superClass) _set_prototype_of(subClass, superClass);
}
function _iterable_to_array(iter) {
    if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter);
}
function _non_iterable_spread() {
    throw new TypeError("Invalid attempt to spread non-iterable instance.\\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}
function _possible_constructor_return(self, call) {
    if (call && (widget_type_of(call) === "object" || typeof call === "function")) {
        return call;
    }
    return _assert_this_initialized(self);
}
function _set_prototype_of(o, p) {
    _set_prototype_of = Object.setPrototypeOf || function setPrototypeOf(o, p) {
        o.__proto__ = p;
        return o;
    };
    return _set_prototype_of(o, p);
}
function _super_prop_base(object, property) {
    while(!Object.prototype.hasOwnProperty.call(object, property)){
        object = _get_prototype_of(object);
        if (object === null) break;
    }
    return object;
}
function _to_consumable_array(arr) {
    return _array_without_holes(arr) || _iterable_to_array(arr) || widget_unsupported_iterable_to_array(arr) || _non_iterable_spread();
}
function widget_type_of(obj) {
    "@swc/helpers - typeof";
    return obj && typeof Symbol !== "undefined" && obj.constructor === Symbol ? "symbol" : typeof obj;
}
function widget_unsupported_iterable_to_array(o, minLen) {
    if (!o) return;
    if (typeof o === "string") return widget_array_like_to_array(o, minLen);
    var n = Object.prototype.toString.call(o).slice(8, -1);
    if (n === "Object" && o.constructor) n = o.constructor.name;
    if (n === "Map" || n === "Set") return Array.from(n);
    if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return widget_array_like_to_array(o, minLen);
}
function _is_native_reflect_construct() {
    try {
        var result = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {}));
    } catch (_) {}
    return (_is_native_reflect_construct = function() {
        return !!result;
    })();
}
function widget_ts_generator(thisArg, body) {
    var f, y, t, _ = {
        label: 0,
        sent: function() {
            if (t[0] & 1) throw t[1];
            return t[1];
        },
        trys: [],
        ops: []
    }, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype), d = Object.defineProperty;
    return d(g, "next", {
        value: verb(0)
    }), d(g, "throw", {
        value: verb(1)
    }), d(g, "return", {
        value: verb(2)
    }), typeof Symbol === "function" && d(g, Symbol.iterator, {
        value: function() {
            return this;
        }
    }), g;
    function verb(n) {
        return function(v) {
            return step([
                n,
                v
            ]);
        };
    }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while(g && (g = 0, op[0] && (_ = 0)), _)try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [
                op[0] & 2,
                t.value
            ];
            switch(op[0]){
                case 0:
                case 1:
                    t = op;
                    break;
                case 4:
                    _.label++;
                    return {
                        value: op[1],
                        done: false
                    };
                case 5:
                    _.label++;
                    y = op[1];
                    op = [
                        0
                    ];
                    continue;
                case 7:
                    op = _.ops.pop();
                    _.trys.pop();
                    continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) {
                        _ = 0;
                        continue;
                    }
                    if (op[0] === 3 && (!t || op[1] > t[0] && op[1] < t[3])) {
                        _.label = op[1];
                        break;
                    }
                    if (op[0] === 6 && _.label < t[1]) {
                        _.label = t[1];
                        t = op;
                        break;
                    }
                    if (t && _.label < t[2]) {
                        _.label = t[2];
                        _.ops.push(op);
                        break;
                    }
                    if (t[2]) _.ops.pop();
                    _.trys.pop();
                    continue;
            }
            op = body.call(thisArg, _);
        } catch (e) {
            op = [
                6,
                e
            ];
            y = 0;
        } finally{
            f = t = 0;
        }
        if (op[0] & 5) throw op[1];
        return {
            value: op[0] ? op[1] : void 0,
            done: true
        };
    }
}



// @ts-expect-error - injected by bundler
var version = "0.11.0";
/* export default */ function src_widget(param) {
    var DOMWidgetModel = param.DOMWidgetModel, DOMWidgetView = param.DOMWidgetView;
    var RUNTIMES = new WeakMap();
    var AnyModel = /*#__PURE__*/ function(DOMWidgetModel) {
        "use strict";
        _inherits(AnyModel, DOMWidgetModel);
        function AnyModel() {
            widget_class_call_check(this, AnyModel);
            return _call_super(this, AnyModel, arguments);
        }
        widget_create_class(AnyModel, [
            {
                key: "initialize",
                value: function initialize() {
                    var _this = this;
                    for(var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++){
                        args[_key] = arguments[_key];
                    }
                    var _$_get;
                    (_$_get = _get(_get_prototype_of(AnyModel.prototype), "initialize", this)).call.apply(_$_get, [
                        this
                    ].concat(_to_consumable_array(args)));
                    var controller = new AbortController();
                    this.once("destroy", function() {
                        controller.abort("[anywidget] Runtime destroyed.");
                        BINDINGS.destroy(_this);
                        RUNTIMES.delete(_this);
                    });
                    RUNTIMES.set(this, new runtime_Runtime(this, {
                        signal: controller.signal
                    }));
                }
            },
            {
                key: "_handle_comm_msg",
                value: function _handle_comm_msg() {
                    var _this = this;
                    for(var _len = arguments.length, msg = new Array(_len), _key = 0; _key < _len; _key++){
                        msg[_key] = arguments[_key];
                    }
                    var _this1 = this, _superprop_get__handle_comm_msg = function _superprop_get__handle_comm_msg() {
                        return _get(_get_prototype_of(AnyModel.prototype), "_handle_comm_msg", _this);
                    };
                    return widget_async_to_generator(function() {
                        var _superprop_get__handle_comm_msg1, runtime;
                        return widget_ts_generator(this, function(_state) {
                            switch(_state.label){
                                case 0:
                                    runtime = RUNTIMES.get(this);
                                    return [
                                        4,
                                        runtime === null || runtime === void 0 ? void 0 : runtime.ready
                                    ];
                                case 1:
                                    _state.sent();
                                    return [
                                        2,
                                        (_superprop_get__handle_comm_msg1 = _superprop_get__handle_comm_msg()).call.apply(_superprop_get__handle_comm_msg1, [
                                            _this1
                                        ].concat(_to_consumable_array(msg)))
                                    ];
                            }
                        });
                    }).call(this);
                }
            },
            {
                /**
     * We override to support binary trailets because JSON.parse(JSON.stringify())
     * does not properly clone binary data (it just returns an empty object).
     *
     * https://github.com/jupyter-widgets/ipywidgets/blob/47058a373d2c2b3acf101677b2745e14b76dd74b/packages/base/src/widget.ts#L562-L583
     */ key: "serialize",
                value: function serialize(state) {
                    // oxlint-disable-next-line typescript-eslint/no-unsafe-type-assertion -- accessing static `.serializers` on `this.constructor`
                    var serializers = this.constructor.serializers || {};
                    var _iteratorNormalCompletion = true, _didIteratorError = false, _iteratorError = undefined;
                    try {
                        for(var _iterator = Object.keys(state)[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true){
                            var k = _step.value;
                            try {
                                var _serializers_k, _state_k;
                                var serialize = (_serializers_k = serializers[k]) === null || _serializers_k === void 0 ? void 0 : _serializers_k.serialize;
                                if (serialize) {
                                    state[k] = serialize(state[k], this);
                                } else if (k === "layout" || k === "style") {
                                    // These keys come from ipywidgets, rely on JSON.stringify trick.
                                    state[k] = JSON.parse(JSON.stringify(state[k]));
                                } else {
                                    state[k] = structuredClone(state[k]);
                                }
                                if (typeof ((_state_k = state[k]) === null || _state_k === void 0 ? void 0 : _state_k.toJSON) === "function") {
                                    state[k] = state[k].toJSON();
                                }
                            } catch (e) {
                                console.error("Error serializing widget state attribute: ", k);
                                throw e;
                            }
                        }
                    } catch (err) {
                        _didIteratorError = true;
                        _iteratorError = err;
                    } finally{
                        try {
                            if (!_iteratorNormalCompletion && _iterator.return != null) {
                                _iterator.return();
                            }
                        } finally{
                            if (_didIteratorError) {
                                throw _iteratorError;
                            }
                        }
                    }
                    return state;
                }
            }
        ]);
        return AnyModel;
    }(DOMWidgetModel);
    widget_define_property(AnyModel, "model_name", "AnyModel");
    widget_define_property(AnyModel, "model_module", "anywidget");
    widget_define_property(AnyModel, "model_module_version", version);
    widget_define_property(AnyModel, "view_name", "AnyView");
    widget_define_property(AnyModel, "view_module", "anywidget");
    widget_define_property(AnyModel, "view_module_version", version);
    var _controller = /*#__PURE__*/ new WeakMap();
    var AnyView = /*#__PURE__*/ function(DOMWidgetView) {
        "use strict";
        _inherits(AnyView, DOMWidgetView);
        function AnyView() {
            widget_class_call_check(this, AnyView);
            var _this;
            _this = _call_super(this, AnyView, arguments), widget_class_private_field_init(_this, _controller, {
                writable: true,
                value: new AbortController()
            });
            return _this;
        }
        widget_create_class(AnyView, [
            {
                key: "render",
                value: function render() {
                    return widget_async_to_generator(function() {
                        var runtime;
                        return widget_ts_generator(this, function(_state) {
                            switch(_state.label){
                                case 0:
                                    runtime = RUNTIMES.get(this.model);
                                    assert(runtime, "[anywidget] Runtime not found.");
                                    return [
                                        4,
                                        runtime.createView(this, {
                                            signal: widget_class_private_field_get(this, _controller).signal
                                        })
                                    ];
                                case 1:
                                    _state.sent();
                                    return [
                                        2
                                    ];
                            }
                        });
                    }).call(this);
                }
            },
            {
                key: "remove",
                value: function remove() {
                    widget_class_private_field_get(this, _controller).abort("[anywidget] View destroyed.");
                    _get(_get_prototype_of(AnyView.prototype), "remove", this).call(this);
                }
            }
        ]);
        return AnyView;
    }(DOMWidgetView);
    return {
        AnyModel: AnyModel,
        AnyView: AnyView
    };
}

;// CONCATENATED MODULE: ./packages/anywidget/src/plugin.js




/**
 * @typedef JupyterLabRegistry
 * @property {(widget: { name: string, version: string, exports: any }) => void} registerWidget
 */

/* export default */ const src_plugin = ({
  id: "anywidget:plugin",
  requires: [/** @type{unknown} */ (base_6_strict_.IJupyterWidgetRegistry)],
  activate: (/** @type {unknown} */ _app, /** @type {JupyterLabRegistry} */ registry) => {
    let exports = src_widget(base_6_strict_);
    registry.registerWidget({
      name: "anywidget",
      // @ts-expect-error Added by bundler
      version: "0.11.0",
      exports,
    });
  },
  autoStart: true,
});


},

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiNTI4LmIwNmY2NTU5LmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvbW9kZWwtcHJveHkudHMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvdXRpbC50cyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvLy4vcGFja2FnZXMvYW55d2lkZ2V0L3NyYy9iaW5kaW5nLnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL2ludm9rZS50cyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvLy4vcGFja2FnZXMvYW55d2lkZ2V0L3NyYy93aWRnZXQtcmVmLnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL2hvc3QudHMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvbG9hZC50cyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvLy4vcGFja2FnZXMvYW55d2lkZ2V0L3NyYy9vYnNlcnZlLnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL3J1bnRpbWUudHMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvd2lkZ2V0LnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL3BsdWdpbi5qcyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgdHlwZSB7IEFueU1vZGVsIH0gZnJvbSBcIkBhbnl3aWRnZXQvdHlwZXNcIjtcbmltcG9ydCB0eXBlIHsgRE9NV2lkZ2V0TW9kZWwgfSBmcm9tIFwiQGp1cHl0ZXItd2lkZ2V0cy9iYXNlXCI7XG5cbi8qKlxuICogVGhpcyBpcyBhIHRyaWNrIHNvIHRoYXQgd2UgY2FuIGNsZWFudXAgZXZlbnQgbGlzdGVuZXJzIGFkZGVkXG4gKiBieSB0aGUgdXNlci1kZWZpbmVkIGZ1bmN0aW9uLlxuICovXG5leHBvcnQgbGV0IElOSVRJQUxJWkVfTUFSS0VSID0gU3ltYm9sKFwiYW55d2lkZ2V0LmluaXRpYWxpemVcIik7XG5cbi8qKlxuICogUHJ1bmVzIHRoZSB2aWV3IGRvd24gdG8gdGhlIG1pbmltdW0gY29udGV4dCBuZWNlc3NhcnkuXG4gKlxuICogQ2FsbHMgdG8gYG1vZGVsLmdldGAgYW5kIGBtb2RlbC5zZXRgIGF1dG9tYXRpY2FsbHkgYWRkIHRoZVxuICogYGNvbnRleHRgLCBzbyB3ZSBjYW4gZ3JhY2VmdWxseSB1bnN1YnNjcmliZSBmcm9tIGV2ZW50c1xuICogYWRkZWQgYnkgdXNlci1kZWZpbmVkIGhvb2tzLlxuICovXG5leHBvcnQgZnVuY3Rpb24gbW9kZWxQcm94eShtb2RlbDogRE9NV2lkZ2V0TW9kZWwsIGNvbnRleHQ6IHVua25vd24pOiBBbnlNb2RlbCB7XG4gIC8vIG94bGludC1kaXNhYmxlLW5leHQtbGluZSB0eXBlc2NyaXB0LWVzbGludC9uby11bnNhZmUtdHlwZS1hc3NlcnRpb24gLS0gRE9NV2lkZ2V0TW9kZWwuZ2V0L3NldC9vbi9vZmYgaGF2ZSB3aWRlciBzaWduYXR1cmVzIHRoYW4gQW55TW9kZWwsIHNvIGJvdW5kIHZlcnNpb25zIGRvbid0IG5hcnJvdyBjbGVhbmx5OyB0aGUgc2hhcGUgaXMgc3RydWN0dXJhbGx5IGNvbXBhdGlibGVcbiAgcmV0dXJuIHtcbiAgICBnZXQ6IG1vZGVsLmdldC5iaW5kKG1vZGVsKSxcbiAgICBzZXQ6IG1vZGVsLnNldC5iaW5kKG1vZGVsKSxcbiAgICBzYXZlX2NoYW5nZXM6IG1vZGVsLnNhdmVfY2hhbmdlcy5iaW5kKG1vZGVsKSxcbiAgICBzZW5kOiBtb2RlbC5zZW5kLmJpbmQobW9kZWwpLFxuICAgIG9uKG5hbWUsIGNhbGxiYWNrKSB7XG4gICAgICBtb2RlbC5vbihuYW1lLCBjYWxsYmFjaywgY29udGV4dCk7XG4gICAgfSxcbiAgICBvZmYobmFtZSwgY2FsbGJhY2spIHtcbiAgICAgIG1vZGVsLm9mZihuYW1lLCBjYWxsYmFjaywgY29udGV4dCk7XG4gICAgfSxcbiAgICAvLyBUaGUgd2lkZ2V0X21hbmFnZXIgdHlwZSBpcyB3aWRlciB0aGFuIHdoYXQgd2Ugd2FudCB0byBleHBvc2UgdG9cbiAgICAvLyBkZXZlbG9wZXJzLiBJbiBhIGZ1dHVyZSB2ZXJzaW9uLCB3ZSB3aWxsIGV4cG9zZSBhIG1vcmUgbGltaXRlZCBBUEkgYnV0XG4gICAgLy8gdGhhdCBjYW4gd2FpdCBmb3IgYSBtaW5vciB2ZXJzaW9uIGJ1bXAuXG4gICAgd2lkZ2V0X21hbmFnZXI6IG1vZGVsLndpZGdldF9tYW5hZ2VyLFxuICB9IGFzIEFueU1vZGVsO1xufVxuIiwiZXhwb3J0IHR5cGUgQXdhaXRhYmxlPFQ+ID0gVCB8IFByb21pc2VMaWtlPFQ+O1xuXG5leHBvcnQgaW50ZXJmYWNlIFJlYWR5PFQ+IHtcbiAgc3RhdHVzOiBcInJlYWR5XCI7XG4gIGRhdGE6IFQ7XG59XG5cbmV4cG9ydCBpbnRlcmZhY2UgUGVuZGluZyB7XG4gIHN0YXR1czogXCJwZW5kaW5nXCI7XG59XG5cbmV4cG9ydCBpbnRlcmZhY2UgRXJyb3JlZCB7XG4gIHN0YXR1czogXCJlcnJvclwiO1xuICBlcnJvcjogdW5rbm93bjtcbn1cblxuZXhwb3J0IHR5cGUgUmVzdWx0PFQ+ID0gUGVuZGluZyB8IFJlYWR5PFQ+IHwgRXJyb3JlZDtcblxuZXhwb3J0IGZ1bmN0aW9uIGFzc2VydChjb25kaXRpb246IHVua25vd24sIG1lc3NhZ2U6IHN0cmluZyk6IGFzc2VydHMgY29uZGl0aW9uIHtcbiAgaWYgKCFjb25kaXRpb24pIHRocm93IG5ldyBFcnJvcihtZXNzYWdlKTtcbn1cblxuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIHNhZmVDbGVhbnVwKFxuICBmbjogdm9pZCB8ICgoKSA9PiBBd2FpdGFibGU8dm9pZD4pIHwgdW5kZWZpbmVkLFxuICBraW5kOiBzdHJpbmcsXG4pOiBQcm9taXNlPHZvaWQ+IHtcbiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSgpXG4gICAgLnRoZW4oKCkgPT4gZm4/LigpKVxuICAgIC5jYXRjaCgoZSkgPT4gY29uc29sZS53YXJuKGBbYW55d2lkZ2V0XSBlcnJvciBjbGVhbmluZyB1cCAke2tpbmR9LmAsIGUpKTtcbn1cblxuLyoqXG4gKiBDbGVhbnMgdXAgdGhlIHN0YWNrIHRyYWNlIGF0IGFueXdpZGdldCBib3VuZGFyeS5cbiAqIFlvdSBjYW4gZnVsbHkgaW5zcGVjdCB0aGUgZW50aXJlIHN0YWNrIHRyYWNlIGluIHRoZSBjb25zb2xlIGludGVyYWN0aXZlbHksXG4gKiBidXQgdGhlIGluaXRpYWwgZXJyb3IgbWVzc2FnZSBpcyBjbGVhbmVkIHVwIHRvIGJlIG1vcmUgdXNlci1mcmllbmRseS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIHRocm93QW55d2lkZ2V0RXJyb3Ioc291cmNlOiB1bmtub3duKTogbmV2ZXIge1xuICBpZiAoIShzb3VyY2UgaW5zdGFuY2VvZiBFcnJvcikpIHtcbiAgICAvLyBEb24ndCBrbm93IHdoYXQgdG8gZG8gd2l0aCB0aGlzLlxuICAgIHRocm93IHNvdXJjZTtcbiAgfVxuICBsZXQgbGluZXMgPSBzb3VyY2Uuc3RhY2s/LnNwbGl0KFwiXFxuXCIpID8/IFtdO1xuICBsZXQgYW55d2lkZ2V0SW5kZXggPSBsaW5lcy5maW5kSW5kZXgoKGxpbmUpID0+IGxpbmUuaW5jbHVkZXMoXCJhbnl3aWRnZXRcIikpO1xuICBsZXQgY2xlYW5TdGFjayA9IGFueXdpZGdldEluZGV4ID09PSAtMSA/IGxpbmVzIDogbGluZXMuc2xpY2UoMCwgYW55d2lkZ2V0SW5kZXggKyAxKTtcbiAgc291cmNlLnN0YWNrID0gY2xlYW5TdGFjay5qb2luKFwiXFxuXCIpO1xuICBjb25zb2xlLmVycm9yKHNvdXJjZSk7XG4gIHRocm93IHNvdXJjZTtcbn1cblxuLyoqXG4gKiBQb2x5ZmlsbCBmb3Ige0BsaW5rIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0phdmFTY3JpcHQvUmVmZXJlbmNlL0dsb2JhbF9PYmplY3RzL1Byb21pc2Uvd2l0aFJlc29sdmVycyBQcm9taXNlLndpdGhSZXNvbHZlcnN9XG4gKlxuICogVHJldm9yKDIwMjUtMDMtMTQpOiBTaG91bGQgYmUgYWJsZSB0byByZW1vdmUgb25jZSBtb3JlIHN0YWJsZSBhY3Jvc3MgYnJvd3NlcnMuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBwcm9taXNlV2l0aFJlc29sdmVyczxUPigpOiBQcm9taXNlV2l0aFJlc29sdmVyczxUPiB7XG4gIGxldCByZXNvbHZlITogKHZhbHVlOiBUIHwgUHJvbWlzZUxpa2U8VD4pID0+IHZvaWQ7XG4gIGxldCByZWplY3QhOiAocmVhc29uPzogdW5rbm93bikgPT4gdm9pZDtcbiAgbGV0IHByb21pc2UgPSBuZXcgUHJvbWlzZTxUPigocmVzLCByZWopID0+IHtcbiAgICByZXNvbHZlID0gcmVzO1xuICAgIHJlamVjdCA9IHJlajtcbiAgfSk7XG4gIHJldHVybiB7IHByb21pc2UsIHJlc29sdmUsIHJlamVjdCB9O1xufVxuIiwiaW1wb3J0IHR5cGUgeyBFeHBlcmltZW50YWwsIEhvc3QgfSBmcm9tIFwiQGFueXdpZGdldC90eXBlc1wiO1xuaW1wb3J0IHR5cGUgeyBET01XaWRnZXRNb2RlbCB9IGZyb20gXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIjtcblxuaW1wb3J0IHR5cGUgeyBBbnlXaWRnZXQgfSBmcm9tIFwiLi9sb2FkLnRzXCI7XG5pbXBvcnQgeyBJTklUSUFMSVpFX01BUktFUiwgbW9kZWxQcm94eSB9IGZyb20gXCIuL21vZGVsLXByb3h5LnRzXCI7XG5pbXBvcnQgeyB0eXBlIEF3YWl0YWJsZSwgcHJvbWlzZVdpdGhSZXNvbHZlcnMsIHNhZmVDbGVhbnVwIH0gZnJvbSBcIi4vdXRpbC50c1wiO1xuXG4vKipcbiAqIFRoZSBtaW5pbWFsIHN1cmZhY2UgYGNyZWF0ZVZpZXdgIG5lZWRzIGZyb20gYSB2aWV3LWxpa2Ugb2JqZWN0LiBUaGUgb2JqZWN0XG4gKiBpZGVudGl0eSBpcyB1c2VkIGFzIHRoZSBsaXN0ZW5lciBjb250ZXh0IGZvciBgbW9kZWxQcm94eWAsIGFuZCBgZWxgIGlzIHRoZVxuICogcmVuZGVyIHRhcmdldC5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBWaWV3VGFyZ2V0IHtcbiAgZWw6IEhUTUxFbGVtZW50O1xufVxuXG5mdW5jdGlvbiBpc1NhZmVDbGVhbnVwRnVuY3Rpb24oeDogdW5rbm93bik6IHggaXMgKCkgPT4gQXdhaXRhYmxlPHZvaWQ+IHtcbiAgcmV0dXJuIHR5cGVvZiB4ID09PSBcImZ1bmN0aW9uXCI7XG59XG5cbmV4cG9ydCBjbGFzcyBXaWRnZXRCaW5kaW5nIHtcbiAgI2NvbnRyb2xsZXI6IEFib3J0Q29udHJvbGxlciB8IHVuZGVmaW5lZDtcbiAgI3dpZGdldERlZjogQW55V2lkZ2V0IHwgdW5kZWZpbmVkO1xuICAjZXhwb3J0czogdW5rbm93bjtcbiAgI21vZGVsOiBET01XaWRnZXRNb2RlbDtcbiAgcmVhZHk6IFByb21pc2U8dW5rbm93bj47XG4gICNyZXNvbHZlcnM6IFByb21pc2VXaXRoUmVzb2x2ZXJzPHVua25vd24+O1xuXG4gIGNvbnN0cnVjdG9yKG1vZGVsOiBET01XaWRnZXRNb2RlbCkge1xuICAgIHRoaXMuI21vZGVsID0gbW9kZWw7XG4gICAgdGhpcy4jcmVzb2x2ZXJzID0gcHJvbWlzZVdpdGhSZXNvbHZlcnMoKTtcbiAgICB0aGlzLnJlYWR5ID0gdGhpcy4jcmVzb2x2ZXJzLnByb21pc2U7XG4gIH1cblxuICBhc3luYyBiaW5kKFxuICAgIHdpZGdldERlZjogQW55V2lkZ2V0LFxuICAgIHsgZXhwZXJpbWVudGFsIH06IHsgZXhwZXJpbWVudGFsOiBFeHBlcmltZW50YWwgfSxcbiAgKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgaWYgKHRoaXMuI3dpZGdldERlZiA9PT0gd2lkZ2V0RGVmKSByZXR1cm47XG5cbiAgICBpZiAodGhpcy4jd2lkZ2V0RGVmICYmIHRoaXMuI3dpZGdldERlZiAhPT0gd2lkZ2V0RGVmKSB7XG4gICAgICB0aGlzLiNjb250cm9sbGVyPy5hYm9ydCgpO1xuICAgICAgLy8gU2V0dGxlIHRoZSBvbGQgcHJvbWlzZSBzbyBhbnkgYXdhaXRlciB0aGF0IGNhcHR1cmVkIGB0aGlzLnJlYWR5YFxuICAgICAgLy8gKGUuZy4gYSBwYXJlbnQncyBgaG9zdC5nZXRXaWRnZXRgIHNuYXBzaG90KSB1bmJsb2NrcyBpbnN0ZWFkIG9mXG4gICAgICAvLyBoYW5naW5nIHVudGlsIHRoZSBob3N0J3MgMTBzIHRpbWVvdXQuIE5vLW9wIGlmIGFscmVhZHkgcmVzb2x2ZWQuXG4gICAgICBsZXQgcHJldlJlc29sdmVycyA9IHRoaXMuI3Jlc29sdmVycztcbiAgICAgIHRoaXMuI3Jlc29sdmVycyA9IHByb21pc2VXaXRoUmVzb2x2ZXJzKCk7XG4gICAgICB0aGlzLnJlYWR5ID0gdGhpcy4jcmVzb2x2ZXJzLnByb21pc2U7XG4gICAgICBwcmV2UmVzb2x2ZXJzLnByb21pc2UuY2F0Y2goKCkgPT4ge30pO1xuICAgICAgcHJldlJlc29sdmVycy5yZWplY3QobmV3IEVycm9yKFwiW2FueXdpZGdldF0gd2lkZ2V0IGJpbmQgYWJvcnRlZCBieSByZS1iaW5kXCIpKTtcbiAgICB9XG5cbiAgICB0aGlzLiN3aWRnZXREZWYgPSB3aWRnZXREZWY7XG4gICAgdGhpcy4jY29udHJvbGxlciA9IG5ldyBBYm9ydENvbnRyb2xsZXIoKTtcbiAgICBsZXQgc2lnbmFsID0gdGhpcy4jY29udHJvbGxlci5zaWduYWw7XG4gICAgbGV0IG1vZGVsID0gdGhpcy4jbW9kZWw7XG5cbiAgICBtb2RlbC5vZmYobnVsbCwgbnVsbCwgSU5JVElBTElaRV9NQVJLRVIpO1xuXG4gICAgbGV0IHJlc3VsdCA9IGF3YWl0IHdpZGdldERlZi5pbml0aWFsaXplPy4oe1xuICAgICAgbW9kZWw6IG1vZGVsUHJveHkobW9kZWwsIElOSVRJQUxJWkVfTUFSS0VSKSxcbiAgICAgIHNpZ25hbCxcbiAgICAgIGV4cGVyaW1lbnRhbCxcbiAgICB9KTtcblxuICAgIGlmIChzaWduYWwuYWJvcnRlZCkge1xuICAgICAgYXdhaXQgc2FmZUNsZWFudXAoaXNTYWZlQ2xlYW51cEZ1bmN0aW9uKHJlc3VsdCkgPyByZXN1bHQgOiB1bmRlZmluZWQsIFwiZXNtIHVwZGF0ZVwiKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBpZiAoaXNTYWZlQ2xlYW51cEZ1bmN0aW9uKHJlc3VsdCkpIHtcbiAgICAgIHNpZ25hbC5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4gc2FmZUNsZWFudXAocmVzdWx0LCBcImVzbSB1cGRhdGVcIikpO1xuICAgICAgdGhpcy4jZXhwb3J0cyA9IHVuZGVmaW5lZDtcbiAgICB9IGVsc2UgaWYgKHR5cGVvZiByZXN1bHQgPT09IFwib2JqZWN0XCIgJiYgcmVzdWx0ICE9PSBudWxsKSB7XG4gICAgICB0aGlzLiNleHBvcnRzID0gcmVzdWx0O1xuICAgIH0gZWxzZSB7XG4gICAgICB0aGlzLiNleHBvcnRzID0gdW5kZWZpbmVkO1xuICAgIH1cblxuICAgIHRoaXMuI3Jlc29sdmVycy5yZXNvbHZlKHRoaXMuI2V4cG9ydHMpO1xuICB9XG5cbiAgYXN5bmMgY3JlYXRlVmlldyhcbiAgICB0YXJnZXQ6IFZpZXdUYXJnZXQsXG4gICAgeyBzaWduYWwsIGV4cGVyaW1lbnRhbCwgaG9zdCB9OiB7IHNpZ25hbDogQWJvcnRTaWduYWw7IGV4cGVyaW1lbnRhbDogRXhwZXJpbWVudGFsOyBob3N0OiBIb3N0IH0sXG4gICk6IFByb21pc2U8dW5kZWZpbmVkPiB7XG4gICAgYXdhaXQgdGhpcy5yZWFkeTtcbiAgICBpZiAoIXRoaXMuI3dpZGdldERlZj8ucmVuZGVyKSByZXR1cm47XG4gICAgbGV0IGNvbnRyb2xsZXIgPSBuZXcgQWJvcnRDb250cm9sbGVyKCk7XG4gICAgbGV0IGNvbWJpbmVkID0gQWJvcnRTaWduYWwuYW55KFtzaWduYWwsIGNvbnRyb2xsZXIuc2lnbmFsXSk7XG4gICAgbGV0IG1vZGVsID0gdGhpcy4jbW9kZWw7XG4gICAgbGV0IGNsZWFudXAgPSBhd2FpdCB0aGlzLiN3aWRnZXREZWYucmVuZGVyKHtcbiAgICAgIG1vZGVsOiBtb2RlbFByb3h5KG1vZGVsLCB0YXJnZXQpLFxuICAgICAgZWw6IHRhcmdldC5lbCxcbiAgICAgIHNpZ25hbDogY29tYmluZWQsXG4gICAgICBob3N0LFxuICAgICAgZXhwZXJpbWVudGFsLFxuICAgIH0pO1xuICAgIGxldCBkaXNwb3NlVmlldyA9IChyZWFzb246IHN0cmluZyk6IHZvaWQgPT4ge1xuICAgICAgLy8gQ2xlYXIgbGlzdGVuZXJzIGtleWVkIHRvIHRoaXMgdGFyZ2V0LiBGb3IgZXBoZW1lcmFsIGB7ZWx9YCB0YXJnZXRzXG4gICAgICAvLyAoaG9zdC5nZXRXaWRnZXQoKS5yZW5kZXIpLCB0aGlzIHByZXZlbnRzIGxlYWtzIGFjcm9zcyByZS1yZW5kZXJzLlxuICAgICAgbW9kZWwub2ZmKG51bGwsIG51bGwsIHRhcmdldCk7XG4gICAgICB2b2lkIHNhZmVDbGVhbnVwKGNsZWFudXAsIHJlYXNvbik7XG4gICAgfTtcbiAgICBpZiAoY29tYmluZWQuYWJvcnRlZCkge1xuICAgICAgZGlzcG9zZVZpZXcoXCJkaXNwb3NlIHZpZXcgLSBhbHJlYWR5IGFib3J0ZWRcIik7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbWJpbmVkLmFkZEV2ZW50TGlzdGVuZXIoXCJhYm9ydFwiLCAoKSA9PiBkaXNwb3NlVmlldyhcImRpc3Bvc2UgdmlldyAtIGFib3J0ZWRcIikpO1xuICB9XG5cbiAgZ2V0IGV4cG9ydHMoKTogdW5rbm93biB7XG4gICAgcmV0dXJuIHRoaXMuI2V4cG9ydHM7XG4gIH1cblxuICBkZXN0cm95KCk6IHZvaWQge1xuICAgIHRoaXMuI2NvbnRyb2xsZXI/LmFib3J0KCk7XG4gICAgdGhpcy4jY29udHJvbGxlciA9IHVuZGVmaW5lZDtcbiAgICB0aGlzLiN3aWRnZXREZWYgPSB1bmRlZmluZWQ7XG4gIH1cbn1cblxuY2xhc3MgQmluZGluZ01hbmFnZXIge1xuICAjYmluZGluZ3MgPSBuZXcgTWFwPERPTVdpZGdldE1vZGVsLCBXaWRnZXRCaW5kaW5nPigpO1xuXG4gIGdldE9yQ3JlYXRlKG1vZGVsOiBET01XaWRnZXRNb2RlbCk6IFdpZGdldEJpbmRpbmcge1xuICAgIGxldCBiaW5kaW5nID0gdGhpcy4jYmluZGluZ3MuZ2V0KG1vZGVsKTtcbiAgICBpZiAoIWJpbmRpbmcpIHtcbiAgICAgIGJpbmRpbmcgPSBuZXcgV2lkZ2V0QmluZGluZyhtb2RlbCk7XG4gICAgICB0aGlzLiNiaW5kaW5ncy5zZXQobW9kZWwsIGJpbmRpbmcpO1xuICAgIH1cbiAgICByZXR1cm4gYmluZGluZztcbiAgfVxuXG4gIGdldChtb2RlbDogRE9NV2lkZ2V0TW9kZWwpOiBXaWRnZXRCaW5kaW5nIHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy4jYmluZGluZ3MuZ2V0KG1vZGVsKTtcbiAgfVxuXG4gIGRlc3Ryb3kobW9kZWw6IERPTVdpZGdldE1vZGVsKTogdm9pZCB7XG4gICAgbGV0IGJpbmRpbmcgPSB0aGlzLiNiaW5kaW5ncy5nZXQobW9kZWwpO1xuICAgIGlmIChiaW5kaW5nKSB7XG4gICAgICBiaW5kaW5nLmRlc3Ryb3koKTtcbiAgICAgIHRoaXMuI2JpbmRpbmdzLmRlbGV0ZShtb2RlbCk7XG4gICAgfVxuICB9XG59XG5cbmV4cG9ydCBsZXQgQklORElOR1MgPSBuZXcgQmluZGluZ01hbmFnZXIoKTtcbiIsImltcG9ydCB0eXBlIHsgQW55TW9kZWwgfSBmcm9tIFwiQGFueXdpZGdldC90eXBlc1wiO1xuaW1wb3J0ICogYXMgdXVpZCBmcm9tIFwiQGx1a2VlZC91dWlkXCI7XG5cbmV4cG9ydCBpbnRlcmZhY2UgSW52b2tlT3B0aW9ucyB7XG4gIGJ1ZmZlcnM/OiBEYXRhVmlld1tdO1xuICBzaWduYWw/OiBBYm9ydFNpZ25hbDtcbn1cblxuZXhwb3J0IGZ1bmN0aW9uIGludm9rZTxUPihcbiAgbW9kZWw6IEFueU1vZGVsLFxuICBuYW1lOiBzdHJpbmcsXG4gIG1zZz86IHVua25vd24sXG4gIG9wdGlvbnM6IEludm9rZU9wdGlvbnMgPSB7fSxcbik6IFByb21pc2U8W1QsIERhdGFWaWV3W11dPiB7XG4gIC8vIGNyeXB0by5yYW5kb21VVUlEKCkgaXMgbm90IGF2YWlsYWJsZSBpbiBub24tc2VjdXJlIGNvbnRleHRzIChpLmUuLCBodHRwOi8vKVxuICAvLyBzbyB3ZSB1c2Ugc2ltcGxlIChub24tc2VjdXJlKSBwb2x5ZmlsbC5cbiAgbGV0IGlkID0gdXVpZC52NCgpO1xuICBsZXQgc2lnbmFsID0gb3B0aW9ucy5zaWduYWwgPz8gQWJvcnRTaWduYWwudGltZW91dCgzMDAwKTtcblxuICByZXR1cm4gbmV3IFByb21pc2UoKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgIGlmIChzaWduYWwuYWJvcnRlZCkge1xuICAgICAgcmVqZWN0KHNpZ25hbC5yZWFzb24pO1xuICAgIH1cbiAgICBzaWduYWwuYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IHtcbiAgICAgIG1vZGVsLm9mZihcIm1zZzpjdXN0b21cIiwgaGFuZGxlcik7XG4gICAgICByZWplY3Qoc2lnbmFsLnJlYXNvbik7XG4gICAgfSk7XG5cbiAgICBmdW5jdGlvbiBoYW5kbGVyKFxuICAgICAgbXNnOiB7IGlkOiBzdHJpbmc7IGtpbmQ6IFwiYW55d2lkZ2V0LWNvbW1hbmQtcmVzcG9uc2VcIjsgcmVzcG9uc2U6IFQgfSxcbiAgICAgIGJ1ZmZlcnM6IERhdGFWaWV3W10sXG4gICAgKTogdm9pZCB7XG4gICAgICBpZiAoIShtc2cuaWQgPT09IGlkKSkgcmV0dXJuO1xuICAgICAgcmVzb2x2ZShbbXNnLnJlc3BvbnNlLCBidWZmZXJzXSk7XG4gICAgICBtb2RlbC5vZmYoXCJtc2c6Y3VzdG9tXCIsIGhhbmRsZXIpO1xuICAgIH1cbiAgICBtb2RlbC5vbihcIm1zZzpjdXN0b21cIiwgaGFuZGxlcik7XG4gICAgbW9kZWwuc2VuZCh7IGlkLCBraW5kOiBcImFueXdpZGdldC1jb21tYW5kXCIsIG5hbWUsIG1zZyB9LCB1bmRlZmluZWQsIG9wdGlvbnMuYnVmZmVycyA/PyBbXSk7XG4gIH0pO1xufVxuIiwiZXhwb3J0IGxldCBXSURHRVRfUkVGX1BSRUZJWCA9IFwiYW55d2lkZ2V0OlwiO1xuXG5leHBvcnQgZnVuY3Rpb24gcGFyc2VXaWRnZXRSZWYocmVmOiB1bmtub3duKTogc3RyaW5nIHtcbiAgaWYgKHR5cGVvZiByZWYgPT09IFwic3RyaW5nXCIgJiYgcmVmLnN0YXJ0c1dpdGgoV0lER0VUX1JFRl9QUkVGSVgpKSB7XG4gICAgcmV0dXJuIHJlZi5zbGljZShXSURHRVRfUkVGX1BSRUZJWC5sZW5ndGgpO1xuICB9XG4gIHRocm93IG5ldyBFcnJvcihgW2FueXdpZGdldF0gSW52YWxpZCB3aWRnZXQgcmVmZXJlbmNlOiAke0pTT04uc3RyaW5naWZ5KHJlZil9YCk7XG59XG4iLCJpbXBvcnQgdHlwZSB7IEhvc3QgfSBmcm9tIFwiQGFueXdpZGdldC90eXBlc1wiO1xuaW1wb3J0IHR5cGUgeyBET01XaWRnZXRNb2RlbCB9IGZyb20gXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIjtcblxuaW1wb3J0IHsgQklORElOR1MgfSBmcm9tIFwiLi9iaW5kaW5nLnRzXCI7XG5pbXBvcnQgeyBpbnZva2UgfSBmcm9tIFwiLi9pbnZva2UudHNcIjtcbmltcG9ydCB7IG1vZGVsUHJveHkgfSBmcm9tIFwiLi9tb2RlbC1wcm94eS50c1wiO1xuaW1wb3J0IHsgcGFyc2VXaWRnZXRSZWYgfSBmcm9tIFwiLi93aWRnZXQtcmVmLnRzXCI7XG5cbmV4cG9ydCBmdW5jdGlvbiBjcmVhdGVIb3N0KG1vZGVsOiBET01XaWRnZXRNb2RlbCwgeyBzaWduYWwgfTogeyBzaWduYWw6IEFib3J0U2lnbmFsIH0pOiBIb3N0IHtcbiAgbGV0IGhvc3Q6IEhvc3QgPSB7XG4gICAgLy8gQHRzLWV4cGVjdC1lcnJvciAtIG1vZGVsUHJveHkgcmV0dXJucyBBbnlNb2RlbDsgZ2VuZXJpYyBUIGlzIGVyYXNlZCBhdCBydW50aW1lXG4gICAgYXN5bmMgZ2V0TW9kZWwocmVmKSB7XG4gICAgICBsZXQgbW9kZWxJZCA9IHBhcnNlV2lkZ2V0UmVmKHJlZik7XG4gICAgICBsZXQgY2hpbGRNb2RlbCA9IGF3YWl0IG1vZGVsLndpZGdldF9tYW5hZ2VyLmdldF9tb2RlbChtb2RlbElkKTtcbiAgICAgIGxldCBjb250ZXh0ID0gU3ltYm9sKFwiYW55d2lkZ2V0Lmhvc3QuZ2V0TW9kZWxcIik7XG4gICAgICBzaWduYWwuYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IGNoaWxkTW9kZWwub2ZmKG51bGwsIG51bGwsIGNvbnRleHQpKTtcbiAgICAgIHJldHVybiBtb2RlbFByb3h5KGNoaWxkTW9kZWwsIGNvbnRleHQpO1xuICAgIH0sXG4gICAgLy8gQHRzLWV4cGVjdC1lcnJvciAtIGdlbmVyaWMgVCBpcyBlcmFzZWQgYXQgcnVudGltZSwgZXhwb3J0cyB0eXBlZCBhcyB1bmtub3duXG4gICAgYXN5bmMgZ2V0V2lkZ2V0KHJlZikge1xuICAgICAgbGV0IG1vZGVsSWQgPSBwYXJzZVdpZGdldFJlZihyZWYpO1xuICAgICAgbGV0IGNoaWxkTW9kZWwgPSBhd2FpdCBtb2RlbC53aWRnZXRfbWFuYWdlci5nZXRfbW9kZWwobW9kZWxJZCk7XG4gICAgICBsZXQgY2hpbGRCaW5kaW5nID0gQklORElOR1MuZ2V0KGNoaWxkTW9kZWwpO1xuICAgICAgaWYgKCFjaGlsZEJpbmRpbmcpIHtcbiAgICAgICAgdGhyb3cgbmV3IEVycm9yKGBbYW55d2lkZ2V0XSBObyBiaW5kaW5nIGZvdW5kIGZvciB3aWRnZXQgJHttb2RlbElkfWApO1xuICAgICAgfVxuICAgICAgbGV0IHRpbWVyOiBSZXR1cm5UeXBlPHR5cGVvZiBzZXRUaW1lb3V0PiB8IHVuZGVmaW5lZDtcbiAgICAgIGxldCBleHBvcnRzID0gYXdhaXQgbmV3IFByb21pc2U8dW5rbm93bj4oKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgICAgICB0aW1lciA9IHNldFRpbWVvdXQoXG4gICAgICAgICAgKCkgPT5cbiAgICAgICAgICAgIHJlamVjdChuZXcgRXJyb3IoYFthbnl3aWRnZXRdIFRpbWVkIG91dCB3YWl0aW5nIGZvciB3aWRnZXQgJHttb2RlbElkfSB0byBpbml0aWFsaXplYCkpLFxuICAgICAgICAgIDEwXzAwMCxcbiAgICAgICAgKTtcbiAgICAgICAgY2hpbGRCaW5kaW5nLnJlYWR5LnRoZW4ocmVzb2x2ZSwgcmVqZWN0KTtcbiAgICAgIH0pLmZpbmFsbHkoKCkgPT4gY2xlYXJUaW1lb3V0KHRpbWVyKSk7XG4gICAgICByZXR1cm4ge1xuICAgICAgICBleHBvcnRzLFxuICAgICAgICBhc3luYyByZW5kZXIoeyBlbCwgc2lnbmFsOiB2aWV3U2lnbmFsIH0pIHtcbiAgICAgICAgICBsZXQgY2hpbGRWaWV3U2lnbmFsID0gdmlld1NpZ25hbCA/PyBzaWduYWw7XG4gICAgICAgICAgYXdhaXQgY2hpbGRCaW5kaW5nLmNyZWF0ZVZpZXcoXG4gICAgICAgICAgICB7IGVsIH0sXG4gICAgICAgICAgICB7XG4gICAgICAgICAgICAgIHNpZ25hbDogY2hpbGRWaWV3U2lnbmFsLFxuICAgICAgICAgICAgICBleHBlcmltZW50YWw6IHtcbiAgICAgICAgICAgICAgICAvLyBAdHMtZXhwZWN0LWVycm9yIC0gYmluZCBpc24ndCB3b3JraW5nXG4gICAgICAgICAgICAgICAgaW52b2tlOiBpbnZva2UuYmluZChudWxsLCBjaGlsZE1vZGVsKSxcbiAgICAgICAgICAgICAgfSxcbiAgICAgICAgICAgICAgaG9zdCxcbiAgICAgICAgICAgIH0sXG4gICAgICAgICAgKTtcbiAgICAgICAgfSxcbiAgICAgIH07XG4gICAgfSxcbiAgfTtcbiAgcmV0dXJuIGhvc3Q7XG59XG4iLCJpbXBvcnQgdHlwZSB7IEluaXRpYWxpemUsIFJlbmRlciB9IGZyb20gXCJAYW55d2lkZ2V0L3R5cGVzXCI7XG5cbmltcG9ydCB7IGFzc2VydCB9IGZyb20gXCIuL3V0aWwudHNcIjtcblxuZXhwb3J0IGludGVyZmFjZSBBbnlXaWRnZXQge1xuICBpbml0aWFsaXplPzogSW5pdGlhbGl6ZTtcbiAgcmVuZGVyPzogUmVuZGVyO1xufVxuXG5leHBvcnQgaW50ZXJmYWNlIEFueVdpZGdldE1vZHVsZSB7XG4gIHJlbmRlcj86IFJlbmRlcjtcbiAgZGVmYXVsdD86IEFueVdpZGdldCB8ICgoKSA9PiBBbnlXaWRnZXQgfCBQcm9taXNlPEFueVdpZGdldD4pO1xufVxuXG5mdW5jdGlvbiBpc0hyZWYoc3RyOiBzdHJpbmcpOiBzdHIgaXMgYGh0dHBzOi8vJHtzdHJpbmd9YCB8IGBodHRwOi8vJHtzdHJpbmd9YCB7XG4gIHJldHVybiBzdHIuc3RhcnRzV2l0aChcImh0dHA6Ly9cIikgfHwgc3RyLnN0YXJ0c1dpdGgoXCJodHRwczovL1wiKTtcbn1cblxuYXN5bmMgZnVuY3Rpb24gbG9hZENzc0hyZWYoaHJlZjogc3RyaW5nLCBhbnl3aWRnZXRJZDogc3RyaW5nKTogUHJvbWlzZTx2b2lkPiB7XG4gIGxldCBwcmV2ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcjxIVE1MTGlua0VsZW1lbnQ+KGBsaW5rW2lkPScke2FueXdpZGdldElkfSddYCk7XG5cbiAgLy8gQWRhcHRlZCBmcm9tIGh0dHBzOi8vZ2l0aHViLmNvbS92aXRlanMvdml0ZS9ibG9iL2Q1OWUxYWNjMmVmYzAzMDc0ODgzNjRlOWYyZmFkNTI4ZWM1N2YyMDQvcGFja2FnZXMvdml0ZS9zcmMvY2xpZW50L2NsaWVudC50cyNMMTg1LUwyMDFcbiAgLy8gU3dhcHMgb3V0IG9sZCBzdHlsZXMgd2l0aCBuZXcsIGJ1dCBhdm9pZHMgZmxhc2ggb2YgdW5zdHlsZWQgY29udGVudC5cbiAgLy8gTm8gbmVlZCB0byBhd2FpdCB0aGUgbG9hZCBzaW5jZSB3ZSBhbHJlYWR5IGhhdmUgc3R5bGVzIGFwcGxpZWQuXG4gIGlmIChwcmV2KSB7XG4gICAgLy8gb3hsaW50LWRpc2FibGUtbmV4dC1saW5lIHR5cGVzY3JpcHQtZXNsaW50L25vLXVuc2FmZS10eXBlLWFzc2VydGlvbiAtLSBOb2RlLmNsb25lTm9kZSgpIHJldHVybnMgTm9kZTsgd2Uga25vdyBwcmV2IGlzIEhUTUxMaW5rRWxlbWVudCBzbyB0aGUgY2xvbmUgaXMgdG9vXG4gICAgbGV0IG5ld0xpbmsgPSBwcmV2LmNsb25lTm9kZSgpIGFzIHVua25vd24gYXMgSFRNTExpbmtFbGVtZW50O1xuICAgIG5ld0xpbmsuaHJlZiA9IGhyZWY7XG4gICAgbmV3TGluay5hZGRFdmVudExpc3RlbmVyKFwibG9hZFwiLCAoKSA9PiBwcmV2Py5yZW1vdmUoKSk7XG4gICAgbmV3TGluay5hZGRFdmVudExpc3RlbmVyKFwiZXJyb3JcIiwgKCkgPT4gcHJldj8ucmVtb3ZlKCkpO1xuICAgIHByZXYuYWZ0ZXIobmV3TGluayk7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgcmV0dXJuIG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7XG4gICAgbGV0IGxpbmsgPSBPYmplY3QuYXNzaWduKGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoXCJsaW5rXCIpLCB7XG4gICAgICByZWw6IFwic3R5bGVzaGVldFwiLFxuICAgICAgaHJlZixcbiAgICAgIG9ubG9hZDogcmVzb2x2ZSxcbiAgICB9KTtcbiAgICBkb2N1bWVudC5oZWFkLmFwcGVuZENoaWxkKGxpbmspO1xuICB9KTtcbn1cblxuZnVuY3Rpb24gbG9hZENzc1RleHQoY3NzVGV4dDogc3RyaW5nLCBhbnl3aWRnZXRJZDogc3RyaW5nKTogdm9pZCB7XG4gIGxldCBwcmV2ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcjxIVE1MU3R5bGVFbGVtZW50Pihgc3R5bGVbaWQ9JyR7YW55d2lkZ2V0SWR9J11gKTtcbiAgaWYgKHByZXYpIHtcbiAgICAvLyByZXBsYWNlIGluc3RlYWQgb2YgY3JlYXRpbmcgYSBuZXcgRE9NIG5vZGVcbiAgICBwcmV2LnRleHRDb250ZW50ID0gY3NzVGV4dDtcbiAgICByZXR1cm47XG4gIH1cbiAgbGV0IHN0eWxlID0gT2JqZWN0LmFzc2lnbihkb2N1bWVudC5jcmVhdGVFbGVtZW50KFwic3R5bGVcIiksIHtcbiAgICBpZDogYW55d2lkZ2V0SWQsXG4gICAgdHlwZTogXCJ0ZXh0L2Nzc1wiLFxuICB9KTtcbiAgc3R5bGUuYXBwZW5kQ2hpbGQoZG9jdW1lbnQuY3JlYXRlVGV4dE5vZGUoY3NzVGV4dCkpO1xuICBkb2N1bWVudC5oZWFkLmFwcGVuZENoaWxkKHN0eWxlKTtcbn1cblxuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIGxvYWRDc3MoY3NzOiBzdHJpbmcgfCB1bmRlZmluZWQsIGFueXdpZGdldElkOiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgaWYgKCFjc3MgfHwgIWFueXdpZGdldElkKSByZXR1cm47XG4gIGlmIChpc0hyZWYoY3NzKSkgcmV0dXJuIGxvYWRDc3NIcmVmKGNzcywgYW55d2lkZ2V0SWQpO1xuICByZXR1cm4gbG9hZENzc1RleHQoY3NzLCBhbnl3aWRnZXRJZCk7XG59XG5cbmFzeW5jIGZ1bmN0aW9uIGxvYWRFc20oZXNtOiBzdHJpbmcpOiBQcm9taXNlPEFueVdpZGdldE1vZHVsZT4ge1xuICBpZiAoaXNIcmVmKGVzbSkpIHtcbiAgICByZXR1cm4gYXdhaXQgaW1wb3J0KC8qIHdlYnBhY2tJZ25vcmU6IHRydWUgKi8gLyogQHZpdGUtaWdub3JlICovIGVzbSk7XG4gIH1cbiAgbGV0IHVybCA9IFVSTC5jcmVhdGVPYmplY3RVUkwobmV3IEJsb2IoW2VzbV0sIHsgdHlwZTogXCJ0ZXh0L2phdmFzY3JpcHRcIiB9KSk7XG4gIGxldCBtb2QgPSBhd2FpdCBpbXBvcnQoLyogd2VicGFja0lnbm9yZTogdHJ1ZSAqLyAvKiBAdml0ZS1pZ25vcmUgKi8gdXJsKTtcbiAgVVJMLnJldm9rZU9iamVjdFVSTCh1cmwpO1xuICByZXR1cm4gbW9kO1xufVxuXG5mdW5jdGlvbiB3YXJuUmVuZGVyRGVwcmVjYXRpb24oYW55d2lkZ2V0SWQ6IHN0cmluZyk6IHZvaWQge1xuICBjb25zb2xlLndhcm4oYFxcXG5bYW55d2lkZ2V0XSBEZXByZWNhdGlvbiBXYXJuaW5nIGZvciAke2FueXdpZGdldElkfTogRGlyZWN0IGV4cG9ydCBvZiBhICdyZW5kZXInIHdpbGwgbGlrZWx5IGJlIGRlcHJlY2F0ZWQgaW4gdGhlIGZ1dHVyZS4gVG8gbWlncmF0ZSAuLi5cblxuUmVtb3ZlIHRoZSAnZXhwb3J0JyBrZXl3b3JkIGZyb20gJ3JlbmRlcidcbi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbmV4cG9ydCBmdW5jdGlvbiByZW5kZXIoeyBtb2RlbCwgZWwgfSkgeyAuLi4gfVxuXl5eXl5eXG5cbkNyZWF0ZSBhIGRlZmF1bHQgZXhwb3J0IHRoYXQgcmV0dXJucyBhbiBvYmplY3Qgd2l0aCAncmVuZGVyJ1xuLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbmZ1bmN0aW9uIHJlbmRlcih7IG1vZGVsLCBlbCB9KSB7IC4uLiB9XG4gICAgICAgICBeXl5eXl5cbmV4cG9ydCBkZWZhdWx0IHsgcmVuZGVyIH1cbiAgICAgICAgICAgICAgICAgXl5eXl5eXG5cblBpbiB0byBhbnl3aWRnZXQ+PTAuOS4wIGluIHlvdXIgcHlwcm9qZWN0LnRvbWxcbi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblxuZGVwZW5kZW5jaWVzID0gW1wiYW55d2lkZ2V0Pj0wLjkuMFwiXVxuXG5UbyBsZWFybiBtb3JlLCBwbGVhc2Ugc2VlOiBodHRwczovL2dpdGh1Yi5jb20vbWFuenQvYW55d2lkZ2V0L3B1bGwvMzk1LlxuYCk7XG59XG5cbmV4cG9ydCBhc3luYyBmdW5jdGlvbiBsb2FkV2lkZ2V0KGVzbTogc3RyaW5nLCBhbnl3aWRnZXRJZDogc3RyaW5nKTogUHJvbWlzZTxBbnlXaWRnZXQ+IHtcbiAgbGV0IG1vZCA9IGF3YWl0IGxvYWRFc20oZXNtKTtcbiAgaWYgKG1vZC5yZW5kZXIpIHtcbiAgICB3YXJuUmVuZGVyRGVwcmVjYXRpb24oYW55d2lkZ2V0SWQpO1xuICAgIHJldHVybiB7XG4gICAgICBhc3luYyBpbml0aWFsaXplKCkge30sXG4gICAgICByZW5kZXI6IG1vZC5yZW5kZXIsXG4gICAgfTtcbiAgfVxuICBhc3NlcnQobW9kLmRlZmF1bHQsIGBbYW55d2lkZ2V0XSBtb2R1bGUgbXVzdCBleHBvcnQgYSBkZWZhdWx0IGZ1bmN0aW9uIG9yIG9iamVjdC5gKTtcbiAgbGV0IHdpZGdldCA9IHR5cGVvZiBtb2QuZGVmYXVsdCA9PT0gXCJmdW5jdGlvblwiID8gYXdhaXQgbW9kLmRlZmF1bHQoKSA6IG1vZC5kZWZhdWx0O1xuICByZXR1cm4gd2lkZ2V0O1xufVxuIiwiaW1wb3J0IHR5cGUgeyBBbnlNb2RlbCB9IGZyb20gXCJAYW55d2lkZ2V0L3R5cGVzXCI7XG5pbXBvcnQgKiBhcyBzb2xpZCBmcm9tIFwic29saWQtanNcIjtcblxuZXhwb3J0IGZ1bmN0aW9uIG9ic2VydmU8VCBleHRlbmRzIFJlY29yZDxzdHJpbmcsIHVua25vd24+LCBLIGV4dGVuZHMga2V5b2YgVCAmIHN0cmluZz4oXG4gIG1vZGVsOiBBbnlNb2RlbDxUPixcbiAgbmFtZTogSyxcbiAgeyBzaWduYWwgfTogeyBzaWduYWw/OiBBYm9ydFNpZ25hbCB9LFxuKTogc29saWQuQWNjZXNzb3I8VFtLXT4ge1xuICBsZXQgW2dldCwgc2V0XSA9IHNvbGlkLmNyZWF0ZVNpZ25hbChtb2RlbC5nZXQobmFtZSkpO1xuICBsZXQgdXBkYXRlID0gKCkgPT4gc2V0KCgpID0+IG1vZGVsLmdldChuYW1lKSk7XG4gIG1vZGVsLm9uKGBjaGFuZ2U6JHtuYW1lfWAsIHVwZGF0ZSk7XG4gIHNpZ25hbD8uYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IHtcbiAgICBtb2RlbC5vZmYoYGNoYW5nZToke25hbWV9YCwgdXBkYXRlKTtcbiAgfSk7XG4gIHJldHVybiBnZXQ7XG59XG4iLCJpbXBvcnQgdHlwZSB7IEFueU1vZGVsLCBFeHBlcmltZW50YWwgfSBmcm9tIFwiQGFueXdpZGdldC90eXBlc1wiO1xuaW1wb3J0IHR5cGUgeyBET01XaWRnZXRNb2RlbCwgRE9NV2lkZ2V0VmlldyB9IGZyb20gXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIjtcbmltcG9ydCAqIGFzIHNvbGlkIGZyb20gXCJzb2xpZC1qc1wiO1xuXG5pbXBvcnQgeyBCSU5ESU5HUyB9IGZyb20gXCIuL2JpbmRpbmcudHNcIjtcbmltcG9ydCB7IGNyZWF0ZUhvc3QgfSBmcm9tIFwiLi9ob3N0LnRzXCI7XG5pbXBvcnQgeyBpbnZva2UgfSBmcm9tIFwiLi9pbnZva2UudHNcIjtcbmltcG9ydCB7IHR5cGUgQW55V2lkZ2V0LCBsb2FkQ3NzLCBsb2FkV2lkZ2V0IH0gZnJvbSBcIi4vbG9hZC50c1wiO1xuaW1wb3J0IHsgb2JzZXJ2ZSB9IGZyb20gXCIuL29ic2VydmUudHNcIjtcbmltcG9ydCB7IGFzc2VydCwgcHJvbWlzZVdpdGhSZXNvbHZlcnMsIHR5cGUgUmVzdWx0LCB0aHJvd0FueXdpZGdldEVycm9yIH0gZnJvbSBcIi4vdXRpbC50c1wiO1xuXG5pbnRlcmZhY2UgU3RhdGUge1xuICBba2V5OiBzdHJpbmddOiB1bmtub3duO1xuICBfZXNtOiBzdHJpbmc7XG4gIF9hbnl3aWRnZXRfaWQ6IHN0cmluZztcbiAgX2Nzczogc3RyaW5nIHwgdW5kZWZpbmVkO1xufVxuXG5leHBvcnQgY2xhc3MgUnVudGltZSB7XG4gIC8vIEB0cy1leHBlY3QtZXJyb3IgLSBTZXQgc3luY2hyb25vdXNseSBpbiBjb25zdHJ1Y3Rvci5cbiAgI3dpZGdldFJlc3VsdDogc29saWQuQWNjZXNzb3I8UmVzdWx0PEFueVdpZGdldD4+O1xuICAjc2lnbmFsOiBBYm9ydFNpZ25hbDtcbiAgcmVhZHk6IFByb21pc2U8dm9pZD47XG5cbiAgY29uc3RydWN0b3IobW9kZWw6IERPTVdpZGdldE1vZGVsLCBvcHRpb25zOiB7IHNpZ25hbDogQWJvcnRTaWduYWwgfSkge1xuICAgIGxldCByZXNvbHZlcnMgPSBwcm9taXNlV2l0aFJlc29sdmVyczx2b2lkPigpO1xuICAgIHRoaXMucmVhZHkgPSByZXNvbHZlcnMucHJvbWlzZTtcbiAgICB0aGlzLiNzaWduYWwgPSBvcHRpb25zLnNpZ25hbDtcbiAgICB0aGlzLiNzaWduYWwudGhyb3dJZkFib3J0ZWQoKTtcbiAgICB0aGlzLiNzaWduYWwuYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IGRpc3Bvc2UoKSk7XG4gICAgQWJvcnRTaWduYWwudGltZW91dCgyMDAwKS5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4ge1xuICAgICAgcmVzb2x2ZXJzLnJlamVjdChuZXcgRXJyb3IoXCJbYW55d2lkZ2V0XSBGYWlsZWQgdG8gaW5pdGlhbGl6ZSBtb2RlbC5cIikpO1xuICAgIH0pO1xuICAgIGxldCBiaW5kaW5nID0gQklORElOR1MuZ2V0T3JDcmVhdGUobW9kZWwpO1xuICAgIGxldCBleHBlcmltZW50YWw6IEV4cGVyaW1lbnRhbCA9IHtcbiAgICAgIC8vIEB0cy1leHBlY3QtZXJyb3IgLSBpbnZva2UuYmluZCBsb3NlcyBnZW5lcmljIHR5cGUgcGFyYW1ldGVyXG4gICAgICBpbnZva2U6IGludm9rZS5iaW5kKG51bGwsIG1vZGVsKSxcbiAgICB9O1xuICAgIGxldCBkaXNwb3NlID0gc29saWQuY3JlYXRlUm9vdCgoZGlzcG9zZSkgPT4ge1xuICAgICAgLy8gRE9NV2lkZ2V0TW9kZWwgaXMgdW50eXBlZCBieSB0cmFpdCBzaGFwZTsgd2Uga25vdyB0aGUgYW55d2lkZ2V0IHRyYWl0cywgc28gbmFycm93IHRvIEFueU1vZGVsPFN0YXRlPiBmb3IgdHlwZS1zYWZlIGAuZ2V0KClgIGFjY2Vzc1xuICAgICAgLy8gb3hsaW50LWRpc2FibGUtbmV4dC1saW5lIHR5cGVzY3JpcHQtZXNsaW50L25vLXVuc2FmZS10eXBlLWFzc2VydGlvbiAtLSBzZWUgYWJvdmVcbiAgICAgIGxldCB0eXBlZE1vZGVsID0gbW9kZWwgYXMgdW5rbm93biBhcyBBbnlNb2RlbDxTdGF0ZT47XG4gICAgICBsZXQgaWQgPSB0eXBlZE1vZGVsLmdldChcIl9hbnl3aWRnZXRfaWRcIik7XG4gICAgICBsZXQgY3NzID0gb2JzZXJ2ZSh0eXBlZE1vZGVsLCBcIl9jc3NcIiwgeyBzaWduYWw6IHRoaXMuI3NpZ25hbCB9KTtcbiAgICAgIGxldCBlc20gPSBvYnNlcnZlKHR5cGVkTW9kZWwsIFwiX2VzbVwiLCB7IHNpZ25hbDogdGhpcy4jc2lnbmFsIH0pO1xuICAgICAgbGV0IFt3aWRnZXRSZXN1bHQsIHNldFdpZGdldFJlc3VsdF0gPSBzb2xpZC5jcmVhdGVTaWduYWw8UmVzdWx0PEFueVdpZGdldD4+KHtcbiAgICAgICAgc3RhdHVzOiBcInBlbmRpbmdcIixcbiAgICAgIH0pO1xuICAgICAgdGhpcy4jd2lkZ2V0UmVzdWx0ID0gd2lkZ2V0UmVzdWx0O1xuXG4gICAgICBzb2xpZC5jcmVhdGVFZmZlY3QoXG4gICAgICAgIHNvbGlkLm9uKGNzcywgKCkgPT4gY29uc29sZS5kZWJ1ZyhgW2FueXdpZGdldF0gY3NzIGhvdCB1cGRhdGVkOiAke2lkfWApLCB7IGRlZmVyOiB0cnVlIH0pLFxuICAgICAgKTtcbiAgICAgIHNvbGlkLmNyZWF0ZUVmZmVjdChcbiAgICAgICAgc29saWQub24oZXNtLCAoKSA9PiBjb25zb2xlLmRlYnVnKGBbYW55d2lkZ2V0XSBlc20gaG90IHVwZGF0ZWQ6ICR7aWR9YCksIHsgZGVmZXI6IHRydWUgfSksXG4gICAgICApO1xuICAgICAgc29saWQuY3JlYXRlRWZmZWN0KCgpID0+IHtcbiAgICAgICAgcmV0dXJuIGxvYWRDc3MoY3NzKCksIGlkKTtcbiAgICAgIH0pO1xuICAgICAgc29saWQuY3JlYXRlRWZmZWN0KCgpID0+IHtcbiAgICAgICAgLy8gUGVyLWVmZmVjdCBjb250cm9sbGVyIHNvIGEgc3RhbGUgbG9hZFdpZGdldCByZXNvbHV0aW9uIGZyb20gYVxuICAgICAgICAvLyBwcmV2aW91cyBfZXNtIHZhbHVlIGNhbm5vdCBvdmVyd3JpdGUgYSBuZXdlciBvbmUuIFNvbGlkIGZpcmVzXG4gICAgICAgIC8vIG9uQ2xlYW51cCBiZWZvcmUgcmUtcnVubmluZyB0aGUgZWZmZWN0LCBhYm9ydGluZyB0aGUgcHJpb3IgbG9hZC5cbiAgICAgICAgbGV0IGNvbnRyb2xsZXIgPSBuZXcgQWJvcnRDb250cm9sbGVyKCk7XG4gICAgICAgIHNvbGlkLm9uQ2xlYW51cCgoKSA9PiBjb250cm9sbGVyLmFib3J0KCkpO1xuICAgICAgICBsb2FkV2lkZ2V0KGVzbSgpLCBpZClcbiAgICAgICAgICAudGhlbihhc3luYyAod2lkZ2V0KSA9PiB7XG4gICAgICAgICAgICBpZiAoY29udHJvbGxlci5zaWduYWwuYWJvcnRlZCkgcmV0dXJuO1xuICAgICAgICAgICAgYXdhaXQgYmluZGluZy5iaW5kKHdpZGdldCwgeyBleHBlcmltZW50YWwgfSk7XG4gICAgICAgICAgICBpZiAoY29udHJvbGxlci5zaWduYWwuYWJvcnRlZCkgcmV0dXJuO1xuICAgICAgICAgICAgc2V0V2lkZ2V0UmVzdWx0KHsgc3RhdHVzOiBcInJlYWR5XCIsIGRhdGE6IHdpZGdldCB9KTtcbiAgICAgICAgICAgIHJlc29sdmVycy5yZXNvbHZlKCk7XG4gICAgICAgICAgfSlcbiAgICAgICAgICAuY2F0Y2goKGVycm9yKSA9PiB7XG4gICAgICAgICAgICBpZiAoY29udHJvbGxlci5zaWduYWwuYWJvcnRlZCkgcmV0dXJuO1xuICAgICAgICAgICAgc2V0V2lkZ2V0UmVzdWx0KHsgc3RhdHVzOiBcImVycm9yXCIsIGVycm9yIH0pO1xuICAgICAgICAgIH0pO1xuICAgICAgfSk7XG5cbiAgICAgIHJldHVybiBkaXNwb3NlO1xuICAgIH0pO1xuICB9XG5cbiAgYXN5bmMgY3JlYXRlVmlldyh2aWV3OiBET01XaWRnZXRWaWV3LCBvcHRpb25zOiB7IHNpZ25hbDogQWJvcnRTaWduYWwgfSk6IFByb21pc2U8dm9pZD4ge1xuICAgIGxldCBtb2RlbCA9IHZpZXcubW9kZWw7XG4gICAgbGV0IHNpZ25hbCA9IEFib3J0U2lnbmFsLmFueShbdGhpcy4jc2lnbmFsLCBvcHRpb25zLnNpZ25hbF0pOyAvLyBlaXRoZXIgbW9kZWwgb3IgdmlldyBkZXN0cm95ZWRcbiAgICBzaWduYWwudGhyb3dJZkFib3J0ZWQoKTtcbiAgICBzaWduYWwuYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IGRpc3Bvc2UoKSk7XG4gICAgbGV0IGJpbmRpbmcgPSBCSU5ESU5HUy5nZXQobW9kZWwpO1xuICAgIGFzc2VydChiaW5kaW5nLCBcIlthbnl3aWRnZXRdIFdpZGdldEJpbmRpbmcgbm90IGZvdW5kLlwiKTtcbiAgICBsZXQgZXhwZXJpbWVudGFsOiBFeHBlcmltZW50YWwgPSB7XG4gICAgICAvLyBAdHMtZXhwZWN0LWVycm9yIC0gaW52b2tlLmJpbmQgbG9zZXMgZ2VuZXJpYyB0eXBlIHBhcmFtZXRlclxuICAgICAgaW52b2tlOiBpbnZva2UuYmluZChudWxsLCBtb2RlbCksXG4gICAgfTtcbiAgICBsZXQgaG9zdCA9IGNyZWF0ZUhvc3QobW9kZWwsIHsgc2lnbmFsIH0pO1xuICAgIGxldCBkaXNwb3NlID0gc29saWQuY3JlYXRlUm9vdCgoZGlzcG9zZSkgPT4ge1xuICAgICAgc29saWQuY3JlYXRlRWZmZWN0KCgpID0+IHtcbiAgICAgICAgLy8gQ2xlYXIgYWxsIHByZXZpb3VzIGV2ZW50IGxpc3RlbmVycyBmcm9tIHRoaXMgaG9vay5cbiAgICAgICAgbW9kZWwub2ZmKG51bGwsIG51bGwsIHZpZXcpO1xuICAgICAgICB2aWV3LiRlbC5lbXB0eSgpO1xuICAgICAgICBsZXQgcmVzdWx0ID0gdGhpcy4jd2lkZ2V0UmVzdWx0KCk7XG4gICAgICAgIGlmIChyZXN1bHQuc3RhdHVzID09PSBcInBlbmRpbmdcIikge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBpZiAocmVzdWx0LnN0YXR1cyA9PT0gXCJlcnJvclwiKSB7XG4gICAgICAgICAgdGhyb3dBbnl3aWRnZXRFcnJvcihyZXN1bHQuZXJyb3IpO1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBsZXQgY29udHJvbGxlciA9IG5ldyBBYm9ydENvbnRyb2xsZXIoKTtcbiAgICAgICAgc29saWQub25DbGVhbnVwKCgpID0+IGNvbnRyb2xsZXIuYWJvcnQoKSk7XG4gICAgICAgIFByb21pc2UucmVzb2x2ZSgpXG4gICAgICAgICAgLnRoZW4oKCkgPT5cbiAgICAgICAgICAgIGJpbmRpbmcuY3JlYXRlVmlldyh2aWV3LCB7XG4gICAgICAgICAgICAgIHNpZ25hbDogQWJvcnRTaWduYWwuYW55KFtzaWduYWwsIGNvbnRyb2xsZXIuc2lnbmFsXSksXG4gICAgICAgICAgICAgIGV4cGVyaW1lbnRhbCxcbiAgICAgICAgICAgICAgaG9zdCxcbiAgICAgICAgICAgIH0pLFxuICAgICAgICAgIClcbiAgICAgICAgICAuY2F0Y2goKGVycm9yKSA9PiB0aHJvd0FueXdpZGdldEVycm9yKGVycm9yKSk7XG4gICAgICB9KTtcbiAgICAgIHJldHVybiAoKSA9PiBkaXNwb3NlKCk7XG4gICAgfSk7XG4gIH1cbn1cbiIsImltcG9ydCB7IEJJTkRJTkdTIH0gZnJvbSBcIi4vYmluZGluZy50c1wiO1xuaW1wb3J0IHsgUnVudGltZSB9IGZyb20gXCIuL3J1bnRpbWUudHNcIjtcbmltcG9ydCB7IGFzc2VydCB9IGZyb20gXCIuL3V0aWwudHNcIjtcblxuLy8gQHRzLWV4cGVjdC1lcnJvciAtIGluamVjdGVkIGJ5IGJ1bmRsZXJcbmxldCB2ZXJzaW9uOiBzdHJpbmcgPSBnbG9iYWxUaGlzLlZFUlNJT047XG5cbmludGVyZmFjZSBXaWRnZXRGYWN0b3J5T3B0aW9ucyB7XG4gIERPTVdpZGdldE1vZGVsOiB0eXBlb2YgaW1wb3J0KFwiQGp1cHl0ZXItd2lkZ2V0cy9iYXNlXCIpLkRPTVdpZGdldE1vZGVsO1xuICBET01XaWRnZXRWaWV3OiB0eXBlb2YgaW1wb3J0KFwiQGp1cHl0ZXItd2lkZ2V0cy9iYXNlXCIpLkRPTVdpZGdldFZpZXc7XG59XG5cbmludGVyZmFjZSBXaWRnZXRGYWN0b3J5UmVzdWx0IHtcbiAgQW55TW9kZWw6IHR5cGVvZiBpbXBvcnQoXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIikuRE9NV2lkZ2V0TW9kZWw7XG4gIEFueVZpZXc6IHR5cGVvZiBpbXBvcnQoXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIikuRE9NV2lkZ2V0Vmlldztcbn1cblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gKHtcbiAgRE9NV2lkZ2V0TW9kZWwsXG4gIERPTVdpZGdldFZpZXcsXG59OiBXaWRnZXRGYWN0b3J5T3B0aW9ucyk6IFdpZGdldEZhY3RvcnlSZXN1bHQge1xuICBsZXQgUlVOVElNRVMgPSBuZXcgV2Vha01hcDxJbnN0YW5jZVR5cGU8dHlwZW9mIERPTVdpZGdldE1vZGVsPiwgUnVudGltZT4oKTtcblxuICBjbGFzcyBBbnlNb2RlbCBleHRlbmRzIERPTVdpZGdldE1vZGVsIHtcbiAgICBzdGF0aWMgbW9kZWxfbmFtZSA9IFwiQW55TW9kZWxcIjtcbiAgICBzdGF0aWMgbW9kZWxfbW9kdWxlID0gXCJhbnl3aWRnZXRcIjtcbiAgICBzdGF0aWMgbW9kZWxfbW9kdWxlX3ZlcnNpb24gPSB2ZXJzaW9uO1xuXG4gICAgc3RhdGljIHZpZXdfbmFtZSA9IFwiQW55Vmlld1wiO1xuICAgIHN0YXRpYyB2aWV3X21vZHVsZSA9IFwiYW55d2lkZ2V0XCI7XG4gICAgc3RhdGljIHZpZXdfbW9kdWxlX3ZlcnNpb24gPSB2ZXJzaW9uO1xuXG4gICAgaW5pdGlhbGl6ZSguLi5hcmdzOiBQYXJhbWV0ZXJzPEluc3RhbmNlVHlwZTx0eXBlb2YgRE9NV2lkZ2V0TW9kZWw+W1wiaW5pdGlhbGl6ZVwiXT4pOiB2b2lkIHtcbiAgICAgIHN1cGVyLmluaXRpYWxpemUoLi4uYXJncyk7XG4gICAgICBsZXQgY29udHJvbGxlciA9IG5ldyBBYm9ydENvbnRyb2xsZXIoKTtcbiAgICAgIHRoaXMub25jZShcImRlc3Ryb3lcIiwgKCkgPT4ge1xuICAgICAgICBjb250cm9sbGVyLmFib3J0KFwiW2FueXdpZGdldF0gUnVudGltZSBkZXN0cm95ZWQuXCIpO1xuICAgICAgICBCSU5ESU5HUy5kZXN0cm95KHRoaXMpO1xuICAgICAgICBSVU5USU1FUy5kZWxldGUodGhpcyk7XG4gICAgICB9KTtcbiAgICAgIFJVTlRJTUVTLnNldCh0aGlzLCBuZXcgUnVudGltZSh0aGlzLCB7IHNpZ25hbDogY29udHJvbGxlci5zaWduYWwgfSkpO1xuICAgIH1cblxuICAgIGFzeW5jIF9oYW5kbGVfY29tbV9tc2coXG4gICAgICAuLi5tc2c6IFBhcmFtZXRlcnM8SW5zdGFuY2VUeXBlPHR5cGVvZiBET01XaWRnZXRNb2RlbD5bXCJfaGFuZGxlX2NvbW1fbXNnXCJdPlxuICAgICk6IFByb21pc2U8dm9pZD4ge1xuICAgICAgbGV0IHJ1bnRpbWUgPSBSVU5USU1FUy5nZXQodGhpcyk7XG4gICAgICBhd2FpdCBydW50aW1lPy5yZWFkeTtcbiAgICAgIHJldHVybiBzdXBlci5faGFuZGxlX2NvbW1fbXNnKC4uLm1zZyk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogV2Ugb3ZlcnJpZGUgdG8gc3VwcG9ydCBiaW5hcnkgdHJhaWxldHMgYmVjYXVzZSBKU09OLnBhcnNlKEpTT04uc3RyaW5naWZ5KCkpXG4gICAgICogZG9lcyBub3QgcHJvcGVybHkgY2xvbmUgYmluYXJ5IGRhdGEgKGl0IGp1c3QgcmV0dXJucyBhbiBlbXB0eSBvYmplY3QpLlxuICAgICAqXG4gICAgICogaHR0cHM6Ly9naXRodWIuY29tL2p1cHl0ZXItd2lkZ2V0cy9pcHl3aWRnZXRzL2Jsb2IvNDcwNThhMzczZDJjMmIzYWNmMTAxNjc3YjI3NDVlMTRiNzZkZDc0Yi9wYWNrYWdlcy9iYXNlL3NyYy93aWRnZXQudHMjTDU2Mi1MNTgzXG4gICAgICovXG4gICAgc2VyaWFsaXplKHN0YXRlOiBSZWNvcmQ8c3RyaW5nLCBhbnk+KTogUmVjb3JkPHN0cmluZywgYW55PiB7XG4gICAgICAvLyBveGxpbnQtZGlzYWJsZS1uZXh0LWxpbmUgdHlwZXNjcmlwdC1lc2xpbnQvbm8tdW5zYWZlLXR5cGUtYXNzZXJ0aW9uIC0tIGFjY2Vzc2luZyBzdGF0aWMgYC5zZXJpYWxpemVyc2Agb24gYHRoaXMuY29uc3RydWN0b3JgXG4gICAgICBsZXQgc2VyaWFsaXplcnMgPSAodGhpcy5jb25zdHJ1Y3RvciBhcyB0eXBlb2YgRE9NV2lkZ2V0TW9kZWwpLnNlcmlhbGl6ZXJzIHx8IHt9O1xuICAgICAgZm9yIChsZXQgayBvZiBPYmplY3Qua2V5cyhzdGF0ZSkpIHtcbiAgICAgICAgdHJ5IHtcbiAgICAgICAgICBsZXQgc2VyaWFsaXplID0gc2VyaWFsaXplcnNba10/LnNlcmlhbGl6ZTtcbiAgICAgICAgICBpZiAoc2VyaWFsaXplKSB7XG4gICAgICAgICAgICBzdGF0ZVtrXSA9IHNlcmlhbGl6ZShzdGF0ZVtrXSwgdGhpcyk7XG4gICAgICAgICAgfSBlbHNlIGlmIChrID09PSBcImxheW91dFwiIHx8IGsgPT09IFwic3R5bGVcIikge1xuICAgICAgICAgICAgLy8gVGhlc2Uga2V5cyBjb21lIGZyb20gaXB5d2lkZ2V0cywgcmVseSBvbiBKU09OLnN0cmluZ2lmeSB0cmljay5cbiAgICAgICAgICAgIHN0YXRlW2tdID0gSlNPTi5wYXJzZShKU09OLnN0cmluZ2lmeShzdGF0ZVtrXSkpO1xuICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICBzdGF0ZVtrXSA9IHN0cnVjdHVyZWRDbG9uZShzdGF0ZVtrXSk7XG4gICAgICAgICAgfVxuICAgICAgICAgIGlmICh0eXBlb2Ygc3RhdGVba10/LnRvSlNPTiA9PT0gXCJmdW5jdGlvblwiKSB7XG4gICAgICAgICAgICBzdGF0ZVtrXSA9IHN0YXRlW2tdLnRvSlNPTigpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSBjYXRjaCAoZSkge1xuICAgICAgICAgIGNvbnNvbGUuZXJyb3IoXCJFcnJvciBzZXJpYWxpemluZyB3aWRnZXQgc3RhdGUgYXR0cmlidXRlOiBcIiwgayk7XG4gICAgICAgICAgdGhyb3cgZTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICAgcmV0dXJuIHN0YXRlO1xuICAgIH1cbiAgfVxuXG4gIGNsYXNzIEFueVZpZXcgZXh0ZW5kcyBET01XaWRnZXRWaWV3IHtcbiAgICAjY29udHJvbGxlciA9IG5ldyBBYm9ydENvbnRyb2xsZXIoKTtcbiAgICBhc3luYyByZW5kZXIoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICBsZXQgcnVudGltZSA9IFJVTlRJTUVTLmdldCh0aGlzLm1vZGVsKTtcbiAgICAgIGFzc2VydChydW50aW1lLCBcIlthbnl3aWRnZXRdIFJ1bnRpbWUgbm90IGZvdW5kLlwiKTtcbiAgICAgIGF3YWl0IHJ1bnRpbWUuY3JlYXRlVmlldyh0aGlzLCB7IHNpZ25hbDogdGhpcy4jY29udHJvbGxlci5zaWduYWwgfSk7XG4gICAgfVxuICAgIHJlbW92ZSgpOiB2b2lkIHtcbiAgICAgIHRoaXMuI2NvbnRyb2xsZXIuYWJvcnQoXCJbYW55d2lkZ2V0XSBWaWV3IGRlc3Ryb3llZC5cIik7XG4gICAgICBzdXBlci5yZW1vdmUoKTtcbiAgICB9XG4gIH1cblxuICByZXR1cm4geyBBbnlNb2RlbCwgQW55VmlldyB9O1xufVxuIiwiaW1wb3J0ICogYXMgYmFzZSBmcm9tIFwiQGp1cHl0ZXItd2lkZ2V0cy9iYXNlXCI7XG5cbmltcG9ydCBjcmVhdGUgZnJvbSBcIi4vd2lkZ2V0LnRzXCI7XG5cbi8qKlxuICogQHR5cGVkZWYgSnVweXRlckxhYlJlZ2lzdHJ5XG4gKiBAcHJvcGVydHkgeyh3aWRnZXQ6IHsgbmFtZTogc3RyaW5nLCB2ZXJzaW9uOiBzdHJpbmcsIGV4cG9ydHM6IGFueSB9KSA9PiB2b2lkfSByZWdpc3RlcldpZGdldFxuICovXG5cbmV4cG9ydCBkZWZhdWx0IHtcbiAgaWQ6IFwiYW55d2lkZ2V0OnBsdWdpblwiLFxuICByZXF1aXJlczogWy8qKiBAdHlwZXt1bmtub3dufSAqLyAoYmFzZS5JSnVweXRlcldpZGdldFJlZ2lzdHJ5KV0sXG4gIGFjdGl2YXRlOiAoLyoqIEB0eXBlIHt1bmtub3dufSAqLyBfYXBwLCAvKiogQHR5cGUge0p1cHl0ZXJMYWJSZWdpc3RyeX0gKi8gcmVnaXN0cnkpID0+IHtcbiAgICBsZXQgZXhwb3J0cyA9IGNyZWF0ZShiYXNlKTtcbiAgICByZWdpc3RyeS5yZWdpc3RlcldpZGdldCh7XG4gICAgICBuYW1lOiBcImFueXdpZGdldFwiLFxuICAgICAgLy8gQHRzLWV4cGVjdC1lcnJvciBBZGRlZCBieSBidW5kbGVyXG4gICAgICB2ZXJzaW9uOiBnbG9iYWxUaGlzLlZFUlNJT04sXG4gICAgICBleHBvcnRzLFxuICAgIH0pO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWUsXG59O1xuIl0sIm5hbWVzIjpbIklOSVRJQUxJWkVfTUFSS0VSIiwiU3ltYm9sIiwibW9kZWxQcm94eSIsIm1vZGVsIiwiY29udGV4dCIsIm9uIiwibmFtZSIsImNhbGxiYWNrIiwib2ZmIiwiYXNzZXJ0IiwiY29uZGl0aW9uIiwibWVzc2FnZSIsIkVycm9yIiwic2FmZUNsZWFudXAiLCJmbiIsImtpbmQiLCJQcm9taXNlIiwiZSIsImNvbnNvbGUiLCJ0aHJvd0FueXdpZGdldEVycm9yIiwic291cmNlIiwiX3NvdXJjZV9zdGFjayIsIl9pbnN0YW5jZW9mIiwibGluZXMiLCJhbnl3aWRnZXRJbmRleCIsImxpbmUiLCJjbGVhblN0YWNrIiwicHJvbWlzZVdpdGhSZXNvbHZlcnMiLCJyZXNvbHZlIiwicmVqZWN0IiwicHJvbWlzZSIsInJlcyIsInJlaiIsImlzU2FmZUNsZWFudXBGdW5jdGlvbiIsIngiLCJfY29udHJvbGxlciIsIl93aWRnZXREZWYiLCJfZXhwb3J0cyIsIl9tb2RlbCIsIl9yZXNvbHZlcnMiLCJXaWRnZXRCaW5kaW5nIiwiYmluZCIsIndpZGdldERlZiIsInBhcmFtIiwiZXhwZXJpbWVudGFsIiwicHJldlJlc29sdmVycyIsInNpZ25hbCIsInJlc3VsdCIsIkFib3J0Q29udHJvbGxlciIsInVuZGVmaW5lZCIsIl90eXBlX29mIiwiY3JlYXRlVmlldyIsInRhcmdldCIsImhvc3QiLCJjb250cm9sbGVyIiwiY29tYmluZWQiLCJjbGVhbnVwIiwiZGlzcG9zZVZpZXciLCJBYm9ydFNpZ25hbCIsInJlYXNvbiIsImRlc3Ryb3kiLCJfYmluZGluZ3MiLCJCaW5kaW5nTWFuYWdlciIsIk1hcCIsImdldE9yQ3JlYXRlIiwiYmluZGluZyIsImdldCIsIkJJTkRJTkdTIiwidXVpZCIsImludm9rZSIsIm1zZyIsIm9wdGlvbnMiLCJfb3B0aW9uc19zaWduYWwiLCJpZCIsIl9vcHRpb25zX2J1ZmZlcnMiLCJoYW5kbGVyIiwiYnVmZmVycyIsIldJREdFVF9SRUZfUFJFRklYIiwicGFyc2VXaWRnZXRSZWYiLCJyZWYiLCJKU09OIiwiY3JlYXRlSG9zdCIsImdldE1vZGVsIiwibW9kZWxJZCIsImNoaWxkTW9kZWwiLCJnZXRXaWRnZXQiLCJjaGlsZEJpbmRpbmciLCJ0aW1lciIsImV4cG9ydHMiLCJzZXRUaW1lb3V0IiwiY2xlYXJUaW1lb3V0IiwicmVuZGVyIiwiZWwiLCJ2aWV3U2lnbmFsIiwiY2hpbGRWaWV3U2lnbmFsIiwiaXNIcmVmIiwic3RyIiwibG9hZENzc0hyZWYiLCJocmVmIiwiYW55d2lkZ2V0SWQiLCJwcmV2IiwibmV3TGluayIsImRvY3VtZW50IiwibGluayIsIk9iamVjdCIsImxvYWRDc3NUZXh0IiwiY3NzVGV4dCIsInN0eWxlIiwibG9hZENzcyIsImNzcyIsImxvYWRFc20iLCJlc20iLCJ1cmwiLCJtb2QiLCJVUkwiLCJCbG9iIiwid2FyblJlbmRlckRlcHJlY2F0aW9uIiwibG9hZFdpZGdldCIsIndpZGdldCIsImluaXRpYWxpemUiLCJzb2xpZCIsIm9ic2VydmUiLCJfc29saWRfY3JlYXRlU2lnbmFsIiwic2V0IiwidXBkYXRlIiwiX3dpZGdldFJlc3VsdCIsIl9zaWduYWwiLCJSdW50aW1lIiwicmVzb2x2ZXJzIiwiZGlzcG9zZSIsInR5cGVkTW9kZWwiLCJ3aWRnZXRSZXN1bHQiLCJzZXRXaWRnZXRSZXN1bHQiLCJlcnJvciIsInZpZXciLCJ2ZXJzaW9uIiwiZ2xvYmFsVGhpcyIsIkRPTVdpZGdldE1vZGVsIiwiRE9NV2lkZ2V0VmlldyIsIlJVTlRJTUVTIiwiV2Vha01hcCIsIkFueU1vZGVsIiwiX2tleSIsImFyZ3MiLCJfJF9nZXQiLCJfaGFuZGxlX2NvbW1fbXNnIiwiX3N1cGVycHJvcF9nZXRfX2hhbmRsZV9jb21tX21zZzEiLCJydW50aW1lIiwic2VyaWFsaXplIiwic3RhdGUiLCJzZXJpYWxpemVycyIsIl9pdGVyYXRvckVycm9yIiwiayIsIl9zZXJpYWxpemVyc19rIiwiX3N0YXRlX2siLCJzdHJ1Y3R1cmVkQ2xvbmUiLCJBbnlWaWV3IiwicmVtb3ZlIl0sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7OztBQUdBOzs7Q0FHQyxHQUNNLElBQUlBLG9CQUFvQkMsT0FBTyx3QkFBd0I7QUFFOUQ7Ozs7OztDQU1DLEdBQ00sU0FBU0MsV0FBV0MsS0FBcUIsRUFBRUMsT0FBZ0I7SUFDaEUseU5BQXlOO0lBQ3pOLE9BQU87UUFDTCxLQUFLRCxNQUFNLEdBQUcsQ0FBQyxJQUFJLENBQUNBO1FBQ3BCLEtBQUtBLE1BQU0sR0FBRyxDQUFDLElBQUksQ0FBQ0E7UUFDcEIsY0FBY0EsTUFBTSxZQUFZLENBQUMsSUFBSSxDQUFDQTtRQUN0QyxNQUFNQSxNQUFNLElBQUksQ0FBQyxJQUFJLENBQUNBO1FBQ3RCRSxJQUFBQSxTQUFBQSxHQUFHQyxJQUFJLEVBQUVDLFFBQVE7WUFDZkosTUFBTSxFQUFFLENBQUNHLE1BQU1DLFVBQVVIO1FBQzNCO1FBQ0FJLEtBQUFBLFNBQUFBLElBQUlGLElBQUksRUFBRUMsUUFBUTtZQUNoQkosTUFBTSxHQUFHLENBQUNHLE1BQU1DLFVBQVVIO1FBQzVCO1FBQ0Esa0VBQWtFO1FBQ2xFLHlFQUF5RTtRQUN6RSwwQ0FBMEM7UUFDMUMsZ0JBQWdCRCxNQUFNLGNBQWM7SUFDdEM7QUFDRjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7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