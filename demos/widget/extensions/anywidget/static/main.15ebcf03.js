(() => {
"use strict";
var __webpack_modules__ = ({
464() {

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
 */ function model_proxy_modelProxy(model, context) {
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
function util_assert(condition, message) {
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
 */ function util_throwAnywidgetError(source) {
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
 */ function util_promiseWithResolvers() {
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
        _class_private_field_set(this, _resolvers, util_promiseWithResolvers());
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
                                    _class_private_field_set(this, _resolvers, util_promiseWithResolvers());
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
                                        model: model_proxy_modelProxy(model, INITIALIZE_MARKER),
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
                                        model: model_proxy_modelProxy(model, target),
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
var binding_BINDINGS = new binding_BindingManager();

;// CONCATENATED MODULE: ./node_modules/.pnpm/@lukeed+uuid@2.0.1/node_modules/@lukeed/uuid/dist/index.mjs
var IDX=256, HEX=[], BUFFER;
while (IDX--) HEX[IDX] = (IDX + 256).toString(16).substring(1);

function v4() {
	var i=0, num, out='';

	if (!BUFFER || ((IDX + 16) > 256)) {
		BUFFER = Array(i=256);
		while (i--) BUFFER[i] = 256 * Math.random() | 0;
		i = IDX = 0;
	}

	for (; i < 16; i++) {
		num = BUFFER[IDX + i];
		if (i==6) out += HEX[num & 15 | 64];
		else if (i==8) out += HEX[num & 63 | 128];
		else out += HEX[num];

		if (i & 1 && i > 1 && i < 11) out += '-';
	}

	IDX++;
	return out;
}

;// CONCATENATED MODULE: ./packages/anywidget/src/invoke.ts

function invoke_invoke(model, name, msg) {
    var options = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {};
    var _options_signal;
    // crypto.randomUUID() is not available in non-secure contexts (i.e., http://)
    // so we use simple (non-secure) polyfill.
    var id = uuid.v4();
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




function host_createHost(model, param) {
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

;// CONCATENATED MODULE: ./packages/anywidget/src/runtime.ts
function _array_like_to_array(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for(var i = 0, arr2 = new Array(len); i < len; i++)arr2[i] = arr[i];
    return arr2;
}
function _array_with_holes(arr) {
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
var runtime_Runtime = /*#__PURE__*/ (/* unused pure expression or super */ null && (function() {
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
        var dispose = solid.createRoot(function(dispose) {
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
            var _solid_createSignal = _sliced_to_array(solid.createSignal({
                status: "pending"
            }), 2), widgetResult = _solid_createSignal[0], setWidgetResult = _solid_createSignal[1];
            runtime_class_private_field_set(_this, _widgetResult, widgetResult);
            solid.createEffect(solid.on(css, function() {
                return console.debug("[anywidget] css hot updated: ".concat(id));
            }, {
                defer: true
            }));
            solid.createEffect(solid.on(esm, function() {
                return console.debug("[anywidget] esm hot updated: ".concat(id));
            }, {
                defer: true
            }));
            solid.createEffect(function() {
                return loadCss(css(), id);
            });
            solid.createEffect(function() {
                // Per-effect controller so a stale loadWidget resolution from a
                // previous _esm value cannot overwrite a newer one. Solid fires
                // onCleanup before re-running the effect, aborting the prior load.
                var controller = new AbortController();
                solid.onCleanup(function() {
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
                        dispose = solid.createRoot(function(dispose) {
                            solid.createEffect(function() {
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
                                solid.onCleanup(function() {
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
}()));

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
                    RUNTIMES.set(this, new Runtime(this, {
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

;// CONCATENATED MODULE: ./packages/anywidget/src/index.js


// @ts-expect-error -- define is a global provided by the notebook runtime.
define(["@jupyter-widgets/base"], create);


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

// webpack/runtime/has_own_property
(() => {
__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
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
// webpack/runtime/consumes_loading
(() => {

__webpack_require__.consumesLoadingData = { chunkMapping: {}, moduleIdToConsumeDataMapping: {}, initialConsumes: [] };
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

})();
// webpack/runtime/rspack_unique_id
(() => {
__webpack_require__.ruid = "bundler=rspack@1.7.11";
})();
// module cache are used so entry inlining is disabled
// startup
// Load entry module and return exports
var __webpack_exports__ = __webpack_require__(464);
})()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWFpbi4yMzQxYjAxMi5qcyIsInNvdXJjZXMiOlsid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL21vZGVsLXByb3h5LnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL3V0aWwudHMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvYmluZGluZy50cyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvLy4vbm9kZV9tb2R1bGVzLy5wbnBtL0BsdWtlZWQrdXVpZEAyLjAuMS9ub2RlX21vZHVsZXMvQGx1a2VlZC91dWlkL2Rpc3QvaW5kZXgubWpzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL2ludm9rZS50cyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvLy4vcGFja2FnZXMvYW55d2lkZ2V0L3NyYy9ob3N0LnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL3J1bnRpbWUudHMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL3BhY2thZ2VzL2FueXdpZGdldC9zcmMvd2lkZ2V0LnRzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9wYWNrYWdlcy9hbnl3aWRnZXQvc3JjL2luZGV4LmpzIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL2hhc19vd25fcHJvcGVydHkiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvcnNwYWNrX3ZlcnNpb24iLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby93ZWJwYWNrL3J1bnRpbWUvc2hhcmluZyIsIndlYnBhY2s6Ly9AYW55d2lkZ2V0L21vbm9yZXBvL3dlYnBhY2svcnVudGltZS9jb25zdW1lc19sb2FkaW5nIiwid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vd2VicGFjay9ydW50aW1lL3JzcGFja191bmlxdWVfaWQiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHR5cGUgeyBBbnlNb2RlbCB9IGZyb20gXCJAYW55d2lkZ2V0L3R5cGVzXCI7XG5pbXBvcnQgdHlwZSB7IERPTVdpZGdldE1vZGVsIH0gZnJvbSBcIkBqdXB5dGVyLXdpZGdldHMvYmFzZVwiO1xuXG4vKipcbiAqIFRoaXMgaXMgYSB0cmljayBzbyB0aGF0IHdlIGNhbiBjbGVhbnVwIGV2ZW50IGxpc3RlbmVycyBhZGRlZFxuICogYnkgdGhlIHVzZXItZGVmaW5lZCBmdW5jdGlvbi5cbiAqL1xuZXhwb3J0IGxldCBJTklUSUFMSVpFX01BUktFUiA9IFN5bWJvbChcImFueXdpZGdldC5pbml0aWFsaXplXCIpO1xuXG4vKipcbiAqIFBydW5lcyB0aGUgdmlldyBkb3duIHRvIHRoZSBtaW5pbXVtIGNvbnRleHQgbmVjZXNzYXJ5LlxuICpcbiAqIENhbGxzIHRvIGBtb2RlbC5nZXRgIGFuZCBgbW9kZWwuc2V0YCBhdXRvbWF0aWNhbGx5IGFkZCB0aGVcbiAqIGBjb250ZXh0YCwgc28gd2UgY2FuIGdyYWNlZnVsbHkgdW5zdWJzY3JpYmUgZnJvbSBldmVudHNcbiAqIGFkZGVkIGJ5IHVzZXItZGVmaW5lZCBob29rcy5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIG1vZGVsUHJveHkobW9kZWw6IERPTVdpZGdldE1vZGVsLCBjb250ZXh0OiB1bmtub3duKTogQW55TW9kZWwge1xuICAvLyBveGxpbnQtZGlzYWJsZS1uZXh0LWxpbmUgdHlwZXNjcmlwdC1lc2xpbnQvbm8tdW5zYWZlLXR5cGUtYXNzZXJ0aW9uIC0tIERPTVdpZGdldE1vZGVsLmdldC9zZXQvb24vb2ZmIGhhdmUgd2lkZXIgc2lnbmF0dXJlcyB0aGFuIEFueU1vZGVsLCBzbyBib3VuZCB2ZXJzaW9ucyBkb24ndCBuYXJyb3cgY2xlYW5seTsgdGhlIHNoYXBlIGlzIHN0cnVjdHVyYWxseSBjb21wYXRpYmxlXG4gIHJldHVybiB7XG4gICAgZ2V0OiBtb2RlbC5nZXQuYmluZChtb2RlbCksXG4gICAgc2V0OiBtb2RlbC5zZXQuYmluZChtb2RlbCksXG4gICAgc2F2ZV9jaGFuZ2VzOiBtb2RlbC5zYXZlX2NoYW5nZXMuYmluZChtb2RlbCksXG4gICAgc2VuZDogbW9kZWwuc2VuZC5iaW5kKG1vZGVsKSxcbiAgICBvbihuYW1lLCBjYWxsYmFjaykge1xuICAgICAgbW9kZWwub24obmFtZSwgY2FsbGJhY2ssIGNvbnRleHQpO1xuICAgIH0sXG4gICAgb2ZmKG5hbWUsIGNhbGxiYWNrKSB7XG4gICAgICBtb2RlbC5vZmYobmFtZSwgY2FsbGJhY2ssIGNvbnRleHQpO1xuICAgIH0sXG4gICAgLy8gVGhlIHdpZGdldF9tYW5hZ2VyIHR5cGUgaXMgd2lkZXIgdGhhbiB3aGF0IHdlIHdhbnQgdG8gZXhwb3NlIHRvXG4gICAgLy8gZGV2ZWxvcGVycy4gSW4gYSBmdXR1cmUgdmVyc2lvbiwgd2Ugd2lsbCBleHBvc2UgYSBtb3JlIGxpbWl0ZWQgQVBJIGJ1dFxuICAgIC8vIHRoYXQgY2FuIHdhaXQgZm9yIGEgbWlub3IgdmVyc2lvbiBidW1wLlxuICAgIHdpZGdldF9tYW5hZ2VyOiBtb2RlbC53aWRnZXRfbWFuYWdlcixcbiAgfSBhcyBBbnlNb2RlbDtcbn1cbiIsImV4cG9ydCB0eXBlIEF3YWl0YWJsZTxUPiA9IFQgfCBQcm9taXNlTGlrZTxUPjtcblxuZXhwb3J0IGludGVyZmFjZSBSZWFkeTxUPiB7XG4gIHN0YXR1czogXCJyZWFkeVwiO1xuICBkYXRhOiBUO1xufVxuXG5leHBvcnQgaW50ZXJmYWNlIFBlbmRpbmcge1xuICBzdGF0dXM6IFwicGVuZGluZ1wiO1xufVxuXG5leHBvcnQgaW50ZXJmYWNlIEVycm9yZWQge1xuICBzdGF0dXM6IFwiZXJyb3JcIjtcbiAgZXJyb3I6IHVua25vd247XG59XG5cbmV4cG9ydCB0eXBlIFJlc3VsdDxUPiA9IFBlbmRpbmcgfCBSZWFkeTxUPiB8IEVycm9yZWQ7XG5cbmV4cG9ydCBmdW5jdGlvbiBhc3NlcnQoY29uZGl0aW9uOiB1bmtub3duLCBtZXNzYWdlOiBzdHJpbmcpOiBhc3NlcnRzIGNvbmRpdGlvbiB7XG4gIGlmICghY29uZGl0aW9uKSB0aHJvdyBuZXcgRXJyb3IobWVzc2FnZSk7XG59XG5cbmV4cG9ydCBhc3luYyBmdW5jdGlvbiBzYWZlQ2xlYW51cChcbiAgZm46IHZvaWQgfCAoKCkgPT4gQXdhaXRhYmxlPHZvaWQ+KSB8IHVuZGVmaW5lZCxcbiAga2luZDogc3RyaW5nLFxuKTogUHJvbWlzZTx2b2lkPiB7XG4gIHJldHVybiBQcm9taXNlLnJlc29sdmUoKVxuICAgIC50aGVuKCgpID0+IGZuPy4oKSlcbiAgICAuY2F0Y2goKGUpID0+IGNvbnNvbGUud2FybihgW2FueXdpZGdldF0gZXJyb3IgY2xlYW5pbmcgdXAgJHtraW5kfS5gLCBlKSk7XG59XG5cbi8qKlxuICogQ2xlYW5zIHVwIHRoZSBzdGFjayB0cmFjZSBhdCBhbnl3aWRnZXQgYm91bmRhcnkuXG4gKiBZb3UgY2FuIGZ1bGx5IGluc3BlY3QgdGhlIGVudGlyZSBzdGFjayB0cmFjZSBpbiB0aGUgY29uc29sZSBpbnRlcmFjdGl2ZWx5LFxuICogYnV0IHRoZSBpbml0aWFsIGVycm9yIG1lc3NhZ2UgaXMgY2xlYW5lZCB1cCB0byBiZSBtb3JlIHVzZXItZnJpZW5kbHkuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiB0aHJvd0FueXdpZGdldEVycm9yKHNvdXJjZTogdW5rbm93bik6IG5ldmVyIHtcbiAgaWYgKCEoc291cmNlIGluc3RhbmNlb2YgRXJyb3IpKSB7XG4gICAgLy8gRG9uJ3Qga25vdyB3aGF0IHRvIGRvIHdpdGggdGhpcy5cbiAgICB0aHJvdyBzb3VyY2U7XG4gIH1cbiAgbGV0IGxpbmVzID0gc291cmNlLnN0YWNrPy5zcGxpdChcIlxcblwiKSA/PyBbXTtcbiAgbGV0IGFueXdpZGdldEluZGV4ID0gbGluZXMuZmluZEluZGV4KChsaW5lKSA9PiBsaW5lLmluY2x1ZGVzKFwiYW55d2lkZ2V0XCIpKTtcbiAgbGV0IGNsZWFuU3RhY2sgPSBhbnl3aWRnZXRJbmRleCA9PT0gLTEgPyBsaW5lcyA6IGxpbmVzLnNsaWNlKDAsIGFueXdpZGdldEluZGV4ICsgMSk7XG4gIHNvdXJjZS5zdGFjayA9IGNsZWFuU3RhY2suam9pbihcIlxcblwiKTtcbiAgY29uc29sZS5lcnJvcihzb3VyY2UpO1xuICB0aHJvdyBzb3VyY2U7XG59XG5cbi8qKlxuICogUG9seWZpbGwgZm9yIHtAbGluayBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9KYXZhU2NyaXB0L1JlZmVyZW5jZS9HbG9iYWxfT2JqZWN0cy9Qcm9taXNlL3dpdGhSZXNvbHZlcnMgUHJvbWlzZS53aXRoUmVzb2x2ZXJzfVxuICpcbiAqIFRyZXZvcigyMDI1LTAzLTE0KTogU2hvdWxkIGJlIGFibGUgdG8gcmVtb3ZlIG9uY2UgbW9yZSBzdGFibGUgYWNyb3NzIGJyb3dzZXJzLlxuICovXG5leHBvcnQgZnVuY3Rpb24gcHJvbWlzZVdpdGhSZXNvbHZlcnM8VD4oKTogUHJvbWlzZVdpdGhSZXNvbHZlcnM8VD4ge1xuICBsZXQgcmVzb2x2ZSE6ICh2YWx1ZTogVCB8IFByb21pc2VMaWtlPFQ+KSA9PiB2b2lkO1xuICBsZXQgcmVqZWN0ITogKHJlYXNvbj86IHVua25vd24pID0+IHZvaWQ7XG4gIGxldCBwcm9taXNlID0gbmV3IFByb21pc2U8VD4oKHJlcywgcmVqKSA9PiB7XG4gICAgcmVzb2x2ZSA9IHJlcztcbiAgICByZWplY3QgPSByZWo7XG4gIH0pO1xuICByZXR1cm4geyBwcm9taXNlLCByZXNvbHZlLCByZWplY3QgfTtcbn1cbiIsImltcG9ydCB0eXBlIHsgRXhwZXJpbWVudGFsLCBIb3N0IH0gZnJvbSBcIkBhbnl3aWRnZXQvdHlwZXNcIjtcbmltcG9ydCB0eXBlIHsgRE9NV2lkZ2V0TW9kZWwgfSBmcm9tIFwiQGp1cHl0ZXItd2lkZ2V0cy9iYXNlXCI7XG5cbmltcG9ydCB0eXBlIHsgQW55V2lkZ2V0IH0gZnJvbSBcIi4vbG9hZC50c1wiO1xuaW1wb3J0IHsgSU5JVElBTElaRV9NQVJLRVIsIG1vZGVsUHJveHkgfSBmcm9tIFwiLi9tb2RlbC1wcm94eS50c1wiO1xuaW1wb3J0IHsgdHlwZSBBd2FpdGFibGUsIHByb21pc2VXaXRoUmVzb2x2ZXJzLCBzYWZlQ2xlYW51cCB9IGZyb20gXCIuL3V0aWwudHNcIjtcblxuLyoqXG4gKiBUaGUgbWluaW1hbCBzdXJmYWNlIGBjcmVhdGVWaWV3YCBuZWVkcyBmcm9tIGEgdmlldy1saWtlIG9iamVjdC4gVGhlIG9iamVjdFxuICogaWRlbnRpdHkgaXMgdXNlZCBhcyB0aGUgbGlzdGVuZXIgY29udGV4dCBmb3IgYG1vZGVsUHJveHlgLCBhbmQgYGVsYCBpcyB0aGVcbiAqIHJlbmRlciB0YXJnZXQuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgVmlld1RhcmdldCB7XG4gIGVsOiBIVE1MRWxlbWVudDtcbn1cblxuZnVuY3Rpb24gaXNTYWZlQ2xlYW51cEZ1bmN0aW9uKHg6IHVua25vd24pOiB4IGlzICgpID0+IEF3YWl0YWJsZTx2b2lkPiB7XG4gIHJldHVybiB0eXBlb2YgeCA9PT0gXCJmdW5jdGlvblwiO1xufVxuXG5leHBvcnQgY2xhc3MgV2lkZ2V0QmluZGluZyB7XG4gICNjb250cm9sbGVyOiBBYm9ydENvbnRyb2xsZXIgfCB1bmRlZmluZWQ7XG4gICN3aWRnZXREZWY6IEFueVdpZGdldCB8IHVuZGVmaW5lZDtcbiAgI2V4cG9ydHM6IHVua25vd247XG4gICNtb2RlbDogRE9NV2lkZ2V0TW9kZWw7XG4gIHJlYWR5OiBQcm9taXNlPHVua25vd24+O1xuICAjcmVzb2x2ZXJzOiBQcm9taXNlV2l0aFJlc29sdmVyczx1bmtub3duPjtcblxuICBjb25zdHJ1Y3Rvcihtb2RlbDogRE9NV2lkZ2V0TW9kZWwpIHtcbiAgICB0aGlzLiNtb2RlbCA9IG1vZGVsO1xuICAgIHRoaXMuI3Jlc29sdmVycyA9IHByb21pc2VXaXRoUmVzb2x2ZXJzKCk7XG4gICAgdGhpcy5yZWFkeSA9IHRoaXMuI3Jlc29sdmVycy5wcm9taXNlO1xuICB9XG5cbiAgYXN5bmMgYmluZChcbiAgICB3aWRnZXREZWY6IEFueVdpZGdldCxcbiAgICB7IGV4cGVyaW1lbnRhbCB9OiB7IGV4cGVyaW1lbnRhbDogRXhwZXJpbWVudGFsIH0sXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGlmICh0aGlzLiN3aWRnZXREZWYgPT09IHdpZGdldERlZikgcmV0dXJuO1xuXG4gICAgaWYgKHRoaXMuI3dpZGdldERlZiAmJiB0aGlzLiN3aWRnZXREZWYgIT09IHdpZGdldERlZikge1xuICAgICAgdGhpcy4jY29udHJvbGxlcj8uYWJvcnQoKTtcbiAgICAgIC8vIFNldHRsZSB0aGUgb2xkIHByb21pc2Ugc28gYW55IGF3YWl0ZXIgdGhhdCBjYXB0dXJlZCBgdGhpcy5yZWFkeWBcbiAgICAgIC8vIChlLmcuIGEgcGFyZW50J3MgYGhvc3QuZ2V0V2lkZ2V0YCBzbmFwc2hvdCkgdW5ibG9ja3MgaW5zdGVhZCBvZlxuICAgICAgLy8gaGFuZ2luZyB1bnRpbCB0aGUgaG9zdCdzIDEwcyB0aW1lb3V0LiBOby1vcCBpZiBhbHJlYWR5IHJlc29sdmVkLlxuICAgICAgbGV0IHByZXZSZXNvbHZlcnMgPSB0aGlzLiNyZXNvbHZlcnM7XG4gICAgICB0aGlzLiNyZXNvbHZlcnMgPSBwcm9taXNlV2l0aFJlc29sdmVycygpO1xuICAgICAgdGhpcy5yZWFkeSA9IHRoaXMuI3Jlc29sdmVycy5wcm9taXNlO1xuICAgICAgcHJldlJlc29sdmVycy5wcm9taXNlLmNhdGNoKCgpID0+IHt9KTtcbiAgICAgIHByZXZSZXNvbHZlcnMucmVqZWN0KG5ldyBFcnJvcihcIlthbnl3aWRnZXRdIHdpZGdldCBiaW5kIGFib3J0ZWQgYnkgcmUtYmluZFwiKSk7XG4gICAgfVxuXG4gICAgdGhpcy4jd2lkZ2V0RGVmID0gd2lkZ2V0RGVmO1xuICAgIHRoaXMuI2NvbnRyb2xsZXIgPSBuZXcgQWJvcnRDb250cm9sbGVyKCk7XG4gICAgbGV0IHNpZ25hbCA9IHRoaXMuI2NvbnRyb2xsZXIuc2lnbmFsO1xuICAgIGxldCBtb2RlbCA9IHRoaXMuI21vZGVsO1xuXG4gICAgbW9kZWwub2ZmKG51bGwsIG51bGwsIElOSVRJQUxJWkVfTUFSS0VSKTtcblxuICAgIGxldCByZXN1bHQgPSBhd2FpdCB3aWRnZXREZWYuaW5pdGlhbGl6ZT8uKHtcbiAgICAgIG1vZGVsOiBtb2RlbFByb3h5KG1vZGVsLCBJTklUSUFMSVpFX01BUktFUiksXG4gICAgICBzaWduYWwsXG4gICAgICBleHBlcmltZW50YWwsXG4gICAgfSk7XG5cbiAgICBpZiAoc2lnbmFsLmFib3J0ZWQpIHtcbiAgICAgIGF3YWl0IHNhZmVDbGVhbnVwKGlzU2FmZUNsZWFudXBGdW5jdGlvbihyZXN1bHQpID8gcmVzdWx0IDogdW5kZWZpbmVkLCBcImVzbSB1cGRhdGVcIik7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgaWYgKGlzU2FmZUNsZWFudXBGdW5jdGlvbihyZXN1bHQpKSB7XG4gICAgICBzaWduYWwuYWRkRXZlbnRMaXN0ZW5lcihcImFib3J0XCIsICgpID0+IHNhZmVDbGVhbnVwKHJlc3VsdCwgXCJlc20gdXBkYXRlXCIpKTtcbiAgICAgIHRoaXMuI2V4cG9ydHMgPSB1bmRlZmluZWQ7XG4gICAgfSBlbHNlIGlmICh0eXBlb2YgcmVzdWx0ID09PSBcIm9iamVjdFwiICYmIHJlc3VsdCAhPT0gbnVsbCkge1xuICAgICAgdGhpcy4jZXhwb3J0cyA9IHJlc3VsdDtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy4jZXhwb3J0cyA9IHVuZGVmaW5lZDtcbiAgICB9XG5cbiAgICB0aGlzLiNyZXNvbHZlcnMucmVzb2x2ZSh0aGlzLiNleHBvcnRzKTtcbiAgfVxuXG4gIGFzeW5jIGNyZWF0ZVZpZXcoXG4gICAgdGFyZ2V0OiBWaWV3VGFyZ2V0LFxuICAgIHsgc2lnbmFsLCBleHBlcmltZW50YWwsIGhvc3QgfTogeyBzaWduYWw6IEFib3J0U2lnbmFsOyBleHBlcmltZW50YWw6IEV4cGVyaW1lbnRhbDsgaG9zdDogSG9zdCB9LFxuICApOiBQcm9taXNlPHVuZGVmaW5lZD4ge1xuICAgIGF3YWl0IHRoaXMucmVhZHk7XG4gICAgaWYgKCF0aGlzLiN3aWRnZXREZWY/LnJlbmRlcikgcmV0dXJuO1xuICAgIGxldCBjb250cm9sbGVyID0gbmV3IEFib3J0Q29udHJvbGxlcigpO1xuICAgIGxldCBjb21iaW5lZCA9IEFib3J0U2lnbmFsLmFueShbc2lnbmFsLCBjb250cm9sbGVyLnNpZ25hbF0pO1xuICAgIGxldCBtb2RlbCA9IHRoaXMuI21vZGVsO1xuICAgIGxldCBjbGVhbnVwID0gYXdhaXQgdGhpcy4jd2lkZ2V0RGVmLnJlbmRlcih7XG4gICAgICBtb2RlbDogbW9kZWxQcm94eShtb2RlbCwgdGFyZ2V0KSxcbiAgICAgIGVsOiB0YXJnZXQuZWwsXG4gICAgICBzaWduYWw6IGNvbWJpbmVkLFxuICAgICAgaG9zdCxcbiAgICAgIGV4cGVyaW1lbnRhbCxcbiAgICB9KTtcbiAgICBsZXQgZGlzcG9zZVZpZXcgPSAocmVhc29uOiBzdHJpbmcpOiB2b2lkID0+IHtcbiAgICAgIC8vIENsZWFyIGxpc3RlbmVycyBrZXllZCB0byB0aGlzIHRhcmdldC4gRm9yIGVwaGVtZXJhbCBge2VsfWAgdGFyZ2V0c1xuICAgICAgLy8gKGhvc3QuZ2V0V2lkZ2V0KCkucmVuZGVyKSwgdGhpcyBwcmV2ZW50cyBsZWFrcyBhY3Jvc3MgcmUtcmVuZGVycy5cbiAgICAgIG1vZGVsLm9mZihudWxsLCBudWxsLCB0YXJnZXQpO1xuICAgICAgdm9pZCBzYWZlQ2xlYW51cChjbGVhbnVwLCByZWFzb24pO1xuICAgIH07XG4gICAgaWYgKGNvbWJpbmVkLmFib3J0ZWQpIHtcbiAgICAgIGRpc3Bvc2VWaWV3KFwiZGlzcG9zZSB2aWV3IC0gYWxyZWFkeSBhYm9ydGVkXCIpO1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb21iaW5lZC5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4gZGlzcG9zZVZpZXcoXCJkaXNwb3NlIHZpZXcgLSBhYm9ydGVkXCIpKTtcbiAgfVxuXG4gIGdldCBleHBvcnRzKCk6IHVua25vd24ge1xuICAgIHJldHVybiB0aGlzLiNleHBvcnRzO1xuICB9XG5cbiAgZGVzdHJveSgpOiB2b2lkIHtcbiAgICB0aGlzLiNjb250cm9sbGVyPy5hYm9ydCgpO1xuICAgIHRoaXMuI2NvbnRyb2xsZXIgPSB1bmRlZmluZWQ7XG4gICAgdGhpcy4jd2lkZ2V0RGVmID0gdW5kZWZpbmVkO1xuICB9XG59XG5cbmNsYXNzIEJpbmRpbmdNYW5hZ2VyIHtcbiAgI2JpbmRpbmdzID0gbmV3IE1hcDxET01XaWRnZXRNb2RlbCwgV2lkZ2V0QmluZGluZz4oKTtcblxuICBnZXRPckNyZWF0ZShtb2RlbDogRE9NV2lkZ2V0TW9kZWwpOiBXaWRnZXRCaW5kaW5nIHtcbiAgICBsZXQgYmluZGluZyA9IHRoaXMuI2JpbmRpbmdzLmdldChtb2RlbCk7XG4gICAgaWYgKCFiaW5kaW5nKSB7XG4gICAgICBiaW5kaW5nID0gbmV3IFdpZGdldEJpbmRpbmcobW9kZWwpO1xuICAgICAgdGhpcy4jYmluZGluZ3Muc2V0KG1vZGVsLCBiaW5kaW5nKTtcbiAgICB9XG4gICAgcmV0dXJuIGJpbmRpbmc7XG4gIH1cblxuICBnZXQobW9kZWw6IERPTVdpZGdldE1vZGVsKTogV2lkZ2V0QmluZGluZyB8IHVuZGVmaW5lZCB7XG4gICAgcmV0dXJuIHRoaXMuI2JpbmRpbmdzLmdldChtb2RlbCk7XG4gIH1cblxuICBkZXN0cm95KG1vZGVsOiBET01XaWRnZXRNb2RlbCk6IHZvaWQge1xuICAgIGxldCBiaW5kaW5nID0gdGhpcy4jYmluZGluZ3MuZ2V0KG1vZGVsKTtcbiAgICBpZiAoYmluZGluZykge1xuICAgICAgYmluZGluZy5kZXN0cm95KCk7XG4gICAgICB0aGlzLiNiaW5kaW5ncy5kZWxldGUobW9kZWwpO1xuICAgIH1cbiAgfVxufVxuXG5leHBvcnQgbGV0IEJJTkRJTkdTID0gbmV3IEJpbmRpbmdNYW5hZ2VyKCk7XG4iLCJ2YXIgSURYPTI1NiwgSEVYPVtdLCBCVUZGRVI7XG53aGlsZSAoSURYLS0pIEhFWFtJRFhdID0gKElEWCArIDI1NikudG9TdHJpbmcoMTYpLnN1YnN0cmluZygxKTtcblxuZXhwb3J0IGZ1bmN0aW9uIHY0KCkge1xuXHR2YXIgaT0wLCBudW0sIG91dD0nJztcblxuXHRpZiAoIUJVRkZFUiB8fCAoKElEWCArIDE2KSA+IDI1NikpIHtcblx0XHRCVUZGRVIgPSBBcnJheShpPTI1Nik7XG5cdFx0d2hpbGUgKGktLSkgQlVGRkVSW2ldID0gMjU2ICogTWF0aC5yYW5kb20oKSB8IDA7XG5cdFx0aSA9IElEWCA9IDA7XG5cdH1cblxuXHRmb3IgKDsgaSA8IDE2OyBpKyspIHtcblx0XHRudW0gPSBCVUZGRVJbSURYICsgaV07XG5cdFx0aWYgKGk9PTYpIG91dCArPSBIRVhbbnVtICYgMTUgfCA2NF07XG5cdFx0ZWxzZSBpZiAoaT09OCkgb3V0ICs9IEhFWFtudW0gJiA2MyB8IDEyOF07XG5cdFx0ZWxzZSBvdXQgKz0gSEVYW251bV07XG5cblx0XHRpZiAoaSAmIDEgJiYgaSA+IDEgJiYgaSA8IDExKSBvdXQgKz0gJy0nO1xuXHR9XG5cblx0SURYKys7XG5cdHJldHVybiBvdXQ7XG59XG4iLCJpbXBvcnQgdHlwZSB7IEFueU1vZGVsIH0gZnJvbSBcIkBhbnl3aWRnZXQvdHlwZXNcIjtcbmltcG9ydCAqIGFzIHV1aWQgZnJvbSBcIkBsdWtlZWQvdXVpZFwiO1xuXG5leHBvcnQgaW50ZXJmYWNlIEludm9rZU9wdGlvbnMge1xuICBidWZmZXJzPzogRGF0YVZpZXdbXTtcbiAgc2lnbmFsPzogQWJvcnRTaWduYWw7XG59XG5cbmV4cG9ydCBmdW5jdGlvbiBpbnZva2U8VD4oXG4gIG1vZGVsOiBBbnlNb2RlbCxcbiAgbmFtZTogc3RyaW5nLFxuICBtc2c/OiB1bmtub3duLFxuICBvcHRpb25zOiBJbnZva2VPcHRpb25zID0ge30sXG4pOiBQcm9taXNlPFtULCBEYXRhVmlld1tdXT4ge1xuICAvLyBjcnlwdG8ucmFuZG9tVVVJRCgpIGlzIG5vdCBhdmFpbGFibGUgaW4gbm9uLXNlY3VyZSBjb250ZXh0cyAoaS5lLiwgaHR0cDovLylcbiAgLy8gc28gd2UgdXNlIHNpbXBsZSAobm9uLXNlY3VyZSkgcG9seWZpbGwuXG4gIGxldCBpZCA9IHV1aWQudjQoKTtcbiAgbGV0IHNpZ25hbCA9IG9wdGlvbnMuc2lnbmFsID8/IEFib3J0U2lnbmFsLnRpbWVvdXQoMzAwMCk7XG5cbiAgcmV0dXJuIG5ldyBQcm9taXNlKChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICBpZiAoc2lnbmFsLmFib3J0ZWQpIHtcbiAgICAgIHJlamVjdChzaWduYWwucmVhc29uKTtcbiAgICB9XG4gICAgc2lnbmFsLmFkZEV2ZW50TGlzdGVuZXIoXCJhYm9ydFwiLCAoKSA9PiB7XG4gICAgICBtb2RlbC5vZmYoXCJtc2c6Y3VzdG9tXCIsIGhhbmRsZXIpO1xuICAgICAgcmVqZWN0KHNpZ25hbC5yZWFzb24pO1xuICAgIH0pO1xuXG4gICAgZnVuY3Rpb24gaGFuZGxlcihcbiAgICAgIG1zZzogeyBpZDogc3RyaW5nOyBraW5kOiBcImFueXdpZGdldC1jb21tYW5kLXJlc3BvbnNlXCI7IHJlc3BvbnNlOiBUIH0sXG4gICAgICBidWZmZXJzOiBEYXRhVmlld1tdLFxuICAgICk6IHZvaWQge1xuICAgICAgaWYgKCEobXNnLmlkID09PSBpZCkpIHJldHVybjtcbiAgICAgIHJlc29sdmUoW21zZy5yZXNwb25zZSwgYnVmZmVyc10pO1xuICAgICAgbW9kZWwub2ZmKFwibXNnOmN1c3RvbVwiLCBoYW5kbGVyKTtcbiAgICB9XG4gICAgbW9kZWwub24oXCJtc2c6Y3VzdG9tXCIsIGhhbmRsZXIpO1xuICAgIG1vZGVsLnNlbmQoeyBpZCwga2luZDogXCJhbnl3aWRnZXQtY29tbWFuZFwiLCBuYW1lLCBtc2cgfSwgdW5kZWZpbmVkLCBvcHRpb25zLmJ1ZmZlcnMgPz8gW10pO1xuICB9KTtcbn1cbiIsImltcG9ydCB0eXBlIHsgSG9zdCB9IGZyb20gXCJAYW55d2lkZ2V0L3R5cGVzXCI7XG5pbXBvcnQgdHlwZSB7IERPTVdpZGdldE1vZGVsIH0gZnJvbSBcIkBqdXB5dGVyLXdpZGdldHMvYmFzZVwiO1xuXG5pbXBvcnQgeyBCSU5ESU5HUyB9IGZyb20gXCIuL2JpbmRpbmcudHNcIjtcbmltcG9ydCB7IGludm9rZSB9IGZyb20gXCIuL2ludm9rZS50c1wiO1xuaW1wb3J0IHsgbW9kZWxQcm94eSB9IGZyb20gXCIuL21vZGVsLXByb3h5LnRzXCI7XG5pbXBvcnQgeyBwYXJzZVdpZGdldFJlZiB9IGZyb20gXCIuL3dpZGdldC1yZWYudHNcIjtcblxuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZUhvc3QobW9kZWw6IERPTVdpZGdldE1vZGVsLCB7IHNpZ25hbCB9OiB7IHNpZ25hbDogQWJvcnRTaWduYWwgfSk6IEhvc3Qge1xuICBsZXQgaG9zdDogSG9zdCA9IHtcbiAgICAvLyBAdHMtZXhwZWN0LWVycm9yIC0gbW9kZWxQcm94eSByZXR1cm5zIEFueU1vZGVsOyBnZW5lcmljIFQgaXMgZXJhc2VkIGF0IHJ1bnRpbWVcbiAgICBhc3luYyBnZXRNb2RlbChyZWYpIHtcbiAgICAgIGxldCBtb2RlbElkID0gcGFyc2VXaWRnZXRSZWYocmVmKTtcbiAgICAgIGxldCBjaGlsZE1vZGVsID0gYXdhaXQgbW9kZWwud2lkZ2V0X21hbmFnZXIuZ2V0X21vZGVsKG1vZGVsSWQpO1xuICAgICAgbGV0IGNvbnRleHQgPSBTeW1ib2woXCJhbnl3aWRnZXQuaG9zdC5nZXRNb2RlbFwiKTtcbiAgICAgIHNpZ25hbC5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4gY2hpbGRNb2RlbC5vZmYobnVsbCwgbnVsbCwgY29udGV4dCkpO1xuICAgICAgcmV0dXJuIG1vZGVsUHJveHkoY2hpbGRNb2RlbCwgY29udGV4dCk7XG4gICAgfSxcbiAgICAvLyBAdHMtZXhwZWN0LWVycm9yIC0gZ2VuZXJpYyBUIGlzIGVyYXNlZCBhdCBydW50aW1lLCBleHBvcnRzIHR5cGVkIGFzIHVua25vd25cbiAgICBhc3luYyBnZXRXaWRnZXQocmVmKSB7XG4gICAgICBsZXQgbW9kZWxJZCA9IHBhcnNlV2lkZ2V0UmVmKHJlZik7XG4gICAgICBsZXQgY2hpbGRNb2RlbCA9IGF3YWl0IG1vZGVsLndpZGdldF9tYW5hZ2VyLmdldF9tb2RlbChtb2RlbElkKTtcbiAgICAgIGxldCBjaGlsZEJpbmRpbmcgPSBCSU5ESU5HUy5nZXQoY2hpbGRNb2RlbCk7XG4gICAgICBpZiAoIWNoaWxkQmluZGluZykge1xuICAgICAgICB0aHJvdyBuZXcgRXJyb3IoYFthbnl3aWRnZXRdIE5vIGJpbmRpbmcgZm91bmQgZm9yIHdpZGdldCAke21vZGVsSWR9YCk7XG4gICAgICB9XG4gICAgICBsZXQgdGltZXI6IFJldHVyblR5cGU8dHlwZW9mIHNldFRpbWVvdXQ+IHwgdW5kZWZpbmVkO1xuICAgICAgbGV0IGV4cG9ydHMgPSBhd2FpdCBuZXcgUHJvbWlzZTx1bmtub3duPigocmVzb2x2ZSwgcmVqZWN0KSA9PiB7XG4gICAgICAgIHRpbWVyID0gc2V0VGltZW91dChcbiAgICAgICAgICAoKSA9PlxuICAgICAgICAgICAgcmVqZWN0KG5ldyBFcnJvcihgW2FueXdpZGdldF0gVGltZWQgb3V0IHdhaXRpbmcgZm9yIHdpZGdldCAke21vZGVsSWR9IHRvIGluaXRpYWxpemVgKSksXG4gICAgICAgICAgMTBfMDAwLFxuICAgICAgICApO1xuICAgICAgICBjaGlsZEJpbmRpbmcucmVhZHkudGhlbihyZXNvbHZlLCByZWplY3QpO1xuICAgICAgfSkuZmluYWxseSgoKSA9PiBjbGVhclRpbWVvdXQodGltZXIpKTtcbiAgICAgIHJldHVybiB7XG4gICAgICAgIGV4cG9ydHMsXG4gICAgICAgIGFzeW5jIHJlbmRlcih7IGVsLCBzaWduYWw6IHZpZXdTaWduYWwgfSkge1xuICAgICAgICAgIGxldCBjaGlsZFZpZXdTaWduYWwgPSB2aWV3U2lnbmFsID8/IHNpZ25hbDtcbiAgICAgICAgICBhd2FpdCBjaGlsZEJpbmRpbmcuY3JlYXRlVmlldyhcbiAgICAgICAgICAgIHsgZWwgfSxcbiAgICAgICAgICAgIHtcbiAgICAgICAgICAgICAgc2lnbmFsOiBjaGlsZFZpZXdTaWduYWwsXG4gICAgICAgICAgICAgIGV4cGVyaW1lbnRhbDoge1xuICAgICAgICAgICAgICAgIC8vIEB0cy1leHBlY3QtZXJyb3IgLSBiaW5kIGlzbid0IHdvcmtpbmdcbiAgICAgICAgICAgICAgICBpbnZva2U6IGludm9rZS5iaW5kKG51bGwsIGNoaWxkTW9kZWwpLFxuICAgICAgICAgICAgICB9LFxuICAgICAgICAgICAgICBob3N0LFxuICAgICAgICAgICAgfSxcbiAgICAgICAgICApO1xuICAgICAgICB9LFxuICAgICAgfTtcbiAgICB9LFxuICB9O1xuICByZXR1cm4gaG9zdDtcbn1cbiIsImltcG9ydCB0eXBlIHsgQW55TW9kZWwsIEV4cGVyaW1lbnRhbCB9IGZyb20gXCJAYW55d2lkZ2V0L3R5cGVzXCI7XG5pbXBvcnQgdHlwZSB7IERPTVdpZGdldE1vZGVsLCBET01XaWRnZXRWaWV3IH0gZnJvbSBcIkBqdXB5dGVyLXdpZGdldHMvYmFzZVwiO1xuaW1wb3J0ICogYXMgc29saWQgZnJvbSBcInNvbGlkLWpzXCI7XG5cbmltcG9ydCB7IEJJTkRJTkdTIH0gZnJvbSBcIi4vYmluZGluZy50c1wiO1xuaW1wb3J0IHsgY3JlYXRlSG9zdCB9IGZyb20gXCIuL2hvc3QudHNcIjtcbmltcG9ydCB7IGludm9rZSB9IGZyb20gXCIuL2ludm9rZS50c1wiO1xuaW1wb3J0IHsgdHlwZSBBbnlXaWRnZXQsIGxvYWRDc3MsIGxvYWRXaWRnZXQgfSBmcm9tIFwiLi9sb2FkLnRzXCI7XG5pbXBvcnQgeyBvYnNlcnZlIH0gZnJvbSBcIi4vb2JzZXJ2ZS50c1wiO1xuaW1wb3J0IHsgYXNzZXJ0LCBwcm9taXNlV2l0aFJlc29sdmVycywgdHlwZSBSZXN1bHQsIHRocm93QW55d2lkZ2V0RXJyb3IgfSBmcm9tIFwiLi91dGlsLnRzXCI7XG5cbmludGVyZmFjZSBTdGF0ZSB7XG4gIFtrZXk6IHN0cmluZ106IHVua25vd247XG4gIF9lc206IHN0cmluZztcbiAgX2FueXdpZGdldF9pZDogc3RyaW5nO1xuICBfY3NzOiBzdHJpbmcgfCB1bmRlZmluZWQ7XG59XG5cbmV4cG9ydCBjbGFzcyBSdW50aW1lIHtcbiAgLy8gQHRzLWV4cGVjdC1lcnJvciAtIFNldCBzeW5jaHJvbm91c2x5IGluIGNvbnN0cnVjdG9yLlxuICAjd2lkZ2V0UmVzdWx0OiBzb2xpZC5BY2Nlc3NvcjxSZXN1bHQ8QW55V2lkZ2V0Pj47XG4gICNzaWduYWw6IEFib3J0U2lnbmFsO1xuICByZWFkeTogUHJvbWlzZTx2b2lkPjtcblxuICBjb25zdHJ1Y3Rvcihtb2RlbDogRE9NV2lkZ2V0TW9kZWwsIG9wdGlvbnM6IHsgc2lnbmFsOiBBYm9ydFNpZ25hbCB9KSB7XG4gICAgbGV0IHJlc29sdmVycyA9IHByb21pc2VXaXRoUmVzb2x2ZXJzPHZvaWQ+KCk7XG4gICAgdGhpcy5yZWFkeSA9IHJlc29sdmVycy5wcm9taXNlO1xuICAgIHRoaXMuI3NpZ25hbCA9IG9wdGlvbnMuc2lnbmFsO1xuICAgIHRoaXMuI3NpZ25hbC50aHJvd0lmQWJvcnRlZCgpO1xuICAgIHRoaXMuI3NpZ25hbC5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4gZGlzcG9zZSgpKTtcbiAgICBBYm9ydFNpZ25hbC50aW1lb3V0KDIwMDApLmFkZEV2ZW50TGlzdGVuZXIoXCJhYm9ydFwiLCAoKSA9PiB7XG4gICAgICByZXNvbHZlcnMucmVqZWN0KG5ldyBFcnJvcihcIlthbnl3aWRnZXRdIEZhaWxlZCB0byBpbml0aWFsaXplIG1vZGVsLlwiKSk7XG4gICAgfSk7XG4gICAgbGV0IGJpbmRpbmcgPSBCSU5ESU5HUy5nZXRPckNyZWF0ZShtb2RlbCk7XG4gICAgbGV0IGV4cGVyaW1lbnRhbDogRXhwZXJpbWVudGFsID0ge1xuICAgICAgLy8gQHRzLWV4cGVjdC1lcnJvciAtIGludm9rZS5iaW5kIGxvc2VzIGdlbmVyaWMgdHlwZSBwYXJhbWV0ZXJcbiAgICAgIGludm9rZTogaW52b2tlLmJpbmQobnVsbCwgbW9kZWwpLFxuICAgIH07XG4gICAgbGV0IGRpc3Bvc2UgPSBzb2xpZC5jcmVhdGVSb290KChkaXNwb3NlKSA9PiB7XG4gICAgICAvLyBET01XaWRnZXRNb2RlbCBpcyB1bnR5cGVkIGJ5IHRyYWl0IHNoYXBlOyB3ZSBrbm93IHRoZSBhbnl3aWRnZXQgdHJhaXRzLCBzbyBuYXJyb3cgdG8gQW55TW9kZWw8U3RhdGU+IGZvciB0eXBlLXNhZmUgYC5nZXQoKWAgYWNjZXNzXG4gICAgICAvLyBveGxpbnQtZGlzYWJsZS1uZXh0LWxpbmUgdHlwZXNjcmlwdC1lc2xpbnQvbm8tdW5zYWZlLXR5cGUtYXNzZXJ0aW9uIC0tIHNlZSBhYm92ZVxuICAgICAgbGV0IHR5cGVkTW9kZWwgPSBtb2RlbCBhcyB1bmtub3duIGFzIEFueU1vZGVsPFN0YXRlPjtcbiAgICAgIGxldCBpZCA9IHR5cGVkTW9kZWwuZ2V0KFwiX2FueXdpZGdldF9pZFwiKTtcbiAgICAgIGxldCBjc3MgPSBvYnNlcnZlKHR5cGVkTW9kZWwsIFwiX2Nzc1wiLCB7IHNpZ25hbDogdGhpcy4jc2lnbmFsIH0pO1xuICAgICAgbGV0IGVzbSA9IG9ic2VydmUodHlwZWRNb2RlbCwgXCJfZXNtXCIsIHsgc2lnbmFsOiB0aGlzLiNzaWduYWwgfSk7XG4gICAgICBsZXQgW3dpZGdldFJlc3VsdCwgc2V0V2lkZ2V0UmVzdWx0XSA9IHNvbGlkLmNyZWF0ZVNpZ25hbDxSZXN1bHQ8QW55V2lkZ2V0Pj4oe1xuICAgICAgICBzdGF0dXM6IFwicGVuZGluZ1wiLFxuICAgICAgfSk7XG4gICAgICB0aGlzLiN3aWRnZXRSZXN1bHQgPSB3aWRnZXRSZXN1bHQ7XG5cbiAgICAgIHNvbGlkLmNyZWF0ZUVmZmVjdChcbiAgICAgICAgc29saWQub24oY3NzLCAoKSA9PiBjb25zb2xlLmRlYnVnKGBbYW55d2lkZ2V0XSBjc3MgaG90IHVwZGF0ZWQ6ICR7aWR9YCksIHsgZGVmZXI6IHRydWUgfSksXG4gICAgICApO1xuICAgICAgc29saWQuY3JlYXRlRWZmZWN0KFxuICAgICAgICBzb2xpZC5vbihlc20sICgpID0+IGNvbnNvbGUuZGVidWcoYFthbnl3aWRnZXRdIGVzbSBob3QgdXBkYXRlZDogJHtpZH1gKSwgeyBkZWZlcjogdHJ1ZSB9KSxcbiAgICAgICk7XG4gICAgICBzb2xpZC5jcmVhdGVFZmZlY3QoKCkgPT4ge1xuICAgICAgICByZXR1cm4gbG9hZENzcyhjc3MoKSwgaWQpO1xuICAgICAgfSk7XG4gICAgICBzb2xpZC5jcmVhdGVFZmZlY3QoKCkgPT4ge1xuICAgICAgICAvLyBQZXItZWZmZWN0IGNvbnRyb2xsZXIgc28gYSBzdGFsZSBsb2FkV2lkZ2V0IHJlc29sdXRpb24gZnJvbSBhXG4gICAgICAgIC8vIHByZXZpb3VzIF9lc20gdmFsdWUgY2Fubm90IG92ZXJ3cml0ZSBhIG5ld2VyIG9uZS4gU29saWQgZmlyZXNcbiAgICAgICAgLy8gb25DbGVhbnVwIGJlZm9yZSByZS1ydW5uaW5nIHRoZSBlZmZlY3QsIGFib3J0aW5nIHRoZSBwcmlvciBsb2FkLlxuICAgICAgICBsZXQgY29udHJvbGxlciA9IG5ldyBBYm9ydENvbnRyb2xsZXIoKTtcbiAgICAgICAgc29saWQub25DbGVhbnVwKCgpID0+IGNvbnRyb2xsZXIuYWJvcnQoKSk7XG4gICAgICAgIGxvYWRXaWRnZXQoZXNtKCksIGlkKVxuICAgICAgICAgIC50aGVuKGFzeW5jICh3aWRnZXQpID0+IHtcbiAgICAgICAgICAgIGlmIChjb250cm9sbGVyLnNpZ25hbC5hYm9ydGVkKSByZXR1cm47XG4gICAgICAgICAgICBhd2FpdCBiaW5kaW5nLmJpbmQod2lkZ2V0LCB7IGV4cGVyaW1lbnRhbCB9KTtcbiAgICAgICAgICAgIGlmIChjb250cm9sbGVyLnNpZ25hbC5hYm9ydGVkKSByZXR1cm47XG4gICAgICAgICAgICBzZXRXaWRnZXRSZXN1bHQoeyBzdGF0dXM6IFwicmVhZHlcIiwgZGF0YTogd2lkZ2V0IH0pO1xuICAgICAgICAgICAgcmVzb2x2ZXJzLnJlc29sdmUoKTtcbiAgICAgICAgICB9KVxuICAgICAgICAgIC5jYXRjaCgoZXJyb3IpID0+IHtcbiAgICAgICAgICAgIGlmIChjb250cm9sbGVyLnNpZ25hbC5hYm9ydGVkKSByZXR1cm47XG4gICAgICAgICAgICBzZXRXaWRnZXRSZXN1bHQoeyBzdGF0dXM6IFwiZXJyb3JcIiwgZXJyb3IgfSk7XG4gICAgICAgICAgfSk7XG4gICAgICB9KTtcblxuICAgICAgcmV0dXJuIGRpc3Bvc2U7XG4gICAgfSk7XG4gIH1cblxuICBhc3luYyBjcmVhdGVWaWV3KHZpZXc6IERPTVdpZGdldFZpZXcsIG9wdGlvbnM6IHsgc2lnbmFsOiBBYm9ydFNpZ25hbCB9KTogUHJvbWlzZTx2b2lkPiB7XG4gICAgbGV0IG1vZGVsID0gdmlldy5tb2RlbDtcbiAgICBsZXQgc2lnbmFsID0gQWJvcnRTaWduYWwuYW55KFt0aGlzLiNzaWduYWwsIG9wdGlvbnMuc2lnbmFsXSk7IC8vIGVpdGhlciBtb2RlbCBvciB2aWV3IGRlc3Ryb3llZFxuICAgIHNpZ25hbC50aHJvd0lmQWJvcnRlZCgpO1xuICAgIHNpZ25hbC5hZGRFdmVudExpc3RlbmVyKFwiYWJvcnRcIiwgKCkgPT4gZGlzcG9zZSgpKTtcbiAgICBsZXQgYmluZGluZyA9IEJJTkRJTkdTLmdldChtb2RlbCk7XG4gICAgYXNzZXJ0KGJpbmRpbmcsIFwiW2FueXdpZGdldF0gV2lkZ2V0QmluZGluZyBub3QgZm91bmQuXCIpO1xuICAgIGxldCBleHBlcmltZW50YWw6IEV4cGVyaW1lbnRhbCA9IHtcbiAgICAgIC8vIEB0cy1leHBlY3QtZXJyb3IgLSBpbnZva2UuYmluZCBsb3NlcyBnZW5lcmljIHR5cGUgcGFyYW1ldGVyXG4gICAgICBpbnZva2U6IGludm9rZS5iaW5kKG51bGwsIG1vZGVsKSxcbiAgICB9O1xuICAgIGxldCBob3N0ID0gY3JlYXRlSG9zdChtb2RlbCwgeyBzaWduYWwgfSk7XG4gICAgbGV0IGRpc3Bvc2UgPSBzb2xpZC5jcmVhdGVSb290KChkaXNwb3NlKSA9PiB7XG4gICAgICBzb2xpZC5jcmVhdGVFZmZlY3QoKCkgPT4ge1xuICAgICAgICAvLyBDbGVhciBhbGwgcHJldmlvdXMgZXZlbnQgbGlzdGVuZXJzIGZyb20gdGhpcyBob29rLlxuICAgICAgICBtb2RlbC5vZmYobnVsbCwgbnVsbCwgdmlldyk7XG4gICAgICAgIHZpZXcuJGVsLmVtcHR5KCk7XG4gICAgICAgIGxldCByZXN1bHQgPSB0aGlzLiN3aWRnZXRSZXN1bHQoKTtcbiAgICAgICAgaWYgKHJlc3VsdC5zdGF0dXMgPT09IFwicGVuZGluZ1wiKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGlmIChyZXN1bHQuc3RhdHVzID09PSBcImVycm9yXCIpIHtcbiAgICAgICAgICB0aHJvd0FueXdpZGdldEVycm9yKHJlc3VsdC5lcnJvcik7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGxldCBjb250cm9sbGVyID0gbmV3IEFib3J0Q29udHJvbGxlcigpO1xuICAgICAgICBzb2xpZC5vbkNsZWFudXAoKCkgPT4gY29udHJvbGxlci5hYm9ydCgpKTtcbiAgICAgICAgUHJvbWlzZS5yZXNvbHZlKClcbiAgICAgICAgICAudGhlbigoKSA9PlxuICAgICAgICAgICAgYmluZGluZy5jcmVhdGVWaWV3KHZpZXcsIHtcbiAgICAgICAgICAgICAgc2lnbmFsOiBBYm9ydFNpZ25hbC5hbnkoW3NpZ25hbCwgY29udHJvbGxlci5zaWduYWxdKSxcbiAgICAgICAgICAgICAgZXhwZXJpbWVudGFsLFxuICAgICAgICAgICAgICBob3N0LFxuICAgICAgICAgICAgfSksXG4gICAgICAgICAgKVxuICAgICAgICAgIC5jYXRjaCgoZXJyb3IpID0+IHRocm93QW55d2lkZ2V0RXJyb3IoZXJyb3IpKTtcbiAgICAgIH0pO1xuICAgICAgcmV0dXJuICgpID0+IGRpc3Bvc2UoKTtcbiAgICB9KTtcbiAgfVxufVxuIiwiaW1wb3J0IHsgQklORElOR1MgfSBmcm9tIFwiLi9iaW5kaW5nLnRzXCI7XG5pbXBvcnQgeyBSdW50aW1lIH0gZnJvbSBcIi4vcnVudGltZS50c1wiO1xuaW1wb3J0IHsgYXNzZXJ0IH0gZnJvbSBcIi4vdXRpbC50c1wiO1xuXG4vLyBAdHMtZXhwZWN0LWVycm9yIC0gaW5qZWN0ZWQgYnkgYnVuZGxlclxubGV0IHZlcnNpb246IHN0cmluZyA9IGdsb2JhbFRoaXMuVkVSU0lPTjtcblxuaW50ZXJmYWNlIFdpZGdldEZhY3RvcnlPcHRpb25zIHtcbiAgRE9NV2lkZ2V0TW9kZWw6IHR5cGVvZiBpbXBvcnQoXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIikuRE9NV2lkZ2V0TW9kZWw7XG4gIERPTVdpZGdldFZpZXc6IHR5cGVvZiBpbXBvcnQoXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIikuRE9NV2lkZ2V0Vmlldztcbn1cblxuaW50ZXJmYWNlIFdpZGdldEZhY3RvcnlSZXN1bHQge1xuICBBbnlNb2RlbDogdHlwZW9mIGltcG9ydChcIkBqdXB5dGVyLXdpZGdldHMvYmFzZVwiKS5ET01XaWRnZXRNb2RlbDtcbiAgQW55VmlldzogdHlwZW9mIGltcG9ydChcIkBqdXB5dGVyLXdpZGdldHMvYmFzZVwiKS5ET01XaWRnZXRWaWV3O1xufVxuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiAoe1xuICBET01XaWRnZXRNb2RlbCxcbiAgRE9NV2lkZ2V0Vmlldyxcbn06IFdpZGdldEZhY3RvcnlPcHRpb25zKTogV2lkZ2V0RmFjdG9yeVJlc3VsdCB7XG4gIGxldCBSVU5USU1FUyA9IG5ldyBXZWFrTWFwPEluc3RhbmNlVHlwZTx0eXBlb2YgRE9NV2lkZ2V0TW9kZWw+LCBSdW50aW1lPigpO1xuXG4gIGNsYXNzIEFueU1vZGVsIGV4dGVuZHMgRE9NV2lkZ2V0TW9kZWwge1xuICAgIHN0YXRpYyBtb2RlbF9uYW1lID0gXCJBbnlNb2RlbFwiO1xuICAgIHN0YXRpYyBtb2RlbF9tb2R1bGUgPSBcImFueXdpZGdldFwiO1xuICAgIHN0YXRpYyBtb2RlbF9tb2R1bGVfdmVyc2lvbiA9IHZlcnNpb247XG5cbiAgICBzdGF0aWMgdmlld19uYW1lID0gXCJBbnlWaWV3XCI7XG4gICAgc3RhdGljIHZpZXdfbW9kdWxlID0gXCJhbnl3aWRnZXRcIjtcbiAgICBzdGF0aWMgdmlld19tb2R1bGVfdmVyc2lvbiA9IHZlcnNpb247XG5cbiAgICBpbml0aWFsaXplKC4uLmFyZ3M6IFBhcmFtZXRlcnM8SW5zdGFuY2VUeXBlPHR5cGVvZiBET01XaWRnZXRNb2RlbD5bXCJpbml0aWFsaXplXCJdPik6IHZvaWQge1xuICAgICAgc3VwZXIuaW5pdGlhbGl6ZSguLi5hcmdzKTtcbiAgICAgIGxldCBjb250cm9sbGVyID0gbmV3IEFib3J0Q29udHJvbGxlcigpO1xuICAgICAgdGhpcy5vbmNlKFwiZGVzdHJveVwiLCAoKSA9PiB7XG4gICAgICAgIGNvbnRyb2xsZXIuYWJvcnQoXCJbYW55d2lkZ2V0XSBSdW50aW1lIGRlc3Ryb3llZC5cIik7XG4gICAgICAgIEJJTkRJTkdTLmRlc3Ryb3kodGhpcyk7XG4gICAgICAgIFJVTlRJTUVTLmRlbGV0ZSh0aGlzKTtcbiAgICAgIH0pO1xuICAgICAgUlVOVElNRVMuc2V0KHRoaXMsIG5ldyBSdW50aW1lKHRoaXMsIHsgc2lnbmFsOiBjb250cm9sbGVyLnNpZ25hbCB9KSk7XG4gICAgfVxuXG4gICAgYXN5bmMgX2hhbmRsZV9jb21tX21zZyhcbiAgICAgIC4uLm1zZzogUGFyYW1ldGVyczxJbnN0YW5jZVR5cGU8dHlwZW9mIERPTVdpZGdldE1vZGVsPltcIl9oYW5kbGVfY29tbV9tc2dcIl0+XG4gICAgKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICBsZXQgcnVudGltZSA9IFJVTlRJTUVTLmdldCh0aGlzKTtcbiAgICAgIGF3YWl0IHJ1bnRpbWU/LnJlYWR5O1xuICAgICAgcmV0dXJuIHN1cGVyLl9oYW5kbGVfY29tbV9tc2coLi4ubXNnKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBXZSBvdmVycmlkZSB0byBzdXBwb3J0IGJpbmFyeSB0cmFpbGV0cyBiZWNhdXNlIEpTT04ucGFyc2UoSlNPTi5zdHJpbmdpZnkoKSlcbiAgICAgKiBkb2VzIG5vdCBwcm9wZXJseSBjbG9uZSBiaW5hcnkgZGF0YSAoaXQganVzdCByZXR1cm5zIGFuIGVtcHR5IG9iamVjdCkuXG4gICAgICpcbiAgICAgKiBodHRwczovL2dpdGh1Yi5jb20vanVweXRlci13aWRnZXRzL2lweXdpZGdldHMvYmxvYi80NzA1OGEzNzNkMmMyYjNhY2YxMDE2NzdiMjc0NWUxNGI3NmRkNzRiL3BhY2thZ2VzL2Jhc2Uvc3JjL3dpZGdldC50cyNMNTYyLUw1ODNcbiAgICAgKi9cbiAgICBzZXJpYWxpemUoc3RhdGU6IFJlY29yZDxzdHJpbmcsIGFueT4pOiBSZWNvcmQ8c3RyaW5nLCBhbnk+IHtcbiAgICAgIC8vIG94bGludC1kaXNhYmxlLW5leHQtbGluZSB0eXBlc2NyaXB0LWVzbGludC9uby11bnNhZmUtdHlwZS1hc3NlcnRpb24gLS0gYWNjZXNzaW5nIHN0YXRpYyBgLnNlcmlhbGl6ZXJzYCBvbiBgdGhpcy5jb25zdHJ1Y3RvcmBcbiAgICAgIGxldCBzZXJpYWxpemVycyA9ICh0aGlzLmNvbnN0cnVjdG9yIGFzIHR5cGVvZiBET01XaWRnZXRNb2RlbCkuc2VyaWFsaXplcnMgfHwge307XG4gICAgICBmb3IgKGxldCBrIG9mIE9iamVjdC5rZXlzKHN0YXRlKSkge1xuICAgICAgICB0cnkge1xuICAgICAgICAgIGxldCBzZXJpYWxpemUgPSBzZXJpYWxpemVyc1trXT8uc2VyaWFsaXplO1xuICAgICAgICAgIGlmIChzZXJpYWxpemUpIHtcbiAgICAgICAgICAgIHN0YXRlW2tdID0gc2VyaWFsaXplKHN0YXRlW2tdLCB0aGlzKTtcbiAgICAgICAgICB9IGVsc2UgaWYgKGsgPT09IFwibGF5b3V0XCIgfHwgayA9PT0gXCJzdHlsZVwiKSB7XG4gICAgICAgICAgICAvLyBUaGVzZSBrZXlzIGNvbWUgZnJvbSBpcHl3aWRnZXRzLCByZWx5IG9uIEpTT04uc3RyaW5naWZ5IHRyaWNrLlxuICAgICAgICAgICAgc3RhdGVba10gPSBKU09OLnBhcnNlKEpTT04uc3RyaW5naWZ5KHN0YXRlW2tdKSk7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHN0YXRlW2tdID0gc3RydWN0dXJlZENsb25lKHN0YXRlW2tdKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgaWYgKHR5cGVvZiBzdGF0ZVtrXT8udG9KU09OID09PSBcImZ1bmN0aW9uXCIpIHtcbiAgICAgICAgICAgIHN0YXRlW2tdID0gc3RhdGVba10udG9KU09OKCk7XG4gICAgICAgICAgfVxuICAgICAgICB9IGNhdGNoIChlKSB7XG4gICAgICAgICAgY29uc29sZS5lcnJvcihcIkVycm9yIHNlcmlhbGl6aW5nIHdpZGdldCBzdGF0ZSBhdHRyaWJ1dGU6IFwiLCBrKTtcbiAgICAgICAgICB0aHJvdyBlO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICByZXR1cm4gc3RhdGU7XG4gICAgfVxuICB9XG5cbiAgY2xhc3MgQW55VmlldyBleHRlbmRzIERPTVdpZGdldFZpZXcge1xuICAgICNjb250cm9sbGVyID0gbmV3IEFib3J0Q29udHJvbGxlcigpO1xuICAgIGFzeW5jIHJlbmRlcigpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgIGxldCBydW50aW1lID0gUlVOVElNRVMuZ2V0KHRoaXMubW9kZWwpO1xuICAgICAgYXNzZXJ0KHJ1bnRpbWUsIFwiW2FueXdpZGdldF0gUnVudGltZSBub3QgZm91bmQuXCIpO1xuICAgICAgYXdhaXQgcnVudGltZS5jcmVhdGVWaWV3KHRoaXMsIHsgc2lnbmFsOiB0aGlzLiNjb250cm9sbGVyLnNpZ25hbCB9KTtcbiAgICB9XG4gICAgcmVtb3ZlKCk6IHZvaWQge1xuICAgICAgdGhpcy4jY29udHJvbGxlci5hYm9ydChcIlthbnl3aWRnZXRdIFZpZXcgZGVzdHJveWVkLlwiKTtcbiAgICAgIHN1cGVyLnJlbW92ZSgpO1xuICAgIH1cbiAgfVxuXG4gIHJldHVybiB7IEFueU1vZGVsLCBBbnlWaWV3IH07XG59XG4iLCJpbXBvcnQgY3JlYXRlIGZyb20gXCIuL3dpZGdldC50c1wiO1xuXG4vLyBAdHMtZXhwZWN0LWVycm9yIC0tIGRlZmluZSBpcyBhIGdsb2JhbCBwcm92aWRlZCBieSB0aGUgbm90ZWJvb2sgcnVudGltZS5cbmRlZmluZShbXCJAanVweXRlci13aWRnZXRzL2Jhc2VcIl0sIGNyZWF0ZSk7XG4iLCJfX3dlYnBhY2tfcmVxdWlyZV9fLm8gPSAob2JqLCBwcm9wKSA9PiAoT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iaiwgcHJvcCkpIiwiX193ZWJwYWNrX3JlcXVpcmVfXy5ydiA9ICgpID0+IChcIjEuNy4xMVwiKSIsIlxuX193ZWJwYWNrX3JlcXVpcmVfXy5TID0ge307XG5fX3dlYnBhY2tfcmVxdWlyZV9fLmluaXRpYWxpemVTaGFyaW5nRGF0YSA9IHsgc2NvcGVUb1NoYXJpbmdEYXRhTWFwcGluZzogeyAgfSwgdW5pcXVlTmFtZTogXCJAYW55d2lkZ2V0L21vbm9yZXBvXCIgfTtcbnZhciBpbml0UHJvbWlzZXMgPSB7fTtcbnZhciBpbml0VG9rZW5zID0ge307XG5fX3dlYnBhY2tfcmVxdWlyZV9fLkkgPSBmdW5jdGlvbihuYW1lLCBpbml0U2NvcGUpIHtcblx0aWYgKCFpbml0U2NvcGUpIGluaXRTY29wZSA9IFtdO1xuXHQvLyBoYW5kbGluZyBjaXJjdWxhciBpbml0IGNhbGxzXG5cdHZhciBpbml0VG9rZW4gPSBpbml0VG9rZW5zW25hbWVdO1xuXHRpZiAoIWluaXRUb2tlbikgaW5pdFRva2VuID0gaW5pdFRva2Vuc1tuYW1lXSA9IHt9O1xuXHRpZiAoaW5pdFNjb3BlLmluZGV4T2YoaW5pdFRva2VuKSA+PSAwKSByZXR1cm47XG5cdGluaXRTY29wZS5wdXNoKGluaXRUb2tlbik7XG5cdC8vIG9ubHkgcnVucyBvbmNlXG5cdGlmIChpbml0UHJvbWlzZXNbbmFtZV0pIHJldHVybiBpbml0UHJvbWlzZXNbbmFtZV07XG5cdC8vIGNyZWF0ZXMgYSBuZXcgc2hhcmUgc2NvcGUgaWYgbmVlZGVkXG5cdGlmICghX193ZWJwYWNrX3JlcXVpcmVfXy5vKF9fd2VicGFja19yZXF1aXJlX18uUywgbmFtZSkpXG5cdFx0X193ZWJwYWNrX3JlcXVpcmVfXy5TW25hbWVdID0ge307XG5cdC8vIHJ1bnMgYWxsIGluaXQgc25pcHBldHMgZnJvbSBhbGwgbW9kdWxlcyByZWFjaGFibGVcblx0dmFyIHNjb3BlID0gX193ZWJwYWNrX3JlcXVpcmVfXy5TW25hbWVdO1xuXHR2YXIgd2FybiA9IGZ1bmN0aW9uIChtc2cpIHtcblx0XHRpZiAodHlwZW9mIGNvbnNvbGUgIT09IFwidW5kZWZpbmVkXCIgJiYgY29uc29sZS53YXJuKSBjb25zb2xlLndhcm4obXNnKTtcblx0fTtcblx0dmFyIHVuaXF1ZU5hbWUgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLmluaXRpYWxpemVTaGFyaW5nRGF0YS51bmlxdWVOYW1lO1xuXHR2YXIgcmVnaXN0ZXIgPSBmdW5jdGlvbiAobmFtZSwgdmVyc2lvbiwgZmFjdG9yeSwgZWFnZXIpIHtcblx0XHR2YXIgdmVyc2lvbnMgPSAoc2NvcGVbbmFtZV0gPSBzY29wZVtuYW1lXSB8fCB7fSk7XG5cdFx0dmFyIGFjdGl2ZVZlcnNpb24gPSB2ZXJzaW9uc1t2ZXJzaW9uXTtcblx0XHRpZiAoXG5cdFx0XHQhYWN0aXZlVmVyc2lvbiB8fFxuXHRcdFx0KCFhY3RpdmVWZXJzaW9uLmxvYWRlZCAmJlxuXHRcdFx0XHQoIWVhZ2VyICE9ICFhY3RpdmVWZXJzaW9uLmVhZ2VyXG5cdFx0XHRcdFx0PyBlYWdlclxuXHRcdFx0XHRcdDogdW5pcXVlTmFtZSA+IGFjdGl2ZVZlcnNpb24uZnJvbSkpXG5cdFx0KVxuXHRcdFx0dmVyc2lvbnNbdmVyc2lvbl0gPSB7IGdldDogZmFjdG9yeSwgZnJvbTogdW5pcXVlTmFtZSwgZWFnZXI6ICEhZWFnZXIgfTtcblx0fTtcblx0dmFyIGluaXRFeHRlcm5hbCA9IGZ1bmN0aW9uIChpZCkge1xuXHRcdHZhciBoYW5kbGVFcnJvciA9IGZ1bmN0aW9uIChlcnIpIHtcblx0XHRcdHdhcm4oXCJJbml0aWFsaXphdGlvbiBvZiBzaGFyaW5nIGV4dGVybmFsIGZhaWxlZDogXCIgKyBlcnIpO1xuXHRcdH07XG5cdFx0dHJ5IHtcblx0XHRcdHZhciBtb2R1bGUgPSBfX3dlYnBhY2tfcmVxdWlyZV9fKGlkKTtcblx0XHRcdGlmICghbW9kdWxlKSByZXR1cm47XG5cdFx0XHR2YXIgaW5pdEZuID0gZnVuY3Rpb24gKG1vZHVsZSkge1xuXHRcdFx0XHRyZXR1cm4gKFxuXHRcdFx0XHRcdG1vZHVsZSAmJlxuXHRcdFx0XHRcdG1vZHVsZS5pbml0ICYmXG5cdFx0XHRcdFx0bW9kdWxlLmluaXQoX193ZWJwYWNrX3JlcXVpcmVfXy5TW25hbWVdLCBpbml0U2NvcGUpXG5cdFx0XHRcdCk7XG5cdFx0XHR9O1xuXHRcdFx0aWYgKG1vZHVsZS50aGVuKSByZXR1cm4gcHJvbWlzZXMucHVzaChtb2R1bGUudGhlbihpbml0Rm4sIGhhbmRsZUVycm9yKSk7XG5cdFx0XHR2YXIgaW5pdFJlc3VsdCA9IGluaXRGbihtb2R1bGUpO1xuXHRcdFx0aWYgKGluaXRSZXN1bHQgJiYgaW5pdFJlc3VsdC50aGVuKVxuXHRcdFx0XHRyZXR1cm4gcHJvbWlzZXMucHVzaChpbml0UmVzdWx0W1wiY2F0Y2hcIl0oaGFuZGxlRXJyb3IpKTtcblx0XHR9IGNhdGNoIChlcnIpIHtcblx0XHRcdGhhbmRsZUVycm9yKGVycik7XG5cdFx0fVxuXHR9O1xuXHR2YXIgcHJvbWlzZXMgPSBbXTtcblx0dmFyIHNjb3BlVG9TaGFyaW5nRGF0YU1hcHBpbmcgPSBfX3dlYnBhY2tfcmVxdWlyZV9fLmluaXRpYWxpemVTaGFyaW5nRGF0YS5zY29wZVRvU2hhcmluZ0RhdGFNYXBwaW5nO1xuXHRpZiAoc2NvcGVUb1NoYXJpbmdEYXRhTWFwcGluZ1tuYW1lXSkge1xuXHRcdHNjb3BlVG9TaGFyaW5nRGF0YU1hcHBpbmdbbmFtZV0uZm9yRWFjaChmdW5jdGlvbiAoc3RhZ2UpIHtcblx0XHRcdGlmICh0eXBlb2Ygc3RhZ2UgPT09IFwib2JqZWN0XCIpIHJlZ2lzdGVyKHN0YWdlLm5hbWUsIHN0YWdlLnZlcnNpb24sIHN0YWdlLmZhY3RvcnksIHN0YWdlLmVhZ2VyKTtcblx0XHRcdGVsc2UgaW5pdEV4dGVybmFsKHN0YWdlKVxuXHRcdH0pO1xuXHR9XG5cdGlmICghcHJvbWlzZXMubGVuZ3RoKSByZXR1cm4gKGluaXRQcm9taXNlc1tuYW1lXSA9IDEpO1xuXHRyZXR1cm4gKGluaXRQcm9taXNlc1tuYW1lXSA9IFByb21pc2UuYWxsKHByb21pc2VzKS50aGVuKGZ1bmN0aW9uICgpIHtcblx0XHRyZXR1cm4gKGluaXRQcm9taXNlc1tuYW1lXSA9IDEpO1xuXHR9KSk7XG59O1xuXG4iLCJcbl9fd2VicGFja19yZXF1aXJlX18uY29uc3VtZXNMb2FkaW5nRGF0YSA9IHsgY2h1bmtNYXBwaW5nOiB7fSwgbW9kdWxlSWRUb0NvbnN1bWVEYXRhTWFwcGluZzoge30sIGluaXRpYWxDb25zdW1lczogW10gfTtcbnZhciBzcGxpdEFuZENvbnZlcnQgPSBmdW5jdGlvbihzdHIpIHtcbiAgcmV0dXJuIHN0ci5zcGxpdChcIi5cIikubWFwKGZ1bmN0aW9uKGl0ZW0pIHtcbiAgICByZXR1cm4gK2l0ZW0gPT0gaXRlbSA/ICtpdGVtIDogaXRlbTtcbiAgfSk7XG59O1xudmFyIHBhcnNlUmFuZ2UgPSBmdW5jdGlvbihzdHIpIHtcbiAgLy8gc2VlIGh0dHBzOi8vZG9jcy5ucG1qcy5jb20vbWlzYy9zZW12ZXIjcmFuZ2UtZ3JhbW1hciBmb3IgZ3JhbW1hclxuICB2YXIgcGFyc2VQYXJ0aWFsID0gZnVuY3Rpb24oc3RyKSB7XG4gICAgdmFyIG1hdGNoID0gL14oW14tK10rKT8oPzotKFteK10rKSk/KD86XFwrKC4rKSk/JC8uZXhlYyhzdHIpO1xuICAgIHZhciB2ZXIgPSBtYXRjaFsxXSA/IFswXS5jb25jYXQoc3BsaXRBbmRDb252ZXJ0KG1hdGNoWzFdKSkgOiBbMF07XG4gICAgaWYgKG1hdGNoWzJdKSB7XG4gICAgICB2ZXIubGVuZ3RoKys7XG4gICAgICB2ZXIucHVzaC5hcHBseSh2ZXIsIHNwbGl0QW5kQ29udmVydChtYXRjaFsyXSkpO1xuICAgIH1cblxuICAgIC8vIHJlbW92ZSB0cmFpbGluZyBhbnkgbWF0Y2hlcnNcbiAgICBsZXQgbGFzdCA9IHZlclt2ZXIubGVuZ3RoIC0gMV07XG4gICAgd2hpbGUgKFxuICAgICAgdmVyLmxlbmd0aCAmJlxuICAgICAgKGxhc3QgPT09IHVuZGVmaW5lZCB8fCAvXlsqeFhdJC8udGVzdCgvKiogQHR5cGUge3N0cmluZ30gKi8gKGxhc3QpKSlcbiAgICApIHtcbiAgICAgIHZlci5wb3AoKTtcbiAgICAgIGxhc3QgPSB2ZXJbdmVyLmxlbmd0aCAtIDFdO1xuICAgIH1cblxuICAgIHJldHVybiB2ZXI7XG4gIH07XG4gIHZhciB0b0ZpeGVkID0gZnVuY3Rpb24ocmFuZ2UpIHtcbiAgICBpZiAocmFuZ2UubGVuZ3RoID09PSAxKSB7XG4gICAgICAvLyBTcGVjaWFsIGNhc2UgZm9yIFwiKlwiIGlzIFwieC54LnhcIiBpbnN0ZWFkIG9mIFwiPVwiXG4gICAgICByZXR1cm4gWzBdO1xuICAgIH0gZWxzZSBpZiAocmFuZ2UubGVuZ3RoID09PSAyKSB7XG4gICAgICAvLyBTcGVjaWFsIGNhc2UgZm9yIFwiMVwiIGlzIFwiMS54LnhcIiBpbnN0ZWFkIG9mIFwiPTFcIlxuICAgICAgcmV0dXJuIFsxXS5jb25jYXQocmFuZ2Uuc2xpY2UoMSkpO1xuICAgIH0gZWxzZSBpZiAocmFuZ2UubGVuZ3RoID09PSAzKSB7XG4gICAgICAvLyBTcGVjaWFsIGNhc2UgZm9yIFwiMS4yXCIgaXMgXCIxLjIueFwiIGluc3RlYWQgb2YgXCI9MS4yXCJcbiAgICAgIHJldHVybiBbMl0uY29uY2F0KHJhbmdlLnNsaWNlKDEpKTtcbiAgICB9IGVsc2Uge1xuICAgICAgcmV0dXJuIFtyYW5nZS5sZW5ndGhdLmNvbmNhdChyYW5nZS5zbGljZSgxKSk7XG4gICAgfVxuICB9O1xuICB2YXIgbmVnYXRlID0gZnVuY3Rpb24ocmFuZ2UpIHtcbiAgICByZXR1cm4gWy1yYW5nZVswXSAtIDFdLmNvbmNhdChyYW5nZS5zbGljZSgxKSk7XG4gIH07XG4gIHZhciBwYXJzZVNpbXBsZSA9IGZ1bmN0aW9uKHN0cikge1xuICAgIC8vIHNpbXBsZSAgICAgICA6Oj0gcHJpbWl0aXZlIHwgcGFydGlhbCB8IHRpbGRlIHwgY2FyZXRcbiAgICAvLyBwcmltaXRpdmUgICAgOjo9ICggJzwnIHwgJz4nIHwgJz49JyB8ICc8PScgfCAnPScgfCAnIScgKSAoICcgJyApICogcGFydGlhbFxuICAgIC8vIHRpbGRlICAgICAgICA6Oj0gJ34nICggJyAnICkgKiBwYXJ0aWFsXG4gICAgLy8gY2FyZXQgICAgICAgIDo6PSAnXicgKCAnICcgKSAqIHBhcnRpYWxcbiAgICBjb25zdCBtYXRjaCA9IC9eKFxcXnx+fDw9fDx8Pj18Pnw9fHZ8ISkvLmV4ZWMoc3RyKTtcbiAgICBjb25zdCBzdGFydCA9IG1hdGNoID8gbWF0Y2hbMF0gOiBcIlwiO1xuICAgIGNvbnN0IHJlbWFpbmRlciA9IHBhcnNlUGFydGlhbChcbiAgICAgIHN0YXJ0Lmxlbmd0aCA/IHN0ci5zbGljZShzdGFydC5sZW5ndGgpLnRyaW0oKSA6IHN0ci50cmltKClcbiAgICApO1xuICAgIHN3aXRjaCAoc3RhcnQpIHtcbiAgICAgIGNhc2UgXCJeXCI6XG4gICAgICAgIGlmIChyZW1haW5kZXIubGVuZ3RoID4gMSAmJiByZW1haW5kZXJbMV0gPT09IDApIHtcbiAgICAgICAgICBpZiAocmVtYWluZGVyLmxlbmd0aCA+IDIgJiYgcmVtYWluZGVyWzJdID09PSAwKSB7XG4gICAgICAgICAgICByZXR1cm4gWzNdLmNvbmNhdChyZW1haW5kZXIuc2xpY2UoMSkpO1xuICAgICAgICAgIH1cbiAgICAgICAgICByZXR1cm4gWzJdLmNvbmNhdChyZW1haW5kZXIuc2xpY2UoMSkpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBbMV0uY29uY2F0KHJlbWFpbmRlci5zbGljZSgxKSk7XG4gICAgICBjYXNlIFwiflwiOlxuICAgICAgICByZXR1cm4gWzJdLmNvbmNhdChyZW1haW5kZXIuc2xpY2UoMSkpO1xuICAgICAgY2FzZSBcIj49XCI6XG4gICAgICAgIHJldHVybiByZW1haW5kZXI7XG4gICAgICBjYXNlIFwiPVwiOlxuICAgICAgY2FzZSBcInZcIjpcbiAgICAgIGNhc2UgXCJcIjpcbiAgICAgICAgcmV0dXJuIHRvRml4ZWQocmVtYWluZGVyKTtcbiAgICAgIGNhc2UgXCI8XCI6XG4gICAgICAgIHJldHVybiBuZWdhdGUocmVtYWluZGVyKTtcbiAgICAgIGNhc2UgXCI+XCI6IHtcbiAgICAgICAgLy8gYW5kKCA+PSwgbm90KCA9ICkgKSA9PiA+PSwgPSwgbm90LCBhbmRcbiAgICAgICAgY29uc3QgZml4ZWQgPSB0b0ZpeGVkKHJlbWFpbmRlcik7XG4gICAgICAgIHJldHVybiBbLCBmaXhlZCwgMCwgcmVtYWluZGVyLCAyXTtcbiAgICAgIH1cbiAgICAgIGNhc2UgXCI8PVwiOlxuICAgICAgICAvLyBvciggPCwgPSApID0+IDwsID0sIG9yXG4gICAgICAgIHJldHVybiBbLCB0b0ZpeGVkKHJlbWFpbmRlciksIG5lZ2F0ZShyZW1haW5kZXIpLCAxXTtcbiAgICAgIGNhc2UgXCIhXCI6IHtcbiAgICAgICAgLy8gbm90ID1cbiAgICAgICAgY29uc3QgZml4ZWQgPSB0b0ZpeGVkKHJlbWFpbmRlcik7XG4gICAgICAgIHJldHVybiBbLCBmaXhlZCwgMF07XG4gICAgICB9XG4gICAgICBkZWZhdWx0OlxuICAgICAgICB0aHJvdyBuZXcgRXJyb3IoXCJVbmV4cGVjdGVkIHN0YXJ0IHZhbHVlXCIpO1xuICAgIH1cbiAgfTtcbiAgdmFyIGNvbWJpbmUgPSBmdW5jdGlvbihpdGVtcywgZm4pIHtcbiAgICBpZiAoaXRlbXMubGVuZ3RoID09PSAxKSByZXR1cm4gaXRlbXNbMF07XG4gICAgY29uc3QgYXJyID0gW107XG4gICAgZm9yIChjb25zdCBpdGVtIG9mIGl0ZW1zLnNsaWNlKCkucmV2ZXJzZSgpKSB7XG4gICAgICBpZiAoMCBpbiBpdGVtKSB7XG4gICAgICAgIGFyci5wdXNoKGl0ZW0pO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgYXJyLnB1c2guYXBwbHkoYXJyLCBpdGVtLnNsaWNlKDEpKTtcbiAgICAgIH1cbiAgICB9XG4gICAgcmV0dXJuIFssXS5jb25jYXQoYXJyLCBpdGVtcy5zbGljZSgxKS5tYXAoKCkgPT4gZm4pKTtcbiAgfTtcbiAgdmFyIHBhcnNlUmFuZ2UgPSBmdW5jdGlvbihzdHIpIHtcbiAgICAvLyByYW5nZSAgICAgIDo6PSBoeXBoZW4gfCBzaW1wbGUgKCAnICcgKCAnICcgKSAqIHNpbXBsZSApICogfCAnJ1xuICAgIC8vIGh5cGhlbiAgICAgOjo9IHBhcnRpYWwgKCAnICcgKSAqICcgLSAnICggJyAnICkgKiBwYXJ0aWFsXG4gICAgY29uc3QgaXRlbXMgPSBzdHIuc3BsaXQoL1xccystXFxzKy8pO1xuICAgIGlmIChpdGVtcy5sZW5ndGggPT09IDEpIHtcblx0XHRcdHN0ciA9IHN0ci50cmltKCk7XG5cdFx0XHRjb25zdCBpdGVtcyA9IFtdO1xuXHRcdFx0Y29uc3QgciA9IC9bLTAtOUEtWmEtel1cXHMrL2c7XG5cdFx0XHR2YXIgc3RhcnQgPSAwO1xuXHRcdFx0dmFyIG1hdGNoO1xuXHRcdFx0d2hpbGUgKChtYXRjaCA9IHIuZXhlYyhzdHIpKSkge1xuXHRcdFx0XHRjb25zdCBlbmQgPSBtYXRjaC5pbmRleCArIDE7XG5cdFx0XHRcdGl0ZW1zLnB1c2gocGFyc2VTaW1wbGUoc3RyLnNsaWNlKHN0YXJ0LCBlbmQpLnRyaW0oKSkpO1xuXHRcdFx0XHRzdGFydCA9IGVuZDtcblx0XHRcdH1cblx0XHRcdGl0ZW1zLnB1c2gocGFyc2VTaW1wbGUoc3RyLnNsaWNlKHN0YXJ0KS50cmltKCkpKTtcbiAgICAgIHJldHVybiBjb21iaW5lKGl0ZW1zLCAyKTtcbiAgICB9XG4gICAgY29uc3QgYSA9IHBhcnNlUGFydGlhbChpdGVtc1swXSk7XG4gICAgY29uc3QgYiA9IHBhcnNlUGFydGlhbChpdGVtc1sxXSk7XG4gICAgLy8gPj1hIDw9YiA9PiBhbmQoID49YSwgb3IoIDxiLCA9YiApICkgPT4gPj1hLCA8YiwgPWIsIG9yLCBhbmRcbiAgICByZXR1cm4gWywgdG9GaXhlZChiKSwgbmVnYXRlKGIpLCAxLCBhLCAyXTtcbiAgfTtcbiAgdmFyIHBhcnNlTG9naWNhbE9yID0gZnVuY3Rpb24oc3RyKSB7XG4gICAgLy8gcmFuZ2Utc2V0ICA6Oj0gcmFuZ2UgKCBsb2dpY2FsLW9yIHJhbmdlICkgKlxuICAgIC8vIGxvZ2ljYWwtb3IgOjo9ICggJyAnICkgKiAnfHwnICggJyAnICkgKlxuICAgIGNvbnN0IGl0ZW1zID0gc3RyLnNwbGl0KC9cXHMqXFx8XFx8XFxzKi8pLm1hcChwYXJzZVJhbmdlKTtcbiAgICByZXR1cm4gY29tYmluZShpdGVtcywgMSk7XG4gIH07XG4gIHJldHVybiBwYXJzZUxvZ2ljYWxPcihzdHIpO1xufTtcbnZhciBwYXJzZVZlcnNpb24gPSBmdW5jdGlvbihzdHIpIHtcblx0dmFyIG1hdGNoID0gL14oW14tK10rKT8oPzotKFteK10rKSk/KD86XFwrKC4rKSk/JC8uZXhlYyhzdHIpO1xuXHQvKiogQHR5cGUgeyhzdHJpbmd8bnVtYmVyfHVuZGVmaW5lZHxbXSlbXX0gKi9cblx0dmFyIHZlciA9IG1hdGNoWzFdID8gc3BsaXRBbmRDb252ZXJ0KG1hdGNoWzFdKSA6IFtdO1xuXHRpZiAobWF0Y2hbMl0pIHtcblx0XHR2ZXIubGVuZ3RoKys7XG5cdFx0dmVyLnB1c2guYXBwbHkodmVyLCBzcGxpdEFuZENvbnZlcnQobWF0Y2hbMl0pKTtcblx0fVxuXHRpZiAobWF0Y2hbM10pIHtcblx0XHR2ZXIucHVzaChbXSk7XG5cdFx0dmVyLnB1c2guYXBwbHkodmVyLCBzcGxpdEFuZENvbnZlcnQobWF0Y2hbM10pKTtcblx0fVxuXHRyZXR1cm4gdmVyO1xufVxudmFyIHZlcnNpb25MdCA9IGZ1bmN0aW9uKGEsIGIpIHtcblx0YSA9IHBhcnNlVmVyc2lvbihhKTtcblx0YiA9IHBhcnNlVmVyc2lvbihiKTtcblx0dmFyIGkgPSAwO1xuXHRmb3IgKDs7KSB7XG5cdFx0Ly8gYSAgICAgICBiICBFT0EgICAgIG9iamVjdCAgdW5kZWZpbmVkICBudW1iZXIgIHN0cmluZ1xuXHRcdC8vIEVPQSAgICAgICAgYSA9PSBiICBhIDwgYiAgIGIgPCBhICAgICAgYSA8IGIgICBhIDwgYlxuXHRcdC8vIG9iamVjdCAgICAgYiA8IGEgICAoMCkgICAgIGIgPCBhICAgICAgYSA8IGIgICBhIDwgYlxuXHRcdC8vIHVuZGVmaW5lZCAgYSA8IGIgICBhIDwgYiAgICgwKSAgICAgICAgYSA8IGIgICBhIDwgYlxuXHRcdC8vIG51bWJlciAgICAgYiA8IGEgICBiIDwgYSAgIGIgPCBhICAgICAgKDEpICAgICBhIDwgYlxuXHRcdC8vIHN0cmluZyAgICAgYiA8IGEgICBiIDwgYSAgIGIgPCBhICAgICAgYiA8IGEgICAoMSlcblx0XHQvLyBFT0EgZW5kIG9mIGFycmF5XG5cdFx0Ly8gKDApIGNvbnRpbnVlIG9uXG5cdFx0Ly8gKDEpIGNvbXBhcmUgdGhlbSB2aWEgXCI8XCJcblxuXHRcdC8vIEhhbmRsZXMgZmlyc3Qgcm93IGluIHRhYmxlXG5cdFx0aWYgKGkgPj0gYS5sZW5ndGgpIHJldHVybiBpIDwgYi5sZW5ndGggJiYgKHR5cGVvZiBiW2ldKVswXSAhPSBcInVcIjtcblxuXHRcdHZhciBhVmFsdWUgPSBhW2ldO1xuXHRcdHZhciBhVHlwZSA9ICh0eXBlb2YgYVZhbHVlKVswXTtcblxuXHRcdC8vIEhhbmRsZXMgZmlyc3QgY29sdW1uIGluIHRhYmxlXG5cdFx0aWYgKGkgPj0gYi5sZW5ndGgpIHJldHVybiBhVHlwZSA9PSBcInVcIjtcblxuXHRcdHZhciBiVmFsdWUgPSBiW2ldO1xuXHRcdHZhciBiVHlwZSA9ICh0eXBlb2YgYlZhbHVlKVswXTtcblxuXHRcdGlmIChhVHlwZSA9PSBiVHlwZSkge1xuXHRcdFx0aWYgKGFUeXBlICE9IFwib1wiICYmIGFUeXBlICE9IFwidVwiICYmIGFWYWx1ZSAhPSBiVmFsdWUpIHtcblx0XHRcdFx0cmV0dXJuIGFWYWx1ZSA8IGJWYWx1ZTtcblx0XHRcdH1cblx0XHRcdGkrKztcblx0XHR9IGVsc2Uge1xuXHRcdFx0Ly8gSGFuZGxlcyByZW1haW5pbmcgY2FzZXNcblx0XHRcdGlmIChhVHlwZSA9PSBcIm9cIiAmJiBiVHlwZSA9PSBcIm5cIikgcmV0dXJuIHRydWU7XG5cdFx0XHRyZXR1cm4gYlR5cGUgPT0gXCJzXCIgfHwgYVR5cGUgPT0gXCJ1XCI7XG5cdFx0fVxuXHR9XG59XG52YXIgcmFuZ2VUb1N0cmluZyA9IGZ1bmN0aW9uKHJhbmdlKSB7XG5cdHZhciBmaXhDb3VudCA9IHJhbmdlWzBdO1xuXHR2YXIgc3RyID0gXCJcIjtcblx0aWYgKHJhbmdlLmxlbmd0aCA9PT0gMSkge1xuXHRcdHJldHVybiBcIipcIjtcblx0fSBlbHNlIGlmIChmaXhDb3VudCArIDAuNSkge1xuXHRcdHN0ciArPVxuXHRcdFx0Zml4Q291bnQgPT0gMFxuXHRcdFx0XHQ/IFwiPj1cIlxuXHRcdFx0XHQ6IGZpeENvdW50ID09IC0xXG5cdFx0XHRcdD8gXCI8XCJcblx0XHRcdFx0OiBmaXhDb3VudCA9PSAxXG5cdFx0XHRcdD8gXCJeXCJcblx0XHRcdFx0OiBmaXhDb3VudCA9PSAyXG5cdFx0XHRcdD8gXCJ+XCJcblx0XHRcdFx0OiBmaXhDb3VudCA+IDBcblx0XHRcdFx0PyBcIj1cIlxuXHRcdFx0XHQ6IFwiIT1cIjtcblx0XHR2YXIgbmVlZERvdCA9IDE7XG5cdFx0Zm9yICh2YXIgaSA9IDE7IGkgPCByYW5nZS5sZW5ndGg7IGkrKykge1xuXHRcdFx0dmFyIGl0ZW0gPSByYW5nZVtpXTtcblx0XHRcdHZhciB0ID0gKHR5cGVvZiBpdGVtKVswXTtcblx0XHRcdG5lZWREb3QtLTtcblx0XHRcdHN0ciArPVxuXHRcdFx0XHR0ID09IFwidVwiXG5cdFx0XHRcdFx0PyAvLyB1bmRlZmluZWQ6IHByZXJlbGVhc2UgbWFya2VyLCBhZGQgYW4gXCItXCJcblx0XHRcdFx0XHQgIFwiLVwiXG5cdFx0XHRcdFx0OiAvLyBudW1iZXIgb3Igc3RyaW5nOiBhZGQgdGhlIGl0ZW0sIHNldCBmbGFnIHRvIGFkZCBhbiBcIi5cIiBiZXR3ZWVuIHR3byBvZiB0aGVtXG5cdFx0XHRcdFx0ICAobmVlZERvdCA+IDAgPyBcIi5cIiA6IFwiXCIpICsgKChuZWVkRG90ID0gMiksIGl0ZW0pO1xuXHRcdH1cblx0XHRyZXR1cm4gc3RyO1xuXHR9IGVsc2Uge1xuXHRcdHZhciBzdGFjayA9IFtdO1xuXHRcdGZvciAodmFyIGkgPSAxOyBpIDwgcmFuZ2UubGVuZ3RoOyBpKyspIHtcblx0XHRcdHZhciBpdGVtID0gcmFuZ2VbaV07XG5cdFx0XHRzdGFjay5wdXNoKFxuXHRcdFx0XHRpdGVtID09PSAwXG5cdFx0XHRcdFx0PyBcIm5vdChcIiArIHBvcCgpICsgXCIpXCJcblx0XHRcdFx0XHQ6IGl0ZW0gPT09IDFcblx0XHRcdFx0XHQ/IFwiKFwiICsgcG9wKCkgKyBcIiB8fCBcIiArIHBvcCgpICsgXCIpXCJcblx0XHRcdFx0XHQ6IGl0ZW0gPT09IDJcblx0XHRcdFx0XHQ/IHN0YWNrLnBvcCgpICsgXCIgXCIgKyBzdGFjay5wb3AoKVxuXHRcdFx0XHRcdDogcmFuZ2VUb1N0cmluZyhpdGVtKVxuXHRcdFx0KTtcblx0XHR9XG5cdFx0cmV0dXJuIHBvcCgpO1xuXHR9XG5cdGZ1bmN0aW9uIHBvcCgpIHtcblx0XHRyZXR1cm4gc3RhY2sucG9wKCkucmVwbGFjZSgvXlxcKCguKylcXCkkLywgXCIkMVwiKTtcblx0fVxufVxudmFyIHNhdGlzZnkgPSBmdW5jdGlvbihyYW5nZSwgdmVyc2lvbikge1xuXHRpZiAoMCBpbiByYW5nZSkge1xuXHRcdHZlcnNpb24gPSBwYXJzZVZlcnNpb24odmVyc2lvbik7XG5cdFx0dmFyIGZpeENvdW50ID0gLyoqIEB0eXBlIHtudW1iZXJ9ICovIChyYW5nZVswXSk7XG5cdFx0Ly8gd2hlbiBuZWdhdGVkIGlzIHNldCBpdCBzd2lsbCBzZXQgZm9yIDwgaW5zdGVhZCBvZiA+PVxuXHRcdHZhciBuZWdhdGVkID0gZml4Q291bnQgPCAwO1xuXHRcdGlmIChuZWdhdGVkKSBmaXhDb3VudCA9IC1maXhDb3VudCAtIDE7XG5cdFx0Zm9yICh2YXIgaSA9IDAsIGogPSAxLCBpc0VxdWFsID0gdHJ1ZTsgOyBqKyssIGkrKykge1xuXHRcdFx0Ly8gY3NwZWxsOndvcmQgbmVxdWFsIG5lcXVcblxuXHRcdFx0Ly8gd2hlbiBpc0VxdWFsID0gdHJ1ZTpcblx0XHRcdC8vIHJhbmdlICAgICAgICAgdmVyc2lvbjogRU9BL29iamVjdCAgdW5kZWZpbmVkICBudW1iZXIgICAgc3RyaW5nXG5cdFx0XHQvLyBFT0EgICAgICAgICAgICAgICAgICAgIGVxdWFsICAgICAgIGJsb2NrICAgICAgYmlnLXZlciAgIGJpZy12ZXJcblx0XHRcdC8vIHVuZGVmaW5lZCAgICAgICAgICAgICAgYmlnZ2VyICAgICAgbmV4dCAgICAgICBiaWctdmVyICAgYmlnLXZlclxuXHRcdFx0Ly8gbnVtYmVyICAgICAgICAgICAgICAgICBzbWFsbGVyICAgICBibG9jayAgICAgIGNtcCAgICAgICBiaWctY21wXG5cdFx0XHQvLyBmaXhlZCBudW1iZXIgICAgICAgICAgIHNtYWxsZXIgICAgIGJsb2NrICAgICAgY21wLWZpeCAgIGRpZmZlclxuXHRcdFx0Ly8gc3RyaW5nICAgICAgICAgICAgICAgICBzbWFsbGVyICAgICBibG9jayAgICAgIGRpZmZlciAgICBjbXBcblx0XHRcdC8vIGZpeGVkIHN0cmluZyAgICAgICAgICAgc21hbGxlciAgICAgYmxvY2sgICAgICBzbWFsbC1jbXAgY21wLWZpeFxuXG5cdFx0XHQvLyB3aGVuIGlzRXF1YWwgPSBmYWxzZTpcblx0XHRcdC8vIHJhbmdlICAgICAgICAgdmVyc2lvbjogRU9BL29iamVjdCAgdW5kZWZpbmVkICBudW1iZXIgICAgc3RyaW5nXG5cdFx0XHQvLyBFT0EgICAgICAgICAgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dC12ZXIgIG5leHQtdmVyXG5cdFx0XHQvLyB1bmRlZmluZWQgICAgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dC12ZXIgIG5leHQtdmVyXG5cdFx0XHQvLyBudW1iZXIgICAgICAgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dCAgICAgIG5leHRcblx0XHRcdC8vIGZpeGVkIG51bWJlciAgICAgICAgICAgbmVxdWFsICAgICAgYmxvY2sgICAgICBuZXh0ICAgICAgbmV4dCAgICh0aGlzIG5ldmVyIGhhcHBlbnMpXG5cdFx0XHQvLyBzdHJpbmcgICAgICAgICAgICAgICAgIG5lcXVhbCAgICAgIGJsb2NrICAgICAgbmV4dCAgICAgIG5leHRcblx0XHRcdC8vIGZpeGVkIHN0cmluZyAgICAgICAgICAgbmVxdWFsICAgICAgYmxvY2sgICAgICBuZXh0ICAgICAgbmV4dCAgICh0aGlzIG5ldmVyIGhhcHBlbnMpXG5cblx0XHRcdC8vIEVPQSBlbmQgb2YgYXJyYXlcblx0XHRcdC8vIGVxdWFsICh2ZXJzaW9uIGlzIGVxdWFsIHJhbmdlKTpcblx0XHRcdC8vICAgd2hlbiAhbmVnYXRlZDogcmV0dXJuIHRydWUsXG5cdFx0XHQvLyAgIHdoZW4gbmVnYXRlZDogcmV0dXJuIGZhbHNlXG5cdFx0XHQvLyBiaWdnZXIgKHZlcnNpb24gaXMgYmlnZ2VyIGFzIHJhbmdlKTpcblx0XHRcdC8vICAgd2hlbiBmaXhlZDogcmV0dXJuIGZhbHNlLFxuXHRcdFx0Ly8gICB3aGVuICFuZWdhdGVkOiByZXR1cm4gdHJ1ZSxcblx0XHRcdC8vICAgd2hlbiBuZWdhdGVkOiByZXR1cm4gZmFsc2UsXG5cdFx0XHQvLyBzbWFsbGVyICh2ZXJzaW9uIGlzIHNtYWxsZXIgYXMgcmFuZ2UpOlxuXHRcdFx0Ly8gICB3aGVuICFuZWdhdGVkOiByZXR1cm4gZmFsc2UsXG5cdFx0XHQvLyAgIHdoZW4gbmVnYXRlZDogcmV0dXJuIHRydWVcblx0XHRcdC8vIG5lcXVhbCAodmVyc2lvbiBpcyBub3QgZXF1YWwgcmFuZ2UgKD4gcmVzcCA8KSk6IHJldHVybiB0cnVlXG5cdFx0XHQvLyBibG9jayAodmVyc2lvbiBpcyBpbiBkaWZmZXJlbnQgcHJlcmVsZWFzZSBhcmVhKTogcmV0dXJuIGZhbHNlXG5cdFx0XHQvLyBkaWZmZXIgKHZlcnNpb24gaXMgZGlmZmVyZW50IGZyb20gZml4ZWQgcmFuZ2UgKHN0cmluZyB2cy4gbnVtYmVyKSk6IHJldHVybiBmYWxzZVxuXHRcdFx0Ly8gbmV4dDogY29udGludWVzIHRvIHRoZSBuZXh0IGl0ZW1zXG5cdFx0XHQvLyBuZXh0LXZlcjogd2hlbiBmaXhlZDogcmV0dXJuIGZhbHNlLCBjb250aW51ZXMgdG8gdGhlIG5leHQgaXRlbSBvbmx5IGZvciB0aGUgdmVyc2lvbiwgc2V0cyBpc0VxdWFsPWZhbHNlXG5cdFx0XHQvLyBiaWctdmVyOiB3aGVuIGZpeGVkIHx8IG5lZ2F0ZWQ6IHJldHVybiBmYWxzZSwgY29udGludWVzIHRvIHRoZSBuZXh0IGl0ZW0gb25seSBmb3IgdGhlIHZlcnNpb24sIHNldHMgaXNFcXVhbD1mYWxzZVxuXHRcdFx0Ly8gbmV4dC1uZXF1OiBjb250aW51ZXMgdG8gdGhlIG5leHQgaXRlbXMsIHNldHMgaXNFcXVhbD1mYWxzZVxuXHRcdFx0Ly8gY21wIChuZWdhdGVkID09PSBmYWxzZSk6IHZlcnNpb24gPCByYW5nZSA9PiByZXR1cm4gZmFsc2UsIHZlcnNpb24gPiByYW5nZSA9PiBuZXh0LW5lcXUsIGVsc2UgPT4gbmV4dFxuXHRcdFx0Ly8gY21wIChuZWdhdGVkID09PSB0cnVlKTogdmVyc2lvbiA+IHJhbmdlID0+IHJldHVybiBmYWxzZSwgdmVyc2lvbiA8IHJhbmdlID0+IG5leHQtbmVxdSwgZWxzZSA9PiBuZXh0XG5cdFx0XHQvLyBjbXAtZml4OiB2ZXJzaW9uID09IHJhbmdlID0+IG5leHQsIGVsc2UgPT4gcmV0dXJuIGZhbHNlXG5cdFx0XHQvLyBiaWctY21wOiB3aGVuIG5lZ2F0ZWQgPT4gcmV0dXJuIGZhbHNlLCBlbHNlID0+IG5leHQtbmVxdVxuXHRcdFx0Ly8gc21hbGwtY21wOiB3aGVuIG5lZ2F0ZWQgPT4gbmV4dC1uZXF1LCBlbHNlID0+IHJldHVybiBmYWxzZVxuXG5cdFx0XHR2YXIgcmFuZ2VUeXBlID0gaiA8IHJhbmdlLmxlbmd0aCA/ICh0eXBlb2YgcmFuZ2Vbal0pWzBdIDogXCJcIjtcblxuXHRcdFx0dmFyIHZlcnNpb25WYWx1ZTtcblx0XHRcdHZhciB2ZXJzaW9uVHlwZTtcblxuXHRcdFx0Ly8gSGFuZGxlcyBmaXJzdCBjb2x1bW4gaW4gYm90aCB0YWJsZXMgKGVuZCBvZiB2ZXJzaW9uIG9yIG9iamVjdClcblx0XHRcdGlmIChcblx0XHRcdFx0aSA+PSB2ZXJzaW9uLmxlbmd0aCB8fFxuXHRcdFx0XHQoKHZlcnNpb25WYWx1ZSA9IHZlcnNpb25baV0pLFxuXHRcdFx0XHQodmVyc2lvblR5cGUgPSAodHlwZW9mIHZlcnNpb25WYWx1ZSlbMF0pID09IFwib1wiKVxuXHRcdFx0KSB7XG5cdFx0XHRcdC8vIEhhbmRsZXMgbmVxdWFsXG5cdFx0XHRcdGlmICghaXNFcXVhbCkgcmV0dXJuIHRydWU7XG5cdFx0XHRcdC8vIEhhbmRsZXMgYmlnZ2VyXG5cdFx0XHRcdGlmIChyYW5nZVR5cGUgPT0gXCJ1XCIpIHJldHVybiBqID4gZml4Q291bnQgJiYgIW5lZ2F0ZWQ7XG5cdFx0XHRcdC8vIEhhbmRsZXMgZXF1YWwgYW5kIHNtYWxsZXI6IChyYW5nZSA9PT0gRU9BKSBYT1IgbmVnYXRlZFxuXHRcdFx0XHRyZXR1cm4gKHJhbmdlVHlwZSA9PSBcIlwiKSAhPSBuZWdhdGVkOyAvLyBlcXVhbCArIHNtYWxsZXJcblx0XHRcdH1cblxuXHRcdFx0Ly8gSGFuZGxlcyBzZWNvbmQgY29sdW1uIGluIGJvdGggdGFibGVzICh2ZXJzaW9uID0gdW5kZWZpbmVkKVxuXHRcdFx0aWYgKHZlcnNpb25UeXBlID09IFwidVwiKSB7XG5cdFx0XHRcdGlmICghaXNFcXVhbCB8fCByYW5nZVR5cGUgIT0gXCJ1XCIpIHtcblx0XHRcdFx0XHRyZXR1cm4gZmFsc2U7XG5cdFx0XHRcdH1cblx0XHRcdH1cblxuXHRcdFx0Ly8gc3dpdGNoIGJldHdlZW4gZmlyc3QgYW5kIHNlY29uZCB0YWJsZVxuXHRcdFx0ZWxzZSBpZiAoaXNFcXVhbCkge1xuXHRcdFx0XHQvLyBIYW5kbGUgZGlhZ29uYWxcblx0XHRcdFx0aWYgKHJhbmdlVHlwZSA9PSB2ZXJzaW9uVHlwZSkge1xuXHRcdFx0XHRcdGlmIChqIDw9IGZpeENvdW50KSB7XG5cdFx0XHRcdFx0XHQvLyBIYW5kbGVzIFwiY21wLWZpeFwiIGNhc2VzXG5cdFx0XHRcdFx0XHRpZiAodmVyc2lvblZhbHVlICE9IHJhbmdlW2pdKSB7XG5cdFx0XHRcdFx0XHRcdHJldHVybiBmYWxzZTtcblx0XHRcdFx0XHRcdH1cblx0XHRcdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHRcdFx0Ly8gSGFuZGxlcyBcImNtcFwiIGNhc2VzXG5cdFx0XHRcdFx0XHRpZiAobmVnYXRlZCA/IHZlcnNpb25WYWx1ZSA+IHJhbmdlW2pdIDogdmVyc2lvblZhbHVlIDwgcmFuZ2Vbal0pIHtcblx0XHRcdFx0XHRcdFx0cmV0dXJuIGZhbHNlO1xuXHRcdFx0XHRcdFx0fVxuXHRcdFx0XHRcdFx0aWYgKHZlcnNpb25WYWx1ZSAhPSByYW5nZVtqXSkgaXNFcXVhbCA9IGZhbHNlO1xuXHRcdFx0XHRcdH1cblx0XHRcdFx0fVxuXG5cdFx0XHRcdC8vIEhhbmRsZSBiaWctdmVyXG5cdFx0XHRcdGVsc2UgaWYgKHJhbmdlVHlwZSAhPSBcInNcIiAmJiByYW5nZVR5cGUgIT0gXCJuXCIpIHtcblx0XHRcdFx0XHRpZiAobmVnYXRlZCB8fCBqIDw9IGZpeENvdW50KSByZXR1cm4gZmFsc2U7XG5cdFx0XHRcdFx0aXNFcXVhbCA9IGZhbHNlO1xuXHRcdFx0XHRcdGotLTtcblx0XHRcdFx0fVxuXG5cdFx0XHRcdC8vIEhhbmRsZSBkaWZmZXIsIGJpZy1jbXAgYW5kIHNtYWxsLWNtcFxuXHRcdFx0XHRlbHNlIGlmIChqIDw9IGZpeENvdW50IHx8IHZlcnNpb25UeXBlIDwgcmFuZ2VUeXBlICE9IG5lZ2F0ZWQpIHtcblx0XHRcdFx0XHRyZXR1cm4gZmFsc2U7XG5cdFx0XHRcdH0gZWxzZSB7XG5cdFx0XHRcdFx0aXNFcXVhbCA9IGZhbHNlO1xuXHRcdFx0XHR9XG5cdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHQvLyBIYW5kbGVzIGFsbCBcIm5leHQtdmVyXCIgY2FzZXMgaW4gdGhlIHNlY29uZCB0YWJsZVxuXHRcdFx0XHRpZiAocmFuZ2VUeXBlICE9IFwic1wiICYmIHJhbmdlVHlwZSAhPSBcIm5cIikge1xuXHRcdFx0XHRcdGlzRXF1YWwgPSBmYWxzZTtcblx0XHRcdFx0XHRqLS07XG5cdFx0XHRcdH1cblxuXHRcdFx0XHQvLyBuZXh0IGlzIGFwcGxpZWQgYnkgZGVmYXVsdFxuXHRcdFx0fVxuXHRcdH1cblx0fVxuXHQvKiogQHR5cGUgeyhib29sZWFuIHwgbnVtYmVyKVtdfSAqL1xuXHR2YXIgc3RhY2sgPSBbXTtcblx0dmFyIHAgPSBzdGFjay5wb3AuYmluZChzdGFjayk7XG5cdGZvciAodmFyIGkgPSAxOyBpIDwgcmFuZ2UubGVuZ3RoOyBpKyspIHtcblx0XHR2YXIgaXRlbSA9IC8qKiBAdHlwZSB7U2VtVmVyUmFuZ2UgfCAwIHwgMSB8IDJ9ICovIChyYW5nZVtpXSk7XG5cdFx0c3RhY2sucHVzaChcblx0XHRcdGl0ZW0gPT0gMVxuXHRcdFx0XHQ/IHAoKSB8IHAoKVxuXHRcdFx0XHQ6IGl0ZW0gPT0gMlxuXHRcdFx0XHQ/IHAoKSAmIHAoKVxuXHRcdFx0XHQ6IGl0ZW1cblx0XHRcdFx0PyBzYXRpc2Z5KGl0ZW0sIHZlcnNpb24pXG5cdFx0XHRcdDogIXAoKVxuXHRcdCk7XG5cdH1cblx0cmV0dXJuICEhcCgpO1xufVxudmFyIGVuc3VyZUV4aXN0ZW5jZSA9IGZ1bmN0aW9uKHNjb3BlTmFtZSwga2V5KSB7XG5cdHZhciBzY29wZSA9IF9fd2VicGFja19yZXF1aXJlX18uU1tzY29wZU5hbWVdO1xuXHRpZighc2NvcGUgfHwgIV9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSkgdGhyb3cgbmV3IEVycm9yKFwiU2hhcmVkIG1vZHVsZSBcIiArIGtleSArIFwiIGRvZXNuJ3QgZXhpc3QgaW4gc2hhcmVkIHNjb3BlIFwiICsgc2NvcGVOYW1lKTtcblx0cmV0dXJuIHNjb3BlO1xufTtcbnZhciBmaW5kVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBrZXkpIHtcblx0dmFyIHZlcnNpb25zID0gc2NvcGVba2V5XTtcblx0dmFyIGtleSA9IE9iamVjdC5rZXlzKHZlcnNpb25zKS5yZWR1Y2UoZnVuY3Rpb24oYSwgYikge1xuXHRcdHJldHVybiAhYSB8fCB2ZXJzaW9uTHQoYSwgYikgPyBiIDogYTtcblx0fSwgMCk7XG5cdHJldHVybiBrZXkgJiYgdmVyc2lvbnNba2V5XVxufTtcbnZhciBmaW5kU2luZ2xldG9uVmVyc2lvbktleSA9IGZ1bmN0aW9uKHNjb3BlLCBrZXkpIHtcblx0dmFyIHZlcnNpb25zID0gc2NvcGVba2V5XTtcblx0cmV0dXJuIE9iamVjdC5rZXlzKHZlcnNpb25zKS5yZWR1Y2UoZnVuY3Rpb24oYSwgYikge1xuXHRcdHJldHVybiAhYSB8fCAoIXZlcnNpb25zW2FdLmxvYWRlZCAmJiB2ZXJzaW9uTHQoYSwgYikpID8gYiA6IGE7XG5cdH0sIDApO1xufTtcbnZhciBnZXRJbnZhbGlkU2luZ2xldG9uVmVyc2lvbk1lc3NhZ2UgPSBmdW5jdGlvbihzY29wZSwga2V5LCB2ZXJzaW9uLCByZXF1aXJlZFZlcnNpb24pIHtcblx0cmV0dXJuIFwiVW5zYXRpc2ZpZWQgdmVyc2lvbiBcIiArIHZlcnNpb24gKyBcIiBmcm9tIFwiICsgKHZlcnNpb24gJiYgc2NvcGVba2V5XVt2ZXJzaW9uXS5mcm9tKSArIFwiIG9mIHNoYXJlZCBzaW5nbGV0b24gbW9kdWxlIFwiICsga2V5ICsgXCIgKHJlcXVpcmVkIFwiICsgcmFuZ2VUb1N0cmluZyhyZXF1aXJlZFZlcnNpb24pICsgXCIpXCJcbn07XG52YXIgZ2V0U2luZ2xldG9uID0gZnVuY3Rpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCByZXF1aXJlZFZlcnNpb24pIHtcblx0dmFyIHZlcnNpb24gPSBmaW5kU2luZ2xldG9uVmVyc2lvbktleShzY29wZSwga2V5KTtcblx0cmV0dXJuIGdldChzY29wZVtrZXldW3ZlcnNpb25dKTtcbn07XG52YXIgZ2V0U2luZ2xldG9uVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciB2ZXJzaW9uID0gZmluZFNpbmdsZXRvblZlcnNpb25LZXkoc2NvcGUsIGtleSk7XG5cdGlmICghc2F0aXNmeShyZXF1aXJlZFZlcnNpb24sIHZlcnNpb24pKSB3YXJuKGdldEludmFsaWRTaW5nbGV0b25WZXJzaW9uTWVzc2FnZShzY29wZSwga2V5LCB2ZXJzaW9uLCByZXF1aXJlZFZlcnNpb24pKTtcblx0cmV0dXJuIGdldChzY29wZVtrZXldW3ZlcnNpb25dKTtcbn07XG52YXIgZ2V0U3RyaWN0U2luZ2xldG9uVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciB2ZXJzaW9uID0gZmluZFNpbmdsZXRvblZlcnNpb25LZXkoc2NvcGUsIGtleSk7XG5cdGlmICghc2F0aXNmeShyZXF1aXJlZFZlcnNpb24sIHZlcnNpb24pKSB0aHJvdyBuZXcgRXJyb3IoZ2V0SW52YWxpZFNpbmdsZXRvblZlcnNpb25NZXNzYWdlKHNjb3BlLCBrZXksIHZlcnNpb24sIHJlcXVpcmVkVmVyc2lvbikpO1xuXHRyZXR1cm4gZ2V0KHNjb3BlW2tleV1bdmVyc2lvbl0pO1xufTtcbnZhciBmaW5kVmFsaWRWZXJzaW9uID0gZnVuY3Rpb24oc2NvcGUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciB2ZXJzaW9ucyA9IHNjb3BlW2tleV07XG5cdHZhciBrZXkgPSBPYmplY3Qua2V5cyh2ZXJzaW9ucykucmVkdWNlKGZ1bmN0aW9uKGEsIGIpIHtcblx0XHRpZiAoIXNhdGlzZnkocmVxdWlyZWRWZXJzaW9uLCBiKSkgcmV0dXJuIGE7XG5cdFx0cmV0dXJuICFhIHx8IHZlcnNpb25MdChhLCBiKSA/IGIgOiBhO1xuXHR9LCAwKTtcblx0cmV0dXJuIGtleSAmJiB2ZXJzaW9uc1trZXldXG59O1xudmFyIGdldEludmFsaWRWZXJzaW9uTWVzc2FnZSA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciB2ZXJzaW9ucyA9IHNjb3BlW2tleV07XG5cdHJldHVybiBcIk5vIHNhdGlzZnlpbmcgdmVyc2lvbiAoXCIgKyByYW5nZVRvU3RyaW5nKHJlcXVpcmVkVmVyc2lvbikgKyBcIikgb2Ygc2hhcmVkIG1vZHVsZSBcIiArIGtleSArIFwiIGZvdW5kIGluIHNoYXJlZCBzY29wZSBcIiArIHNjb3BlTmFtZSArIFwiLlxcblwiICtcblx0XHRcIkF2YWlsYWJsZSB2ZXJzaW9uczogXCIgKyBPYmplY3Qua2V5cyh2ZXJzaW9ucykubWFwKGZ1bmN0aW9uKGtleSkge1xuXHRcdHJldHVybiBrZXkgKyBcIiBmcm9tIFwiICsgdmVyc2lvbnNba2V5XS5mcm9tO1xuXHR9KS5qb2luKFwiLCBcIik7XG59O1xudmFyIGdldFZhbGlkVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHZhciBlbnRyeSA9IGZpbmRWYWxpZFZlcnNpb24oc2NvcGUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKTtcblx0aWYoZW50cnkpIHJldHVybiBnZXQoZW50cnkpO1xuXHR0aHJvdyBuZXcgRXJyb3IoZ2V0SW52YWxpZFZlcnNpb25NZXNzYWdlKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSk7XG59O1xudmFyIHdhcm4gPSBmdW5jdGlvbihtc2cpIHtcblx0aWYgKHR5cGVvZiBjb25zb2xlICE9PSBcInVuZGVmaW5lZFwiICYmIGNvbnNvbGUud2FybikgY29uc29sZS53YXJuKG1zZyk7XG59O1xudmFyIHdhcm5JbnZhbGlkVmVyc2lvbiA9IGZ1bmN0aW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSB7XG5cdHdhcm4oZ2V0SW52YWxpZFZlcnNpb25NZXNzYWdlKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgcmVxdWlyZWRWZXJzaW9uKSk7XG59O1xudmFyIGdldCA9IGZ1bmN0aW9uKGVudHJ5KSB7XG5cdGVudHJ5LmxvYWRlZCA9IDE7XG5cdHJldHVybiBlbnRyeS5nZXQoKVxufTtcbnZhciBpbml0ID0gZnVuY3Rpb24oZm4pIHsgcmV0dXJuIGZ1bmN0aW9uKHNjb3BlTmFtZSwgYSwgYiwgYykge1xuXHR2YXIgcHJvbWlzZSA9IF9fd2VicGFja19yZXF1aXJlX18uSShzY29wZU5hbWUpO1xuXHRpZiAocHJvbWlzZSAmJiBwcm9taXNlLnRoZW4pIHJldHVybiBwcm9taXNlLnRoZW4oZm4uYmluZChmbiwgc2NvcGVOYW1lLCBfX3dlYnBhY2tfcmVxdWlyZV9fLlNbc2NvcGVOYW1lXSwgYSwgYiwgYykpO1xuXHRyZXR1cm4gZm4oc2NvcGVOYW1lLCBfX3dlYnBhY2tfcmVxdWlyZV9fLlNbc2NvcGVOYW1lXSwgYSwgYiwgYyk7XG59OyB9O1xuXG52YXIgbG9hZCA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXkpIHtcblx0ZW5zdXJlRXhpc3RlbmNlKHNjb3BlTmFtZSwga2V5KTtcblx0cmV0dXJuIGdldChmaW5kVmVyc2lvbihzY29wZSwga2V5KSk7XG59KTtcbnZhciBsb2FkRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCBmYWxsYmFjaykge1xuXHRyZXR1cm4gc2NvcGUgJiYgX193ZWJwYWNrX3JlcXVpcmVfXy5vKHNjb3BlLCBrZXkpID8gZ2V0KGZpbmRWZXJzaW9uKHNjb3BlLCBrZXkpKSA6IGZhbGxiYWNrKCk7XG59KTtcbnZhciBsb2FkVmVyc2lvbkNoZWNrID0gLyojX19QVVJFX18qLyBpbml0KGZ1bmN0aW9uKHNjb3BlTmFtZSwgc2NvcGUsIGtleSwgdmVyc2lvbikge1xuXHRlbnN1cmVFeGlzdGVuY2Uoc2NvcGVOYW1lLCBrZXkpO1xuXHRyZXR1cm4gZ2V0KGZpbmRWYWxpZFZlcnNpb24oc2NvcGUsIGtleSwgdmVyc2lvbikgfHwgd2FybkludmFsaWRWZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbikgfHwgZmluZFZlcnNpb24oc2NvcGUsIGtleSkpO1xufSk7XG52YXIgbG9hZFNpbmdsZXRvbiA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXkpIHtcblx0ZW5zdXJlRXhpc3RlbmNlKHNjb3BlTmFtZSwga2V5KTtcblx0cmV0dXJuIGdldFNpbmdsZXRvbihzY29wZSwgc2NvcGVOYW1lLCBrZXkpO1xufSk7XG52YXIgbG9hZFNpbmdsZXRvblZlcnNpb25DaGVjayA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXksIHZlcnNpb24pIHtcblx0ZW5zdXJlRXhpc3RlbmNlKHNjb3BlTmFtZSwga2V5KTtcblx0cmV0dXJuIGdldFNpbmdsZXRvblZlcnNpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCB2ZXJzaW9uKTtcbn0pO1xudmFyIGxvYWRTdHJpY3RWZXJzaW9uQ2hlY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uKSB7XG5cdGVuc3VyZUV4aXN0ZW5jZShzY29wZU5hbWUsIGtleSk7XG5cdHJldHVybiBnZXRWYWxpZFZlcnNpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCB2ZXJzaW9uKTtcbn0pO1xudmFyIGxvYWRTdHJpY3RTaW5nbGV0b25WZXJzaW9uQ2hlY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uKSB7XG5cdGVuc3VyZUV4aXN0ZW5jZShzY29wZU5hbWUsIGtleSk7XG5cdHJldHVybiBnZXRTdHJpY3RTaW5nbGV0b25WZXJzaW9uKHNjb3BlLCBzY29wZU5hbWUsIGtleSwgdmVyc2lvbik7XG59KTtcbnZhciBsb2FkVmVyc2lvbkNoZWNrRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCB2ZXJzaW9uLCBmYWxsYmFjaykge1xuXHRpZighc2NvcGUgfHwgIV9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSkgcmV0dXJuIGZhbGxiYWNrKCk7XG5cdHJldHVybiBnZXQoZmluZFZhbGlkVmVyc2lvbihzY29wZSwga2V5LCB2ZXJzaW9uKSB8fCB3YXJuSW52YWxpZFZlcnNpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCB2ZXJzaW9uKSB8fCBmaW5kVmVyc2lvbihzY29wZSwga2V5KSk7XG59KTtcbnZhciBsb2FkU2luZ2xldG9uRmFsbGJhY2sgPSAvKiNfX1BVUkVfXyovIGluaXQoZnVuY3Rpb24oc2NvcGVOYW1lLCBzY29wZSwga2V5LCBmYWxsYmFjaykge1xuXHRpZighc2NvcGUgfHwgIV9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSkgcmV0dXJuIGZhbGxiYWNrKCk7XG5cdHJldHVybiBnZXRTaW5nbGV0b24oc2NvcGUsIHNjb3BlTmFtZSwga2V5KTtcbn0pO1xudmFyIGxvYWRTaW5nbGV0b25WZXJzaW9uQ2hlY2tGYWxsYmFjayA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXksIHZlcnNpb24sIGZhbGxiYWNrKSB7XG5cdGlmKCFzY29wZSB8fCAhX193ZWJwYWNrX3JlcXVpcmVfXy5vKHNjb3BlLCBrZXkpKSByZXR1cm4gZmFsbGJhY2soKTtcblx0cmV0dXJuIGdldFNpbmdsZXRvblZlcnNpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCB2ZXJzaW9uKTtcbn0pO1xudmFyIGxvYWRTdHJpY3RWZXJzaW9uQ2hlY2tGYWxsYmFjayA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXksIHZlcnNpb24sIGZhbGxiYWNrKSB7XG5cdHZhciBlbnRyeSA9IHNjb3BlICYmIF9fd2VicGFja19yZXF1aXJlX18ubyhzY29wZSwga2V5KSAmJiBmaW5kVmFsaWRWZXJzaW9uKHNjb3BlLCBrZXksIHZlcnNpb24pO1xuXHRyZXR1cm4gZW50cnkgPyBnZXQoZW50cnkpIDogZmFsbGJhY2soKTtcbn0pO1xudmFyIGxvYWRTdHJpY3RTaW5nbGV0b25WZXJzaW9uQ2hlY2tGYWxsYmFjayA9IC8qI19fUFVSRV9fKi8gaW5pdChmdW5jdGlvbihzY29wZU5hbWUsIHNjb3BlLCBrZXksIHZlcnNpb24sIGZhbGxiYWNrKSB7XG5cdGlmKCFzY29wZSB8fCAhX193ZWJwYWNrX3JlcXVpcmVfXy5vKHNjb3BlLCBrZXkpKSByZXR1cm4gZmFsbGJhY2soKTtcblx0cmV0dXJuIGdldFN0cmljdFNpbmdsZXRvblZlcnNpb24oc2NvcGUsIHNjb3BlTmFtZSwga2V5LCB2ZXJzaW9uKTtcbn0pO1xudmFyIHJlc29sdmVIYW5kbGVyID0gZnVuY3Rpb24oZGF0YSkge1xuXHR2YXIgc3RyaWN0ID0gZmFsc2Vcblx0dmFyIHNpbmdsZXRvbiA9IGZhbHNlXG5cdHZhciB2ZXJzaW9uQ2hlY2sgPSBmYWxzZVxuXHR2YXIgZmFsbGJhY2sgPSBmYWxzZVxuXHR2YXIgYXJncyA9IFtkYXRhLnNoYXJlU2NvcGUsIGRhdGEuc2hhcmVLZXldO1xuXHRpZiAoZGF0YS5yZXF1aXJlZFZlcnNpb24pIHtcblx0XHRpZiAoZGF0YS5zdHJpY3RWZXJzaW9uKSBzdHJpY3QgPSB0cnVlO1xuXHRcdGlmIChkYXRhLnNpbmdsZXRvbikgc2luZ2xldG9uID0gdHJ1ZTtcblx0XHRhcmdzLnB1c2gocGFyc2VSYW5nZShkYXRhLnJlcXVpcmVkVmVyc2lvbikpO1xuXHRcdHZlcnNpb25DaGVjayA9IHRydWVcblx0fSBlbHNlIGlmIChkYXRhLnNpbmdsZXRvbikgc2luZ2xldG9uID0gdHJ1ZTtcblx0aWYgKGRhdGEuZmFsbGJhY2spIHtcblx0XHRmYWxsYmFjayA9IHRydWU7XG5cdFx0YXJncy5wdXNoKGRhdGEuZmFsbGJhY2spO1xuXHR9XG5cdGlmIChzdHJpY3QgJiYgc2luZ2xldG9uICYmIHZlcnNpb25DaGVjayAmJiBmYWxsYmFjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFN0cmljdFNpbmdsZXRvblZlcnNpb25DaGVja0ZhbGxiYWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmIChzdHJpY3QgJiYgdmVyc2lvbkNoZWNrICYmIGZhbGxiYWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkU3RyaWN0VmVyc2lvbkNoZWNrRmFsbGJhY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHNpbmdsZXRvbiAmJiB2ZXJzaW9uQ2hlY2sgJiYgZmFsbGJhY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTaW5nbGV0b25WZXJzaW9uQ2hlY2tGYWxsYmFjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAoc3RyaWN0ICYmIHNpbmdsZXRvbiAmJiB2ZXJzaW9uQ2hlY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRTdHJpY3RTaW5nbGV0b25WZXJzaW9uQ2hlY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKHNpbmdsZXRvbiAmJiBmYWxsYmFjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFNpbmdsZXRvbkZhbGxiYWNrLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmICh2ZXJzaW9uQ2hlY2sgJiYgZmFsbGJhY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRWZXJzaW9uQ2hlY2tGYWxsYmFjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAoc3RyaWN0ICYmIHZlcnNpb25DaGVjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFN0cmljdFZlcnNpb25DaGVjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAoc2luZ2xldG9uICYmIHZlcnNpb25DaGVjaykgcmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZFNpbmdsZXRvblZlcnNpb25DaGVjay5hcHBseShudWxsLCBhcmdzKTsgfVxuXHRpZiAoc2luZ2xldG9uKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkU2luZ2xldG9uLmFwcGx5KG51bGwsIGFyZ3MpOyB9XG5cdGlmICh2ZXJzaW9uQ2hlY2spIHJldHVybiBmdW5jdGlvbigpIHsgcmV0dXJuIGxvYWRWZXJzaW9uQ2hlY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0aWYgKGZhbGxiYWNrKSByZXR1cm4gZnVuY3Rpb24oKSB7IHJldHVybiBsb2FkRmFsbGJhY2suYXBwbHkobnVsbCwgYXJncyk7IH1cblx0cmV0dXJuIGZ1bmN0aW9uKCkgeyByZXR1cm4gbG9hZC5hcHBseShudWxsLCBhcmdzKTsgfVxufTtcbnZhciBpbnN0YWxsZWRNb2R1bGVzID0ge307XG4iLCJfX3dlYnBhY2tfcmVxdWlyZV9fLnJ1aWQgPSBcImJ1bmRsZXI9cnNwYWNrQDEuNy4xMVwiOyJdLCJuYW1lcyI6WyJJTklUSUFMSVpFX01BUktFUiIsIlN5bWJvbCIsIm1vZGVsUHJveHkiLCJtb2RlbCIsImNvbnRleHQiLCJvbiIsIm5hbWUiLCJjYWxsYmFjayIsIm9mZiIsImFzc2VydCIsImNvbmRpdGlvbiIsIm1lc3NhZ2UiLCJFcnJvciIsInNhZmVDbGVhbnVwIiwiZm4iLCJraW5kIiwiUHJvbWlzZSIsImUiLCJjb25zb2xlIiwidGhyb3dBbnl3aWRnZXRFcnJvciIsInNvdXJjZSIsIl9zb3VyY2Vfc3RhY2siLCJfaW5zdGFuY2VvZiIsImxpbmVzIiwiYW55d2lkZ2V0SW5kZXgiLCJsaW5lIiwiY2xlYW5TdGFjayIsInByb21pc2VXaXRoUmVzb2x2ZXJzIiwicmVzb2x2ZSIsInJlamVjdCIsInByb21pc2UiLCJyZXMiLCJyZWoiLCJpc1NhZmVDbGVhbnVwRnVuY3Rpb24iLCJ4IiwiX2NvbnRyb2xsZXIiLCJfd2lkZ2V0RGVmIiwiX2V4cG9ydHMiLCJfbW9kZWwiLCJfcmVzb2x2ZXJzIiwiV2lkZ2V0QmluZGluZyIsImJpbmQiLCJ3aWRnZXREZWYiLCJwYXJhbSIsImV4cGVyaW1lbnRhbCIsInByZXZSZXNvbHZlcnMiLCJzaWduYWwiLCJyZXN1bHQiLCJBYm9ydENvbnRyb2xsZXIiLCJ1bmRlZmluZWQiLCJfdHlwZV9vZiIsImNyZWF0ZVZpZXciLCJ0YXJnZXQiLCJob3N0IiwiY29udHJvbGxlciIsImNvbWJpbmVkIiwiY2xlYW51cCIsImRpc3Bvc2VWaWV3IiwiQWJvcnRTaWduYWwiLCJyZWFzb24iLCJkZXN0cm95IiwiX2JpbmRpbmdzIiwiQmluZGluZ01hbmFnZXIiLCJNYXAiLCJnZXRPckNyZWF0ZSIsImJpbmRpbmciLCJnZXQiLCJCSU5ESU5HUyIsInV1aWQiLCJpbnZva2UiLCJtc2ciLCJvcHRpb25zIiwiX29wdGlvbnNfc2lnbmFsIiwiaWQiLCJfb3B0aW9uc19idWZmZXJzIiwiaGFuZGxlciIsImJ1ZmZlcnMiLCJwYXJzZVdpZGdldFJlZiIsImNyZWF0ZUhvc3QiLCJnZXRNb2RlbCIsInJlZiIsIm1vZGVsSWQiLCJjaGlsZE1vZGVsIiwiZ2V0V2lkZ2V0IiwiY2hpbGRCaW5kaW5nIiwidGltZXIiLCJleHBvcnRzIiwic2V0VGltZW91dCIsImNsZWFyVGltZW91dCIsInJlbmRlciIsImVsIiwidmlld1NpZ25hbCIsImNoaWxkVmlld1NpZ25hbCIsInNvbGlkIiwibG9hZENzcyIsImxvYWRXaWRnZXQiLCJvYnNlcnZlIiwiX3dpZGdldFJlc3VsdCIsIl9zaWduYWwiLCJSdW50aW1lIiwicmVzb2x2ZXJzIiwiZGlzcG9zZSIsInR5cGVkTW9kZWwiLCJjc3MiLCJlc20iLCJfc29saWRfY3JlYXRlU2lnbmFsIiwid2lkZ2V0UmVzdWx0Iiwic2V0V2lkZ2V0UmVzdWx0Iiwid2lkZ2V0IiwiZXJyb3IiLCJ2aWV3IiwidmVyc2lvbiIsImdsb2JhbFRoaXMiLCJET01XaWRnZXRNb2RlbCIsIkRPTVdpZGdldFZpZXciLCJSVU5USU1FUyIsIldlYWtNYXAiLCJBbnlNb2RlbCIsImluaXRpYWxpemUiLCJfa2V5IiwiYXJncyIsIl8kX2dldCIsIl9oYW5kbGVfY29tbV9tc2ciLCJfc3VwZXJwcm9wX2dldF9faGFuZGxlX2NvbW1fbXNnMSIsInJ1bnRpbWUiLCJzZXJpYWxpemUiLCJzdGF0ZSIsInNlcmlhbGl6ZXJzIiwiX2l0ZXJhdG9yRXJyb3IiLCJPYmplY3QiLCJrIiwiX3NlcmlhbGl6ZXJzX2siLCJfc3RhdGVfayIsIkpTT04iLCJzdHJ1Y3R1cmVkQ2xvbmUiLCJBbnlWaWV3IiwicmVtb3ZlIl0sIm1hcHBpbmdzIjoiOzs7Ozs7QUFHQTs7O0NBR0MsR0FDTSxJQUFJQSxvQkFBb0JDLE9BQU8sd0JBQXdCO0FBRTlEOzs7Ozs7Q0FNQyxHQUNNLFNBQVNDLHNCQUFVQSxDQUFDQyxLQUFxQixFQUFFQyxPQUFnQjtJQUNoRSx5TkFBeU47SUFDek4sT0FBTztRQUNMLEtBQUtELE1BQU0sR0FBRyxDQUFDLElBQUksQ0FBQ0E7UUFDcEIsS0FBS0EsTUFBTSxHQUFHLENBQUMsSUFBSSxDQUFDQTtRQUNwQixjQUFjQSxNQUFNLFlBQVksQ0FBQyxJQUFJLENBQUNBO1FBQ3RDLE1BQU1BLE1BQU0sSUFBSSxDQUFDLElBQUksQ0FBQ0E7UUFDdEJFLElBQUFBLFNBQUFBLEdBQUdDLElBQUksRUFBRUMsUUFBUTtZQUNmSixNQUFNLEVBQUUsQ0FBQ0csTUFBTUMsVUFBVUg7UUFDM0I7UUFDQUksS0FBQUEsU0FBQUEsSUFBSUYsSUFBSSxFQUFFQyxRQUFRO1lBQ2hCSixNQUFNLEdBQUcsQ0FBQ0csTUFBTUMsVUFBVUg7UUFDNUI7UUFDQSxrRUFBa0U7UUFDbEUseUVBQXlFO1FBQ3pFLDBDQUEwQztRQUMxQyxnQkFBZ0JELE1BQU0sY0FBYztJQUN0QztBQUNGOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7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QUNwRUEsNENBQTRDLGdCQUFnQixrQ0FBa0M7QUFDOUY7QUFDQTtBQUNBO0FBQ0EsR0FBRztBQUNIO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsdURBQXVELFFBQVE7QUFDL0Q7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsTUFBTTtBQUNOO0FBQ0E7QUFDQSxNQUFNO0FBQ047QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsWUFBWSxnQ0FBZ0M7QUFDNUM7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsUUFBUTtBQUNSO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGtCQUFrQixrQkFBa0I7QUFDcEM7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBLGtCQUFrQixrQkFBa0I7QUFDcEM7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDRCQUE0QixRQUFRO0FBQ3BDO0FBQ0E7QUFDQTtBQUNBLDJDQUEyQztBQUMzQzs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSx5Q0FBeUM7QUFDekM7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE9BQU87QUFDUDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0EsTUFBTTtBQUNOO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFlBQVksc0JBQXNCO0FBQ2xDO0FBQ0E7QUFDQSxpQkFBaUIsa0JBQWtCO0FBQ25DLHdCQUF3Qix5QkFBeUI7QUFDakQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsRUFBRTtBQUNGO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEVBQUU7QUFDRjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsRUFBRTtBQUNGO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsRUFBRTtBQUNGO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsMEJBQTBCO0FBQzFCO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxDQUFDO0FBQ0Q7QUFDQTtBQUNBO0FBQ0EsQ0FBQztBQUNEO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsR0FBRztBQUNIO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsMEVBQTBFO0FBQzFFLDZEQUE2RDtBQUM3RCxnRUFBZ0U7QUFDaEUsOERBQThEO0FBQzlELGdEQUFnRDtBQUNoRCxtREFBbUQ7QUFDbkQsaURBQWlEO0FBQ2pELG9EQUFvRDtBQUNwRCxvQ0FBb0M7QUFDcEMsdUNBQXVDO0FBQ3ZDLG1DQUFtQztBQUNuQyxxQkFBcUI7QUFDckI7QUFDQTs7Ozs7QUMzZ0JBLG1EIn0=