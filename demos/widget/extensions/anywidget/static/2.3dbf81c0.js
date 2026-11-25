"use strict";
(self["webpackChunk_anywidget_monorepo"] = self["webpackChunk_anywidget_monorepo"] || []).push([["2"], {
661(__unused_rspack___webpack_module__, __webpack_exports__, __webpack_require__) {
__webpack_require__.d(__webpack_exports__, {
  v4: () => (v4)
});
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


},
621(__unused_rspack___webpack_module__, __webpack_exports__, __webpack_require__) {
__webpack_require__.d(__webpack_exports__, {
  EH: () => (createEffect),
  Hr: () => (createRoot),
  Ki: () => (onCleanup),
  n5: () => (createSignal),
  on: () => (on)
});
let taskIdCounter = 1,
  isCallbackScheduled = false,
  isPerformingWork = false,
  taskQueue = (/* unused pure expression or super */ null && ([])),
  currentTask = null,
  shouldYieldToHost = null,
  yieldInterval = 5,
  deadline = 0,
  maxYieldInterval = 300,
  maxDeadline = 0,
  scheduleCallback = null,
  scheduledCallback = null;
const maxSigned31BitInt = 1073741823;
function setupScheduler() {
  const channel = new MessageChannel(),
    port1 = channel.port1,
    port = channel.port2;
  if (typeof port1.unref === "function") port1.unref();
  if (typeof port.unref === "function") port.unref();
  scheduleCallback = () => port.postMessage(null);
  port1.onmessage = () => {
    if (scheduledCallback !== null) {
      const currentTime = performance.now();
      deadline = currentTime + yieldInterval;
      maxDeadline = currentTime + maxYieldInterval;
      try {
        const hasMoreWork = scheduledCallback(currentTime);
        if (!hasMoreWork) {
          scheduledCallback = null;
        } else port.postMessage(null);
      } catch (error) {
        port.postMessage(null);
        throw error;
      }
    }
  };
  if (navigator && navigator.scheduling && navigator.scheduling.isInputPending) {
    const scheduling = navigator.scheduling;
    shouldYieldToHost = () => {
      const currentTime = performance.now();
      if (currentTime >= deadline) {
        if (scheduling.isInputPending()) {
          return true;
        }
        return currentTime >= maxDeadline;
      } else {
        return false;
      }
    };
  } else {
    shouldYieldToHost = () => performance.now() >= deadline;
  }
}
function enqueue(taskQueue, task) {
  function findIndex() {
    let m = 0;
    let n = taskQueue.length - 1;
    while (m <= n) {
      const k = n + m >> 1;
      const cmp = task.expirationTime - taskQueue[k].expirationTime;
      if (cmp > 0) m = k + 1;else if (cmp < 0) n = k - 1;else return k;
    }
    return m;
  }
  taskQueue.splice(findIndex(), 0, task);
}
function requestCallback(fn, options) {
  if (!scheduleCallback) setupScheduler();
  let startTime = performance.now(),
    timeout = maxSigned31BitInt;
  if (options && options.timeout) timeout = options.timeout;
  const newTask = {
    id: taskIdCounter++,
    fn,
    startTime,
    expirationTime: startTime + timeout
  };
  enqueue(taskQueue, newTask);
  if (!isCallbackScheduled && !isPerformingWork) {
    isCallbackScheduled = true;
    scheduledCallback = flushWork;
    scheduleCallback();
  }
  return newTask;
}
function cancelCallback(task) {
  task.fn = null;
}
function flushWork(initialTime) {
  isCallbackScheduled = false;
  isPerformingWork = true;
  try {
    return workLoop(initialTime);
  } finally {
    currentTask = null;
    isPerformingWork = false;
  }
}
function workLoop(initialTime) {
  let currentTime = initialTime;
  currentTask = taskQueue[0] || null;
  while (currentTask !== null) {
    if (currentTask.expirationTime > currentTime && shouldYieldToHost()) {
      break;
    }
    const callback = currentTask.fn;
    if (callback !== null) {
      currentTask.fn = null;
      const didUserCallbackTimeout = currentTask.expirationTime <= currentTime;
      callback(didUserCallbackTimeout);
      currentTime = performance.now();
      if (currentTask === taskQueue[0]) {
        taskQueue.shift();
      }
    } else taskQueue.shift();
    currentTask = taskQueue[0] || null;
  }
  return currentTask !== null;
}

const sharedConfig = {
  context: undefined,
  registry: undefined,
  effects: undefined,
  done: false,
  getContextId() {
    return getContextId(this.context.count);
  },
  getNextContextId() {
    return getContextId(this.context.count++);
  }
};
function getContextId(count) {
  const num = String(count),
    len = num.length - 1;
  return sharedConfig.context.id + (len ? String.fromCharCode(96 + len) : "") + num;
}
function setHydrateContext(context) {
  sharedConfig.context = context;
}
function nextHydrateContext() {
  return {
    ...sharedConfig.context,
    id: sharedConfig.getNextContextId(),
    count: 0
  };
}

const IS_DEV = false;
const equalFn = (a, b) => a === b;
const $PROXY = Symbol("solid-proxy");
const SUPPORTS_PROXY = (/* unused pure expression or super */ null && (typeof Proxy === "function"));
const $TRACK = Symbol("solid-track");
const $DEVCOMP = Symbol("solid-dev-component");
const signalOptions = {
  equals: equalFn
};
let ERROR = null;
let runEffects = runQueue;
const STALE = 1;
const PENDING = 2;
const UNOWNED = {
  owned: null,
  cleanups: null,
  context: null,
  owner: null
};
const NO_INIT = (/* unused pure expression or super */ null && ({}));
var Owner = null;
let Transition = null;
let Scheduler = null;
let ExternalSourceConfig = null;
let Listener = null;
let Updates = null;
let Effects = null;
let ExecCount = 0;
function createRoot(fn, detachedOwner) {
  const listener = Listener,
    owner = Owner,
    unowned = fn.length === 0,
    current = detachedOwner === undefined ? owner : detachedOwner,
    root = unowned ? UNOWNED : {
      owned: null,
      cleanups: null,
      context: current ? current.context : null,
      owner: current
    },
    updateFn = unowned ? fn : () => fn(() => untrack(() => cleanNode(root)));
  Owner = root;
  Listener = null;
  try {
    return runUpdates(updateFn, true);
  } finally {
    Listener = listener;
    Owner = owner;
  }
}
function createSignal(value, options) {
  options = options ? Object.assign({}, signalOptions, options) : signalOptions;
  const s = {
    value,
    observers: null,
    observerSlots: null,
    comparator: options.equals || undefined
  };
  const setter = value => {
    if (typeof value === "function") {
      if (Transition && Transition.running && Transition.sources.has(s)) value = value(s.tValue);else value = value(s.value);
    }
    return writeSignal(s, value);
  };
  return [readSignal.bind(s), setter];
}
function createComputed(fn, value, options) {
  const c = createComputation(fn, value, true, STALE);
  if (Scheduler && Transition && Transition.running) Updates.push(c);else updateComputation(c);
}
function createRenderEffect(fn, value, options) {
  const c = createComputation(fn, value, false, STALE);
  if (Scheduler && Transition && Transition.running) Updates.push(c);else updateComputation(c);
}
function createEffect(fn, value, options) {
  runEffects = runUserEffects;
  const c = createComputation(fn, value, false, STALE),
    s = SuspenseContext && useContext(SuspenseContext);
  if (s) c.suspense = s;
  if (!options || !options.render) c.user = true;
  Effects ? Effects.push(c) : updateComputation(c);
}
function createReaction(onInvalidate, options) {
  let fn;
  const c = createComputation(() => {
      fn ? fn() : untrack(onInvalidate);
      fn = undefined;
    }, undefined, false, 0),
    s = SuspenseContext && useContext(SuspenseContext);
  if (s) c.suspense = s;
  c.user = true;
  return tracking => {
    fn = tracking;
    updateComputation(c);
  };
}
function createMemo(fn, value, options) {
  options = options ? Object.assign({}, signalOptions, options) : signalOptions;
  const c = createComputation(fn, value, true, 0);
  c.observers = null;
  c.observerSlots = null;
  c.comparator = options.equals || undefined;
  if (Scheduler && Transition && Transition.running) {
    c.tState = STALE;
    Updates.push(c);
  } else updateComputation(c);
  return readSignal.bind(c);
}
function isPromise(v) {
  return v && typeof v === "object" && "then" in v;
}
function createResource(pSource, pFetcher, pOptions) {
  let source;
  let fetcher;
  let options;
  if (typeof pFetcher === "function") {
    source = pSource;
    fetcher = pFetcher;
    options = pOptions || {};
  } else {
    source = true;
    fetcher = pSource;
    options = pFetcher || {};
  }
  let pr = null,
    initP = NO_INIT,
    id = null,
    loadedUnderTransition = false,
    scheduled = false,
    resolved = "initialValue" in options,
    dynamic = typeof source === "function" && createMemo(source);
  const contexts = new Set(),
    [value, setValue] = (options.storage || createSignal)(options.initialValue),
    [error, setError] = createSignal(undefined),
    [track, trigger] = createSignal(undefined, {
      equals: false
    }),
    [state, setState] = createSignal(resolved ? "ready" : "unresolved");
  if (sharedConfig.context) {
    id = sharedConfig.getNextContextId();
    if (options.ssrLoadFrom === "initial") initP = options.initialValue;else if (sharedConfig.load && sharedConfig.has(id)) initP = sharedConfig.load(id);
  }
  function loadEnd(p, v, error, key) {
    if (pr === p) {
      pr = null;
      key !== undefined && (resolved = true);
      if ((p === initP || v === initP) && options.onHydrated) queueMicrotask(() => options.onHydrated(key, {
        value: v
      }));
      initP = NO_INIT;
      if (Transition && p && loadedUnderTransition) {
        Transition.promises.delete(p);
        loadedUnderTransition = false;
        runUpdates(() => {
          Transition.running = true;
          completeLoad(v, error);
        }, false);
      } else completeLoad(v, error);
    }
    return v;
  }
  function completeLoad(v, err) {
    runUpdates(() => {
      if (err === undefined) setValue(() => v);
      setState(err !== undefined ? "errored" : resolved ? "ready" : "unresolved");
      setError(err);
      for (const c of contexts.keys()) c.decrement();
      contexts.clear();
    }, false);
  }
  function read() {
    const c = SuspenseContext && useContext(SuspenseContext),
      v = value(),
      err = error();
    if (err !== undefined && !pr) throw err;
    if (Listener && !Listener.user && c) {
      createComputed(() => {
        track();
        if (pr) {
          if (c.resolved && Transition && loadedUnderTransition) Transition.promises.add(pr);else if (!contexts.has(c)) {
            c.increment();
            contexts.add(c);
          }
        }
      });
    }
    return v;
  }
  function load(refetching = true) {
    if (refetching !== false && scheduled) return;
    scheduled = false;
    const lookup = dynamic ? dynamic() : source;
    loadedUnderTransition = Transition && Transition.running;
    if (lookup == null || lookup === false) {
      loadEnd(pr, untrack(value));
      return;
    }
    if (Transition && pr) Transition.promises.delete(pr);
    let error;
    const p = initP !== NO_INIT ? initP : untrack(() => {
      try {
        return fetcher(lookup, {
          value: value(),
          refetching
        });
      } catch (fetcherError) {
        error = fetcherError;
      }
    });
    if (error !== undefined) {
      loadEnd(pr, undefined, castError(error), lookup);
      return;
    } else if (!isPromise(p)) {
      loadEnd(pr, p, undefined, lookup);
      return p;
    }
    pr = p;
    if ("v" in p) {
      if (p.s === 1) loadEnd(pr, p.v, undefined, lookup);else loadEnd(pr, undefined, castError(p.v), lookup);
      return p;
    }
    scheduled = true;
    queueMicrotask(() => scheduled = false);
    runUpdates(() => {
      setState(resolved ? "refreshing" : "pending");
      trigger();
    }, false);
    return p.then(v => loadEnd(p, v, undefined, lookup), e => loadEnd(p, undefined, castError(e), lookup));
  }
  Object.defineProperties(read, {
    state: {
      get: () => state()
    },
    error: {
      get: () => error()
    },
    loading: {
      get() {
        const s = state();
        return s === "pending" || s === "refreshing";
      }
    },
    latest: {
      get() {
        if (!resolved) return read();
        const err = error();
        if (err && !pr) throw err;
        return value();
      }
    }
  });
  let owner = Owner;
  if (dynamic) createComputed(() => (owner = Owner, load(false)));else load(false);
  return [read, {
    refetch: info => runWithOwner(owner, () => load(info)),
    mutate: setValue
  }];
}
function createDeferred(source, options) {
  let t,
    timeout = options ? options.timeoutMs : undefined;
  const node = createComputation(() => {
    if (!t || !t.fn) t = requestCallback(() => setDeferred(() => node.value), timeout !== undefined ? {
      timeout
    } : undefined);
    return source();
  }, undefined, true);
  const [deferred, setDeferred] = createSignal(Transition && Transition.running && Transition.sources.has(node) ? node.tValue : node.value, options);
  updateComputation(node);
  setDeferred(() => Transition && Transition.running && Transition.sources.has(node) ? node.tValue : node.value);
  return deferred;
}
function createSelector(source, fn = equalFn, options) {
  const subs = new Map();
  const node = createComputation(p => {
    const v = source();
    for (const [key, val] of subs.entries()) if (fn(key, v) !== fn(key, p)) {
      for (const c of val.values()) {
        c.state = STALE;
        if (c.pure) Updates.push(c);else Effects.push(c);
      }
    }
    return v;
  }, undefined, true, STALE);
  updateComputation(node);
  return key => {
    const listener = Listener;
    if (listener) {
      let l;
      if (l = subs.get(key)) l.add(listener);else subs.set(key, l = new Set([listener]));
      onCleanup(() => {
        l.delete(listener);
        !l.size && subs.delete(key);
      });
    }
    return fn(key, Transition && Transition.running && Transition.sources.has(node) ? node.tValue : node.value);
  };
}
function batch(fn) {
  return runUpdates(fn, false);
}
function untrack(fn) {
  if (!ExternalSourceConfig && Listener === null) return fn();
  const listener = Listener;
  Listener = null;
  try {
    if (ExternalSourceConfig) return ExternalSourceConfig.untrack(fn);
    return fn();
  } finally {
    Listener = listener;
  }
}
function on(deps, fn, options) {
  const isArray = Array.isArray(deps);
  let prevInput;
  let defer = options && options.defer;
  return prevValue => {
    let input;
    if (isArray) {
      input = Array(deps.length);
      for (let i = 0; i < deps.length; i++) input[i] = deps[i]();
    } else input = deps();
    if (defer) {
      defer = false;
      return prevValue;
    }
    const result = untrack(() => fn(input, prevInput, prevValue));
    prevInput = input;
    return result;
  };
}
function onMount(fn) {
  createEffect(() => untrack(fn));
}
function onCleanup(fn) {
  if (Owner === null) ;else if (Owner.cleanups === null) Owner.cleanups = [fn];else Owner.cleanups.push(fn);
  return fn;
}
function catchError(fn, handler) {
  ERROR || (ERROR = Symbol("error"));
  Owner = createComputation(undefined, undefined, true);
  Owner.context = {
    ...Owner.context,
    [ERROR]: [handler]
  };
  if (Transition && Transition.running) Transition.sources.add(Owner);
  try {
    return fn();
  } catch (err) {
    handleError(err);
  } finally {
    Owner = Owner.owner;
  }
}
function getListener() {
  return Listener;
}
function getOwner() {
  return Owner;
}
function runWithOwner(o, fn) {
  const prev = Owner;
  const prevListener = Listener;
  Owner = o;
  Listener = null;
  try {
    return runUpdates(fn, true);
  } catch (err) {
    handleError(err);
  } finally {
    Owner = prev;
    Listener = prevListener;
  }
}
function enableScheduling(scheduler = requestCallback) {
  Scheduler = scheduler;
}
function startTransition(fn) {
  if (Transition && Transition.running) {
    fn();
    return Transition.done;
  }
  const l = Listener;
  const o = Owner;
  return Promise.resolve().then(() => {
    Listener = l;
    Owner = o;
    let t;
    if (Scheduler || SuspenseContext) {
      t = Transition || (Transition = {
        sources: new Set(),
        effects: [],
        promises: new Set(),
        disposed: new Set(),
        queue: new Set(),
        running: true
      });
      t.done || (t.done = new Promise(res => t.resolve = res));
      t.running = true;
    }
    runUpdates(fn, false);
    Listener = Owner = null;
    return t ? t.done : undefined;
  });
}
const [transPending, setTransPending] = /*@__PURE__*/createSignal(false);
function useTransition() {
  return [transPending, startTransition];
}
function resumeEffects(e) {
  Effects.push.apply(Effects, e);
  e.length = 0;
}
function createContext(defaultValue, options) {
  const id = Symbol("context");
  return {
    id,
    Provider: createProvider(id),
    defaultValue
  };
}
function useContext(context) {
  let value;
  return Owner && Owner.context && (value = Owner.context[context.id]) !== undefined ? value : context.defaultValue;
}
function children(fn) {
  const children = createMemo(fn);
  const memo = createMemo(() => resolveChildren(children()));
  memo.toArray = () => {
    const c = memo();
    return Array.isArray(c) ? c : c != null ? [c] : [];
  };
  return memo;
}
let SuspenseContext;
function getSuspenseContext() {
  return SuspenseContext || (SuspenseContext = createContext());
}
function enableExternalSource(factory, untrack = fn => fn()) {
  if (ExternalSourceConfig) {
    const {
      factory: oldFactory,
      untrack: oldUntrack
    } = ExternalSourceConfig;
    ExternalSourceConfig = {
      factory: (fn, trigger) => {
        const oldSource = oldFactory(fn, trigger);
        const source = factory(x => oldSource.track(x), trigger);
        return {
          track: x => source.track(x),
          dispose() {
            source.dispose();
            oldSource.dispose();
          }
        };
      },
      untrack: fn => oldUntrack(() => untrack(fn))
    };
  } else {
    ExternalSourceConfig = {
      factory,
      untrack
    };
  }
}
function readSignal() {
  const runningTransition = Transition && Transition.running;
  if (this.sources && (runningTransition ? this.tState : this.state)) {
    if ((runningTransition ? this.tState : this.state) === STALE) updateComputation(this);else {
      const updates = Updates;
      Updates = null;
      runUpdates(() => lookUpstream(this), false);
      Updates = updates;
    }
  }
  if (Listener) {
    const sSlot = this.observers ? this.observers.length : 0;
    if (!Listener.sources) {
      Listener.sources = [this];
      Listener.sourceSlots = [sSlot];
    } else {
      Listener.sources.push(this);
      Listener.sourceSlots.push(sSlot);
    }
    if (!this.observers) {
      this.observers = [Listener];
      this.observerSlots = [Listener.sources.length - 1];
    } else {
      this.observers.push(Listener);
      this.observerSlots.push(Listener.sources.length - 1);
    }
  }
  if (runningTransition && Transition.sources.has(this)) return this.tValue;
  return this.value;
}
function writeSignal(node, value, isComp) {
  let current = Transition && Transition.running && Transition.sources.has(node) ? node.tValue : node.value;
  if (!node.comparator || !node.comparator(current, value)) {
    if (Transition) {
      const TransitionRunning = Transition.running;
      if (TransitionRunning || !isComp && Transition.sources.has(node)) {
        Transition.sources.add(node);
        node.tValue = value;
      }
      if (!TransitionRunning) node.value = value;
    } else node.value = value;
    if (node.observers && node.observers.length) {
      runUpdates(() => {
        for (let i = 0; i < node.observers.length; i += 1) {
          const o = node.observers[i];
          const TransitionRunning = Transition && Transition.running;
          if (TransitionRunning && Transition.disposed.has(o)) continue;
          if (TransitionRunning ? !o.tState : !o.state) {
            if (o.pure) Updates.push(o);else Effects.push(o);
            if (o.observers) markDownstream(o);
          }
          if (!TransitionRunning) o.state = STALE;else o.tState = STALE;
        }
        if (Updates.length > 10e5) {
          Updates = [];
          if (false) {}
          throw new Error();
        }
      }, false);
    }
  }
  return value;
}
function updateComputation(node) {
  if (!node.fn) return;
  cleanNode(node);
  const time = ExecCount;
  runComputation(node, Transition && Transition.running && Transition.sources.has(node) ? node.tValue : node.value, time);
  if (Transition && !Transition.running && Transition.sources.has(node)) {
    queueMicrotask(() => {
      runUpdates(() => {
        Transition && (Transition.running = true);
        Listener = Owner = node;
        runComputation(node, node.tValue, time);
        Listener = Owner = null;
      }, false);
    });
  }
}
function runComputation(node, value, time) {
  let nextValue;
  const owner = Owner,
    listener = Listener;
  Listener = Owner = node;
  try {
    nextValue = node.fn(value);
  } catch (err) {
    if (node.pure) {
      if (Transition && Transition.running) {
        node.tState = STALE;
        node.tOwned && node.tOwned.forEach(cleanNode);
        node.tOwned = undefined;
      } else {
        node.state = STALE;
        node.owned && node.owned.forEach(cleanNode);
        node.owned = null;
      }
    }
    node.updatedAt = time + 1;
    return handleError(err);
  } finally {
    Listener = listener;
    Owner = owner;
  }
  if (!node.updatedAt || node.updatedAt <= time) {
    if (node.updatedAt != null && "observers" in node) {
      writeSignal(node, nextValue, true);
    } else if (Transition && Transition.running && node.pure) {
      if (!Transition.sources.has(node)) node.value = nextValue;
      Transition.sources.add(node);
      node.tValue = nextValue;
    } else node.value = nextValue;
    node.updatedAt = time;
  }
}
function createComputation(fn, init, pure, state = STALE, options) {
  const c = {
    fn,
    state: state,
    updatedAt: null,
    owned: null,
    sources: null,
    sourceSlots: null,
    cleanups: null,
    value: init,
    owner: Owner,
    context: Owner ? Owner.context : null,
    pure
  };
  if (Transition && Transition.running) {
    c.state = 0;
    c.tState = state;
  }
  if (Owner === null) ;else if (Owner !== UNOWNED) {
    if (Transition && Transition.running && Owner.pure) {
      if (!Owner.tOwned) Owner.tOwned = [c];else Owner.tOwned.push(c);
    } else {
      if (!Owner.owned) Owner.owned = [c];else Owner.owned.push(c);
    }
  }
  if (ExternalSourceConfig && c.fn) {
    const sourceFn = c.fn;
    const [track, trigger] = createSignal(undefined, {
      equals: false
    });
    const ordinary = ExternalSourceConfig.factory(sourceFn, trigger);
    onCleanup(() => ordinary.dispose());
    let inTransition;
    const triggerInTransition = () => startTransition(trigger).then(() => {
      if (inTransition) {
        inTransition.dispose();
        inTransition = undefined;
      }
    });
    c.fn = x => {
      track();
      if (Transition && Transition.running) {
        if (!inTransition) inTransition = ExternalSourceConfig.factory(sourceFn, triggerInTransition);
        return inTransition.track(x);
      }
      return ordinary.track(x);
    };
  }
  return c;
}
function runTop(node) {
  const runningTransition = Transition && Transition.running;
  if ((runningTransition ? node.tState : node.state) === 0) return;
  if ((runningTransition ? node.tState : node.state) === PENDING) return lookUpstream(node);
  if (node.suspense && untrack(node.suspense.inFallback)) return node.suspense.effects.push(node);
  const ancestors = [node];
  while ((node = node.owner) && (!node.updatedAt || node.updatedAt < ExecCount)) {
    if (runningTransition && Transition.disposed.has(node)) return;
    if (runningTransition ? node.tState : node.state) ancestors.push(node);
  }
  for (let i = ancestors.length - 1; i >= 0; i--) {
    node = ancestors[i];
    if (runningTransition) {
      let top = node,
        prev = ancestors[i + 1];
      while ((top = top.owner) && top !== prev) {
        if (Transition.disposed.has(top)) return;
      }
    }
    if ((runningTransition ? node.tState : node.state) === STALE) {
      updateComputation(node);
    } else if ((runningTransition ? node.tState : node.state) === PENDING) {
      const updates = Updates;
      Updates = null;
      runUpdates(() => lookUpstream(node, ancestors[0]), false);
      Updates = updates;
    }
  }
}
function runUpdates(fn, init) {
  if (Updates) return fn();
  let wait = false;
  if (!init) Updates = [];
  if (Effects) wait = true;else Effects = [];
  ExecCount++;
  try {
    const res = fn();
    completeUpdates(wait);
    return res;
  } catch (err) {
    if (!wait) Effects = null;
    Updates = null;
    handleError(err);
  }
}
function completeUpdates(wait) {
  if (Updates) {
    if (Scheduler && Transition && Transition.running) scheduleQueue(Updates);else runQueue(Updates);
    Updates = null;
  }
  if (wait) return;
  let res;
  if (Transition) {
    if (!Transition.promises.size && !Transition.queue.size) {
      const sources = Transition.sources;
      const disposed = Transition.disposed;
      Effects.push.apply(Effects, Transition.effects);
      res = Transition.resolve;
      for (const e of Effects) {
        "tState" in e && (e.state = e.tState);
        delete e.tState;
      }
      Transition = null;
      runUpdates(() => {
        for (const d of disposed) cleanNode(d);
        for (const v of sources) {
          v.value = v.tValue;
          if (v.owned) {
            for (let i = 0, len = v.owned.length; i < len; i++) cleanNode(v.owned[i]);
          }
          if (v.tOwned) v.owned = v.tOwned;
          delete v.tValue;
          delete v.tOwned;
          v.tState = 0;
        }
        setTransPending(false);
      }, false);
    } else if (Transition.running) {
      Transition.running = false;
      Transition.effects.push.apply(Transition.effects, Effects);
      Effects = null;
      setTransPending(true);
      return;
    }
  }
  const e = Effects;
  Effects = null;
  if (e.length) runUpdates(() => runEffects(e), false);
  if (res) res();
}
function runQueue(queue) {
  for (let i = 0; i < queue.length; i++) runTop(queue[i]);
}
function scheduleQueue(queue) {
  for (let i = 0; i < queue.length; i++) {
    const item = queue[i];
    const tasks = Transition.queue;
    if (!tasks.has(item)) {
      tasks.add(item);
      Scheduler(() => {
        tasks.delete(item);
        runUpdates(() => {
          Transition.running = true;
          runTop(item);
        }, false);
        Transition && (Transition.running = false);
      });
    }
  }
}
function runUserEffects(queue) {
  let i,
    userLength = 0;
  for (i = 0; i < queue.length; i++) {
    const e = queue[i];
    if (!e.user) runTop(e);else queue[userLength++] = e;
  }
  if (sharedConfig.context) {
    if (sharedConfig.count) {
      sharedConfig.effects || (sharedConfig.effects = []);
      sharedConfig.effects.push(...queue.slice(0, userLength));
      return;
    }
    setHydrateContext();
  }
  if (sharedConfig.effects && (sharedConfig.done || !sharedConfig.count)) {
    queue = [...sharedConfig.effects, ...queue];
    userLength += sharedConfig.effects.length;
    delete sharedConfig.effects;
  }
  for (i = 0; i < userLength; i++) runTop(queue[i]);
}
function lookUpstream(node, ignore) {
  const runningTransition = Transition && Transition.running;
  if (runningTransition) node.tState = 0;else node.state = 0;
  for (let i = 0; i < node.sources.length; i += 1) {
    const source = node.sources[i];
    if (source.sources) {
      const state = runningTransition ? source.tState : source.state;
      if (state === STALE) {
        if (source !== ignore && (!source.updatedAt || source.updatedAt < ExecCount)) runTop(source);
      } else if (state === PENDING) lookUpstream(source, ignore);
    }
  }
}
function markDownstream(node) {
  const runningTransition = Transition && Transition.running;
  for (let i = 0; i < node.observers.length; i += 1) {
    const o = node.observers[i];
    if (runningTransition ? !o.tState : !o.state) {
      if (runningTransition) o.tState = PENDING;else o.state = PENDING;
      if (o.pure) Updates.push(o);else Effects.push(o);
      o.observers && markDownstream(o);
    }
  }
}
function cleanNode(node) {
  let i;
  if (node.sources) {
    while (node.sources.length) {
      const source = node.sources.pop(),
        index = node.sourceSlots.pop(),
        obs = source.observers;
      if (obs && obs.length) {
        const n = obs.pop(),
          s = source.observerSlots.pop();
        if (index < obs.length) {
          n.sourceSlots[s] = index;
          obs[index] = n;
          source.observerSlots[index] = s;
        }
      }
    }
  }
  if (node.tOwned) {
    for (i = node.tOwned.length - 1; i >= 0; i--) cleanNode(node.tOwned[i]);
    delete node.tOwned;
  }
  if (Transition && Transition.running && node.pure) {
    reset(node, true);
  } else if (node.owned) {
    for (i = node.owned.length - 1; i >= 0; i--) cleanNode(node.owned[i]);
    node.owned = null;
  }
  if (node.cleanups) {
    for (i = node.cleanups.length - 1; i >= 0; i--) node.cleanups[i]();
    node.cleanups = null;
  }
  if (Transition && Transition.running) node.tState = 0;else node.state = 0;
}
function reset(node, top) {
  if (!top) {
    node.tState = 0;
    Transition.disposed.add(node);
  }
  if (node.owned) {
    for (let i = 0; i < node.owned.length; i++) reset(node.owned[i]);
  }
}
function castError(err) {
  if (err instanceof Error) return err;
  return new Error(typeof err === "string" ? err : "Unknown error", {
    cause: err
  });
}
function runErrors(err, fns, owner) {
  try {
    for (const f of fns) f(err);
  } catch (e) {
    handleError(e, owner && owner.owner || null);
  }
}
function handleError(err, owner = Owner) {
  const fns = ERROR && owner && owner.context && owner.context[ERROR];
  const error = castError(err);
  if (!fns) throw error;
  if (Effects) Effects.push({
    fn() {
      runErrors(error, fns, owner);
    },
    state: STALE
  });else runErrors(error, fns, owner);
}
function resolveChildren(children) {
  if (typeof children === "function" && !children.length) return resolveChildren(children());
  if (Array.isArray(children)) {
    const results = [];
    for (let i = 0; i < children.length; i++) {
      const result = resolveChildren(children[i]);
      Array.isArray(result) ? results.push.apply(results, result) : results.push(result);
    }
    return results;
  }
  return children;
}
function createProvider(id, options) {
  return function provider(props) {
    let res;
    createRenderEffect(() => res = untrack(() => {
      Owner.context = {
        ...Owner.context,
        [id]: props.value
      };
      return children(() => props.children);
    }), undefined);
    return res;
  };
}
function onError(fn) {
  ERROR || (ERROR = Symbol("error"));
  if (Owner === null) ;else if (Owner.context === null || !Owner.context[ERROR]) {
    Owner.context = {
      ...Owner.context,
      [ERROR]: [fn]
    };
    mutateContext(Owner, ERROR, [fn]);
  } else Owner.context[ERROR].push(fn);
}
function mutateContext(o, key, value) {
  if (o.owned) {
    for (let i = 0; i < o.owned.length; i++) {
      if (o.owned[i].context === o.context) mutateContext(o.owned[i], key, value);
      if (!o.owned[i].context) {
        o.owned[i].context = o.context;
        mutateContext(o.owned[i], key, value);
      } else if (!o.owned[i].context[key]) {
        o.owned[i].context[key] = value;
        mutateContext(o.owned[i], key, value);
      }
    }
  }
}

function observable(input) {
  return {
    subscribe(observer) {
      if (!(observer instanceof Object) || observer == null) {
        throw new TypeError("Expected the observer to be an object.");
      }
      const handler = typeof observer === "function" ? observer : observer.next && observer.next.bind(observer);
      if (!handler) {
        return {
          unsubscribe() {}
        };
      }
      const dispose = createRoot(disposer => {
        createEffect(() => {
          const v = input();
          untrack(() => handler(v));
        });
        return disposer;
      });
      if (getOwner()) onCleanup(dispose);
      return {
        unsubscribe() {
          dispose();
        }
      };
    },
    [Symbol.observable || "@@observable"]() {
      return this;
    }
  };
}
function from(producer, initalValue = undefined) {
  const [s, set] = createSignal(initalValue, {
    equals: false
  });
  if ("subscribe" in producer) {
    const unsub = producer.subscribe(v => set(() => v));
    onCleanup(() => "unsubscribe" in unsub ? unsub.unsubscribe() : unsub());
  } else {
    const clean = producer(set);
    onCleanup(clean);
  }
  return s;
}

const FALLBACK = Symbol("fallback");
function dispose(d) {
  for (let i = 0; i < d.length; i++) d[i]();
}
function mapArray(list, mapFn, options = {}) {
  let items = [],
    mapped = [],
    disposers = [],
    len = 0,
    indexes = mapFn.length > 1 ? [] : null;
  onCleanup(() => dispose(disposers));
  return () => {
    let newItems = list() || [],
      newLen = newItems.length,
      i,
      j;
    newItems[$TRACK];
    return untrack(() => {
      let newIndices, newIndicesNext, temp, tempdisposers, tempIndexes, start, end, newEnd, item;
      if (newLen === 0) {
        if (len !== 0) {
          dispose(disposers);
          disposers = [];
          items = [];
          mapped = [];
          len = 0;
          indexes && (indexes = []);
        }
        if (options.fallback) {
          items = [FALLBACK];
          mapped[0] = createRoot(disposer => {
            disposers[0] = disposer;
            return options.fallback();
          });
          len = 1;
        }
      }
      else if (len === 0) {
        mapped = new Array(newLen);
        for (j = 0; j < newLen; j++) {
          items[j] = newItems[j];
          mapped[j] = createRoot(mapper);
        }
        len = newLen;
      } else {
        temp = new Array(newLen);
        tempdisposers = new Array(newLen);
        indexes && (tempIndexes = new Array(newLen));
        for (start = 0, end = Math.min(len, newLen); start < end && items[start] === newItems[start]; start++);
        for (end = len - 1, newEnd = newLen - 1; end >= start && newEnd >= start && items[end] === newItems[newEnd]; end--, newEnd--) {
          temp[newEnd] = mapped[end];
          tempdisposers[newEnd] = disposers[end];
          indexes && (tempIndexes[newEnd] = indexes[end]);
        }
        newIndices = new Map();
        newIndicesNext = new Array(newEnd + 1);
        for (j = newEnd; j >= start; j--) {
          item = newItems[j];
          i = newIndices.get(item);
          newIndicesNext[j] = i === undefined ? -1 : i;
          newIndices.set(item, j);
        }
        for (i = start; i <= end; i++) {
          item = items[i];
          j = newIndices.get(item);
          if (j !== undefined && j !== -1) {
            temp[j] = mapped[i];
            tempdisposers[j] = disposers[i];
            indexes && (tempIndexes[j] = indexes[i]);
            j = newIndicesNext[j];
            newIndices.set(item, j);
          } else disposers[i]();
        }
        for (j = start; j < newLen; j++) {
          if (j in temp) {
            mapped[j] = temp[j];
            disposers[j] = tempdisposers[j];
            if (indexes) {
              indexes[j] = tempIndexes[j];
              indexes[j](j);
            }
          } else mapped[j] = createRoot(mapper);
        }
        mapped = mapped.slice(0, len = newLen);
        items = newItems.slice(0);
      }
      return mapped;
    });
    function mapper(disposer) {
      disposers[j] = disposer;
      if (indexes) {
        const [s, set] = createSignal(j);
        indexes[j] = set;
        return mapFn(newItems[j], s);
      }
      return mapFn(newItems[j]);
    }
  };
}
function indexArray(list, mapFn, options = {}) {
  let items = [],
    mapped = [],
    disposers = [],
    signals = [],
    len = 0,
    i;
  onCleanup(() => dispose(disposers));
  return () => {
    const newItems = list() || [],
      newLen = newItems.length;
    newItems[$TRACK];
    return untrack(() => {
      if (newLen === 0) {
        if (len !== 0) {
          dispose(disposers);
          disposers = [];
          items = [];
          mapped = [];
          len = 0;
          signals = [];
        }
        if (options.fallback) {
          items = [FALLBACK];
          mapped[0] = createRoot(disposer => {
            disposers[0] = disposer;
            return options.fallback();
          });
          len = 1;
        }
        return mapped;
      }
      if (items[0] === FALLBACK) {
        disposers[0]();
        disposers = [];
        items = [];
        mapped = [];
        len = 0;
      }
      for (i = 0; i < newLen; i++) {
        if (i < items.length && items[i] !== newItems[i]) {
          signals[i](() => newItems[i]);
        } else if (i >= items.length) {
          mapped[i] = createRoot(mapper);
        }
      }
      for (; i < items.length; i++) {
        disposers[i]();
      }
      len = signals.length = disposers.length = newLen;
      items = newItems.slice(0);
      return mapped = mapped.slice(0, len);
    });
    function mapper(disposer) {
      disposers[i] = disposer;
      const [s, set] = createSignal(newItems[i]);
      signals[i] = set;
      return mapFn(s, i);
    }
  };
}

let hydrationEnabled = false;
function enableHydration() {
  hydrationEnabled = true;
}
function createComponent(Comp, props) {
  if (hydrationEnabled) {
    if (sharedConfig.context) {
      const c = sharedConfig.context;
      setHydrateContext(nextHydrateContext());
      const r = untrack(() => Comp(props || {}));
      setHydrateContext(c);
      return r;
    }
  }
  return untrack(() => Comp(props || {}));
}
function trueFn() {
  return true;
}
const propTraps = (/* unused pure expression or super */ null && ({
  get(_, property, receiver) {
    if (property === $PROXY) return receiver;
    return _.get(property);
  },
  has(_, property) {
    if (property === $PROXY) return true;
    return _.has(property);
  },
  set: trueFn,
  deleteProperty: trueFn,
  getOwnPropertyDescriptor(_, property) {
    return {
      configurable: true,
      enumerable: true,
      get() {
        return _.get(property);
      },
      set: trueFn,
      deleteProperty: trueFn
    };
  },
  ownKeys(_) {
    return _.keys();
  }
}));
function resolveSource(s) {
  return !(s = typeof s === "function" ? s() : s) ? {} : s;
}
function resolveSources() {
  for (let i = 0, length = this.length; i < length; ++i) {
    const v = this[i]();
    if (v !== undefined) return v;
  }
}
function mergeProps(...sources) {
  let proxy = false;
  for (let i = 0; i < sources.length; i++) {
    const s = sources[i];
    proxy = proxy || !!s && $PROXY in s;
    sources[i] = typeof s === "function" ? (proxy = true, createMemo(s)) : s;
  }
  if (SUPPORTS_PROXY && proxy) {
    return new Proxy({
      get(property) {
        for (let i = sources.length - 1; i >= 0; i--) {
          const v = resolveSource(sources[i])[property];
          if (v !== undefined) return v;
        }
      },
      has(property) {
        for (let i = sources.length - 1; i >= 0; i--) {
          if (property in resolveSource(sources[i])) return true;
        }
        return false;
      },
      keys() {
        const keys = [];
        for (let i = 0; i < sources.length; i++) keys.push(...Object.keys(resolveSource(sources[i])));
        return [...new Set(keys)];
      }
    }, propTraps);
  }
  const sourcesMap = {};
  const defined = Object.create(null);
  for (let i = sources.length - 1; i >= 0; i--) {
    const source = sources[i];
    if (!source) continue;
    const sourceKeys = Object.getOwnPropertyNames(source);
    for (let i = sourceKeys.length - 1; i >= 0; i--) {
      const key = sourceKeys[i];
      if (key === "__proto__" || key === "constructor") continue;
      const desc = Object.getOwnPropertyDescriptor(source, key);
      if (!defined[key]) {
        defined[key] = desc.get ? {
          enumerable: true,
          configurable: true,
          get: resolveSources.bind(sourcesMap[key] = [desc.get.bind(source)])
        } : desc.value !== undefined ? desc : undefined;
      } else {
        const sources = sourcesMap[key];
        if (sources) {
          if (desc.get) sources.push(desc.get.bind(source));else if (desc.value !== undefined) sources.push(() => desc.value);
        }
      }
    }
  }
  const target = {};
  const definedKeys = Object.keys(defined);
  for (let i = definedKeys.length - 1; i >= 0; i--) {
    const key = definedKeys[i],
      desc = defined[key];
    if (desc && desc.get) Object.defineProperty(target, key, desc);else target[key] = desc ? desc.value : undefined;
  }
  return target;
}
function splitProps(props, ...keys) {
  const len = keys.length;
  if (SUPPORTS_PROXY && $PROXY in props) {
    const blocked = len > 1 ? keys.flat() : keys[0];
    const res = keys.map(k => {
      return new Proxy({
        get(property) {
          return k.includes(property) ? props[property] : undefined;
        },
        has(property) {
          return k.includes(property) && property in props;
        },
        keys() {
          return k.filter(property => property in props);
        }
      }, propTraps);
    });
    res.push(new Proxy({
      get(property) {
        return blocked.includes(property) ? undefined : props[property];
      },
      has(property) {
        return blocked.includes(property) ? false : property in props;
      },
      keys() {
        return Object.keys(props).filter(k => !blocked.includes(k));
      }
    }, propTraps));
    return res;
  }
  const objects = [];
  for (let i = 0; i <= len; i++) {
    objects[i] = {};
  }
  for (const propName of Object.getOwnPropertyNames(props)) {
    let keyIndex = len;
    for (let i = 0; i < keys.length; i++) {
      if (keys[i].includes(propName)) {
        keyIndex = i;
        break;
      }
    }
    const desc = Object.getOwnPropertyDescriptor(props, propName);
    const isDefaultDesc = !desc.get && !desc.set && desc.enumerable && desc.writable && desc.configurable;
    isDefaultDesc ? objects[keyIndex][propName] = desc.value : Object.defineProperty(objects[keyIndex], propName, desc);
  }
  return objects;
}
function lazy(fn) {
  let comp;
  let p;
  const wrap = props => {
    const ctx = sharedConfig.context;
    if (ctx) {
      const [s, set] = createSignal();
      sharedConfig.count || (sharedConfig.count = 0);
      sharedConfig.count++;
      (p || (p = fn())).then(mod => {
        !sharedConfig.done && setHydrateContext(ctx);
        sharedConfig.count--;
        set(() => mod.default);
        setHydrateContext();
      });
      comp = s;
    } else if (!comp) {
      const [s] = createResource(() => (p || (p = fn())).then(mod => mod.default));
      comp = s;
    }
    let Comp;
    return createMemo(() => (Comp = comp()) ? untrack(() => {
      if (false) {}
      if (!ctx || sharedConfig.done) return Comp(props);
      const c = sharedConfig.context;
      setHydrateContext(ctx);
      const r = Comp(props);
      setHydrateContext(c);
      return r;
    }) : "");
  };
  wrap.preload = () => p || ((p = fn()).then(mod => comp = () => mod.default), p);
  return wrap;
}
let counter = 0;
function createUniqueId() {
  const ctx = sharedConfig.context;
  return ctx ? sharedConfig.getNextContextId() : `cl-${counter++}`;
}

const narrowedError = name => `Stale read from <${name}>.`;
function For(props) {
  const fallback = "fallback" in props && {
    fallback: () => props.fallback
  };
  return createMemo(mapArray(() => props.each, props.children, fallback || undefined));
}
function Index(props) {
  const fallback = "fallback" in props && {
    fallback: () => props.fallback
  };
  return createMemo(indexArray(() => props.each, props.children, fallback || undefined));
}
function Show(props) {
  const keyed = props.keyed;
  const conditionValue = createMemo(() => props.when, undefined, undefined);
  const condition = keyed ? conditionValue : createMemo(conditionValue, undefined, {
    equals: (a, b) => !a === !b
  });
  return createMemo(() => {
    const c = condition();
    if (c) {
      const child = props.children;
      const fn = typeof child === "function" && child.length > 0;
      return fn ? untrack(() => child(keyed ? c : () => {
        if (!untrack(condition)) throw narrowedError("Show");
        return conditionValue();
      })) : child;
    }
    return props.fallback;
  }, undefined, undefined);
}
function Switch(props) {
  const chs = children(() => props.children);
  const switchFunc = createMemo(() => {
    const ch = chs();
    const mps = Array.isArray(ch) ? ch : [ch];
    let func = () => undefined;
    for (let i = 0; i < mps.length; i++) {
      const index = i;
      const mp = mps[i];
      const prevFunc = func;
      const conditionValue = createMemo(() => prevFunc() ? undefined : mp.when, undefined, undefined);
      const condition = mp.keyed ? conditionValue : createMemo(conditionValue, undefined, {
        equals: (a, b) => !a === !b
      });
      func = () => prevFunc() || (condition() ? [index, conditionValue, mp] : undefined);
    }
    return func;
  });
  return createMemo(() => {
    const sel = switchFunc()();
    if (!sel) return props.fallback;
    const [index, conditionValue, mp] = sel;
    const child = mp.children;
    const fn = typeof child === "function" && child.length > 0;
    return fn ? untrack(() => child(mp.keyed ? conditionValue() : () => {
      if (untrack(switchFunc)()?.[0] !== index) throw narrowedError("Match");
      return conditionValue();
    })) : child;
  }, undefined, undefined);
}
function Match(props) {
  return props;
}
let Errors;
function resetErrorBoundaries() {
  Errors && [...Errors].forEach(fn => fn());
}
function ErrorBoundary(props) {
  let err;
  if (sharedConfig.context && sharedConfig.load) err = sharedConfig.load(sharedConfig.getContextId());
  const [errored, setErrored] = createSignal(err, undefined);
  Errors || (Errors = new Set());
  Errors.add(setErrored);
  onCleanup(() => Errors.delete(setErrored));
  return createMemo(() => {
    let e;
    if (e = errored()) {
      const f = props.fallback;
      return typeof f === "function" && f.length ? untrack(() => f(e, () => setErrored())) : f;
    }
    return catchError(() => props.children, setErrored);
  }, undefined, undefined);
}

const suspenseListEquals = (a, b) => a.showContent === b.showContent && a.showFallback === b.showFallback;
const SuspenseListContext = /* #__PURE__ */(/* unused pure expression or super */ null && (createContext()));
function SuspenseList(props) {
  let [wrapper, setWrapper] = createSignal(() => ({
      inFallback: false
    })),
    show;
  const listContext = useContext(SuspenseListContext);
  const [registry, setRegistry] = createSignal([]);
  if (listContext) {
    show = listContext.register(createMemo(() => wrapper()().inFallback));
  }
  const resolved = createMemo(prev => {
    const reveal = props.revealOrder,
      tail = props.tail,
      {
        showContent = true,
        showFallback = true
      } = show ? show() : {},
      reg = registry(),
      reverse = reveal === "backwards";
    if (reveal === "together") {
      const all = reg.every(inFallback => !inFallback());
      const res = reg.map(() => ({
        showContent: all && showContent,
        showFallback
      }));
      res.inFallback = !all;
      return res;
    }
    let stop = false;
    let inFallback = prev.inFallback;
    const res = [];
    for (let i = 0, len = reg.length; i < len; i++) {
      const n = reverse ? len - i - 1 : i,
        s = reg[n]();
      if (!stop && !s) {
        res[n] = {
          showContent,
          showFallback
        };
      } else {
        const next = !stop;
        if (next) inFallback = true;
        res[n] = {
          showContent: next,
          showFallback: !tail || next && tail === "collapsed" ? showFallback : false
        };
        stop = true;
      }
    }
    if (!stop) inFallback = false;
    res.inFallback = inFallback;
    return res;
  }, {
    inFallback: false
  });
  setWrapper(() => resolved);
  return createComponent(SuspenseListContext.Provider, {
    value: {
      register: inFallback => {
        let index;
        setRegistry(registry => {
          index = registry.length;
          return [...registry, inFallback];
        });
        return createMemo(() => resolved()[index], undefined, {
          equals: suspenseListEquals
        });
      }
    },
    get children() {
      return props.children;
    }
  });
}
function Suspense(props) {
  let counter = 0,
    show,
    ctx,
    p,
    flicker,
    error;
  const [inFallback, setFallback] = createSignal(false),
    SuspenseContext = getSuspenseContext(),
    store = {
      increment: () => {
        if (++counter === 1) setFallback(true);
      },
      decrement: () => {
        if (--counter === 0) setFallback(false);
      },
      inFallback,
      effects: [],
      resolved: false
    },
    owner = getOwner();
  if (sharedConfig.context && sharedConfig.load) {
    const key = sharedConfig.getContextId();
    let ref = sharedConfig.load(key);
    if (ref) {
      if (typeof ref !== "object" || ref.s !== 1) p = ref;else sharedConfig.gather(key);
    }
    if (p && p !== "$$f") {
      const [s, set] = createSignal(undefined, {
        equals: false
      });
      flicker = s;
      p.then(() => {
        if (sharedConfig.done) return set();
        sharedConfig.gather(key);
        setHydrateContext(ctx);
        set();
        setHydrateContext();
      }, err => {
        error = err;
        set();
      });
    }
  }
  const listContext = useContext(SuspenseListContext);
  if (listContext) show = listContext.register(store.inFallback);
  let dispose;
  onCleanup(() => dispose && dispose());
  return createComponent(SuspenseContext.Provider, {
    value: store,
    get children() {
      return createMemo(() => {
        if (error) throw error;
        ctx = sharedConfig.context;
        if (flicker) {
          flicker();
          return flicker = undefined;
        }
        if (ctx && p === "$$f") setHydrateContext();
        const rendered = createMemo(() => props.children);
        return createMemo(prev => {
          const inFallback = store.inFallback(),
            {
              showContent = true,
              showFallback = true
            } = show ? show() : {};
          if ((!inFallback || p && p !== "$$f") && showContent) {
            store.resolved = true;
            dispose && dispose();
            dispose = ctx = p = undefined;
            resumeEffects(store.effects);
            return rendered();
          }
          if (!showFallback) return;
          if (dispose) return prev;
          return createRoot(disposer => {
            dispose = disposer;
            if (ctx) {
              setHydrateContext({
                id: ctx.id + "F",
                count: 0
              });
              ctx = undefined;
            }
            return props.fallback;
          }, owner);
        });
      });
    }
  });
}

const DEV = (/* unused pure expression or super */ null && (undefined));




},

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMi4wZmI1ZGRlMy5qcyIsInNvdXJjZXMiOlsid2VicGFjazovL0Bhbnl3aWRnZXQvbW9ub3JlcG8vLi9ub2RlX21vZHVsZXMvLnBucG0vQGx1a2VlZCt1dWlkQDIuMC4xL25vZGVfbW9kdWxlcy9AbHVrZWVkL3V1aWQvZGlzdC9pbmRleC5tanMiLCJ3ZWJwYWNrOi8vQGFueXdpZGdldC9tb25vcmVwby8uL25vZGVfbW9kdWxlcy8ucG5wbS9zb2xpZC1qc0AxLjkuMTIvbm9kZV9tb2R1bGVzL3NvbGlkLWpzL2Rpc3Qvc29saWQuanMiXSwic291cmNlc0NvbnRlbnQiOlsidmFyIElEWD0yNTYsIEhFWD1bXSwgQlVGRkVSO1xud2hpbGUgKElEWC0tKSBIRVhbSURYXSA9IChJRFggKyAyNTYpLnRvU3RyaW5nKDE2KS5zdWJzdHJpbmcoMSk7XG5cbmV4cG9ydCBmdW5jdGlvbiB2NCgpIHtcblx0dmFyIGk9MCwgbnVtLCBvdXQ9Jyc7XG5cblx0aWYgKCFCVUZGRVIgfHwgKChJRFggKyAxNikgPiAyNTYpKSB7XG5cdFx0QlVGRkVSID0gQXJyYXkoaT0yNTYpO1xuXHRcdHdoaWxlIChpLS0pIEJVRkZFUltpXSA9IDI1NiAqIE1hdGgucmFuZG9tKCkgfCAwO1xuXHRcdGkgPSBJRFggPSAwO1xuXHR9XG5cblx0Zm9yICg7IGkgPCAxNjsgaSsrKSB7XG5cdFx0bnVtID0gQlVGRkVSW0lEWCArIGldO1xuXHRcdGlmIChpPT02KSBvdXQgKz0gSEVYW251bSAmIDE1IHwgNjRdO1xuXHRcdGVsc2UgaWYgKGk9PTgpIG91dCArPSBIRVhbbnVtICYgNjMgfCAxMjhdO1xuXHRcdGVsc2Ugb3V0ICs9IEhFWFtudW1dO1xuXG5cdFx0aWYgKGkgJiAxICYmIGkgPiAxICYmIGkgPCAxMSkgb3V0ICs9ICctJztcblx0fVxuXG5cdElEWCsrO1xuXHRyZXR1cm4gb3V0O1xufVxuIiwibGV0IHRhc2tJZENvdW50ZXIgPSAxLFxuICBpc0NhbGxiYWNrU2NoZWR1bGVkID0gZmFsc2UsXG4gIGlzUGVyZm9ybWluZ1dvcmsgPSBmYWxzZSxcbiAgdGFza1F1ZXVlID0gW10sXG4gIGN1cnJlbnRUYXNrID0gbnVsbCxcbiAgc2hvdWxkWWllbGRUb0hvc3QgPSBudWxsLFxuICB5aWVsZEludGVydmFsID0gNSxcbiAgZGVhZGxpbmUgPSAwLFxuICBtYXhZaWVsZEludGVydmFsID0gMzAwLFxuICBtYXhEZWFkbGluZSA9IDAsXG4gIHNjaGVkdWxlQ2FsbGJhY2sgPSBudWxsLFxuICBzY2hlZHVsZWRDYWxsYmFjayA9IG51bGw7XG5jb25zdCBtYXhTaWduZWQzMUJpdEludCA9IDEwNzM3NDE4MjM7XG5mdW5jdGlvbiBzZXR1cFNjaGVkdWxlcigpIHtcbiAgY29uc3QgY2hhbm5lbCA9IG5ldyBNZXNzYWdlQ2hhbm5lbCgpLFxuICAgIHBvcnQxID0gY2hhbm5lbC5wb3J0MSxcbiAgICBwb3J0ID0gY2hhbm5lbC5wb3J0MjtcbiAgaWYgKHR5cGVvZiBwb3J0MS51bnJlZiA9PT0gXCJmdW5jdGlvblwiKSBwb3J0MS51bnJlZigpO1xuICBpZiAodHlwZW9mIHBvcnQudW5yZWYgPT09IFwiZnVuY3Rpb25cIikgcG9ydC51bnJlZigpO1xuICBzY2hlZHVsZUNhbGxiYWNrID0gKCkgPT4gcG9ydC5wb3N0TWVzc2FnZShudWxsKTtcbiAgcG9ydDEub25tZXNzYWdlID0gKCkgPT4ge1xuICAgIGlmIChzY2hlZHVsZWRDYWxsYmFjayAhPT0gbnVsbCkge1xuICAgICAgY29uc3QgY3VycmVudFRpbWUgPSBwZXJmb3JtYW5jZS5ub3coKTtcbiAgICAgIGRlYWRsaW5lID0gY3VycmVudFRpbWUgKyB5aWVsZEludGVydmFsO1xuICAgICAgbWF4RGVhZGxpbmUgPSBjdXJyZW50VGltZSArIG1heFlpZWxkSW50ZXJ2YWw7XG4gICAgICB0cnkge1xuICAgICAgICBjb25zdCBoYXNNb3JlV29yayA9IHNjaGVkdWxlZENhbGxiYWNrKGN1cnJlbnRUaW1lKTtcbiAgICAgICAgaWYgKCFoYXNNb3JlV29yaykge1xuICAgICAgICAgIHNjaGVkdWxlZENhbGxiYWNrID0gbnVsbDtcbiAgICAgICAgfSBlbHNlIHBvcnQucG9zdE1lc3NhZ2UobnVsbCk7XG4gICAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICBwb3J0LnBvc3RNZXNzYWdlKG51bGwpO1xuICAgICAgICB0aHJvdyBlcnJvcjtcbiAgICAgIH1cbiAgICB9XG4gIH07XG4gIGlmIChuYXZpZ2F0b3IgJiYgbmF2aWdhdG9yLnNjaGVkdWxpbmcgJiYgbmF2aWdhdG9yLnNjaGVkdWxpbmcuaXNJbnB1dFBlbmRpbmcpIHtcbiAgICBjb25zdCBzY2hlZHVsaW5nID0gbmF2aWdhdG9yLnNjaGVkdWxpbmc7XG4gICAgc2hvdWxkWWllbGRUb0hvc3QgPSAoKSA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50VGltZSA9IHBlcmZvcm1hbmNlLm5vdygpO1xuICAgICAgaWYgKGN1cnJlbnRUaW1lID49IGRlYWRsaW5lKSB7XG4gICAgICAgIGlmIChzY2hlZHVsaW5nLmlzSW5wdXRQZW5kaW5nKCkpIHtcbiAgICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gY3VycmVudFRpbWUgPj0gbWF4RGVhZGxpbmU7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG4gICAgfTtcbiAgfSBlbHNlIHtcbiAgICBzaG91bGRZaWVsZFRvSG9zdCA9ICgpID0+IHBlcmZvcm1hbmNlLm5vdygpID49IGRlYWRsaW5lO1xuICB9XG59XG5mdW5jdGlvbiBlbnF1ZXVlKHRhc2tRdWV1ZSwgdGFzaykge1xuICBmdW5jdGlvbiBmaW5kSW5kZXgoKSB7XG4gICAgbGV0IG0gPSAwO1xuICAgIGxldCBuID0gdGFza1F1ZXVlLmxlbmd0aCAtIDE7XG4gICAgd2hpbGUgKG0gPD0gbikge1xuICAgICAgY29uc3QgayA9IG4gKyBtID4+IDE7XG4gICAgICBjb25zdCBjbXAgPSB0YXNrLmV4cGlyYXRpb25UaW1lIC0gdGFza1F1ZXVlW2tdLmV4cGlyYXRpb25UaW1lO1xuICAgICAgaWYgKGNtcCA+IDApIG0gPSBrICsgMTtlbHNlIGlmIChjbXAgPCAwKSBuID0gayAtIDE7ZWxzZSByZXR1cm4gaztcbiAgICB9XG4gICAgcmV0dXJuIG07XG4gIH1cbiAgdGFza1F1ZXVlLnNwbGljZShmaW5kSW5kZXgoKSwgMCwgdGFzayk7XG59XG5mdW5jdGlvbiByZXF1ZXN0Q2FsbGJhY2soZm4sIG9wdGlvbnMpIHtcbiAgaWYgKCFzY2hlZHVsZUNhbGxiYWNrKSBzZXR1cFNjaGVkdWxlcigpO1xuICBsZXQgc3RhcnRUaW1lID0gcGVyZm9ybWFuY2Uubm93KCksXG4gICAgdGltZW91dCA9IG1heFNpZ25lZDMxQml0SW50O1xuICBpZiAob3B0aW9ucyAmJiBvcHRpb25zLnRpbWVvdXQpIHRpbWVvdXQgPSBvcHRpb25zLnRpbWVvdXQ7XG4gIGNvbnN0IG5ld1Rhc2sgPSB7XG4gICAgaWQ6IHRhc2tJZENvdW50ZXIrKyxcbiAgICBmbixcbiAgICBzdGFydFRpbWUsXG4gICAgZXhwaXJhdGlvblRpbWU6IHN0YXJ0VGltZSArIHRpbWVvdXRcbiAgfTtcbiAgZW5xdWV1ZSh0YXNrUXVldWUsIG5ld1Rhc2spO1xuICBpZiAoIWlzQ2FsbGJhY2tTY2hlZHVsZWQgJiYgIWlzUGVyZm9ybWluZ1dvcmspIHtcbiAgICBpc0NhbGxiYWNrU2NoZWR1bGVkID0gdHJ1ZTtcbiAgICBzY2hlZHVsZWRDYWxsYmFjayA9IGZsdXNoV29yaztcbiAgICBzY2hlZHVsZUNhbGxiYWNrKCk7XG4gIH1cbiAgcmV0dXJuIG5ld1Rhc2s7XG59XG5mdW5jdGlvbiBjYW5jZWxDYWxsYmFjayh0YXNrKSB7XG4gIHRhc2suZm4gPSBudWxsO1xufVxuZnVuY3Rpb24gZmx1c2hXb3JrKGluaXRpYWxUaW1lKSB7XG4gIGlzQ2FsbGJhY2tTY2hlZHVsZWQgPSBmYWxzZTtcbiAgaXNQZXJmb3JtaW5nV29yayA9IHRydWU7XG4gIHRyeSB7XG4gICAgcmV0dXJuIHdvcmtMb29wKGluaXRpYWxUaW1lKTtcbiAgfSBmaW5hbGx5IHtcbiAgICBjdXJyZW50VGFzayA9IG51bGw7XG4gICAgaXNQZXJmb3JtaW5nV29yayA9IGZhbHNlO1xuICB9XG59XG5mdW5jdGlvbiB3b3JrTG9vcChpbml0aWFsVGltZSkge1xuICBsZXQgY3VycmVudFRpbWUgPSBpbml0aWFsVGltZTtcbiAgY3VycmVudFRhc2sgPSB0YXNrUXVldWVbMF0gfHwgbnVsbDtcbiAgd2hpbGUgKGN1cnJlbnRUYXNrICE9PSBudWxsKSB7XG4gICAgaWYgKGN1cnJlbnRUYXNrLmV4cGlyYXRpb25UaW1lID4gY3VycmVudFRpbWUgJiYgc2hvdWxkWWllbGRUb0hvc3QoKSkge1xuICAgICAgYnJlYWs7XG4gICAgfVxuICAgIGNvbnN0IGNhbGxiYWNrID0gY3VycmVudFRhc2suZm47XG4gICAgaWYgKGNhbGxiYWNrICE9PSBudWxsKSB7XG4gICAgICBjdXJyZW50VGFzay5mbiA9IG51bGw7XG4gICAgICBjb25zdCBkaWRVc2VyQ2FsbGJhY2tUaW1lb3V0ID0gY3VycmVudFRhc2suZXhwaXJhdGlvblRpbWUgPD0gY3VycmVudFRpbWU7XG4gICAgICBjYWxsYmFjayhkaWRVc2VyQ2FsbGJhY2tUaW1lb3V0KTtcbiAgICAgIGN1cnJlbnRUaW1lID0gcGVyZm9ybWFuY2Uubm93KCk7XG4gICAgICBpZiAoY3VycmVudFRhc2sgPT09IHRhc2tRdWV1ZVswXSkge1xuICAgICAgICB0YXNrUXVldWUuc2hpZnQoKTtcbiAgICAgIH1cbiAgICB9IGVsc2UgdGFza1F1ZXVlLnNoaWZ0KCk7XG4gICAgY3VycmVudFRhc2sgPSB0YXNrUXVldWVbMF0gfHwgbnVsbDtcbiAgfVxuICByZXR1cm4gY3VycmVudFRhc2sgIT09IG51bGw7XG59XG5cbmNvbnN0IHNoYXJlZENvbmZpZyA9IHtcbiAgY29udGV4dDogdW5kZWZpbmVkLFxuICByZWdpc3RyeTogdW5kZWZpbmVkLFxuICBlZmZlY3RzOiB1bmRlZmluZWQsXG4gIGRvbmU6IGZhbHNlLFxuICBnZXRDb250ZXh0SWQoKSB7XG4gICAgcmV0dXJuIGdldENvbnRleHRJZCh0aGlzLmNvbnRleHQuY291bnQpO1xuICB9LFxuICBnZXROZXh0Q29udGV4dElkKCkge1xuICAgIHJldHVybiBnZXRDb250ZXh0SWQodGhpcy5jb250ZXh0LmNvdW50KyspO1xuICB9XG59O1xuZnVuY3Rpb24gZ2V0Q29udGV4dElkKGNvdW50KSB7XG4gIGNvbnN0IG51bSA9IFN0cmluZyhjb3VudCksXG4gICAgbGVuID0gbnVtLmxlbmd0aCAtIDE7XG4gIHJldHVybiBzaGFyZWRDb25maWcuY29udGV4dC5pZCArIChsZW4gPyBTdHJpbmcuZnJvbUNoYXJDb2RlKDk2ICsgbGVuKSA6IFwiXCIpICsgbnVtO1xufVxuZnVuY3Rpb24gc2V0SHlkcmF0ZUNvbnRleHQoY29udGV4dCkge1xuICBzaGFyZWRDb25maWcuY29udGV4dCA9IGNvbnRleHQ7XG59XG5mdW5jdGlvbiBuZXh0SHlkcmF0ZUNvbnRleHQoKSB7XG4gIHJldHVybiB7XG4gICAgLi4uc2hhcmVkQ29uZmlnLmNvbnRleHQsXG4gICAgaWQ6IHNoYXJlZENvbmZpZy5nZXROZXh0Q29udGV4dElkKCksXG4gICAgY291bnQ6IDBcbiAgfTtcbn1cblxuY29uc3QgSVNfREVWID0gZmFsc2U7XG5jb25zdCBlcXVhbEZuID0gKGEsIGIpID0+IGEgPT09IGI7XG5jb25zdCAkUFJPWFkgPSBTeW1ib2woXCJzb2xpZC1wcm94eVwiKTtcbmNvbnN0IFNVUFBPUlRTX1BST1hZID0gdHlwZW9mIFByb3h5ID09PSBcImZ1bmN0aW9uXCI7XG5jb25zdCAkVFJBQ0sgPSBTeW1ib2woXCJzb2xpZC10cmFja1wiKTtcbmNvbnN0ICRERVZDT01QID0gU3ltYm9sKFwic29saWQtZGV2LWNvbXBvbmVudFwiKTtcbmNvbnN0IHNpZ25hbE9wdGlvbnMgPSB7XG4gIGVxdWFsczogZXF1YWxGblxufTtcbmxldCBFUlJPUiA9IG51bGw7XG5sZXQgcnVuRWZmZWN0cyA9IHJ1blF1ZXVlO1xuY29uc3QgU1RBTEUgPSAxO1xuY29uc3QgUEVORElORyA9IDI7XG5jb25zdCBVTk9XTkVEID0ge1xuICBvd25lZDogbnVsbCxcbiAgY2xlYW51cHM6IG51bGwsXG4gIGNvbnRleHQ6IG51bGwsXG4gIG93bmVyOiBudWxsXG59O1xuY29uc3QgTk9fSU5JVCA9IHt9O1xudmFyIE93bmVyID0gbnVsbDtcbmxldCBUcmFuc2l0aW9uID0gbnVsbDtcbmxldCBTY2hlZHVsZXIgPSBudWxsO1xubGV0IEV4dGVybmFsU291cmNlQ29uZmlnID0gbnVsbDtcbmxldCBMaXN0ZW5lciA9IG51bGw7XG5sZXQgVXBkYXRlcyA9IG51bGw7XG5sZXQgRWZmZWN0cyA9IG51bGw7XG5sZXQgRXhlY0NvdW50ID0gMDtcbmZ1bmN0aW9uIGNyZWF0ZVJvb3QoZm4sIGRldGFjaGVkT3duZXIpIHtcbiAgY29uc3QgbGlzdGVuZXIgPSBMaXN0ZW5lcixcbiAgICBvd25lciA9IE93bmVyLFxuICAgIHVub3duZWQgPSBmbi5sZW5ndGggPT09IDAsXG4gICAgY3VycmVudCA9IGRldGFjaGVkT3duZXIgPT09IHVuZGVmaW5lZCA/IG93bmVyIDogZGV0YWNoZWRPd25lcixcbiAgICByb290ID0gdW5vd25lZCA/IFVOT1dORUQgOiB7XG4gICAgICBvd25lZDogbnVsbCxcbiAgICAgIGNsZWFudXBzOiBudWxsLFxuICAgICAgY29udGV4dDogY3VycmVudCA/IGN1cnJlbnQuY29udGV4dCA6IG51bGwsXG4gICAgICBvd25lcjogY3VycmVudFxuICAgIH0sXG4gICAgdXBkYXRlRm4gPSB1bm93bmVkID8gZm4gOiAoKSA9PiBmbigoKSA9PiB1bnRyYWNrKCgpID0+IGNsZWFuTm9kZShyb290KSkpO1xuICBPd25lciA9IHJvb3Q7XG4gIExpc3RlbmVyID0gbnVsbDtcbiAgdHJ5IHtcbiAgICByZXR1cm4gcnVuVXBkYXRlcyh1cGRhdGVGbiwgdHJ1ZSk7XG4gIH0gZmluYWxseSB7XG4gICAgTGlzdGVuZXIgPSBsaXN0ZW5lcjtcbiAgICBPd25lciA9IG93bmVyO1xuICB9XG59XG5mdW5jdGlvbiBjcmVhdGVTaWduYWwodmFsdWUsIG9wdGlvbnMpIHtcbiAgb3B0aW9ucyA9IG9wdGlvbnMgPyBPYmplY3QuYXNzaWduKHt9LCBzaWduYWxPcHRpb25zLCBvcHRpb25zKSA6IHNpZ25hbE9wdGlvbnM7XG4gIGNvbnN0IHMgPSB7XG4gICAgdmFsdWUsXG4gICAgb2JzZXJ2ZXJzOiBudWxsLFxuICAgIG9ic2VydmVyU2xvdHM6IG51bGwsXG4gICAgY29tcGFyYXRvcjogb3B0aW9ucy5lcXVhbHMgfHwgdW5kZWZpbmVkXG4gIH07XG4gIGNvbnN0IHNldHRlciA9IHZhbHVlID0+IHtcbiAgICBpZiAodHlwZW9mIHZhbHVlID09PSBcImZ1bmN0aW9uXCIpIHtcbiAgICAgIGlmIChUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZyAmJiBUcmFuc2l0aW9uLnNvdXJjZXMuaGFzKHMpKSB2YWx1ZSA9IHZhbHVlKHMudFZhbHVlKTtlbHNlIHZhbHVlID0gdmFsdWUocy52YWx1ZSk7XG4gICAgfVxuICAgIHJldHVybiB3cml0ZVNpZ25hbChzLCB2YWx1ZSk7XG4gIH07XG4gIHJldHVybiBbcmVhZFNpZ25hbC5iaW5kKHMpLCBzZXR0ZXJdO1xufVxuZnVuY3Rpb24gY3JlYXRlQ29tcHV0ZWQoZm4sIHZhbHVlLCBvcHRpb25zKSB7XG4gIGNvbnN0IGMgPSBjcmVhdGVDb21wdXRhdGlvbihmbiwgdmFsdWUsIHRydWUsIFNUQUxFKTtcbiAgaWYgKFNjaGVkdWxlciAmJiBUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZykgVXBkYXRlcy5wdXNoKGMpO2Vsc2UgdXBkYXRlQ29tcHV0YXRpb24oYyk7XG59XG5mdW5jdGlvbiBjcmVhdGVSZW5kZXJFZmZlY3QoZm4sIHZhbHVlLCBvcHRpb25zKSB7XG4gIGNvbnN0IGMgPSBjcmVhdGVDb21wdXRhdGlvbihmbiwgdmFsdWUsIGZhbHNlLCBTVEFMRSk7XG4gIGlmIChTY2hlZHVsZXIgJiYgVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcpIFVwZGF0ZXMucHVzaChjKTtlbHNlIHVwZGF0ZUNvbXB1dGF0aW9uKGMpO1xufVxuZnVuY3Rpb24gY3JlYXRlRWZmZWN0KGZuLCB2YWx1ZSwgb3B0aW9ucykge1xuICBydW5FZmZlY3RzID0gcnVuVXNlckVmZmVjdHM7XG4gIGNvbnN0IGMgPSBjcmVhdGVDb21wdXRhdGlvbihmbiwgdmFsdWUsIGZhbHNlLCBTVEFMRSksXG4gICAgcyA9IFN1c3BlbnNlQ29udGV4dCAmJiB1c2VDb250ZXh0KFN1c3BlbnNlQ29udGV4dCk7XG4gIGlmIChzKSBjLnN1c3BlbnNlID0gcztcbiAgaWYgKCFvcHRpb25zIHx8ICFvcHRpb25zLnJlbmRlcikgYy51c2VyID0gdHJ1ZTtcbiAgRWZmZWN0cyA/IEVmZmVjdHMucHVzaChjKSA6IHVwZGF0ZUNvbXB1dGF0aW9uKGMpO1xufVxuZnVuY3Rpb24gY3JlYXRlUmVhY3Rpb24ob25JbnZhbGlkYXRlLCBvcHRpb25zKSB7XG4gIGxldCBmbjtcbiAgY29uc3QgYyA9IGNyZWF0ZUNvbXB1dGF0aW9uKCgpID0+IHtcbiAgICAgIGZuID8gZm4oKSA6IHVudHJhY2sob25JbnZhbGlkYXRlKTtcbiAgICAgIGZuID0gdW5kZWZpbmVkO1xuICAgIH0sIHVuZGVmaW5lZCwgZmFsc2UsIDApLFxuICAgIHMgPSBTdXNwZW5zZUNvbnRleHQgJiYgdXNlQ29udGV4dChTdXNwZW5zZUNvbnRleHQpO1xuICBpZiAocykgYy5zdXNwZW5zZSA9IHM7XG4gIGMudXNlciA9IHRydWU7XG4gIHJldHVybiB0cmFja2luZyA9PiB7XG4gICAgZm4gPSB0cmFja2luZztcbiAgICB1cGRhdGVDb21wdXRhdGlvbihjKTtcbiAgfTtcbn1cbmZ1bmN0aW9uIGNyZWF0ZU1lbW8oZm4sIHZhbHVlLCBvcHRpb25zKSB7XG4gIG9wdGlvbnMgPSBvcHRpb25zID8gT2JqZWN0LmFzc2lnbih7fSwgc2lnbmFsT3B0aW9ucywgb3B0aW9ucykgOiBzaWduYWxPcHRpb25zO1xuICBjb25zdCBjID0gY3JlYXRlQ29tcHV0YXRpb24oZm4sIHZhbHVlLCB0cnVlLCAwKTtcbiAgYy5vYnNlcnZlcnMgPSBudWxsO1xuICBjLm9ic2VydmVyU2xvdHMgPSBudWxsO1xuICBjLmNvbXBhcmF0b3IgPSBvcHRpb25zLmVxdWFscyB8fCB1bmRlZmluZWQ7XG4gIGlmIChTY2hlZHVsZXIgJiYgVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcpIHtcbiAgICBjLnRTdGF0ZSA9IFNUQUxFO1xuICAgIFVwZGF0ZXMucHVzaChjKTtcbiAgfSBlbHNlIHVwZGF0ZUNvbXB1dGF0aW9uKGMpO1xuICByZXR1cm4gcmVhZFNpZ25hbC5iaW5kKGMpO1xufVxuZnVuY3Rpb24gaXNQcm9taXNlKHYpIHtcbiAgcmV0dXJuIHYgJiYgdHlwZW9mIHYgPT09IFwib2JqZWN0XCIgJiYgXCJ0aGVuXCIgaW4gdjtcbn1cbmZ1bmN0aW9uIGNyZWF0ZVJlc291cmNlKHBTb3VyY2UsIHBGZXRjaGVyLCBwT3B0aW9ucykge1xuICBsZXQgc291cmNlO1xuICBsZXQgZmV0Y2hlcjtcbiAgbGV0IG9wdGlvbnM7XG4gIGlmICh0eXBlb2YgcEZldGNoZXIgPT09IFwiZnVuY3Rpb25cIikge1xuICAgIHNvdXJjZSA9IHBTb3VyY2U7XG4gICAgZmV0Y2hlciA9IHBGZXRjaGVyO1xuICAgIG9wdGlvbnMgPSBwT3B0aW9ucyB8fCB7fTtcbiAgfSBlbHNlIHtcbiAgICBzb3VyY2UgPSB0cnVlO1xuICAgIGZldGNoZXIgPSBwU291cmNlO1xuICAgIG9wdGlvbnMgPSBwRmV0Y2hlciB8fCB7fTtcbiAgfVxuICBsZXQgcHIgPSBudWxsLFxuICAgIGluaXRQID0gTk9fSU5JVCxcbiAgICBpZCA9IG51bGwsXG4gICAgbG9hZGVkVW5kZXJUcmFuc2l0aW9uID0gZmFsc2UsXG4gICAgc2NoZWR1bGVkID0gZmFsc2UsXG4gICAgcmVzb2x2ZWQgPSBcImluaXRpYWxWYWx1ZVwiIGluIG9wdGlvbnMsXG4gICAgZHluYW1pYyA9IHR5cGVvZiBzb3VyY2UgPT09IFwiZnVuY3Rpb25cIiAmJiBjcmVhdGVNZW1vKHNvdXJjZSk7XG4gIGNvbnN0IGNvbnRleHRzID0gbmV3IFNldCgpLFxuICAgIFt2YWx1ZSwgc2V0VmFsdWVdID0gKG9wdGlvbnMuc3RvcmFnZSB8fCBjcmVhdGVTaWduYWwpKG9wdGlvbnMuaW5pdGlhbFZhbHVlKSxcbiAgICBbZXJyb3IsIHNldEVycm9yXSA9IGNyZWF0ZVNpZ25hbCh1bmRlZmluZWQpLFxuICAgIFt0cmFjaywgdHJpZ2dlcl0gPSBjcmVhdGVTaWduYWwodW5kZWZpbmVkLCB7XG4gICAgICBlcXVhbHM6IGZhbHNlXG4gICAgfSksXG4gICAgW3N0YXRlLCBzZXRTdGF0ZV0gPSBjcmVhdGVTaWduYWwocmVzb2x2ZWQgPyBcInJlYWR5XCIgOiBcInVucmVzb2x2ZWRcIik7XG4gIGlmIChzaGFyZWRDb25maWcuY29udGV4dCkge1xuICAgIGlkID0gc2hhcmVkQ29uZmlnLmdldE5leHRDb250ZXh0SWQoKTtcbiAgICBpZiAob3B0aW9ucy5zc3JMb2FkRnJvbSA9PT0gXCJpbml0aWFsXCIpIGluaXRQID0gb3B0aW9ucy5pbml0aWFsVmFsdWU7ZWxzZSBpZiAoc2hhcmVkQ29uZmlnLmxvYWQgJiYgc2hhcmVkQ29uZmlnLmhhcyhpZCkpIGluaXRQID0gc2hhcmVkQ29uZmlnLmxvYWQoaWQpO1xuICB9XG4gIGZ1bmN0aW9uIGxvYWRFbmQocCwgdiwgZXJyb3IsIGtleSkge1xuICAgIGlmIChwciA9PT0gcCkge1xuICAgICAgcHIgPSBudWxsO1xuICAgICAga2V5ICE9PSB1bmRlZmluZWQgJiYgKHJlc29sdmVkID0gdHJ1ZSk7XG4gICAgICBpZiAoKHAgPT09IGluaXRQIHx8IHYgPT09IGluaXRQKSAmJiBvcHRpb25zLm9uSHlkcmF0ZWQpIHF1ZXVlTWljcm90YXNrKCgpID0+IG9wdGlvbnMub25IeWRyYXRlZChrZXksIHtcbiAgICAgICAgdmFsdWU6IHZcbiAgICAgIH0pKTtcbiAgICAgIGluaXRQID0gTk9fSU5JVDtcbiAgICAgIGlmIChUcmFuc2l0aW9uICYmIHAgJiYgbG9hZGVkVW5kZXJUcmFuc2l0aW9uKSB7XG4gICAgICAgIFRyYW5zaXRpb24ucHJvbWlzZXMuZGVsZXRlKHApO1xuICAgICAgICBsb2FkZWRVbmRlclRyYW5zaXRpb24gPSBmYWxzZTtcbiAgICAgICAgcnVuVXBkYXRlcygoKSA9PiB7XG4gICAgICAgICAgVHJhbnNpdGlvbi5ydW5uaW5nID0gdHJ1ZTtcbiAgICAgICAgICBjb21wbGV0ZUxvYWQodiwgZXJyb3IpO1xuICAgICAgICB9LCBmYWxzZSk7XG4gICAgICB9IGVsc2UgY29tcGxldGVMb2FkKHYsIGVycm9yKTtcbiAgICB9XG4gICAgcmV0dXJuIHY7XG4gIH1cbiAgZnVuY3Rpb24gY29tcGxldGVMb2FkKHYsIGVycikge1xuICAgIHJ1blVwZGF0ZXMoKCkgPT4ge1xuICAgICAgaWYgKGVyciA9PT0gdW5kZWZpbmVkKSBzZXRWYWx1ZSgoKSA9PiB2KTtcbiAgICAgIHNldFN0YXRlKGVyciAhPT0gdW5kZWZpbmVkID8gXCJlcnJvcmVkXCIgOiByZXNvbHZlZCA/IFwicmVhZHlcIiA6IFwidW5yZXNvbHZlZFwiKTtcbiAgICAgIHNldEVycm9yKGVycik7XG4gICAgICBmb3IgKGNvbnN0IGMgb2YgY29udGV4dHMua2V5cygpKSBjLmRlY3JlbWVudCgpO1xuICAgICAgY29udGV4dHMuY2xlYXIoKTtcbiAgICB9LCBmYWxzZSk7XG4gIH1cbiAgZnVuY3Rpb24gcmVhZCgpIHtcbiAgICBjb25zdCBjID0gU3VzcGVuc2VDb250ZXh0ICYmIHVzZUNvbnRleHQoU3VzcGVuc2VDb250ZXh0KSxcbiAgICAgIHYgPSB2YWx1ZSgpLFxuICAgICAgZXJyID0gZXJyb3IoKTtcbiAgICBpZiAoZXJyICE9PSB1bmRlZmluZWQgJiYgIXByKSB0aHJvdyBlcnI7XG4gICAgaWYgKExpc3RlbmVyICYmICFMaXN0ZW5lci51c2VyICYmIGMpIHtcbiAgICAgIGNyZWF0ZUNvbXB1dGVkKCgpID0+IHtcbiAgICAgICAgdHJhY2soKTtcbiAgICAgICAgaWYgKHByKSB7XG4gICAgICAgICAgaWYgKGMucmVzb2x2ZWQgJiYgVHJhbnNpdGlvbiAmJiBsb2FkZWRVbmRlclRyYW5zaXRpb24pIFRyYW5zaXRpb24ucHJvbWlzZXMuYWRkKHByKTtlbHNlIGlmICghY29udGV4dHMuaGFzKGMpKSB7XG4gICAgICAgICAgICBjLmluY3JlbWVudCgpO1xuICAgICAgICAgICAgY29udGV4dHMuYWRkKGMpO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuICAgIHJldHVybiB2O1xuICB9XG4gIGZ1bmN0aW9uIGxvYWQocmVmZXRjaGluZyA9IHRydWUpIHtcbiAgICBpZiAocmVmZXRjaGluZyAhPT0gZmFsc2UgJiYgc2NoZWR1bGVkKSByZXR1cm47XG4gICAgc2NoZWR1bGVkID0gZmFsc2U7XG4gICAgY29uc3QgbG9va3VwID0gZHluYW1pYyA/IGR5bmFtaWMoKSA6IHNvdXJjZTtcbiAgICBsb2FkZWRVbmRlclRyYW5zaXRpb24gPSBUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZztcbiAgICBpZiAobG9va3VwID09IG51bGwgfHwgbG9va3VwID09PSBmYWxzZSkge1xuICAgICAgbG9hZEVuZChwciwgdW50cmFjayh2YWx1ZSkpO1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBpZiAoVHJhbnNpdGlvbiAmJiBwcikgVHJhbnNpdGlvbi5wcm9taXNlcy5kZWxldGUocHIpO1xuICAgIGxldCBlcnJvcjtcbiAgICBjb25zdCBwID0gaW5pdFAgIT09IE5PX0lOSVQgPyBpbml0UCA6IHVudHJhY2soKCkgPT4ge1xuICAgICAgdHJ5IHtcbiAgICAgICAgcmV0dXJuIGZldGNoZXIobG9va3VwLCB7XG4gICAgICAgICAgdmFsdWU6IHZhbHVlKCksXG4gICAgICAgICAgcmVmZXRjaGluZ1xuICAgICAgICB9KTtcbiAgICAgIH0gY2F0Y2ggKGZldGNoZXJFcnJvcikge1xuICAgICAgICBlcnJvciA9IGZldGNoZXJFcnJvcjtcbiAgICAgIH1cbiAgICB9KTtcbiAgICBpZiAoZXJyb3IgIT09IHVuZGVmaW5lZCkge1xuICAgICAgbG9hZEVuZChwciwgdW5kZWZpbmVkLCBjYXN0RXJyb3IoZXJyb3IpLCBsb29rdXApO1xuICAgICAgcmV0dXJuO1xuICAgIH0gZWxzZSBpZiAoIWlzUHJvbWlzZShwKSkge1xuICAgICAgbG9hZEVuZChwciwgcCwgdW5kZWZpbmVkLCBsb29rdXApO1xuICAgICAgcmV0dXJuIHA7XG4gICAgfVxuICAgIHByID0gcDtcbiAgICBpZiAoXCJ2XCIgaW4gcCkge1xuICAgICAgaWYgKHAucyA9PT0gMSkgbG9hZEVuZChwciwgcC52LCB1bmRlZmluZWQsIGxvb2t1cCk7ZWxzZSBsb2FkRW5kKHByLCB1bmRlZmluZWQsIGNhc3RFcnJvcihwLnYpLCBsb29rdXApO1xuICAgICAgcmV0dXJuIHA7XG4gICAgfVxuICAgIHNjaGVkdWxlZCA9IHRydWU7XG4gICAgcXVldWVNaWNyb3Rhc2soKCkgPT4gc2NoZWR1bGVkID0gZmFsc2UpO1xuICAgIHJ1blVwZGF0ZXMoKCkgPT4ge1xuICAgICAgc2V0U3RhdGUocmVzb2x2ZWQgPyBcInJlZnJlc2hpbmdcIiA6IFwicGVuZGluZ1wiKTtcbiAgICAgIHRyaWdnZXIoKTtcbiAgICB9LCBmYWxzZSk7XG4gICAgcmV0dXJuIHAudGhlbih2ID0+IGxvYWRFbmQocCwgdiwgdW5kZWZpbmVkLCBsb29rdXApLCBlID0+IGxvYWRFbmQocCwgdW5kZWZpbmVkLCBjYXN0RXJyb3IoZSksIGxvb2t1cCkpO1xuICB9XG4gIE9iamVjdC5kZWZpbmVQcm9wZXJ0aWVzKHJlYWQsIHtcbiAgICBzdGF0ZToge1xuICAgICAgZ2V0OiAoKSA9PiBzdGF0ZSgpXG4gICAgfSxcbiAgICBlcnJvcjoge1xuICAgICAgZ2V0OiAoKSA9PiBlcnJvcigpXG4gICAgfSxcbiAgICBsb2FkaW5nOiB7XG4gICAgICBnZXQoKSB7XG4gICAgICAgIGNvbnN0IHMgPSBzdGF0ZSgpO1xuICAgICAgICByZXR1cm4gcyA9PT0gXCJwZW5kaW5nXCIgfHwgcyA9PT0gXCJyZWZyZXNoaW5nXCI7XG4gICAgICB9XG4gICAgfSxcbiAgICBsYXRlc3Q6IHtcbiAgICAgIGdldCgpIHtcbiAgICAgICAgaWYgKCFyZXNvbHZlZCkgcmV0dXJuIHJlYWQoKTtcbiAgICAgICAgY29uc3QgZXJyID0gZXJyb3IoKTtcbiAgICAgICAgaWYgKGVyciAmJiAhcHIpIHRocm93IGVycjtcbiAgICAgICAgcmV0dXJuIHZhbHVlKCk7XG4gICAgICB9XG4gICAgfVxuICB9KTtcbiAgbGV0IG93bmVyID0gT3duZXI7XG4gIGlmIChkeW5hbWljKSBjcmVhdGVDb21wdXRlZCgoKSA9PiAob3duZXIgPSBPd25lciwgbG9hZChmYWxzZSkpKTtlbHNlIGxvYWQoZmFsc2UpO1xuICByZXR1cm4gW3JlYWQsIHtcbiAgICByZWZldGNoOiBpbmZvID0+IHJ1bldpdGhPd25lcihvd25lciwgKCkgPT4gbG9hZChpbmZvKSksXG4gICAgbXV0YXRlOiBzZXRWYWx1ZVxuICB9XTtcbn1cbmZ1bmN0aW9uIGNyZWF0ZURlZmVycmVkKHNvdXJjZSwgb3B0aW9ucykge1xuICBsZXQgdCxcbiAgICB0aW1lb3V0ID0gb3B0aW9ucyA/IG9wdGlvbnMudGltZW91dE1zIDogdW5kZWZpbmVkO1xuICBjb25zdCBub2RlID0gY3JlYXRlQ29tcHV0YXRpb24oKCkgPT4ge1xuICAgIGlmICghdCB8fCAhdC5mbikgdCA9IHJlcXVlc3RDYWxsYmFjaygoKSA9PiBzZXREZWZlcnJlZCgoKSA9PiBub2RlLnZhbHVlKSwgdGltZW91dCAhPT0gdW5kZWZpbmVkID8ge1xuICAgICAgdGltZW91dFxuICAgIH0gOiB1bmRlZmluZWQpO1xuICAgIHJldHVybiBzb3VyY2UoKTtcbiAgfSwgdW5kZWZpbmVkLCB0cnVlKTtcbiAgY29uc3QgW2RlZmVycmVkLCBzZXREZWZlcnJlZF0gPSBjcmVhdGVTaWduYWwoVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcgJiYgVHJhbnNpdGlvbi5zb3VyY2VzLmhhcyhub2RlKSA/IG5vZGUudFZhbHVlIDogbm9kZS52YWx1ZSwgb3B0aW9ucyk7XG4gIHVwZGF0ZUNvbXB1dGF0aW9uKG5vZGUpO1xuICBzZXREZWZlcnJlZCgoKSA9PiBUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZyAmJiBUcmFuc2l0aW9uLnNvdXJjZXMuaGFzKG5vZGUpID8gbm9kZS50VmFsdWUgOiBub2RlLnZhbHVlKTtcbiAgcmV0dXJuIGRlZmVycmVkO1xufVxuZnVuY3Rpb24gY3JlYXRlU2VsZWN0b3Ioc291cmNlLCBmbiA9IGVxdWFsRm4sIG9wdGlvbnMpIHtcbiAgY29uc3Qgc3VicyA9IG5ldyBNYXAoKTtcbiAgY29uc3Qgbm9kZSA9IGNyZWF0ZUNvbXB1dGF0aW9uKHAgPT4ge1xuICAgIGNvbnN0IHYgPSBzb3VyY2UoKTtcbiAgICBmb3IgKGNvbnN0IFtrZXksIHZhbF0gb2Ygc3Vicy5lbnRyaWVzKCkpIGlmIChmbihrZXksIHYpICE9PSBmbihrZXksIHApKSB7XG4gICAgICBmb3IgKGNvbnN0IGMgb2YgdmFsLnZhbHVlcygpKSB7XG4gICAgICAgIGMuc3RhdGUgPSBTVEFMRTtcbiAgICAgICAgaWYgKGMucHVyZSkgVXBkYXRlcy5wdXNoKGMpO2Vsc2UgRWZmZWN0cy5wdXNoKGMpO1xuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gdjtcbiAgfSwgdW5kZWZpbmVkLCB0cnVlLCBTVEFMRSk7XG4gIHVwZGF0ZUNvbXB1dGF0aW9uKG5vZGUpO1xuICByZXR1cm4ga2V5ID0+IHtcbiAgICBjb25zdCBsaXN0ZW5lciA9IExpc3RlbmVyO1xuICAgIGlmIChsaXN0ZW5lcikge1xuICAgICAgbGV0IGw7XG4gICAgICBpZiAobCA9IHN1YnMuZ2V0KGtleSkpIGwuYWRkKGxpc3RlbmVyKTtlbHNlIHN1YnMuc2V0KGtleSwgbCA9IG5ldyBTZXQoW2xpc3RlbmVyXSkpO1xuICAgICAgb25DbGVhbnVwKCgpID0+IHtcbiAgICAgICAgbC5kZWxldGUobGlzdGVuZXIpO1xuICAgICAgICAhbC5zaXplICYmIHN1YnMuZGVsZXRlKGtleSk7XG4gICAgICB9KTtcbiAgICB9XG4gICAgcmV0dXJuIGZuKGtleSwgVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcgJiYgVHJhbnNpdGlvbi5zb3VyY2VzLmhhcyhub2RlKSA/IG5vZGUudFZhbHVlIDogbm9kZS52YWx1ZSk7XG4gIH07XG59XG5mdW5jdGlvbiBiYXRjaChmbikge1xuICByZXR1cm4gcnVuVXBkYXRlcyhmbiwgZmFsc2UpO1xufVxuZnVuY3Rpb24gdW50cmFjayhmbikge1xuICBpZiAoIUV4dGVybmFsU291cmNlQ29uZmlnICYmIExpc3RlbmVyID09PSBudWxsKSByZXR1cm4gZm4oKTtcbiAgY29uc3QgbGlzdGVuZXIgPSBMaXN0ZW5lcjtcbiAgTGlzdGVuZXIgPSBudWxsO1xuICB0cnkge1xuICAgIGlmIChFeHRlcm5hbFNvdXJjZUNvbmZpZykgcmV0dXJuIEV4dGVybmFsU291cmNlQ29uZmlnLnVudHJhY2soZm4pO1xuICAgIHJldHVybiBmbigpO1xuICB9IGZpbmFsbHkge1xuICAgIExpc3RlbmVyID0gbGlzdGVuZXI7XG4gIH1cbn1cbmZ1bmN0aW9uIG9uKGRlcHMsIGZuLCBvcHRpb25zKSB7XG4gIGNvbnN0IGlzQXJyYXkgPSBBcnJheS5pc0FycmF5KGRlcHMpO1xuICBsZXQgcHJldklucHV0O1xuICBsZXQgZGVmZXIgPSBvcHRpb25zICYmIG9wdGlvbnMuZGVmZXI7XG4gIHJldHVybiBwcmV2VmFsdWUgPT4ge1xuICAgIGxldCBpbnB1dDtcbiAgICBpZiAoaXNBcnJheSkge1xuICAgICAgaW5wdXQgPSBBcnJheShkZXBzLmxlbmd0aCk7XG4gICAgICBmb3IgKGxldCBpID0gMDsgaSA8IGRlcHMubGVuZ3RoOyBpKyspIGlucHV0W2ldID0gZGVwc1tpXSgpO1xuICAgIH0gZWxzZSBpbnB1dCA9IGRlcHMoKTtcbiAgICBpZiAoZGVmZXIpIHtcbiAgICAgIGRlZmVyID0gZmFsc2U7XG4gICAgICByZXR1cm4gcHJldlZhbHVlO1xuICAgIH1cbiAgICBjb25zdCByZXN1bHQgPSB1bnRyYWNrKCgpID0+IGZuKGlucHV0LCBwcmV2SW5wdXQsIHByZXZWYWx1ZSkpO1xuICAgIHByZXZJbnB1dCA9IGlucHV0O1xuICAgIHJldHVybiByZXN1bHQ7XG4gIH07XG59XG5mdW5jdGlvbiBvbk1vdW50KGZuKSB7XG4gIGNyZWF0ZUVmZmVjdCgoKSA9PiB1bnRyYWNrKGZuKSk7XG59XG5mdW5jdGlvbiBvbkNsZWFudXAoZm4pIHtcbiAgaWYgKE93bmVyID09PSBudWxsKSA7ZWxzZSBpZiAoT3duZXIuY2xlYW51cHMgPT09IG51bGwpIE93bmVyLmNsZWFudXBzID0gW2ZuXTtlbHNlIE93bmVyLmNsZWFudXBzLnB1c2goZm4pO1xuICByZXR1cm4gZm47XG59XG5mdW5jdGlvbiBjYXRjaEVycm9yKGZuLCBoYW5kbGVyKSB7XG4gIEVSUk9SIHx8IChFUlJPUiA9IFN5bWJvbChcImVycm9yXCIpKTtcbiAgT3duZXIgPSBjcmVhdGVDb21wdXRhdGlvbih1bmRlZmluZWQsIHVuZGVmaW5lZCwgdHJ1ZSk7XG4gIE93bmVyLmNvbnRleHQgPSB7XG4gICAgLi4uT3duZXIuY29udGV4dCxcbiAgICBbRVJST1JdOiBbaGFuZGxlcl1cbiAgfTtcbiAgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nKSBUcmFuc2l0aW9uLnNvdXJjZXMuYWRkKE93bmVyKTtcbiAgdHJ5IHtcbiAgICByZXR1cm4gZm4oKTtcbiAgfSBjYXRjaCAoZXJyKSB7XG4gICAgaGFuZGxlRXJyb3IoZXJyKTtcbiAgfSBmaW5hbGx5IHtcbiAgICBPd25lciA9IE93bmVyLm93bmVyO1xuICB9XG59XG5mdW5jdGlvbiBnZXRMaXN0ZW5lcigpIHtcbiAgcmV0dXJuIExpc3RlbmVyO1xufVxuZnVuY3Rpb24gZ2V0T3duZXIoKSB7XG4gIHJldHVybiBPd25lcjtcbn1cbmZ1bmN0aW9uIHJ1bldpdGhPd25lcihvLCBmbikge1xuICBjb25zdCBwcmV2ID0gT3duZXI7XG4gIGNvbnN0IHByZXZMaXN0ZW5lciA9IExpc3RlbmVyO1xuICBPd25lciA9IG87XG4gIExpc3RlbmVyID0gbnVsbDtcbiAgdHJ5IHtcbiAgICByZXR1cm4gcnVuVXBkYXRlcyhmbiwgdHJ1ZSk7XG4gIH0gY2F0Y2ggKGVycikge1xuICAgIGhhbmRsZUVycm9yKGVycik7XG4gIH0gZmluYWxseSB7XG4gICAgT3duZXIgPSBwcmV2O1xuICAgIExpc3RlbmVyID0gcHJldkxpc3RlbmVyO1xuICB9XG59XG5mdW5jdGlvbiBlbmFibGVTY2hlZHVsaW5nKHNjaGVkdWxlciA9IHJlcXVlc3RDYWxsYmFjaykge1xuICBTY2hlZHVsZXIgPSBzY2hlZHVsZXI7XG59XG5mdW5jdGlvbiBzdGFydFRyYW5zaXRpb24oZm4pIHtcbiAgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nKSB7XG4gICAgZm4oKTtcbiAgICByZXR1cm4gVHJhbnNpdGlvbi5kb25lO1xuICB9XG4gIGNvbnN0IGwgPSBMaXN0ZW5lcjtcbiAgY29uc3QgbyA9IE93bmVyO1xuICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKCkudGhlbigoKSA9PiB7XG4gICAgTGlzdGVuZXIgPSBsO1xuICAgIE93bmVyID0gbztcbiAgICBsZXQgdDtcbiAgICBpZiAoU2NoZWR1bGVyIHx8IFN1c3BlbnNlQ29udGV4dCkge1xuICAgICAgdCA9IFRyYW5zaXRpb24gfHwgKFRyYW5zaXRpb24gPSB7XG4gICAgICAgIHNvdXJjZXM6IG5ldyBTZXQoKSxcbiAgICAgICAgZWZmZWN0czogW10sXG4gICAgICAgIHByb21pc2VzOiBuZXcgU2V0KCksXG4gICAgICAgIGRpc3Bvc2VkOiBuZXcgU2V0KCksXG4gICAgICAgIHF1ZXVlOiBuZXcgU2V0KCksXG4gICAgICAgIHJ1bm5pbmc6IHRydWVcbiAgICAgIH0pO1xuICAgICAgdC5kb25lIHx8ICh0LmRvbmUgPSBuZXcgUHJvbWlzZShyZXMgPT4gdC5yZXNvbHZlID0gcmVzKSk7XG4gICAgICB0LnJ1bm5pbmcgPSB0cnVlO1xuICAgIH1cbiAgICBydW5VcGRhdGVzKGZuLCBmYWxzZSk7XG4gICAgTGlzdGVuZXIgPSBPd25lciA9IG51bGw7XG4gICAgcmV0dXJuIHQgPyB0LmRvbmUgOiB1bmRlZmluZWQ7XG4gIH0pO1xufVxuY29uc3QgW3RyYW5zUGVuZGluZywgc2V0VHJhbnNQZW5kaW5nXSA9IC8qQF9fUFVSRV9fKi9jcmVhdGVTaWduYWwoZmFsc2UpO1xuZnVuY3Rpb24gdXNlVHJhbnNpdGlvbigpIHtcbiAgcmV0dXJuIFt0cmFuc1BlbmRpbmcsIHN0YXJ0VHJhbnNpdGlvbl07XG59XG5mdW5jdGlvbiByZXN1bWVFZmZlY3RzKGUpIHtcbiAgRWZmZWN0cy5wdXNoLmFwcGx5KEVmZmVjdHMsIGUpO1xuICBlLmxlbmd0aCA9IDA7XG59XG5mdW5jdGlvbiBjcmVhdGVDb250ZXh0KGRlZmF1bHRWYWx1ZSwgb3B0aW9ucykge1xuICBjb25zdCBpZCA9IFN5bWJvbChcImNvbnRleHRcIik7XG4gIHJldHVybiB7XG4gICAgaWQsXG4gICAgUHJvdmlkZXI6IGNyZWF0ZVByb3ZpZGVyKGlkKSxcbiAgICBkZWZhdWx0VmFsdWVcbiAgfTtcbn1cbmZ1bmN0aW9uIHVzZUNvbnRleHQoY29udGV4dCkge1xuICBsZXQgdmFsdWU7XG4gIHJldHVybiBPd25lciAmJiBPd25lci5jb250ZXh0ICYmICh2YWx1ZSA9IE93bmVyLmNvbnRleHRbY29udGV4dC5pZF0pICE9PSB1bmRlZmluZWQgPyB2YWx1ZSA6IGNvbnRleHQuZGVmYXVsdFZhbHVlO1xufVxuZnVuY3Rpb24gY2hpbGRyZW4oZm4pIHtcbiAgY29uc3QgY2hpbGRyZW4gPSBjcmVhdGVNZW1vKGZuKTtcbiAgY29uc3QgbWVtbyA9IGNyZWF0ZU1lbW8oKCkgPT4gcmVzb2x2ZUNoaWxkcmVuKGNoaWxkcmVuKCkpKTtcbiAgbWVtby50b0FycmF5ID0gKCkgPT4ge1xuICAgIGNvbnN0IGMgPSBtZW1vKCk7XG4gICAgcmV0dXJuIEFycmF5LmlzQXJyYXkoYykgPyBjIDogYyAhPSBudWxsID8gW2NdIDogW107XG4gIH07XG4gIHJldHVybiBtZW1vO1xufVxubGV0IFN1c3BlbnNlQ29udGV4dDtcbmZ1bmN0aW9uIGdldFN1c3BlbnNlQ29udGV4dCgpIHtcbiAgcmV0dXJuIFN1c3BlbnNlQ29udGV4dCB8fCAoU3VzcGVuc2VDb250ZXh0ID0gY3JlYXRlQ29udGV4dCgpKTtcbn1cbmZ1bmN0aW9uIGVuYWJsZUV4dGVybmFsU291cmNlKGZhY3RvcnksIHVudHJhY2sgPSBmbiA9PiBmbigpKSB7XG4gIGlmIChFeHRlcm5hbFNvdXJjZUNvbmZpZykge1xuICAgIGNvbnN0IHtcbiAgICAgIGZhY3Rvcnk6IG9sZEZhY3RvcnksXG4gICAgICB1bnRyYWNrOiBvbGRVbnRyYWNrXG4gICAgfSA9IEV4dGVybmFsU291cmNlQ29uZmlnO1xuICAgIEV4dGVybmFsU291cmNlQ29uZmlnID0ge1xuICAgICAgZmFjdG9yeTogKGZuLCB0cmlnZ2VyKSA9PiB7XG4gICAgICAgIGNvbnN0IG9sZFNvdXJjZSA9IG9sZEZhY3RvcnkoZm4sIHRyaWdnZXIpO1xuICAgICAgICBjb25zdCBzb3VyY2UgPSBmYWN0b3J5KHggPT4gb2xkU291cmNlLnRyYWNrKHgpLCB0cmlnZ2VyKTtcbiAgICAgICAgcmV0dXJuIHtcbiAgICAgICAgICB0cmFjazogeCA9PiBzb3VyY2UudHJhY2soeCksXG4gICAgICAgICAgZGlzcG9zZSgpIHtcbiAgICAgICAgICAgIHNvdXJjZS5kaXNwb3NlKCk7XG4gICAgICAgICAgICBvbGRTb3VyY2UuZGlzcG9zZSgpO1xuICAgICAgICAgIH1cbiAgICAgICAgfTtcbiAgICAgIH0sXG4gICAgICB1bnRyYWNrOiBmbiA9PiBvbGRVbnRyYWNrKCgpID0+IHVudHJhY2soZm4pKVxuICAgIH07XG4gIH0gZWxzZSB7XG4gICAgRXh0ZXJuYWxTb3VyY2VDb25maWcgPSB7XG4gICAgICBmYWN0b3J5LFxuICAgICAgdW50cmFja1xuICAgIH07XG4gIH1cbn1cbmZ1bmN0aW9uIHJlYWRTaWduYWwoKSB7XG4gIGNvbnN0IHJ1bm5pbmdUcmFuc2l0aW9uID0gVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmc7XG4gIGlmICh0aGlzLnNvdXJjZXMgJiYgKHJ1bm5pbmdUcmFuc2l0aW9uID8gdGhpcy50U3RhdGUgOiB0aGlzLnN0YXRlKSkge1xuICAgIGlmICgocnVubmluZ1RyYW5zaXRpb24gPyB0aGlzLnRTdGF0ZSA6IHRoaXMuc3RhdGUpID09PSBTVEFMRSkgdXBkYXRlQ29tcHV0YXRpb24odGhpcyk7ZWxzZSB7XG4gICAgICBjb25zdCB1cGRhdGVzID0gVXBkYXRlcztcbiAgICAgIFVwZGF0ZXMgPSBudWxsO1xuICAgICAgcnVuVXBkYXRlcygoKSA9PiBsb29rVXBzdHJlYW0odGhpcyksIGZhbHNlKTtcbiAgICAgIFVwZGF0ZXMgPSB1cGRhdGVzO1xuICAgIH1cbiAgfVxuICBpZiAoTGlzdGVuZXIpIHtcbiAgICBjb25zdCBzU2xvdCA9IHRoaXMub2JzZXJ2ZXJzID8gdGhpcy5vYnNlcnZlcnMubGVuZ3RoIDogMDtcbiAgICBpZiAoIUxpc3RlbmVyLnNvdXJjZXMpIHtcbiAgICAgIExpc3RlbmVyLnNvdXJjZXMgPSBbdGhpc107XG4gICAgICBMaXN0ZW5lci5zb3VyY2VTbG90cyA9IFtzU2xvdF07XG4gICAgfSBlbHNlIHtcbiAgICAgIExpc3RlbmVyLnNvdXJjZXMucHVzaCh0aGlzKTtcbiAgICAgIExpc3RlbmVyLnNvdXJjZVNsb3RzLnB1c2goc1Nsb3QpO1xuICAgIH1cbiAgICBpZiAoIXRoaXMub2JzZXJ2ZXJzKSB7XG4gICAgICB0aGlzLm9ic2VydmVycyA9IFtMaXN0ZW5lcl07XG4gICAgICB0aGlzLm9ic2VydmVyU2xvdHMgPSBbTGlzdGVuZXIuc291cmNlcy5sZW5ndGggLSAxXTtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5vYnNlcnZlcnMucHVzaChMaXN0ZW5lcik7XG4gICAgICB0aGlzLm9ic2VydmVyU2xvdHMucHVzaChMaXN0ZW5lci5zb3VyY2VzLmxlbmd0aCAtIDEpO1xuICAgIH1cbiAgfVxuICBpZiAocnVubmluZ1RyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5zb3VyY2VzLmhhcyh0aGlzKSkgcmV0dXJuIHRoaXMudFZhbHVlO1xuICByZXR1cm4gdGhpcy52YWx1ZTtcbn1cbmZ1bmN0aW9uIHdyaXRlU2lnbmFsKG5vZGUsIHZhbHVlLCBpc0NvbXApIHtcbiAgbGV0IGN1cnJlbnQgPSBUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZyAmJiBUcmFuc2l0aW9uLnNvdXJjZXMuaGFzKG5vZGUpID8gbm9kZS50VmFsdWUgOiBub2RlLnZhbHVlO1xuICBpZiAoIW5vZGUuY29tcGFyYXRvciB8fCAhbm9kZS5jb21wYXJhdG9yKGN1cnJlbnQsIHZhbHVlKSkge1xuICAgIGlmIChUcmFuc2l0aW9uKSB7XG4gICAgICBjb25zdCBUcmFuc2l0aW9uUnVubmluZyA9IFRyYW5zaXRpb24ucnVubmluZztcbiAgICAgIGlmIChUcmFuc2l0aW9uUnVubmluZyB8fCAhaXNDb21wICYmIFRyYW5zaXRpb24uc291cmNlcy5oYXMobm9kZSkpIHtcbiAgICAgICAgVHJhbnNpdGlvbi5zb3VyY2VzLmFkZChub2RlKTtcbiAgICAgICAgbm9kZS50VmFsdWUgPSB2YWx1ZTtcbiAgICAgIH1cbiAgICAgIGlmICghVHJhbnNpdGlvblJ1bm5pbmcpIG5vZGUudmFsdWUgPSB2YWx1ZTtcbiAgICB9IGVsc2Ugbm9kZS52YWx1ZSA9IHZhbHVlO1xuICAgIGlmIChub2RlLm9ic2VydmVycyAmJiBub2RlLm9ic2VydmVycy5sZW5ndGgpIHtcbiAgICAgIHJ1blVwZGF0ZXMoKCkgPT4ge1xuICAgICAgICBmb3IgKGxldCBpID0gMDsgaSA8IG5vZGUub2JzZXJ2ZXJzLmxlbmd0aDsgaSArPSAxKSB7XG4gICAgICAgICAgY29uc3QgbyA9IG5vZGUub2JzZXJ2ZXJzW2ldO1xuICAgICAgICAgIGNvbnN0IFRyYW5zaXRpb25SdW5uaW5nID0gVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmc7XG4gICAgICAgICAgaWYgKFRyYW5zaXRpb25SdW5uaW5nICYmIFRyYW5zaXRpb24uZGlzcG9zZWQuaGFzKG8pKSBjb250aW51ZTtcbiAgICAgICAgICBpZiAoVHJhbnNpdGlvblJ1bm5pbmcgPyAhby50U3RhdGUgOiAhby5zdGF0ZSkge1xuICAgICAgICAgICAgaWYgKG8ucHVyZSkgVXBkYXRlcy5wdXNoKG8pO2Vsc2UgRWZmZWN0cy5wdXNoKG8pO1xuICAgICAgICAgICAgaWYgKG8ub2JzZXJ2ZXJzKSBtYXJrRG93bnN0cmVhbShvKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgaWYgKCFUcmFuc2l0aW9uUnVubmluZykgby5zdGF0ZSA9IFNUQUxFO2Vsc2Ugby50U3RhdGUgPSBTVEFMRTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoVXBkYXRlcy5sZW5ndGggPiAxMGU1KSB7XG4gICAgICAgICAgVXBkYXRlcyA9IFtdO1xuICAgICAgICAgIGlmIChJU19ERVYpIDtcbiAgICAgICAgICB0aHJvdyBuZXcgRXJyb3IoKTtcbiAgICAgICAgfVxuICAgICAgfSwgZmFsc2UpO1xuICAgIH1cbiAgfVxuICByZXR1cm4gdmFsdWU7XG59XG5mdW5jdGlvbiB1cGRhdGVDb21wdXRhdGlvbihub2RlKSB7XG4gIGlmICghbm9kZS5mbikgcmV0dXJuO1xuICBjbGVhbk5vZGUobm9kZSk7XG4gIGNvbnN0IHRpbWUgPSBFeGVjQ291bnQ7XG4gIHJ1bkNvbXB1dGF0aW9uKG5vZGUsIFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nICYmIFRyYW5zaXRpb24uc291cmNlcy5oYXMobm9kZSkgPyBub2RlLnRWYWx1ZSA6IG5vZGUudmFsdWUsIHRpbWUpO1xuICBpZiAoVHJhbnNpdGlvbiAmJiAhVHJhbnNpdGlvbi5ydW5uaW5nICYmIFRyYW5zaXRpb24uc291cmNlcy5oYXMobm9kZSkpIHtcbiAgICBxdWV1ZU1pY3JvdGFzaygoKSA9PiB7XG4gICAgICBydW5VcGRhdGVzKCgpID0+IHtcbiAgICAgICAgVHJhbnNpdGlvbiAmJiAoVHJhbnNpdGlvbi5ydW5uaW5nID0gdHJ1ZSk7XG4gICAgICAgIExpc3RlbmVyID0gT3duZXIgPSBub2RlO1xuICAgICAgICBydW5Db21wdXRhdGlvbihub2RlLCBub2RlLnRWYWx1ZSwgdGltZSk7XG4gICAgICAgIExpc3RlbmVyID0gT3duZXIgPSBudWxsO1xuICAgICAgfSwgZmFsc2UpO1xuICAgIH0pO1xuICB9XG59XG5mdW5jdGlvbiBydW5Db21wdXRhdGlvbihub2RlLCB2YWx1ZSwgdGltZSkge1xuICBsZXQgbmV4dFZhbHVlO1xuICBjb25zdCBvd25lciA9IE93bmVyLFxuICAgIGxpc3RlbmVyID0gTGlzdGVuZXI7XG4gIExpc3RlbmVyID0gT3duZXIgPSBub2RlO1xuICB0cnkge1xuICAgIG5leHRWYWx1ZSA9IG5vZGUuZm4odmFsdWUpO1xuICB9IGNhdGNoIChlcnIpIHtcbiAgICBpZiAobm9kZS5wdXJlKSB7XG4gICAgICBpZiAoVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcpIHtcbiAgICAgICAgbm9kZS50U3RhdGUgPSBTVEFMRTtcbiAgICAgICAgbm9kZS50T3duZWQgJiYgbm9kZS50T3duZWQuZm9yRWFjaChjbGVhbk5vZGUpO1xuICAgICAgICBub2RlLnRPd25lZCA9IHVuZGVmaW5lZDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIG5vZGUuc3RhdGUgPSBTVEFMRTtcbiAgICAgICAgbm9kZS5vd25lZCAmJiBub2RlLm93bmVkLmZvckVhY2goY2xlYW5Ob2RlKTtcbiAgICAgICAgbm9kZS5vd25lZCA9IG51bGw7XG4gICAgICB9XG4gICAgfVxuICAgIG5vZGUudXBkYXRlZEF0ID0gdGltZSArIDE7XG4gICAgcmV0dXJuIGhhbmRsZUVycm9yKGVycik7XG4gIH0gZmluYWxseSB7XG4gICAgTGlzdGVuZXIgPSBsaXN0ZW5lcjtcbiAgICBPd25lciA9IG93bmVyO1xuICB9XG4gIGlmICghbm9kZS51cGRhdGVkQXQgfHwgbm9kZS51cGRhdGVkQXQgPD0gdGltZSkge1xuICAgIGlmIChub2RlLnVwZGF0ZWRBdCAhPSBudWxsICYmIFwib2JzZXJ2ZXJzXCIgaW4gbm9kZSkge1xuICAgICAgd3JpdGVTaWduYWwobm9kZSwgbmV4dFZhbHVlLCB0cnVlKTtcbiAgICB9IGVsc2UgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nICYmIG5vZGUucHVyZSkge1xuICAgICAgaWYgKCFUcmFuc2l0aW9uLnNvdXJjZXMuaGFzKG5vZGUpKSBub2RlLnZhbHVlID0gbmV4dFZhbHVlO1xuICAgICAgVHJhbnNpdGlvbi5zb3VyY2VzLmFkZChub2RlKTtcbiAgICAgIG5vZGUudFZhbHVlID0gbmV4dFZhbHVlO1xuICAgIH0gZWxzZSBub2RlLnZhbHVlID0gbmV4dFZhbHVlO1xuICAgIG5vZGUudXBkYXRlZEF0ID0gdGltZTtcbiAgfVxufVxuZnVuY3Rpb24gY3JlYXRlQ29tcHV0YXRpb24oZm4sIGluaXQsIHB1cmUsIHN0YXRlID0gU1RBTEUsIG9wdGlvbnMpIHtcbiAgY29uc3QgYyA9IHtcbiAgICBmbixcbiAgICBzdGF0ZTogc3RhdGUsXG4gICAgdXBkYXRlZEF0OiBudWxsLFxuICAgIG93bmVkOiBudWxsLFxuICAgIHNvdXJjZXM6IG51bGwsXG4gICAgc291cmNlU2xvdHM6IG51bGwsXG4gICAgY2xlYW51cHM6IG51bGwsXG4gICAgdmFsdWU6IGluaXQsXG4gICAgb3duZXI6IE93bmVyLFxuICAgIGNvbnRleHQ6IE93bmVyID8gT3duZXIuY29udGV4dCA6IG51bGwsXG4gICAgcHVyZVxuICB9O1xuICBpZiAoVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcpIHtcbiAgICBjLnN0YXRlID0gMDtcbiAgICBjLnRTdGF0ZSA9IHN0YXRlO1xuICB9XG4gIGlmIChPd25lciA9PT0gbnVsbCkgO2Vsc2UgaWYgKE93bmVyICE9PSBVTk9XTkVEKSB7XG4gICAgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nICYmIE93bmVyLnB1cmUpIHtcbiAgICAgIGlmICghT3duZXIudE93bmVkKSBPd25lci50T3duZWQgPSBbY107ZWxzZSBPd25lci50T3duZWQucHVzaChjKTtcbiAgICB9IGVsc2Uge1xuICAgICAgaWYgKCFPd25lci5vd25lZCkgT3duZXIub3duZWQgPSBbY107ZWxzZSBPd25lci5vd25lZC5wdXNoKGMpO1xuICAgIH1cbiAgfVxuICBpZiAoRXh0ZXJuYWxTb3VyY2VDb25maWcgJiYgYy5mbikge1xuICAgIGNvbnN0IHNvdXJjZUZuID0gYy5mbjtcbiAgICBjb25zdCBbdHJhY2ssIHRyaWdnZXJdID0gY3JlYXRlU2lnbmFsKHVuZGVmaW5lZCwge1xuICAgICAgZXF1YWxzOiBmYWxzZVxuICAgIH0pO1xuICAgIGNvbnN0IG9yZGluYXJ5ID0gRXh0ZXJuYWxTb3VyY2VDb25maWcuZmFjdG9yeShzb3VyY2VGbiwgdHJpZ2dlcik7XG4gICAgb25DbGVhbnVwKCgpID0+IG9yZGluYXJ5LmRpc3Bvc2UoKSk7XG4gICAgbGV0IGluVHJhbnNpdGlvbjtcbiAgICBjb25zdCB0cmlnZ2VySW5UcmFuc2l0aW9uID0gKCkgPT4gc3RhcnRUcmFuc2l0aW9uKHRyaWdnZXIpLnRoZW4oKCkgPT4ge1xuICAgICAgaWYgKGluVHJhbnNpdGlvbikge1xuICAgICAgICBpblRyYW5zaXRpb24uZGlzcG9zZSgpO1xuICAgICAgICBpblRyYW5zaXRpb24gPSB1bmRlZmluZWQ7XG4gICAgICB9XG4gICAgfSk7XG4gICAgYy5mbiA9IHggPT4ge1xuICAgICAgdHJhY2soKTtcbiAgICAgIGlmIChUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZykge1xuICAgICAgICBpZiAoIWluVHJhbnNpdGlvbikgaW5UcmFuc2l0aW9uID0gRXh0ZXJuYWxTb3VyY2VDb25maWcuZmFjdG9yeShzb3VyY2VGbiwgdHJpZ2dlckluVHJhbnNpdGlvbik7XG4gICAgICAgIHJldHVybiBpblRyYW5zaXRpb24udHJhY2soeCk7XG4gICAgICB9XG4gICAgICByZXR1cm4gb3JkaW5hcnkudHJhY2soeCk7XG4gICAgfTtcbiAgfVxuICByZXR1cm4gYztcbn1cbmZ1bmN0aW9uIHJ1blRvcChub2RlKSB7XG4gIGNvbnN0IHJ1bm5pbmdUcmFuc2l0aW9uID0gVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmc7XG4gIGlmICgocnVubmluZ1RyYW5zaXRpb24gPyBub2RlLnRTdGF0ZSA6IG5vZGUuc3RhdGUpID09PSAwKSByZXR1cm47XG4gIGlmICgocnVubmluZ1RyYW5zaXRpb24gPyBub2RlLnRTdGF0ZSA6IG5vZGUuc3RhdGUpID09PSBQRU5ESU5HKSByZXR1cm4gbG9va1Vwc3RyZWFtKG5vZGUpO1xuICBpZiAobm9kZS5zdXNwZW5zZSAmJiB1bnRyYWNrKG5vZGUuc3VzcGVuc2UuaW5GYWxsYmFjaykpIHJldHVybiBub2RlLnN1c3BlbnNlLmVmZmVjdHMucHVzaChub2RlKTtcbiAgY29uc3QgYW5jZXN0b3JzID0gW25vZGVdO1xuICB3aGlsZSAoKG5vZGUgPSBub2RlLm93bmVyKSAmJiAoIW5vZGUudXBkYXRlZEF0IHx8IG5vZGUudXBkYXRlZEF0IDwgRXhlY0NvdW50KSkge1xuICAgIGlmIChydW5uaW5nVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLmRpc3Bvc2VkLmhhcyhub2RlKSkgcmV0dXJuO1xuICAgIGlmIChydW5uaW5nVHJhbnNpdGlvbiA/IG5vZGUudFN0YXRlIDogbm9kZS5zdGF0ZSkgYW5jZXN0b3JzLnB1c2gobm9kZSk7XG4gIH1cbiAgZm9yIChsZXQgaSA9IGFuY2VzdG9ycy5sZW5ndGggLSAxOyBpID49IDA7IGktLSkge1xuICAgIG5vZGUgPSBhbmNlc3RvcnNbaV07XG4gICAgaWYgKHJ1bm5pbmdUcmFuc2l0aW9uKSB7XG4gICAgICBsZXQgdG9wID0gbm9kZSxcbiAgICAgICAgcHJldiA9IGFuY2VzdG9yc1tpICsgMV07XG4gICAgICB3aGlsZSAoKHRvcCA9IHRvcC5vd25lcikgJiYgdG9wICE9PSBwcmV2KSB7XG4gICAgICAgIGlmIChUcmFuc2l0aW9uLmRpc3Bvc2VkLmhhcyh0b3ApKSByZXR1cm47XG4gICAgICB9XG4gICAgfVxuICAgIGlmICgocnVubmluZ1RyYW5zaXRpb24gPyBub2RlLnRTdGF0ZSA6IG5vZGUuc3RhdGUpID09PSBTVEFMRSkge1xuICAgICAgdXBkYXRlQ29tcHV0YXRpb24obm9kZSk7XG4gICAgfSBlbHNlIGlmICgocnVubmluZ1RyYW5zaXRpb24gPyBub2RlLnRTdGF0ZSA6IG5vZGUuc3RhdGUpID09PSBQRU5ESU5HKSB7XG4gICAgICBjb25zdCB1cGRhdGVzID0gVXBkYXRlcztcbiAgICAgIFVwZGF0ZXMgPSBudWxsO1xuICAgICAgcnVuVXBkYXRlcygoKSA9PiBsb29rVXBzdHJlYW0obm9kZSwgYW5jZXN0b3JzWzBdKSwgZmFsc2UpO1xuICAgICAgVXBkYXRlcyA9IHVwZGF0ZXM7XG4gICAgfVxuICB9XG59XG5mdW5jdGlvbiBydW5VcGRhdGVzKGZuLCBpbml0KSB7XG4gIGlmIChVcGRhdGVzKSByZXR1cm4gZm4oKTtcbiAgbGV0IHdhaXQgPSBmYWxzZTtcbiAgaWYgKCFpbml0KSBVcGRhdGVzID0gW107XG4gIGlmIChFZmZlY3RzKSB3YWl0ID0gdHJ1ZTtlbHNlIEVmZmVjdHMgPSBbXTtcbiAgRXhlY0NvdW50Kys7XG4gIHRyeSB7XG4gICAgY29uc3QgcmVzID0gZm4oKTtcbiAgICBjb21wbGV0ZVVwZGF0ZXMod2FpdCk7XG4gICAgcmV0dXJuIHJlcztcbiAgfSBjYXRjaCAoZXJyKSB7XG4gICAgaWYgKCF3YWl0KSBFZmZlY3RzID0gbnVsbDtcbiAgICBVcGRhdGVzID0gbnVsbDtcbiAgICBoYW5kbGVFcnJvcihlcnIpO1xuICB9XG59XG5mdW5jdGlvbiBjb21wbGV0ZVVwZGF0ZXMod2FpdCkge1xuICBpZiAoVXBkYXRlcykge1xuICAgIGlmIChTY2hlZHVsZXIgJiYgVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmcpIHNjaGVkdWxlUXVldWUoVXBkYXRlcyk7ZWxzZSBydW5RdWV1ZShVcGRhdGVzKTtcbiAgICBVcGRhdGVzID0gbnVsbDtcbiAgfVxuICBpZiAod2FpdCkgcmV0dXJuO1xuICBsZXQgcmVzO1xuICBpZiAoVHJhbnNpdGlvbikge1xuICAgIGlmICghVHJhbnNpdGlvbi5wcm9taXNlcy5zaXplICYmICFUcmFuc2l0aW9uLnF1ZXVlLnNpemUpIHtcbiAgICAgIGNvbnN0IHNvdXJjZXMgPSBUcmFuc2l0aW9uLnNvdXJjZXM7XG4gICAgICBjb25zdCBkaXNwb3NlZCA9IFRyYW5zaXRpb24uZGlzcG9zZWQ7XG4gICAgICBFZmZlY3RzLnB1c2guYXBwbHkoRWZmZWN0cywgVHJhbnNpdGlvbi5lZmZlY3RzKTtcbiAgICAgIHJlcyA9IFRyYW5zaXRpb24ucmVzb2x2ZTtcbiAgICAgIGZvciAoY29uc3QgZSBvZiBFZmZlY3RzKSB7XG4gICAgICAgIFwidFN0YXRlXCIgaW4gZSAmJiAoZS5zdGF0ZSA9IGUudFN0YXRlKTtcbiAgICAgICAgZGVsZXRlIGUudFN0YXRlO1xuICAgICAgfVxuICAgICAgVHJhbnNpdGlvbiA9IG51bGw7XG4gICAgICBydW5VcGRhdGVzKCgpID0+IHtcbiAgICAgICAgZm9yIChjb25zdCBkIG9mIGRpc3Bvc2VkKSBjbGVhbk5vZGUoZCk7XG4gICAgICAgIGZvciAoY29uc3QgdiBvZiBzb3VyY2VzKSB7XG4gICAgICAgICAgdi52YWx1ZSA9IHYudFZhbHVlO1xuICAgICAgICAgIGlmICh2Lm93bmVkKSB7XG4gICAgICAgICAgICBmb3IgKGxldCBpID0gMCwgbGVuID0gdi5vd25lZC5sZW5ndGg7IGkgPCBsZW47IGkrKykgY2xlYW5Ob2RlKHYub3duZWRbaV0pO1xuICAgICAgICAgIH1cbiAgICAgICAgICBpZiAodi50T3duZWQpIHYub3duZWQgPSB2LnRPd25lZDtcbiAgICAgICAgICBkZWxldGUgdi50VmFsdWU7XG4gICAgICAgICAgZGVsZXRlIHYudE93bmVkO1xuICAgICAgICAgIHYudFN0YXRlID0gMDtcbiAgICAgICAgfVxuICAgICAgICBzZXRUcmFuc1BlbmRpbmcoZmFsc2UpO1xuICAgICAgfSwgZmFsc2UpO1xuICAgIH0gZWxzZSBpZiAoVHJhbnNpdGlvbi5ydW5uaW5nKSB7XG4gICAgICBUcmFuc2l0aW9uLnJ1bm5pbmcgPSBmYWxzZTtcbiAgICAgIFRyYW5zaXRpb24uZWZmZWN0cy5wdXNoLmFwcGx5KFRyYW5zaXRpb24uZWZmZWN0cywgRWZmZWN0cyk7XG4gICAgICBFZmZlY3RzID0gbnVsbDtcbiAgICAgIHNldFRyYW5zUGVuZGluZyh0cnVlKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gIH1cbiAgY29uc3QgZSA9IEVmZmVjdHM7XG4gIEVmZmVjdHMgPSBudWxsO1xuICBpZiAoZS5sZW5ndGgpIHJ1blVwZGF0ZXMoKCkgPT4gcnVuRWZmZWN0cyhlKSwgZmFsc2UpO1xuICBpZiAocmVzKSByZXMoKTtcbn1cbmZ1bmN0aW9uIHJ1blF1ZXVlKHF1ZXVlKSB7XG4gIGZvciAobGV0IGkgPSAwOyBpIDwgcXVldWUubGVuZ3RoOyBpKyspIHJ1blRvcChxdWV1ZVtpXSk7XG59XG5mdW5jdGlvbiBzY2hlZHVsZVF1ZXVlKHF1ZXVlKSB7XG4gIGZvciAobGV0IGkgPSAwOyBpIDwgcXVldWUubGVuZ3RoOyBpKyspIHtcbiAgICBjb25zdCBpdGVtID0gcXVldWVbaV07XG4gICAgY29uc3QgdGFza3MgPSBUcmFuc2l0aW9uLnF1ZXVlO1xuICAgIGlmICghdGFza3MuaGFzKGl0ZW0pKSB7XG4gICAgICB0YXNrcy5hZGQoaXRlbSk7XG4gICAgICBTY2hlZHVsZXIoKCkgPT4ge1xuICAgICAgICB0YXNrcy5kZWxldGUoaXRlbSk7XG4gICAgICAgIHJ1blVwZGF0ZXMoKCkgPT4ge1xuICAgICAgICAgIFRyYW5zaXRpb24ucnVubmluZyA9IHRydWU7XG4gICAgICAgICAgcnVuVG9wKGl0ZW0pO1xuICAgICAgICB9LCBmYWxzZSk7XG4gICAgICAgIFRyYW5zaXRpb24gJiYgKFRyYW5zaXRpb24ucnVubmluZyA9IGZhbHNlKTtcbiAgICAgIH0pO1xuICAgIH1cbiAgfVxufVxuZnVuY3Rpb24gcnVuVXNlckVmZmVjdHMocXVldWUpIHtcbiAgbGV0IGksXG4gICAgdXNlckxlbmd0aCA9IDA7XG4gIGZvciAoaSA9IDA7IGkgPCBxdWV1ZS5sZW5ndGg7IGkrKykge1xuICAgIGNvbnN0IGUgPSBxdWV1ZVtpXTtcbiAgICBpZiAoIWUudXNlcikgcnVuVG9wKGUpO2Vsc2UgcXVldWVbdXNlckxlbmd0aCsrXSA9IGU7XG4gIH1cbiAgaWYgKHNoYXJlZENvbmZpZy5jb250ZXh0KSB7XG4gICAgaWYgKHNoYXJlZENvbmZpZy5jb3VudCkge1xuICAgICAgc2hhcmVkQ29uZmlnLmVmZmVjdHMgfHwgKHNoYXJlZENvbmZpZy5lZmZlY3RzID0gW10pO1xuICAgICAgc2hhcmVkQ29uZmlnLmVmZmVjdHMucHVzaCguLi5xdWV1ZS5zbGljZSgwLCB1c2VyTGVuZ3RoKSk7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHNldEh5ZHJhdGVDb250ZXh0KCk7XG4gIH1cbiAgaWYgKHNoYXJlZENvbmZpZy5lZmZlY3RzICYmIChzaGFyZWRDb25maWcuZG9uZSB8fCAhc2hhcmVkQ29uZmlnLmNvdW50KSkge1xuICAgIHF1ZXVlID0gWy4uLnNoYXJlZENvbmZpZy5lZmZlY3RzLCAuLi5xdWV1ZV07XG4gICAgdXNlckxlbmd0aCArPSBzaGFyZWRDb25maWcuZWZmZWN0cy5sZW5ndGg7XG4gICAgZGVsZXRlIHNoYXJlZENvbmZpZy5lZmZlY3RzO1xuICB9XG4gIGZvciAoaSA9IDA7IGkgPCB1c2VyTGVuZ3RoOyBpKyspIHJ1blRvcChxdWV1ZVtpXSk7XG59XG5mdW5jdGlvbiBsb29rVXBzdHJlYW0obm9kZSwgaWdub3JlKSB7XG4gIGNvbnN0IHJ1bm5pbmdUcmFuc2l0aW9uID0gVHJhbnNpdGlvbiAmJiBUcmFuc2l0aW9uLnJ1bm5pbmc7XG4gIGlmIChydW5uaW5nVHJhbnNpdGlvbikgbm9kZS50U3RhdGUgPSAwO2Vsc2Ugbm9kZS5zdGF0ZSA9IDA7XG4gIGZvciAobGV0IGkgPSAwOyBpIDwgbm9kZS5zb3VyY2VzLmxlbmd0aDsgaSArPSAxKSB7XG4gICAgY29uc3Qgc291cmNlID0gbm9kZS5zb3VyY2VzW2ldO1xuICAgIGlmIChzb3VyY2Uuc291cmNlcykge1xuICAgICAgY29uc3Qgc3RhdGUgPSBydW5uaW5nVHJhbnNpdGlvbiA/IHNvdXJjZS50U3RhdGUgOiBzb3VyY2Uuc3RhdGU7XG4gICAgICBpZiAoc3RhdGUgPT09IFNUQUxFKSB7XG4gICAgICAgIGlmIChzb3VyY2UgIT09IGlnbm9yZSAmJiAoIXNvdXJjZS51cGRhdGVkQXQgfHwgc291cmNlLnVwZGF0ZWRBdCA8IEV4ZWNDb3VudCkpIHJ1blRvcChzb3VyY2UpO1xuICAgICAgfSBlbHNlIGlmIChzdGF0ZSA9PT0gUEVORElORykgbG9va1Vwc3RyZWFtKHNvdXJjZSwgaWdub3JlKTtcbiAgICB9XG4gIH1cbn1cbmZ1bmN0aW9uIG1hcmtEb3duc3RyZWFtKG5vZGUpIHtcbiAgY29uc3QgcnVubmluZ1RyYW5zaXRpb24gPSBUcmFuc2l0aW9uICYmIFRyYW5zaXRpb24ucnVubmluZztcbiAgZm9yIChsZXQgaSA9IDA7IGkgPCBub2RlLm9ic2VydmVycy5sZW5ndGg7IGkgKz0gMSkge1xuICAgIGNvbnN0IG8gPSBub2RlLm9ic2VydmVyc1tpXTtcbiAgICBpZiAocnVubmluZ1RyYW5zaXRpb24gPyAhby50U3RhdGUgOiAhby5zdGF0ZSkge1xuICAgICAgaWYgKHJ1bm5pbmdUcmFuc2l0aW9uKSBvLnRTdGF0ZSA9IFBFTkRJTkc7ZWxzZSBvLnN0YXRlID0gUEVORElORztcbiAgICAgIGlmIChvLnB1cmUpIFVwZGF0ZXMucHVzaChvKTtlbHNlIEVmZmVjdHMucHVzaChvKTtcbiAgICAgIG8ub2JzZXJ2ZXJzICYmIG1hcmtEb3duc3RyZWFtKG8pO1xuICAgIH1cbiAgfVxufVxuZnVuY3Rpb24gY2xlYW5Ob2RlKG5vZGUpIHtcbiAgbGV0IGk7XG4gIGlmIChub2RlLnNvdXJjZXMpIHtcbiAgICB3aGlsZSAobm9kZS5zb3VyY2VzLmxlbmd0aCkge1xuICAgICAgY29uc3Qgc291cmNlID0gbm9kZS5zb3VyY2VzLnBvcCgpLFxuICAgICAgICBpbmRleCA9IG5vZGUuc291cmNlU2xvdHMucG9wKCksXG4gICAgICAgIG9icyA9IHNvdXJjZS5vYnNlcnZlcnM7XG4gICAgICBpZiAob2JzICYmIG9icy5sZW5ndGgpIHtcbiAgICAgICAgY29uc3QgbiA9IG9icy5wb3AoKSxcbiAgICAgICAgICBzID0gc291cmNlLm9ic2VydmVyU2xvdHMucG9wKCk7XG4gICAgICAgIGlmIChpbmRleCA8IG9icy5sZW5ndGgpIHtcbiAgICAgICAgICBuLnNvdXJjZVNsb3RzW3NdID0gaW5kZXg7XG4gICAgICAgICAgb2JzW2luZGV4XSA9IG47XG4gICAgICAgICAgc291cmNlLm9ic2VydmVyU2xvdHNbaW5kZXhdID0gcztcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgfVxuICBpZiAobm9kZS50T3duZWQpIHtcbiAgICBmb3IgKGkgPSBub2RlLnRPd25lZC5sZW5ndGggLSAxOyBpID49IDA7IGktLSkgY2xlYW5Ob2RlKG5vZGUudE93bmVkW2ldKTtcbiAgICBkZWxldGUgbm9kZS50T3duZWQ7XG4gIH1cbiAgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nICYmIG5vZGUucHVyZSkge1xuICAgIHJlc2V0KG5vZGUsIHRydWUpO1xuICB9IGVsc2UgaWYgKG5vZGUub3duZWQpIHtcbiAgICBmb3IgKGkgPSBub2RlLm93bmVkLmxlbmd0aCAtIDE7IGkgPj0gMDsgaS0tKSBjbGVhbk5vZGUobm9kZS5vd25lZFtpXSk7XG4gICAgbm9kZS5vd25lZCA9IG51bGw7XG4gIH1cbiAgaWYgKG5vZGUuY2xlYW51cHMpIHtcbiAgICBmb3IgKGkgPSBub2RlLmNsZWFudXBzLmxlbmd0aCAtIDE7IGkgPj0gMDsgaS0tKSBub2RlLmNsZWFudXBzW2ldKCk7XG4gICAgbm9kZS5jbGVhbnVwcyA9IG51bGw7XG4gIH1cbiAgaWYgKFRyYW5zaXRpb24gJiYgVHJhbnNpdGlvbi5ydW5uaW5nKSBub2RlLnRTdGF0ZSA9IDA7ZWxzZSBub2RlLnN0YXRlID0gMDtcbn1cbmZ1bmN0aW9uIHJlc2V0KG5vZGUsIHRvcCkge1xuICBpZiAoIXRvcCkge1xuICAgIG5vZGUudFN0YXRlID0gMDtcbiAgICBUcmFuc2l0aW9uLmRpc3Bvc2VkLmFkZChub2RlKTtcbiAgfVxuICBpZiAobm9kZS5vd25lZCkge1xuICAgIGZvciAobGV0IGkgPSAwOyBpIDwgbm9kZS5vd25lZC5sZW5ndGg7IGkrKykgcmVzZXQobm9kZS5vd25lZFtpXSk7XG4gIH1cbn1cbmZ1bmN0aW9uIGNhc3RFcnJvcihlcnIpIHtcbiAgaWYgKGVyciBpbnN0YW5jZW9mIEVycm9yKSByZXR1cm4gZXJyO1xuICByZXR1cm4gbmV3IEVycm9yKHR5cGVvZiBlcnIgPT09IFwic3RyaW5nXCIgPyBlcnIgOiBcIlVua25vd24gZXJyb3JcIiwge1xuICAgIGNhdXNlOiBlcnJcbiAgfSk7XG59XG5mdW5jdGlvbiBydW5FcnJvcnMoZXJyLCBmbnMsIG93bmVyKSB7XG4gIHRyeSB7XG4gICAgZm9yIChjb25zdCBmIG9mIGZucykgZihlcnIpO1xuICB9IGNhdGNoIChlKSB7XG4gICAgaGFuZGxlRXJyb3IoZSwgb3duZXIgJiYgb3duZXIub3duZXIgfHwgbnVsbCk7XG4gIH1cbn1cbmZ1bmN0aW9uIGhhbmRsZUVycm9yKGVyciwgb3duZXIgPSBPd25lcikge1xuICBjb25zdCBmbnMgPSBFUlJPUiAmJiBvd25lciAmJiBvd25lci5jb250ZXh0ICYmIG93bmVyLmNvbnRleHRbRVJST1JdO1xuICBjb25zdCBlcnJvciA9IGNhc3RFcnJvcihlcnIpO1xuICBpZiAoIWZucykgdGhyb3cgZXJyb3I7XG4gIGlmIChFZmZlY3RzKSBFZmZlY3RzLnB1c2goe1xuICAgIGZuKCkge1xuICAgICAgcnVuRXJyb3JzKGVycm9yLCBmbnMsIG93bmVyKTtcbiAgICB9LFxuICAgIHN0YXRlOiBTVEFMRVxuICB9KTtlbHNlIHJ1bkVycm9ycyhlcnJvciwgZm5zLCBvd25lcik7XG59XG5mdW5jdGlvbiByZXNvbHZlQ2hpbGRyZW4oY2hpbGRyZW4pIHtcbiAgaWYgKHR5cGVvZiBjaGlsZHJlbiA9PT0gXCJmdW5jdGlvblwiICYmICFjaGlsZHJlbi5sZW5ndGgpIHJldHVybiByZXNvbHZlQ2hpbGRyZW4oY2hpbGRyZW4oKSk7XG4gIGlmIChBcnJheS5pc0FycmF5KGNoaWxkcmVuKSkge1xuICAgIGNvbnN0IHJlc3VsdHMgPSBbXTtcbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IGNoaWxkcmVuLmxlbmd0aDsgaSsrKSB7XG4gICAgICBjb25zdCByZXN1bHQgPSByZXNvbHZlQ2hpbGRyZW4oY2hpbGRyZW5baV0pO1xuICAgICAgQXJyYXkuaXNBcnJheShyZXN1bHQpID8gcmVzdWx0cy5wdXNoLmFwcGx5KHJlc3VsdHMsIHJlc3VsdCkgOiByZXN1bHRzLnB1c2gocmVzdWx0KTtcbiAgICB9XG4gICAgcmV0dXJuIHJlc3VsdHM7XG4gIH1cbiAgcmV0dXJuIGNoaWxkcmVuO1xufVxuZnVuY3Rpb24gY3JlYXRlUHJvdmlkZXIoaWQsIG9wdGlvbnMpIHtcbiAgcmV0dXJuIGZ1bmN0aW9uIHByb3ZpZGVyKHByb3BzKSB7XG4gICAgbGV0IHJlcztcbiAgICBjcmVhdGVSZW5kZXJFZmZlY3QoKCkgPT4gcmVzID0gdW50cmFjaygoKSA9PiB7XG4gICAgICBPd25lci5jb250ZXh0ID0ge1xuICAgICAgICAuLi5Pd25lci5jb250ZXh0LFxuICAgICAgICBbaWRdOiBwcm9wcy52YWx1ZVxuICAgICAgfTtcbiAgICAgIHJldHVybiBjaGlsZHJlbigoKSA9PiBwcm9wcy5jaGlsZHJlbik7XG4gICAgfSksIHVuZGVmaW5lZCk7XG4gICAgcmV0dXJuIHJlcztcbiAgfTtcbn1cbmZ1bmN0aW9uIG9uRXJyb3IoZm4pIHtcbiAgRVJST1IgfHwgKEVSUk9SID0gU3ltYm9sKFwiZXJyb3JcIikpO1xuICBpZiAoT3duZXIgPT09IG51bGwpIDtlbHNlIGlmIChPd25lci5jb250ZXh0ID09PSBudWxsIHx8ICFPd25lci5jb250ZXh0W0VSUk9SXSkge1xuICAgIE93bmVyLmNvbnRleHQgPSB7XG4gICAgICAuLi5Pd25lci5jb250ZXh0LFxuICAgICAgW0VSUk9SXTogW2ZuXVxuICAgIH07XG4gICAgbXV0YXRlQ29udGV4dChPd25lciwgRVJST1IsIFtmbl0pO1xuICB9IGVsc2UgT3duZXIuY29udGV4dFtFUlJPUl0ucHVzaChmbik7XG59XG5mdW5jdGlvbiBtdXRhdGVDb250ZXh0KG8sIGtleSwgdmFsdWUpIHtcbiAgaWYgKG8ub3duZWQpIHtcbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IG8ub3duZWQubGVuZ3RoOyBpKyspIHtcbiAgICAgIGlmIChvLm93bmVkW2ldLmNvbnRleHQgPT09IG8uY29udGV4dCkgbXV0YXRlQ29udGV4dChvLm93bmVkW2ldLCBrZXksIHZhbHVlKTtcbiAgICAgIGlmICghby5vd25lZFtpXS5jb250ZXh0KSB7XG4gICAgICAgIG8ub3duZWRbaV0uY29udGV4dCA9IG8uY29udGV4dDtcbiAgICAgICAgbXV0YXRlQ29udGV4dChvLm93bmVkW2ldLCBrZXksIHZhbHVlKTtcbiAgICAgIH0gZWxzZSBpZiAoIW8ub3duZWRbaV0uY29udGV4dFtrZXldKSB7XG4gICAgICAgIG8ub3duZWRbaV0uY29udGV4dFtrZXldID0gdmFsdWU7XG4gICAgICAgIG11dGF0ZUNvbnRleHQoby5vd25lZFtpXSwga2V5LCB2YWx1ZSk7XG4gICAgICB9XG4gICAgfVxuICB9XG59XG5cbmZ1bmN0aW9uIG9ic2VydmFibGUoaW5wdXQpIHtcbiAgcmV0dXJuIHtcbiAgICBzdWJzY3JpYmUob2JzZXJ2ZXIpIHtcbiAgICAgIGlmICghKG9ic2VydmVyIGluc3RhbmNlb2YgT2JqZWN0KSB8fCBvYnNlcnZlciA9PSBudWxsKSB7XG4gICAgICAgIHRocm93IG5ldyBUeXBlRXJyb3IoXCJFeHBlY3RlZCB0aGUgb2JzZXJ2ZXIgdG8gYmUgYW4gb2JqZWN0LlwiKTtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGhhbmRsZXIgPSB0eXBlb2Ygb2JzZXJ2ZXIgPT09IFwiZnVuY3Rpb25cIiA/IG9ic2VydmVyIDogb2JzZXJ2ZXIubmV4dCAmJiBvYnNlcnZlci5uZXh0LmJpbmQob2JzZXJ2ZXIpO1xuICAgICAgaWYgKCFoYW5kbGVyKSB7XG4gICAgICAgIHJldHVybiB7XG4gICAgICAgICAgdW5zdWJzY3JpYmUoKSB7fVxuICAgICAgICB9O1xuICAgICAgfVxuICAgICAgY29uc3QgZGlzcG9zZSA9IGNyZWF0ZVJvb3QoZGlzcG9zZXIgPT4ge1xuICAgICAgICBjcmVhdGVFZmZlY3QoKCkgPT4ge1xuICAgICAgICAgIGNvbnN0IHYgPSBpbnB1dCgpO1xuICAgICAgICAgIHVudHJhY2soKCkgPT4gaGFuZGxlcih2KSk7XG4gICAgICAgIH0pO1xuICAgICAgICByZXR1cm4gZGlzcG9zZXI7XG4gICAgICB9KTtcbiAgICAgIGlmIChnZXRPd25lcigpKSBvbkNsZWFudXAoZGlzcG9zZSk7XG4gICAgICByZXR1cm4ge1xuICAgICAgICB1bnN1YnNjcmliZSgpIHtcbiAgICAgICAgICBkaXNwb3NlKCk7XG4gICAgICAgIH1cbiAgICAgIH07XG4gICAgfSxcbiAgICBbU3ltYm9sLm9ic2VydmFibGUgfHwgXCJAQG9ic2VydmFibGVcIl0oKSB7XG4gICAgICByZXR1cm4gdGhpcztcbiAgICB9XG4gIH07XG59XG5mdW5jdGlvbiBmcm9tKHByb2R1Y2VyLCBpbml0YWxWYWx1ZSA9IHVuZGVmaW5lZCkge1xuICBjb25zdCBbcywgc2V0XSA9IGNyZWF0ZVNpZ25hbChpbml0YWxWYWx1ZSwge1xuICAgIGVxdWFsczogZmFsc2VcbiAgfSk7XG4gIGlmIChcInN1YnNjcmliZVwiIGluIHByb2R1Y2VyKSB7XG4gICAgY29uc3QgdW5zdWIgPSBwcm9kdWNlci5zdWJzY3JpYmUodiA9PiBzZXQoKCkgPT4gdikpO1xuICAgIG9uQ2xlYW51cCgoKSA9PiBcInVuc3Vic2NyaWJlXCIgaW4gdW5zdWIgPyB1bnN1Yi51bnN1YnNjcmliZSgpIDogdW5zdWIoKSk7XG4gIH0gZWxzZSB7XG4gICAgY29uc3QgY2xlYW4gPSBwcm9kdWNlcihzZXQpO1xuICAgIG9uQ2xlYW51cChjbGVhbik7XG4gIH1cbiAgcmV0dXJuIHM7XG59XG5cbmNvbnN0IEZBTExCQUNLID0gU3ltYm9sKFwiZmFsbGJhY2tcIik7XG5mdW5jdGlvbiBkaXNwb3NlKGQpIHtcbiAgZm9yIChsZXQgaSA9IDA7IGkgPCBkLmxlbmd0aDsgaSsrKSBkW2ldKCk7XG59XG5mdW5jdGlvbiBtYXBBcnJheShsaXN0LCBtYXBGbiwgb3B0aW9ucyA9IHt9KSB7XG4gIGxldCBpdGVtcyA9IFtdLFxuICAgIG1hcHBlZCA9IFtdLFxuICAgIGRpc3Bvc2VycyA9IFtdLFxuICAgIGxlbiA9IDAsXG4gICAgaW5kZXhlcyA9IG1hcEZuLmxlbmd0aCA+IDEgPyBbXSA6IG51bGw7XG4gIG9uQ2xlYW51cCgoKSA9PiBkaXNwb3NlKGRpc3Bvc2VycykpO1xuICByZXR1cm4gKCkgPT4ge1xuICAgIGxldCBuZXdJdGVtcyA9IGxpc3QoKSB8fCBbXSxcbiAgICAgIG5ld0xlbiA9IG5ld0l0ZW1zLmxlbmd0aCxcbiAgICAgIGksXG4gICAgICBqO1xuICAgIG5ld0l0ZW1zWyRUUkFDS107XG4gICAgcmV0dXJuIHVudHJhY2soKCkgPT4ge1xuICAgICAgbGV0IG5ld0luZGljZXMsIG5ld0luZGljZXNOZXh0LCB0ZW1wLCB0ZW1wZGlzcG9zZXJzLCB0ZW1wSW5kZXhlcywgc3RhcnQsIGVuZCwgbmV3RW5kLCBpdGVtO1xuICAgICAgaWYgKG5ld0xlbiA9PT0gMCkge1xuICAgICAgICBpZiAobGVuICE9PSAwKSB7XG4gICAgICAgICAgZGlzcG9zZShkaXNwb3NlcnMpO1xuICAgICAgICAgIGRpc3Bvc2VycyA9IFtdO1xuICAgICAgICAgIGl0ZW1zID0gW107XG4gICAgICAgICAgbWFwcGVkID0gW107XG4gICAgICAgICAgbGVuID0gMDtcbiAgICAgICAgICBpbmRleGVzICYmIChpbmRleGVzID0gW10pO1xuICAgICAgICB9XG4gICAgICAgIGlmIChvcHRpb25zLmZhbGxiYWNrKSB7XG4gICAgICAgICAgaXRlbXMgPSBbRkFMTEJBQ0tdO1xuICAgICAgICAgIG1hcHBlZFswXSA9IGNyZWF0ZVJvb3QoZGlzcG9zZXIgPT4ge1xuICAgICAgICAgICAgZGlzcG9zZXJzWzBdID0gZGlzcG9zZXI7XG4gICAgICAgICAgICByZXR1cm4gb3B0aW9ucy5mYWxsYmFjaygpO1xuICAgICAgICAgIH0pO1xuICAgICAgICAgIGxlbiA9IDE7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICAgIGVsc2UgaWYgKGxlbiA9PT0gMCkge1xuICAgICAgICBtYXBwZWQgPSBuZXcgQXJyYXkobmV3TGVuKTtcbiAgICAgICAgZm9yIChqID0gMDsgaiA8IG5ld0xlbjsgaisrKSB7XG4gICAgICAgICAgaXRlbXNbal0gPSBuZXdJdGVtc1tqXTtcbiAgICAgICAgICBtYXBwZWRbal0gPSBjcmVhdGVSb290KG1hcHBlcik7XG4gICAgICAgIH1cbiAgICAgICAgbGVuID0gbmV3TGVuO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgdGVtcCA9IG5ldyBBcnJheShuZXdMZW4pO1xuICAgICAgICB0ZW1wZGlzcG9zZXJzID0gbmV3IEFycmF5KG5ld0xlbik7XG4gICAgICAgIGluZGV4ZXMgJiYgKHRlbXBJbmRleGVzID0gbmV3IEFycmF5KG5ld0xlbikpO1xuICAgICAgICBmb3IgKHN0YXJ0ID0gMCwgZW5kID0gTWF0aC5taW4obGVuLCBuZXdMZW4pOyBzdGFydCA8IGVuZCAmJiBpdGVtc1tzdGFydF0gPT09IG5ld0l0ZW1zW3N0YXJ0XTsgc3RhcnQrKyk7XG4gICAgICAgIGZvciAoZW5kID0gbGVuIC0gMSwgbmV3RW5kID0gbmV3TGVuIC0gMTsgZW5kID49IHN0YXJ0ICYmIG5ld0VuZCA+PSBzdGFydCAmJiBpdGVtc1tlbmRdID09PSBuZXdJdGVtc1tuZXdFbmRdOyBlbmQtLSwgbmV3RW5kLS0pIHtcbiAgICAgICAgICB0ZW1wW25ld0VuZF0gPSBtYXBwZWRbZW5kXTtcbiAgICAgICAgICB0ZW1wZGlzcG9zZXJzW25ld0VuZF0gPSBkaXNwb3NlcnNbZW5kXTtcbiAgICAgICAgICBpbmRleGVzICYmICh0ZW1wSW5kZXhlc1tuZXdFbmRdID0gaW5kZXhlc1tlbmRdKTtcbiAgICAgICAgfVxuICAgICAgICBuZXdJbmRpY2VzID0gbmV3IE1hcCgpO1xuICAgICAgICBuZXdJbmRpY2VzTmV4dCA9IG5ldyBBcnJheShuZXdFbmQgKyAxKTtcbiAgICAgICAgZm9yIChqID0gbmV3RW5kOyBqID49IHN0YXJ0OyBqLS0pIHtcbiAgICAgICAgICBpdGVtID0gbmV3SXRlbXNbal07XG4gICAgICAgICAgaSA9IG5ld0luZGljZXMuZ2V0KGl0ZW0pO1xuICAgICAgICAgIG5ld0luZGljZXNOZXh0W2pdID0gaSA9PT0gdW5kZWZpbmVkID8gLTEgOiBpO1xuICAgICAgICAgIG5ld0luZGljZXMuc2V0KGl0ZW0sIGopO1xuICAgICAgICB9XG4gICAgICAgIGZvciAoaSA9IHN0YXJ0OyBpIDw9IGVuZDsgaSsrKSB7XG4gICAgICAgICAgaXRlbSA9IGl0ZW1zW2ldO1xuICAgICAgICAgIGogPSBuZXdJbmRpY2VzLmdldChpdGVtKTtcbiAgICAgICAgICBpZiAoaiAhPT0gdW5kZWZpbmVkICYmIGogIT09IC0xKSB7XG4gICAgICAgICAgICB0ZW1wW2pdID0gbWFwcGVkW2ldO1xuICAgICAgICAgICAgdGVtcGRpc3Bvc2Vyc1tqXSA9IGRpc3Bvc2Vyc1tpXTtcbiAgICAgICAgICAgIGluZGV4ZXMgJiYgKHRlbXBJbmRleGVzW2pdID0gaW5kZXhlc1tpXSk7XG4gICAgICAgICAgICBqID0gbmV3SW5kaWNlc05leHRbal07XG4gICAgICAgICAgICBuZXdJbmRpY2VzLnNldChpdGVtLCBqKTtcbiAgICAgICAgICB9IGVsc2UgZGlzcG9zZXJzW2ldKCk7XG4gICAgICAgIH1cbiAgICAgICAgZm9yIChqID0gc3RhcnQ7IGogPCBuZXdMZW47IGorKykge1xuICAgICAgICAgIGlmIChqIGluIHRlbXApIHtcbiAgICAgICAgICAgIG1hcHBlZFtqXSA9IHRlbXBbal07XG4gICAgICAgICAgICBkaXNwb3NlcnNbal0gPSB0ZW1wZGlzcG9zZXJzW2pdO1xuICAgICAgICAgICAgaWYgKGluZGV4ZXMpIHtcbiAgICAgICAgICAgICAgaW5kZXhlc1tqXSA9IHRlbXBJbmRleGVzW2pdO1xuICAgICAgICAgICAgICBpbmRleGVzW2pdKGopO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH0gZWxzZSBtYXBwZWRbal0gPSBjcmVhdGVSb290KG1hcHBlcik7XG4gICAgICAgIH1cbiAgICAgICAgbWFwcGVkID0gbWFwcGVkLnNsaWNlKDAsIGxlbiA9IG5ld0xlbik7XG4gICAgICAgIGl0ZW1zID0gbmV3SXRlbXMuc2xpY2UoMCk7XG4gICAgICB9XG4gICAgICByZXR1cm4gbWFwcGVkO1xuICAgIH0pO1xuICAgIGZ1bmN0aW9uIG1hcHBlcihkaXNwb3Nlcikge1xuICAgICAgZGlzcG9zZXJzW2pdID0gZGlzcG9zZXI7XG4gICAgICBpZiAoaW5kZXhlcykge1xuICAgICAgICBjb25zdCBbcywgc2V0XSA9IGNyZWF0ZVNpZ25hbChqKTtcbiAgICAgICAgaW5kZXhlc1tqXSA9IHNldDtcbiAgICAgICAgcmV0dXJuIG1hcEZuKG5ld0l0ZW1zW2pdLCBzKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiBtYXBGbihuZXdJdGVtc1tqXSk7XG4gICAgfVxuICB9O1xufVxuZnVuY3Rpb24gaW5kZXhBcnJheShsaXN0LCBtYXBGbiwgb3B0aW9ucyA9IHt9KSB7XG4gIGxldCBpdGVtcyA9IFtdLFxuICAgIG1hcHBlZCA9IFtdLFxuICAgIGRpc3Bvc2VycyA9IFtdLFxuICAgIHNpZ25hbHMgPSBbXSxcbiAgICBsZW4gPSAwLFxuICAgIGk7XG4gIG9uQ2xlYW51cCgoKSA9PiBkaXNwb3NlKGRpc3Bvc2VycykpO1xuICByZXR1cm4gKCkgPT4ge1xuICAgIGNvbnN0IG5ld0l0ZW1zID0gbGlzdCgpIHx8IFtdLFxuICAgICAgbmV3TGVuID0gbmV3SXRlbXMubGVuZ3RoO1xuICAgIG5ld0l0ZW1zWyRUUkFDS107XG4gICAgcmV0dXJuIHVudHJhY2soKCkgPT4ge1xuICAgICAgaWYgKG5ld0xlbiA9PT0gMCkge1xuICAgICAgICBpZiAobGVuICE9PSAwKSB7XG4gICAgICAgICAgZGlzcG9zZShkaXNwb3NlcnMpO1xuICAgICAgICAgIGRpc3Bvc2VycyA9IFtdO1xuICAgICAgICAgIGl0ZW1zID0gW107XG4gICAgICAgICAgbWFwcGVkID0gW107XG4gICAgICAgICAgbGVuID0gMDtcbiAgICAgICAgICBzaWduYWxzID0gW107XG4gICAgICAgIH1cbiAgICAgICAgaWYgKG9wdGlvbnMuZmFsbGJhY2spIHtcbiAgICAgICAgICBpdGVtcyA9IFtGQUxMQkFDS107XG4gICAgICAgICAgbWFwcGVkWzBdID0gY3JlYXRlUm9vdChkaXNwb3NlciA9PiB7XG4gICAgICAgICAgICBkaXNwb3NlcnNbMF0gPSBkaXNwb3NlcjtcbiAgICAgICAgICAgIHJldHVybiBvcHRpb25zLmZhbGxiYWNrKCk7XG4gICAgICAgICAgfSk7XG4gICAgICAgICAgbGVuID0gMTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gbWFwcGVkO1xuICAgICAgfVxuICAgICAgaWYgKGl0ZW1zWzBdID09PSBGQUxMQkFDSykge1xuICAgICAgICBkaXNwb3NlcnNbMF0oKTtcbiAgICAgICAgZGlzcG9zZXJzID0gW107XG4gICAgICAgIGl0ZW1zID0gW107XG4gICAgICAgIG1hcHBlZCA9IFtdO1xuICAgICAgICBsZW4gPSAwO1xuICAgICAgfVxuICAgICAgZm9yIChpID0gMDsgaSA8IG5ld0xlbjsgaSsrKSB7XG4gICAgICAgIGlmIChpIDwgaXRlbXMubGVuZ3RoICYmIGl0ZW1zW2ldICE9PSBuZXdJdGVtc1tpXSkge1xuICAgICAgICAgIHNpZ25hbHNbaV0oKCkgPT4gbmV3SXRlbXNbaV0pO1xuICAgICAgICB9IGVsc2UgaWYgKGkgPj0gaXRlbXMubGVuZ3RoKSB7XG4gICAgICAgICAgbWFwcGVkW2ldID0gY3JlYXRlUm9vdChtYXBwZXIpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICBmb3IgKDsgaSA8IGl0ZW1zLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgIGRpc3Bvc2Vyc1tpXSgpO1xuICAgICAgfVxuICAgICAgbGVuID0gc2lnbmFscy5sZW5ndGggPSBkaXNwb3NlcnMubGVuZ3RoID0gbmV3TGVuO1xuICAgICAgaXRlbXMgPSBuZXdJdGVtcy5zbGljZSgwKTtcbiAgICAgIHJldHVybiBtYXBwZWQgPSBtYXBwZWQuc2xpY2UoMCwgbGVuKTtcbiAgICB9KTtcbiAgICBmdW5jdGlvbiBtYXBwZXIoZGlzcG9zZXIpIHtcbiAgICAgIGRpc3Bvc2Vyc1tpXSA9IGRpc3Bvc2VyO1xuICAgICAgY29uc3QgW3MsIHNldF0gPSBjcmVhdGVTaWduYWwobmV3SXRlbXNbaV0pO1xuICAgICAgc2lnbmFsc1tpXSA9IHNldDtcbiAgICAgIHJldHVybiBtYXBGbihzLCBpKTtcbiAgICB9XG4gIH07XG59XG5cbmxldCBoeWRyYXRpb25FbmFibGVkID0gZmFsc2U7XG5mdW5jdGlvbiBlbmFibGVIeWRyYXRpb24oKSB7XG4gIGh5ZHJhdGlvbkVuYWJsZWQgPSB0cnVlO1xufVxuZnVuY3Rpb24gY3JlYXRlQ29tcG9uZW50KENvbXAsIHByb3BzKSB7XG4gIGlmIChoeWRyYXRpb25FbmFibGVkKSB7XG4gICAgaWYgKHNoYXJlZENvbmZpZy5jb250ZXh0KSB7XG4gICAgICBjb25zdCBjID0gc2hhcmVkQ29uZmlnLmNvbnRleHQ7XG4gICAgICBzZXRIeWRyYXRlQ29udGV4dChuZXh0SHlkcmF0ZUNvbnRleHQoKSk7XG4gICAgICBjb25zdCByID0gdW50cmFjaygoKSA9PiBDb21wKHByb3BzIHx8IHt9KSk7XG4gICAgICBzZXRIeWRyYXRlQ29udGV4dChjKTtcbiAgICAgIHJldHVybiByO1xuICAgIH1cbiAgfVxuICByZXR1cm4gdW50cmFjaygoKSA9PiBDb21wKHByb3BzIHx8IHt9KSk7XG59XG5mdW5jdGlvbiB0cnVlRm4oKSB7XG4gIHJldHVybiB0cnVlO1xufVxuY29uc3QgcHJvcFRyYXBzID0ge1xuICBnZXQoXywgcHJvcGVydHksIHJlY2VpdmVyKSB7XG4gICAgaWYgKHByb3BlcnR5ID09PSAkUFJPWFkpIHJldHVybiByZWNlaXZlcjtcbiAgICByZXR1cm4gXy5nZXQocHJvcGVydHkpO1xuICB9LFxuICBoYXMoXywgcHJvcGVydHkpIHtcbiAgICBpZiAocHJvcGVydHkgPT09ICRQUk9YWSkgcmV0dXJuIHRydWU7XG4gICAgcmV0dXJuIF8uaGFzKHByb3BlcnR5KTtcbiAgfSxcbiAgc2V0OiB0cnVlRm4sXG4gIGRlbGV0ZVByb3BlcnR5OiB0cnVlRm4sXG4gIGdldE93blByb3BlcnR5RGVzY3JpcHRvcihfLCBwcm9wZXJ0eSkge1xuICAgIHJldHVybiB7XG4gICAgICBjb25maWd1cmFibGU6IHRydWUsXG4gICAgICBlbnVtZXJhYmxlOiB0cnVlLFxuICAgICAgZ2V0KCkge1xuICAgICAgICByZXR1cm4gXy5nZXQocHJvcGVydHkpO1xuICAgICAgfSxcbiAgICAgIHNldDogdHJ1ZUZuLFxuICAgICAgZGVsZXRlUHJvcGVydHk6IHRydWVGblxuICAgIH07XG4gIH0sXG4gIG93bktleXMoXykge1xuICAgIHJldHVybiBfLmtleXMoKTtcbiAgfVxufTtcbmZ1bmN0aW9uIHJlc29sdmVTb3VyY2Uocykge1xuICByZXR1cm4gIShzID0gdHlwZW9mIHMgPT09IFwiZnVuY3Rpb25cIiA/IHMoKSA6IHMpID8ge30gOiBzO1xufVxuZnVuY3Rpb24gcmVzb2x2ZVNvdXJjZXMoKSB7XG4gIGZvciAobGV0IGkgPSAwLCBsZW5ndGggPSB0aGlzLmxlbmd0aDsgaSA8IGxlbmd0aDsgKytpKSB7XG4gICAgY29uc3QgdiA9IHRoaXNbaV0oKTtcbiAgICBpZiAodiAhPT0gdW5kZWZpbmVkKSByZXR1cm4gdjtcbiAgfVxufVxuZnVuY3Rpb24gbWVyZ2VQcm9wcyguLi5zb3VyY2VzKSB7XG4gIGxldCBwcm94eSA9IGZhbHNlO1xuICBmb3IgKGxldCBpID0gMDsgaSA8IHNvdXJjZXMubGVuZ3RoOyBpKyspIHtcbiAgICBjb25zdCBzID0gc291cmNlc1tpXTtcbiAgICBwcm94eSA9IHByb3h5IHx8ICEhcyAmJiAkUFJPWFkgaW4gcztcbiAgICBzb3VyY2VzW2ldID0gdHlwZW9mIHMgPT09IFwiZnVuY3Rpb25cIiA/IChwcm94eSA9IHRydWUsIGNyZWF0ZU1lbW8ocykpIDogcztcbiAgfVxuICBpZiAoU1VQUE9SVFNfUFJPWFkgJiYgcHJveHkpIHtcbiAgICByZXR1cm4gbmV3IFByb3h5KHtcbiAgICAgIGdldChwcm9wZXJ0eSkge1xuICAgICAgICBmb3IgKGxldCBpID0gc291cmNlcy5sZW5ndGggLSAxOyBpID49IDA7IGktLSkge1xuICAgICAgICAgIGNvbnN0IHYgPSByZXNvbHZlU291cmNlKHNvdXJjZXNbaV0pW3Byb3BlcnR5XTtcbiAgICAgICAgICBpZiAodiAhPT0gdW5kZWZpbmVkKSByZXR1cm4gdjtcbiAgICAgICAgfVxuICAgICAgfSxcbiAgICAgIGhhcyhwcm9wZXJ0eSkge1xuICAgICAgICBmb3IgKGxldCBpID0gc291cmNlcy5sZW5ndGggLSAxOyBpID49IDA7IGktLSkge1xuICAgICAgICAgIGlmIChwcm9wZXJ0eSBpbiByZXNvbHZlU291cmNlKHNvdXJjZXNbaV0pKSByZXR1cm4gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9LFxuICAgICAga2V5cygpIHtcbiAgICAgICAgY29uc3Qga2V5cyA9IFtdO1xuICAgICAgICBmb3IgKGxldCBpID0gMDsgaSA8IHNvdXJjZXMubGVuZ3RoOyBpKyspIGtleXMucHVzaCguLi5PYmplY3Qua2V5cyhyZXNvbHZlU291cmNlKHNvdXJjZXNbaV0pKSk7XG4gICAgICAgIHJldHVybiBbLi4ubmV3IFNldChrZXlzKV07XG4gICAgICB9XG4gICAgfSwgcHJvcFRyYXBzKTtcbiAgfVxuICBjb25zdCBzb3VyY2VzTWFwID0ge307XG4gIGNvbnN0IGRlZmluZWQgPSBPYmplY3QuY3JlYXRlKG51bGwpO1xuICBmb3IgKGxldCBpID0gc291cmNlcy5sZW5ndGggLSAxOyBpID49IDA7IGktLSkge1xuICAgIGNvbnN0IHNvdXJjZSA9IHNvdXJjZXNbaV07XG4gICAgaWYgKCFzb3VyY2UpIGNvbnRpbnVlO1xuICAgIGNvbnN0IHNvdXJjZUtleXMgPSBPYmplY3QuZ2V0T3duUHJvcGVydHlOYW1lcyhzb3VyY2UpO1xuICAgIGZvciAobGV0IGkgPSBzb3VyY2VLZXlzLmxlbmd0aCAtIDE7IGkgPj0gMDsgaS0tKSB7XG4gICAgICBjb25zdCBrZXkgPSBzb3VyY2VLZXlzW2ldO1xuICAgICAgaWYgKGtleSA9PT0gXCJfX3Byb3RvX19cIiB8fCBrZXkgPT09IFwiY29uc3RydWN0b3JcIikgY29udGludWU7XG4gICAgICBjb25zdCBkZXNjID0gT2JqZWN0LmdldE93blByb3BlcnR5RGVzY3JpcHRvcihzb3VyY2UsIGtleSk7XG4gICAgICBpZiAoIWRlZmluZWRba2V5XSkge1xuICAgICAgICBkZWZpbmVkW2tleV0gPSBkZXNjLmdldCA/IHtcbiAgICAgICAgICBlbnVtZXJhYmxlOiB0cnVlLFxuICAgICAgICAgIGNvbmZpZ3VyYWJsZTogdHJ1ZSxcbiAgICAgICAgICBnZXQ6IHJlc29sdmVTb3VyY2VzLmJpbmQoc291cmNlc01hcFtrZXldID0gW2Rlc2MuZ2V0LmJpbmQoc291cmNlKV0pXG4gICAgICAgIH0gOiBkZXNjLnZhbHVlICE9PSB1bmRlZmluZWQgPyBkZXNjIDogdW5kZWZpbmVkO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgY29uc3Qgc291cmNlcyA9IHNvdXJjZXNNYXBba2V5XTtcbiAgICAgICAgaWYgKHNvdXJjZXMpIHtcbiAgICAgICAgICBpZiAoZGVzYy5nZXQpIHNvdXJjZXMucHVzaChkZXNjLmdldC5iaW5kKHNvdXJjZSkpO2Vsc2UgaWYgKGRlc2MudmFsdWUgIT09IHVuZGVmaW5lZCkgc291cmNlcy5wdXNoKCgpID0+IGRlc2MudmFsdWUpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICB9XG4gIGNvbnN0IHRhcmdldCA9IHt9O1xuICBjb25zdCBkZWZpbmVkS2V5cyA9IE9iamVjdC5rZXlzKGRlZmluZWQpO1xuICBmb3IgKGxldCBpID0gZGVmaW5lZEtleXMubGVuZ3RoIC0gMTsgaSA+PSAwOyBpLS0pIHtcbiAgICBjb25zdCBrZXkgPSBkZWZpbmVkS2V5c1tpXSxcbiAgICAgIGRlc2MgPSBkZWZpbmVkW2tleV07XG4gICAgaWYgKGRlc2MgJiYgZGVzYy5nZXQpIE9iamVjdC5kZWZpbmVQcm9wZXJ0eSh0YXJnZXQsIGtleSwgZGVzYyk7ZWxzZSB0YXJnZXRba2V5XSA9IGRlc2MgPyBkZXNjLnZhbHVlIDogdW5kZWZpbmVkO1xuICB9XG4gIHJldHVybiB0YXJnZXQ7XG59XG5mdW5jdGlvbiBzcGxpdFByb3BzKHByb3BzLCAuLi5rZXlzKSB7XG4gIGNvbnN0IGxlbiA9IGtleXMubGVuZ3RoO1xuICBpZiAoU1VQUE9SVFNfUFJPWFkgJiYgJFBST1hZIGluIHByb3BzKSB7XG4gICAgY29uc3QgYmxvY2tlZCA9IGxlbiA+IDEgPyBrZXlzLmZsYXQoKSA6IGtleXNbMF07XG4gICAgY29uc3QgcmVzID0ga2V5cy5tYXAoayA9PiB7XG4gICAgICByZXR1cm4gbmV3IFByb3h5KHtcbiAgICAgICAgZ2V0KHByb3BlcnR5KSB7XG4gICAgICAgICAgcmV0dXJuIGsuaW5jbHVkZXMocHJvcGVydHkpID8gcHJvcHNbcHJvcGVydHldIDogdW5kZWZpbmVkO1xuICAgICAgICB9LFxuICAgICAgICBoYXMocHJvcGVydHkpIHtcbiAgICAgICAgICByZXR1cm4gay5pbmNsdWRlcyhwcm9wZXJ0eSkgJiYgcHJvcGVydHkgaW4gcHJvcHM7XG4gICAgICAgIH0sXG4gICAgICAgIGtleXMoKSB7XG4gICAgICAgICAgcmV0dXJuIGsuZmlsdGVyKHByb3BlcnR5ID0+IHByb3BlcnR5IGluIHByb3BzKTtcbiAgICAgICAgfVxuICAgICAgfSwgcHJvcFRyYXBzKTtcbiAgICB9KTtcbiAgICByZXMucHVzaChuZXcgUHJveHkoe1xuICAgICAgZ2V0KHByb3BlcnR5KSB7XG4gICAgICAgIHJldHVybiBibG9ja2VkLmluY2x1ZGVzKHByb3BlcnR5KSA/IHVuZGVmaW5lZCA6IHByb3BzW3Byb3BlcnR5XTtcbiAgICAgIH0sXG4gICAgICBoYXMocHJvcGVydHkpIHtcbiAgICAgICAgcmV0dXJuIGJsb2NrZWQuaW5jbHVkZXMocHJvcGVydHkpID8gZmFsc2UgOiBwcm9wZXJ0eSBpbiBwcm9wcztcbiAgICAgIH0sXG4gICAgICBrZXlzKCkge1xuICAgICAgICByZXR1cm4gT2JqZWN0LmtleXMocHJvcHMpLmZpbHRlcihrID0+ICFibG9ja2VkLmluY2x1ZGVzKGspKTtcbiAgICAgIH1cbiAgICB9LCBwcm9wVHJhcHMpKTtcbiAgICByZXR1cm4gcmVzO1xuICB9XG4gIGNvbnN0IG9iamVjdHMgPSBbXTtcbiAgZm9yIChsZXQgaSA9IDA7IGkgPD0gbGVuOyBpKyspIHtcbiAgICBvYmplY3RzW2ldID0ge307XG4gIH1cbiAgZm9yIChjb25zdCBwcm9wTmFtZSBvZiBPYmplY3QuZ2V0T3duUHJvcGVydHlOYW1lcyhwcm9wcykpIHtcbiAgICBsZXQga2V5SW5kZXggPSBsZW47XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBrZXlzLmxlbmd0aDsgaSsrKSB7XG4gICAgICBpZiAoa2V5c1tpXS5pbmNsdWRlcyhwcm9wTmFtZSkpIHtcbiAgICAgICAga2V5SW5kZXggPSBpO1xuICAgICAgICBicmVhaztcbiAgICAgIH1cbiAgICB9XG4gICAgY29uc3QgZGVzYyA9IE9iamVjdC5nZXRPd25Qcm9wZXJ0eURlc2NyaXB0b3IocHJvcHMsIHByb3BOYW1lKTtcbiAgICBjb25zdCBpc0RlZmF1bHREZXNjID0gIWRlc2MuZ2V0ICYmICFkZXNjLnNldCAmJiBkZXNjLmVudW1lcmFibGUgJiYgZGVzYy53cml0YWJsZSAmJiBkZXNjLmNvbmZpZ3VyYWJsZTtcbiAgICBpc0RlZmF1bHREZXNjID8gb2JqZWN0c1trZXlJbmRleF1bcHJvcE5hbWVdID0gZGVzYy52YWx1ZSA6IE9iamVjdC5kZWZpbmVQcm9wZXJ0eShvYmplY3RzW2tleUluZGV4XSwgcHJvcE5hbWUsIGRlc2MpO1xuICB9XG4gIHJldHVybiBvYmplY3RzO1xufVxuZnVuY3Rpb24gbGF6eShmbikge1xuICBsZXQgY29tcDtcbiAgbGV0IHA7XG4gIGNvbnN0IHdyYXAgPSBwcm9wcyA9PiB7XG4gICAgY29uc3QgY3R4ID0gc2hhcmVkQ29uZmlnLmNvbnRleHQ7XG4gICAgaWYgKGN0eCkge1xuICAgICAgY29uc3QgW3MsIHNldF0gPSBjcmVhdGVTaWduYWwoKTtcbiAgICAgIHNoYXJlZENvbmZpZy5jb3VudCB8fCAoc2hhcmVkQ29uZmlnLmNvdW50ID0gMCk7XG4gICAgICBzaGFyZWRDb25maWcuY291bnQrKztcbiAgICAgIChwIHx8IChwID0gZm4oKSkpLnRoZW4obW9kID0+IHtcbiAgICAgICAgIXNoYXJlZENvbmZpZy5kb25lICYmIHNldEh5ZHJhdGVDb250ZXh0KGN0eCk7XG4gICAgICAgIHNoYXJlZENvbmZpZy5jb3VudC0tO1xuICAgICAgICBzZXQoKCkgPT4gbW9kLmRlZmF1bHQpO1xuICAgICAgICBzZXRIeWRyYXRlQ29udGV4dCgpO1xuICAgICAgfSk7XG4gICAgICBjb21wID0gcztcbiAgICB9IGVsc2UgaWYgKCFjb21wKSB7XG4gICAgICBjb25zdCBbc10gPSBjcmVhdGVSZXNvdXJjZSgoKSA9PiAocCB8fCAocCA9IGZuKCkpKS50aGVuKG1vZCA9PiBtb2QuZGVmYXVsdCkpO1xuICAgICAgY29tcCA9IHM7XG4gICAgfVxuICAgIGxldCBDb21wO1xuICAgIHJldHVybiBjcmVhdGVNZW1vKCgpID0+IChDb21wID0gY29tcCgpKSA/IHVudHJhY2soKCkgPT4ge1xuICAgICAgaWYgKElTX0RFVikgO1xuICAgICAgaWYgKCFjdHggfHwgc2hhcmVkQ29uZmlnLmRvbmUpIHJldHVybiBDb21wKHByb3BzKTtcbiAgICAgIGNvbnN0IGMgPSBzaGFyZWRDb25maWcuY29udGV4dDtcbiAgICAgIHNldEh5ZHJhdGVDb250ZXh0KGN0eCk7XG4gICAgICBjb25zdCByID0gQ29tcChwcm9wcyk7XG4gICAgICBzZXRIeWRyYXRlQ29udGV4dChjKTtcbiAgICAgIHJldHVybiByO1xuICAgIH0pIDogXCJcIik7XG4gIH07XG4gIHdyYXAucHJlbG9hZCA9ICgpID0+IHAgfHwgKChwID0gZm4oKSkudGhlbihtb2QgPT4gY29tcCA9ICgpID0+IG1vZC5kZWZhdWx0KSwgcCk7XG4gIHJldHVybiB3cmFwO1xufVxubGV0IGNvdW50ZXIgPSAwO1xuZnVuY3Rpb24gY3JlYXRlVW5pcXVlSWQoKSB7XG4gIGNvbnN0IGN0eCA9IHNoYXJlZENvbmZpZy5jb250ZXh0O1xuICByZXR1cm4gY3R4ID8gc2hhcmVkQ29uZmlnLmdldE5leHRDb250ZXh0SWQoKSA6IGBjbC0ke2NvdW50ZXIrK31gO1xufVxuXG5jb25zdCBuYXJyb3dlZEVycm9yID0gbmFtZSA9PiBgU3RhbGUgcmVhZCBmcm9tIDwke25hbWV9Pi5gO1xuZnVuY3Rpb24gRm9yKHByb3BzKSB7XG4gIGNvbnN0IGZhbGxiYWNrID0gXCJmYWxsYmFja1wiIGluIHByb3BzICYmIHtcbiAgICBmYWxsYmFjazogKCkgPT4gcHJvcHMuZmFsbGJhY2tcbiAgfTtcbiAgcmV0dXJuIGNyZWF0ZU1lbW8obWFwQXJyYXkoKCkgPT4gcHJvcHMuZWFjaCwgcHJvcHMuY2hpbGRyZW4sIGZhbGxiYWNrIHx8IHVuZGVmaW5lZCkpO1xufVxuZnVuY3Rpb24gSW5kZXgocHJvcHMpIHtcbiAgY29uc3QgZmFsbGJhY2sgPSBcImZhbGxiYWNrXCIgaW4gcHJvcHMgJiYge1xuICAgIGZhbGxiYWNrOiAoKSA9PiBwcm9wcy5mYWxsYmFja1xuICB9O1xuICByZXR1cm4gY3JlYXRlTWVtbyhpbmRleEFycmF5KCgpID0+IHByb3BzLmVhY2gsIHByb3BzLmNoaWxkcmVuLCBmYWxsYmFjayB8fCB1bmRlZmluZWQpKTtcbn1cbmZ1bmN0aW9uIFNob3cocHJvcHMpIHtcbiAgY29uc3Qga2V5ZWQgPSBwcm9wcy5rZXllZDtcbiAgY29uc3QgY29uZGl0aW9uVmFsdWUgPSBjcmVhdGVNZW1vKCgpID0+IHByb3BzLndoZW4sIHVuZGVmaW5lZCwgdW5kZWZpbmVkKTtcbiAgY29uc3QgY29uZGl0aW9uID0ga2V5ZWQgPyBjb25kaXRpb25WYWx1ZSA6IGNyZWF0ZU1lbW8oY29uZGl0aW9uVmFsdWUsIHVuZGVmaW5lZCwge1xuICAgIGVxdWFsczogKGEsIGIpID0+ICFhID09PSAhYlxuICB9KTtcbiAgcmV0dXJuIGNyZWF0ZU1lbW8oKCkgPT4ge1xuICAgIGNvbnN0IGMgPSBjb25kaXRpb24oKTtcbiAgICBpZiAoYykge1xuICAgICAgY29uc3QgY2hpbGQgPSBwcm9wcy5jaGlsZHJlbjtcbiAgICAgIGNvbnN0IGZuID0gdHlwZW9mIGNoaWxkID09PSBcImZ1bmN0aW9uXCIgJiYgY2hpbGQubGVuZ3RoID4gMDtcbiAgICAgIHJldHVybiBmbiA/IHVudHJhY2soKCkgPT4gY2hpbGQoa2V5ZWQgPyBjIDogKCkgPT4ge1xuICAgICAgICBpZiAoIXVudHJhY2soY29uZGl0aW9uKSkgdGhyb3cgbmFycm93ZWRFcnJvcihcIlNob3dcIik7XG4gICAgICAgIHJldHVybiBjb25kaXRpb25WYWx1ZSgpO1xuICAgICAgfSkpIDogY2hpbGQ7XG4gICAgfVxuICAgIHJldHVybiBwcm9wcy5mYWxsYmFjaztcbiAgfSwgdW5kZWZpbmVkLCB1bmRlZmluZWQpO1xufVxuZnVuY3Rpb24gU3dpdGNoKHByb3BzKSB7XG4gIGNvbnN0IGNocyA9IGNoaWxkcmVuKCgpID0+IHByb3BzLmNoaWxkcmVuKTtcbiAgY29uc3Qgc3dpdGNoRnVuYyA9IGNyZWF0ZU1lbW8oKCkgPT4ge1xuICAgIGNvbnN0IGNoID0gY2hzKCk7XG4gICAgY29uc3QgbXBzID0gQXJyYXkuaXNBcnJheShjaCkgPyBjaCA6IFtjaF07XG4gICAgbGV0IGZ1bmMgPSAoKSA9PiB1bmRlZmluZWQ7XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBtcHMubGVuZ3RoOyBpKyspIHtcbiAgICAgIGNvbnN0IGluZGV4ID0gaTtcbiAgICAgIGNvbnN0IG1wID0gbXBzW2ldO1xuICAgICAgY29uc3QgcHJldkZ1bmMgPSBmdW5jO1xuICAgICAgY29uc3QgY29uZGl0aW9uVmFsdWUgPSBjcmVhdGVNZW1vKCgpID0+IHByZXZGdW5jKCkgPyB1bmRlZmluZWQgOiBtcC53aGVuLCB1bmRlZmluZWQsIHVuZGVmaW5lZCk7XG4gICAgICBjb25zdCBjb25kaXRpb24gPSBtcC5rZXllZCA/IGNvbmRpdGlvblZhbHVlIDogY3JlYXRlTWVtbyhjb25kaXRpb25WYWx1ZSwgdW5kZWZpbmVkLCB7XG4gICAgICAgIGVxdWFsczogKGEsIGIpID0+ICFhID09PSAhYlxuICAgICAgfSk7XG4gICAgICBmdW5jID0gKCkgPT4gcHJldkZ1bmMoKSB8fCAoY29uZGl0aW9uKCkgPyBbaW5kZXgsIGNvbmRpdGlvblZhbHVlLCBtcF0gOiB1bmRlZmluZWQpO1xuICAgIH1cbiAgICByZXR1cm4gZnVuYztcbiAgfSk7XG4gIHJldHVybiBjcmVhdGVNZW1vKCgpID0+IHtcbiAgICBjb25zdCBzZWwgPSBzd2l0Y2hGdW5jKCkoKTtcbiAgICBpZiAoIXNlbCkgcmV0dXJuIHByb3BzLmZhbGxiYWNrO1xuICAgIGNvbnN0IFtpbmRleCwgY29uZGl0aW9uVmFsdWUsIG1wXSA9IHNlbDtcbiAgICBjb25zdCBjaGlsZCA9IG1wLmNoaWxkcmVuO1xuICAgIGNvbnN0IGZuID0gdHlwZW9mIGNoaWxkID09PSBcImZ1bmN0aW9uXCIgJiYgY2hpbGQubGVuZ3RoID4gMDtcbiAgICByZXR1cm4gZm4gPyB1bnRyYWNrKCgpID0+IGNoaWxkKG1wLmtleWVkID8gY29uZGl0aW9uVmFsdWUoKSA6ICgpID0+IHtcbiAgICAgIGlmICh1bnRyYWNrKHN3aXRjaEZ1bmMpKCk/LlswXSAhPT0gaW5kZXgpIHRocm93IG5hcnJvd2VkRXJyb3IoXCJNYXRjaFwiKTtcbiAgICAgIHJldHVybiBjb25kaXRpb25WYWx1ZSgpO1xuICAgIH0pKSA6IGNoaWxkO1xuICB9LCB1bmRlZmluZWQsIHVuZGVmaW5lZCk7XG59XG5mdW5jdGlvbiBNYXRjaChwcm9wcykge1xuICByZXR1cm4gcHJvcHM7XG59XG5sZXQgRXJyb3JzO1xuZnVuY3Rpb24gcmVzZXRFcnJvckJvdW5kYXJpZXMoKSB7XG4gIEVycm9ycyAmJiBbLi4uRXJyb3JzXS5mb3JFYWNoKGZuID0+IGZuKCkpO1xufVxuZnVuY3Rpb24gRXJyb3JCb3VuZGFyeShwcm9wcykge1xuICBsZXQgZXJyO1xuICBpZiAoc2hhcmVkQ29uZmlnLmNvbnRleHQgJiYgc2hhcmVkQ29uZmlnLmxvYWQpIGVyciA9IHNoYXJlZENvbmZpZy5sb2FkKHNoYXJlZENvbmZpZy5nZXRDb250ZXh0SWQoKSk7XG4gIGNvbnN0IFtlcnJvcmVkLCBzZXRFcnJvcmVkXSA9IGNyZWF0ZVNpZ25hbChlcnIsIHVuZGVmaW5lZCk7XG4gIEVycm9ycyB8fCAoRXJyb3JzID0gbmV3IFNldCgpKTtcbiAgRXJyb3JzLmFkZChzZXRFcnJvcmVkKTtcbiAgb25DbGVhbnVwKCgpID0+IEVycm9ycy5kZWxldGUoc2V0RXJyb3JlZCkpO1xuICByZXR1cm4gY3JlYXRlTWVtbygoKSA9PiB7XG4gICAgbGV0IGU7XG4gICAgaWYgKGUgPSBlcnJvcmVkKCkpIHtcbiAgICAgIGNvbnN0IGYgPSBwcm9wcy5mYWxsYmFjaztcbiAgICAgIHJldHVybiB0eXBlb2YgZiA9PT0gXCJmdW5jdGlvblwiICYmIGYubGVuZ3RoID8gdW50cmFjaygoKSA9PiBmKGUsICgpID0+IHNldEVycm9yZWQoKSkpIDogZjtcbiAgICB9XG4gICAgcmV0dXJuIGNhdGNoRXJyb3IoKCkgPT4gcHJvcHMuY2hpbGRyZW4sIHNldEVycm9yZWQpO1xuICB9LCB1bmRlZmluZWQsIHVuZGVmaW5lZCk7XG59XG5cbmNvbnN0IHN1c3BlbnNlTGlzdEVxdWFscyA9IChhLCBiKSA9PiBhLnNob3dDb250ZW50ID09PSBiLnNob3dDb250ZW50ICYmIGEuc2hvd0ZhbGxiYWNrID09PSBiLnNob3dGYWxsYmFjaztcbmNvbnN0IFN1c3BlbnNlTGlzdENvbnRleHQgPSAvKiAjX19QVVJFX18gKi9jcmVhdGVDb250ZXh0KCk7XG5mdW5jdGlvbiBTdXNwZW5zZUxpc3QocHJvcHMpIHtcbiAgbGV0IFt3cmFwcGVyLCBzZXRXcmFwcGVyXSA9IGNyZWF0ZVNpZ25hbCgoKSA9PiAoe1xuICAgICAgaW5GYWxsYmFjazogZmFsc2VcbiAgICB9KSksXG4gICAgc2hvdztcbiAgY29uc3QgbGlzdENvbnRleHQgPSB1c2VDb250ZXh0KFN1c3BlbnNlTGlzdENvbnRleHQpO1xuICBjb25zdCBbcmVnaXN0cnksIHNldFJlZ2lzdHJ5XSA9IGNyZWF0ZVNpZ25hbChbXSk7XG4gIGlmIChsaXN0Q29udGV4dCkge1xuICAgIHNob3cgPSBsaXN0Q29udGV4dC5yZWdpc3RlcihjcmVhdGVNZW1vKCgpID0+IHdyYXBwZXIoKSgpLmluRmFsbGJhY2spKTtcbiAgfVxuICBjb25zdCByZXNvbHZlZCA9IGNyZWF0ZU1lbW8ocHJldiA9PiB7XG4gICAgY29uc3QgcmV2ZWFsID0gcHJvcHMucmV2ZWFsT3JkZXIsXG4gICAgICB0YWlsID0gcHJvcHMudGFpbCxcbiAgICAgIHtcbiAgICAgICAgc2hvd0NvbnRlbnQgPSB0cnVlLFxuICAgICAgICBzaG93RmFsbGJhY2sgPSB0cnVlXG4gICAgICB9ID0gc2hvdyA/IHNob3coKSA6IHt9LFxuICAgICAgcmVnID0gcmVnaXN0cnkoKSxcbiAgICAgIHJldmVyc2UgPSByZXZlYWwgPT09IFwiYmFja3dhcmRzXCI7XG4gICAgaWYgKHJldmVhbCA9PT0gXCJ0b2dldGhlclwiKSB7XG4gICAgICBjb25zdCBhbGwgPSByZWcuZXZlcnkoaW5GYWxsYmFjayA9PiAhaW5GYWxsYmFjaygpKTtcbiAgICAgIGNvbnN0IHJlcyA9IHJlZy5tYXAoKCkgPT4gKHtcbiAgICAgICAgc2hvd0NvbnRlbnQ6IGFsbCAmJiBzaG93Q29udGVudCxcbiAgICAgICAgc2hvd0ZhbGxiYWNrXG4gICAgICB9KSk7XG4gICAgICByZXMuaW5GYWxsYmFjayA9ICFhbGw7XG4gICAgICByZXR1cm4gcmVzO1xuICAgIH1cbiAgICBsZXQgc3RvcCA9IGZhbHNlO1xuICAgIGxldCBpbkZhbGxiYWNrID0gcHJldi5pbkZhbGxiYWNrO1xuICAgIGNvbnN0IHJlcyA9IFtdO1xuICAgIGZvciAobGV0IGkgPSAwLCBsZW4gPSByZWcubGVuZ3RoOyBpIDwgbGVuOyBpKyspIHtcbiAgICAgIGNvbnN0IG4gPSByZXZlcnNlID8gbGVuIC0gaSAtIDEgOiBpLFxuICAgICAgICBzID0gcmVnW25dKCk7XG4gICAgICBpZiAoIXN0b3AgJiYgIXMpIHtcbiAgICAgICAgcmVzW25dID0ge1xuICAgICAgICAgIHNob3dDb250ZW50LFxuICAgICAgICAgIHNob3dGYWxsYmFja1xuICAgICAgICB9O1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgY29uc3QgbmV4dCA9ICFzdG9wO1xuICAgICAgICBpZiAobmV4dCkgaW5GYWxsYmFjayA9IHRydWU7XG4gICAgICAgIHJlc1tuXSA9IHtcbiAgICAgICAgICBzaG93Q29udGVudDogbmV4dCxcbiAgICAgICAgICBzaG93RmFsbGJhY2s6ICF0YWlsIHx8IG5leHQgJiYgdGFpbCA9PT0gXCJjb2xsYXBzZWRcIiA/IHNob3dGYWxsYmFjayA6IGZhbHNlXG4gICAgICAgIH07XG4gICAgICAgIHN0b3AgPSB0cnVlO1xuICAgICAgfVxuICAgIH1cbiAgICBpZiAoIXN0b3ApIGluRmFsbGJhY2sgPSBmYWxzZTtcbiAgICByZXMuaW5GYWxsYmFjayA9IGluRmFsbGJhY2s7XG4gICAgcmV0dXJuIHJlcztcbiAgfSwge1xuICAgIGluRmFsbGJhY2s6IGZhbHNlXG4gIH0pO1xuICBzZXRXcmFwcGVyKCgpID0+IHJlc29sdmVkKTtcbiAgcmV0dXJuIGNyZWF0ZUNvbXBvbmVudChTdXNwZW5zZUxpc3RDb250ZXh0LlByb3ZpZGVyLCB7XG4gICAgdmFsdWU6IHtcbiAgICAgIHJlZ2lzdGVyOiBpbkZhbGxiYWNrID0+IHtcbiAgICAgICAgbGV0IGluZGV4O1xuICAgICAgICBzZXRSZWdpc3RyeShyZWdpc3RyeSA9PiB7XG4gICAgICAgICAgaW5kZXggPSByZWdpc3RyeS5sZW5ndGg7XG4gICAgICAgICAgcmV0dXJuIFsuLi5yZWdpc3RyeSwgaW5GYWxsYmFja107XG4gICAgICAgIH0pO1xuICAgICAgICByZXR1cm4gY3JlYXRlTWVtbygoKSA9PiByZXNvbHZlZCgpW2luZGV4XSwgdW5kZWZpbmVkLCB7XG4gICAgICAgICAgZXF1YWxzOiBzdXNwZW5zZUxpc3RFcXVhbHNcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSxcbiAgICBnZXQgY2hpbGRyZW4oKSB7XG4gICAgICByZXR1cm4gcHJvcHMuY2hpbGRyZW47XG4gICAgfVxuICB9KTtcbn1cbmZ1bmN0aW9uIFN1c3BlbnNlKHByb3BzKSB7XG4gIGxldCBjb3VudGVyID0gMCxcbiAgICBzaG93LFxuICAgIGN0eCxcbiAgICBwLFxuICAgIGZsaWNrZXIsXG4gICAgZXJyb3I7XG4gIGNvbnN0IFtpbkZhbGxiYWNrLCBzZXRGYWxsYmFja10gPSBjcmVhdGVTaWduYWwoZmFsc2UpLFxuICAgIFN1c3BlbnNlQ29udGV4dCA9IGdldFN1c3BlbnNlQ29udGV4dCgpLFxuICAgIHN0b3JlID0ge1xuICAgICAgaW5jcmVtZW50OiAoKSA9PiB7XG4gICAgICAgIGlmICgrK2NvdW50ZXIgPT09IDEpIHNldEZhbGxiYWNrKHRydWUpO1xuICAgICAgfSxcbiAgICAgIGRlY3JlbWVudDogKCkgPT4ge1xuICAgICAgICBpZiAoLS1jb3VudGVyID09PSAwKSBzZXRGYWxsYmFjayhmYWxzZSk7XG4gICAgICB9LFxuICAgICAgaW5GYWxsYmFjayxcbiAgICAgIGVmZmVjdHM6IFtdLFxuICAgICAgcmVzb2x2ZWQ6IGZhbHNlXG4gICAgfSxcbiAgICBvd25lciA9IGdldE93bmVyKCk7XG4gIGlmIChzaGFyZWRDb25maWcuY29udGV4dCAmJiBzaGFyZWRDb25maWcubG9hZCkge1xuICAgIGNvbnN0IGtleSA9IHNoYXJlZENvbmZpZy5nZXRDb250ZXh0SWQoKTtcbiAgICBsZXQgcmVmID0gc2hhcmVkQ29uZmlnLmxvYWQoa2V5KTtcbiAgICBpZiAocmVmKSB7XG4gICAgICBpZiAodHlwZW9mIHJlZiAhPT0gXCJvYmplY3RcIiB8fCByZWYucyAhPT0gMSkgcCA9IHJlZjtlbHNlIHNoYXJlZENvbmZpZy5nYXRoZXIoa2V5KTtcbiAgICB9XG4gICAgaWYgKHAgJiYgcCAhPT0gXCIkJGZcIikge1xuICAgICAgY29uc3QgW3MsIHNldF0gPSBjcmVhdGVTaWduYWwodW5kZWZpbmVkLCB7XG4gICAgICAgIGVxdWFsczogZmFsc2VcbiAgICAgIH0pO1xuICAgICAgZmxpY2tlciA9IHM7XG4gICAgICBwLnRoZW4oKCkgPT4ge1xuICAgICAgICBpZiAoc2hhcmVkQ29uZmlnLmRvbmUpIHJldHVybiBzZXQoKTtcbiAgICAgICAgc2hhcmVkQ29uZmlnLmdhdGhlcihrZXkpO1xuICAgICAgICBzZXRIeWRyYXRlQ29udGV4dChjdHgpO1xuICAgICAgICBzZXQoKTtcbiAgICAgICAgc2V0SHlkcmF0ZUNvbnRleHQoKTtcbiAgICAgIH0sIGVyciA9PiB7XG4gICAgICAgIGVycm9yID0gZXJyO1xuICAgICAgICBzZXQoKTtcbiAgICAgIH0pO1xuICAgIH1cbiAgfVxuICBjb25zdCBsaXN0Q29udGV4dCA9IHVzZUNvbnRleHQoU3VzcGVuc2VMaXN0Q29udGV4dCk7XG4gIGlmIChsaXN0Q29udGV4dCkgc2hvdyA9IGxpc3RDb250ZXh0LnJlZ2lzdGVyKHN0b3JlLmluRmFsbGJhY2spO1xuICBsZXQgZGlzcG9zZTtcbiAgb25DbGVhbnVwKCgpID0+IGRpc3Bvc2UgJiYgZGlzcG9zZSgpKTtcbiAgcmV0dXJuIGNyZWF0ZUNvbXBvbmVudChTdXNwZW5zZUNvbnRleHQuUHJvdmlkZXIsIHtcbiAgICB2YWx1ZTogc3RvcmUsXG4gICAgZ2V0IGNoaWxkcmVuKCkge1xuICAgICAgcmV0dXJuIGNyZWF0ZU1lbW8oKCkgPT4ge1xuICAgICAgICBpZiAoZXJyb3IpIHRocm93IGVycm9yO1xuICAgICAgICBjdHggPSBzaGFyZWRDb25maWcuY29udGV4dDtcbiAgICAgICAgaWYgKGZsaWNrZXIpIHtcbiAgICAgICAgICBmbGlja2VyKCk7XG4gICAgICAgICAgcmV0dXJuIGZsaWNrZXIgPSB1bmRlZmluZWQ7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKGN0eCAmJiBwID09PSBcIiQkZlwiKSBzZXRIeWRyYXRlQ29udGV4dCgpO1xuICAgICAgICBjb25zdCByZW5kZXJlZCA9IGNyZWF0ZU1lbW8oKCkgPT4gcHJvcHMuY2hpbGRyZW4pO1xuICAgICAgICByZXR1cm4gY3JlYXRlTWVtbyhwcmV2ID0+IHtcbiAgICAgICAgICBjb25zdCBpbkZhbGxiYWNrID0gc3RvcmUuaW5GYWxsYmFjaygpLFxuICAgICAgICAgICAge1xuICAgICAgICAgICAgICBzaG93Q29udGVudCA9IHRydWUsXG4gICAgICAgICAgICAgIHNob3dGYWxsYmFjayA9IHRydWVcbiAgICAgICAgICAgIH0gPSBzaG93ID8gc2hvdygpIDoge307XG4gICAgICAgICAgaWYgKCghaW5GYWxsYmFjayB8fCBwICYmIHAgIT09IFwiJCRmXCIpICYmIHNob3dDb250ZW50KSB7XG4gICAgICAgICAgICBzdG9yZS5yZXNvbHZlZCA9IHRydWU7XG4gICAgICAgICAgICBkaXNwb3NlICYmIGRpc3Bvc2UoKTtcbiAgICAgICAgICAgIGRpc3Bvc2UgPSBjdHggPSBwID0gdW5kZWZpbmVkO1xuICAgICAgICAgICAgcmVzdW1lRWZmZWN0cyhzdG9yZS5lZmZlY3RzKTtcbiAgICAgICAgICAgIHJldHVybiByZW5kZXJlZCgpO1xuICAgICAgICAgIH1cbiAgICAgICAgICBpZiAoIXNob3dGYWxsYmFjaykgcmV0dXJuO1xuICAgICAgICAgIGlmIChkaXNwb3NlKSByZXR1cm4gcHJldjtcbiAgICAgICAgICByZXR1cm4gY3JlYXRlUm9vdChkaXNwb3NlciA9PiB7XG4gICAgICAgICAgICBkaXNwb3NlID0gZGlzcG9zZXI7XG4gICAgICAgICAgICBpZiAoY3R4KSB7XG4gICAgICAgICAgICAgIHNldEh5ZHJhdGVDb250ZXh0KHtcbiAgICAgICAgICAgICAgICBpZDogY3R4LmlkICsgXCJGXCIsXG4gICAgICAgICAgICAgICAgY291bnQ6IDBcbiAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgIGN0eCA9IHVuZGVmaW5lZDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiBwcm9wcy5mYWxsYmFjaztcbiAgICAgICAgICB9LCBvd25lcik7XG4gICAgICAgIH0pO1xuICAgICAgfSk7XG4gICAgfVxuICB9KTtcbn1cblxuY29uc3QgREVWID0gdW5kZWZpbmVkO1xuXG5leHBvcnQgeyAkREVWQ09NUCwgJFBST1hZLCAkVFJBQ0ssIERFViwgRXJyb3JCb3VuZGFyeSwgRm9yLCBJbmRleCwgTWF0Y2gsIFNob3csIFN1c3BlbnNlLCBTdXNwZW5zZUxpc3QsIFN3aXRjaCwgYmF0Y2gsIGNhbmNlbENhbGxiYWNrLCBjYXRjaEVycm9yLCBjaGlsZHJlbiwgY3JlYXRlQ29tcG9uZW50LCBjcmVhdGVDb21wdXRlZCwgY3JlYXRlQ29udGV4dCwgY3JlYXRlRGVmZXJyZWQsIGNyZWF0ZUVmZmVjdCwgY3JlYXRlTWVtbywgY3JlYXRlUmVhY3Rpb24sIGNyZWF0ZVJlbmRlckVmZmVjdCwgY3JlYXRlUmVzb3VyY2UsIGNyZWF0ZVJvb3QsIGNyZWF0ZVNlbGVjdG9yLCBjcmVhdGVTaWduYWwsIGNyZWF0ZVVuaXF1ZUlkLCBlbmFibGVFeHRlcm5hbFNvdXJjZSwgZW5hYmxlSHlkcmF0aW9uLCBlbmFibGVTY2hlZHVsaW5nLCBlcXVhbEZuLCBmcm9tLCBnZXRMaXN0ZW5lciwgZ2V0T3duZXIsIGluZGV4QXJyYXksIGxhenksIG1hcEFycmF5LCBtZXJnZVByb3BzLCBvYnNlcnZhYmxlLCBvbiwgb25DbGVhbnVwLCBvbkVycm9yLCBvbk1vdW50LCByZXF1ZXN0Q2FsbGJhY2ssIHJlc2V0RXJyb3JCb3VuZGFyaWVzLCBydW5XaXRoT3duZXIsIHNoYXJlZENvbmZpZywgc3BsaXRQcm9wcywgc3RhcnRUcmFuc2l0aW9uLCB1bnRyYWNrLCB1c2VDb250ZXh0LCB1c2VUcmFuc2l0aW9uIH07XG4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7O0FBQUE7QUFDQTs7QUFFTztBQUNQOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUEsUUFBUSxRQUFRO0FBQ2hCO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOzs7Ozs7Ozs7Ozs7QUN2QkE7QUFDQTtBQUNBO0FBQ0EsY0FBYyxrREFBRTtBQUNoQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFVBQVU7QUFDVixRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSw2QkFBNkIsNEJBQTRCO0FBQ3pEO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQSx1QkFBdUIsMkVBQTJCO0FBQ2xEO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGdCQUFnQixrREFBRTtBQUNsQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLElBQUk7QUFDSjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0Esc0NBQXNDO0FBQ3RDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxpR0FBaUc7QUFDakc7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxxRUFBcUU7QUFDckU7QUFDQTtBQUNBO0FBQ0EscUVBQXFFO0FBQ3JFO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0Esc0NBQXNDO0FBQ3RDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsS0FBSztBQUNMO0FBQ0E7QUFDQTtBQUNBLHdFQUF3RTtBQUN4RTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE9BQU87QUFDUDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFNBQVM7QUFDVCxRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSw2RkFBNkY7QUFDN0Y7QUFDQTtBQUNBO0FBQ0E7QUFDQSxPQUFPO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxTQUFTO0FBQ1QsUUFBUTtBQUNSO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0EsTUFBTTtBQUNOO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSx5REFBeUQ7QUFDekQ7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBO0FBQ0EsS0FBSztBQUNMO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBLGtFQUFrRTtBQUNsRTtBQUNBO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxNQUFNO0FBQ047QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0Esb0NBQW9DO0FBQ3BDO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsNkNBQTZDO0FBQzdDO0FBQ0E7QUFDQTtBQUNBLE9BQU87QUFDUDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxzQkFBc0IsaUJBQWlCO0FBQ3ZDLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLHVCQUF1Qix3REFBd0Q7QUFDL0U7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsSUFBSTtBQUNKO0FBQ0EsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxPQUFPO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsR0FBRztBQUNIO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsT0FBTztBQUNQO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtB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