// The homepage's showcase: the stepper that builds a table one layer at a time, the tour of an
// interactive table (with the code for the reader's view of it), the copy buttons, and Tabblen
(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // Copy text, and show that it's copied on the button (its icon, for a moment)
  function copyText(button, text) {
    const done = () => {
      const icon = button.querySelector(".bi");
      button.classList.add("gth-copied");
      if (icon) icon.className = "bi bi-check2";
      setTimeout(() => {
        button.classList.remove("gth-copied");
        if (icon) icon.className = "bi bi-clipboard";
      }, 1400);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, () => {});
    } else {
      const area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      try {
        document.execCommand("copy");
        done();
      } catch (_) {}
      area.remove();
    }
  }

  function setUpCopyButtons() {
    for (const button of document.querySelectorAll("[data-copy]")) {
      button.addEventListener("click", () => copyText(button, button.dataset.copy));
    }
  }

  // The lines of a code cell's code, as elements, each with the line break after it (so that a line
  // can be folded away; the code's text, which the copy button copies, is as it was)
  function codeLines(cell) {
    const lines = Array.from(cell.querySelectorAll("pre code > span"));
    for (const line of lines) {
      const after = line.nextSibling;
      if (after && after.nodeType === Node.TEXT_NODE && after.data === "\n") line.appendChild(after);
    }
    return lines;
  }

  // Fold the runs of lines that aren't new (but the line before and after each new one) into a
  // line that says how many there are, which unfolds them when clicked
  function foldUnchanged(lines, added) {
    const keep = lines.map((_, k) => added[k] || added[k - 1] || added[k + 1]);
    let k = 0;
    while (k < lines.length) {
      if (keep[k]) {
        k++;
        continue;
      }
      let end = k;
      while (end < lines.length && !keep[end]) end++;
      const run = lines.slice(k, end);
      if (run.length >= 3) {
        const [mark, ...rest] = run;
        mark.classList.add("gth-fold-mark");
        mark.dataset.fold = `${run.length} unchanged lines`;
        mark.tabIndex = 0;
        mark.setAttribute("role", "button");
        mark.setAttribute("aria-label", `Show ${run.length} unchanged lines`);
        for (const line of rest) line.classList.add("gth-folded");
        const unfold = () => {
          mark.classList.remove("gth-fold-mark");
          mark.removeAttribute("role");
          mark.removeAttribute("tabindex");
          mark.removeAttribute("aria-label");
          for (const line of rest) line.classList.remove("gth-folded");
        };
        mark.addEventListener("click", unfold);
        mark.addEventListener("keydown", (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            unfold();
          }
        });
      }
      k = end;
    }
  }

  // Which lines of `next` aren't in `prev` (by the longest common subsequence of the two)
  function newLines(prev, next) {
    const m = prev.length;
    const n = next.length;
    const lcs = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = m - 1; i >= 0; i--) {
      for (let j = n - 1; j >= 0; j--) {
        lcs[i][j] = prev[i] === next[j] ? lcs[i + 1][j + 1] + 1 : Math.max(lcs[i + 1][j], lcs[i][j + 1]);
      }
    }
    const added = new Array(n).fill(true);
    let i = 0;
    let j = 0;
    while (i < m && j < n) {
      if (prev[i] === next[j]) {
        added[j] = false;
        i++;
        j++;
      } else if (lcs[i + 1][j] >= lcs[i][j + 1]) {
        i++;
      } else {
        j++;
      }
    }
    return added;
  }

  function setUpStepper(stepper) {
    const steps = Array.from(stepper.querySelectorAll(":scope > .gth-step"));
    if (steps.length === 0) return;

    const tabs = document.createElement("div");
    tabs.className = "gth-tabs";
    tabs.setAttribute("role", "tablist");
    tabs.setAttribute("aria-label", "The layers of the table");

    const viewport = document.createElement("div");
    viewport.className = "gth-panels";
    const stack = document.createElement("div");
    stack.className = "gth-stack";
    viewport.appendChild(stack);

    const id = stepper.id || "gth-stepper";
    let previous = [];

    const buttons = steps.map((step, index) => {
      // The step's name (its first paragraph) goes on its tab
      const nameEl = step.querySelector(".gth-step-name");
      const name = nameEl ? nameEl.textContent.trim() : `Step ${index + 1}`;
      if (nameEl) {
        const para = nameEl.closest("p");
        (para && para.parentElement === step ? para : nameEl).remove();
      }

      const button = document.createElement("button");
      button.type = "button";
      button.className = "gth-tab";
      button.id = `${id}-tab-${index}`;
      button.setAttribute("role", "tab");
      button.setAttribute("aria-controls", `${id}-panel-${index}`);
      button.innerHTML = `<span class="gth-tab-num">${index + 1}</span><span class="gth-tab-name"></span><span class="gth-tab-progress" aria-hidden="true"></span>`;
      button.querySelector(".gth-tab-name").textContent = name;
      tabs.appendChild(button);

      step.id = `${id}-panel-${index}`;
      step.setAttribute("role", "tabpanel");
      step.setAttribute("aria-labelledby", button.id);
      step.classList.add("gth-panel");

      // The code's lines, with those new to this step marked
      const cell = step.querySelector(".cell");
      if (cell) {
        const lines = codeLines(cell);
        const text = lines.map((line) => line.textContent.replace(/\s+$/, ""));
        const added = newLines(previous, text);
        let count = 0;
        lines.forEach((line, k) => {
          if (added[k] && text[k] !== "" && previous.length > 0) {
            line.classList.add("gth-new");
            count++;
          }
        });
        if (previous.length > 0) foldUnchanged(lines, added);
        previous = text;
        const code = cell.querySelector(".cell-code");
        if (code && count > 0) {
          const badge = document.createElement("span");
          badge.className = "gth-new-count";
          badge.textContent = `${count} new line${count === 1 ? "" : "s"}`;
          code.appendChild(badge);
        }
        // The table first, then the code that made it
        const output = cell.querySelector(".cell-output-display");
        if (code && output) cell.insertBefore(output, code);
      }

      stack.appendChild(step);
      return button;
    });

    stepper.prepend(tabs);
    stepper.appendChild(viewport);

    let active = -1;
    let observer = null;

    function fitHeight() {
      if (active < 0) return;
      viewport.style.height = `${steps[active].offsetHeight}px`;
    }

    function scrollToNew(step) {
      const pre = step.querySelector(".cell-code pre");
      const first = step.querySelector(".gth-new");
      if (!pre || !first) return;
      const top = first.offsetTop - pre.offsetTop - 12;
      pre.scrollTo({ top: Math.max(0, top), behavior: reduceMotion.matches ? "auto" : "smooth" });
    }

    function show(index, focus = false) {
      if (index === active) return;
      active = index;
      steps.forEach((step, k) => {
        const on = k === index;
        step.classList.toggle("gth-active", on);
        step.inert = !on;
        step.setAttribute("aria-hidden", on ? "false" : "true");
        buttons[k].setAttribute("aria-selected", on ? "true" : "false");
        buttons[k].tabIndex = on ? 0 : -1;
        buttons[k].classList.toggle("gth-done", k < index);
      });
      if (focus) buttons[index].focus();
      if (observer) {
        observer.disconnect();
        observer.observe(steps[index]);
      }
      fitHeight();
      scrollToNew(steps[index]);
    }

    // Autoplay: through the steps while the stepper is in view, until the reader takes over
    const DWELL = 5200;
    let timer = null;
    let playing = !reduceMotion.matches;
    let visible = false;

    function stopPlaying() {
      playing = false;
      stepper.classList.remove("gth-playing");
      clearTimeout(timer);
      timer = null;
    }

    function schedule() {
      clearTimeout(timer);
      timer = null;
      if (!playing || !visible) {
        stepper.classList.remove("gth-playing");
        return;
      }
      if (active >= steps.length - 1) {
        stopPlaying();
        return;
      }
      // (Restarting the tab's progress bar)
      stepper.classList.remove("gth-playing");
      void stepper.offsetWidth;
      stepper.style.setProperty("--gth-dwell", `${DWELL}ms`);
      stepper.classList.add("gth-playing");
      timer = setTimeout(() => {
        show(active + 1);
        schedule();
      }, DWELL);
    }

    buttons.forEach((button, index) => {
      button.addEventListener("click", () => {
        stopPlaying();
        show(index);
      });
    });

    tabs.addEventListener("keydown", (event) => {
      const keys = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 };
      let next = null;
      if (event.key in keys) next = (active + keys[event.key] + steps.length) % steps.length;
      else if (event.key === "Home") next = 0;
      else if (event.key === "End") next = steps.length - 1;
      if (next === null) return;
      event.preventDefault();
      stopPlaying();
      show(next, true);
    });

    // Working with the table (or its code) stops the autoplay too
    viewport.addEventListener("pointerdown", stopPlaying);
    viewport.addEventListener("focusin", stopPlaying);

    if ("ResizeObserver" in window) {
      observer = new ResizeObserver(fitHeight);
    }
    window.addEventListener("resize", fitHeight);

    stepper.classList.add("gth-ready");
    show(0);

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            visible = entry.isIntersecting;
            schedule();
          }
        },
        // (In view: across the middle of the window, however tall the stepper is)
        { rootMargin: "-35% 0px -35% 0px" },
      ).observe(stepper);
    }
  }

  // The tour of an interactive table: chips that set its view, and the code for the view
  function setUpTour(tour) {
    const table = tour.querySelector("gt-table");
    if (!table) return;
    // (The table right after the chips, then the code that made it)
    const output = table.closest(".cell-output-display");
    const cell = output ? output.closest(".cell") : null;
    if (cell && output.parentElement === cell) cell.prepend(output);
    const chips = Array.from(tour.querySelectorAll(".gth-chip"));
    const live = tour.querySelector(".gth-livecode");
    const codeEl = live ? live.querySelector("code") : null;
    let backend = "polars";
    let applied = null;

    const snapshot = () => JSON.stringify([table.filter, table.sort, table.groupBy]);

    function updateCode() {
      if (!live || typeof table.toCode !== "function") return;
      let code = "";
      try {
        code = table.toCode(backend);
      } catch (_) {
        code = "";
      }
      if (!code) {
        live.hidden = true;
        return;
      }
      live.hidden = false;
      // (Until there's a view, the code is only the data)
      const hidden = table.hiddenColumns || [];
      if (table.filter === null && table.sort.length === 0 && table.groupBy === null && hidden.length === 0) {
        code = "# Pick a view above, or filter, sort or group the table,\n# to see the code that gets its rows from the data";
      }
      if (codeEl.textContent !== code) {
        codeEl.textContent = code;
        live.classList.remove("gth-flash");
        void live.offsetWidth;
        live.classList.add("gth-flash");
      }
    }

    function updateChips() {
      const now = snapshot();
      for (const chip of chips) {
        chip.setAttribute("aria-pressed", applied && applied.chip === chip && applied.state === now ? "true" : "false");
      }
      if (applied && applied.state !== now) applied = null;
    }

    let pending = 0;
    function refresh() {
      cancelAnimationFrame(pending);
      pending = requestAnimationFrame(() => {
        updateCode();
        updateChips();
      });
    }

    function apply(chip) {
      const spec = chip.dataset.view;
      if (spec === "reset") {
        table.resetView();
        applied = null;
      } else {
        const view = JSON.parse(spec);
        table.search = "";
        table.groupBy = view.groupBy ?? null;
        table.filter = view.filter ?? null;
        table.sort = view.sort ?? [];
        applied = { chip, state: snapshot() };
      }
      refresh();
    }

    for (const chip of chips) {
      chip.setAttribute("aria-pressed", "false");
      chip.addEventListener("click", () => apply(chip));
    }

    if (live) {
      for (const button of live.querySelectorAll("[data-backend]")) {
        button.addEventListener("click", () => {
          backend = button.dataset.backend;
          for (const other of live.querySelectorAll("[data-backend]")) {
            other.setAttribute("aria-pressed", other === button ? "true" : "false");
          }
          refresh();
        });
      }
      const copy = live.querySelector(".gth-livecode-copy");
      if (copy) copy.addEventListener("click", () => copyText(copy, codeEl.textContent));
    }

    // (Setting the view's properties fires no events, but the reader's changes do; grouping and
    // hiding columns are watched for as clicks and changes in the table)
    for (const type of ["gt-table-view", "gt-table-filter", "gt-table-sort", "change", "click"]) {
      table.addEventListener(type, () => setTimeout(refresh, 30));
    }

    const ready = () => table.state === "ready";
    if (ready()) {
      refresh();
    } else {
      const watcher = new MutationObserver(() => {
        if (ready()) {
          watcher.disconnect();
          refresh();
        }
      });
      watcher.observe(table, { attributes: true, attributeFilter: ["data-gti-state"] });
    }
  }

  // Tabblen (assets/tabblen.js), by the steps for getting started: when he's first seen, he waves,
  // says hello and spells out his library's name in his cells, and he hops when the install
  // command is copied
  function setUpTabblen(start) {
    const tabblen = start.querySelector("gt-tabblen");
    if (!tabblen || !window.customElements) return;
    customElements.whenDefined("gt-tabblen").then(async () => {
      start.addEventListener("click", (event) => {
        if (!event.target.closest(".gd-code-copy, .code-copy-button, [data-copy]")) return;
        tabblen.say("Copied! Off you go.", 1800);
        tabblen.play([["mood", "grin"], ["hop", 2], ["mood", "happy"]]);
      });
      await tabblen.seen();
      tabblen.say("Hi! I'm Tabblen.", 2200);
      await tabblen.play([
        ["wave", 2],
        ["arms", "open"],
        ["write", "GREAT TABLES"],
        ["mood", "grin"],
        ["hop", 1],
        ["wait", 400],
        ["mood", "happy"],
        ["arms", "rest"],
      ]);
    });
  }

  function init() {
    setUpCopyButtons();
    document.querySelectorAll(".gth-stepper").forEach(setUpStepper);
    document.querySelectorAll(".gth-tour").forEach(setUpTour);
    document.querySelectorAll(".gth-start").forEach(setUpTabblen);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
