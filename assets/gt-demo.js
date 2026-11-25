// A live app demo in the docs, as a <gt-demo> element: a poster of the app, until the reader asks
// for it to be run, when the app (a page of its own, run in the browser on Pyodide) is shown in a
// frame in its place. Nothing of the app's is loaded until then, as it's tens of MB.
//
//   <script src="../assets/gt-demo.js" defer></script>
//   <gt-demo src="../demos/streamlit/" poster="../assets/demos/streamlit.webp" height="760"
//     label="The Streamlit app" size="45 MB"></gt-demo>
//
// Attributes:
//   src      the app's page (also opened, as the full page, by the link below the frame)
//   poster   an image of the app
//   height   the frame's height, in pixels (720 by default)
//   label    what the app is, for the frame's title and the poster's description
//   size     about how much the app downloads the first time it's run
//   action   the poster's button ("Run this app" by default)

(() => {
  const STYLE = `
    :host {
      display: block;
      margin: 1rem 0 1.5rem;
    }
    .frame {
      position: relative;
      overflow: hidden;
      border: 1px solid color-mix(in srgb, currentColor 20%, transparent);
      border-radius: 6px;
      background: #fff;
    }
    img, iframe {
      display: block;
      width: 100%;
      height: 100%;
      border: 0;
    }
    img {
      object-fit: cover;
      object-position: top left;
      opacity: 0.55;
    }
    .start {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
    }
    button {
      font: inherit;
      font-weight: 600;
      padding: 0.6rem 1.2rem;
      border: 0;
      border-radius: 999px;
      color: #fff;
      background: #0b5cad;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
      cursor: pointer;
    }
    button:hover {
      background: #094c8f;
    }
    button:focus-visible {
      outline: 3px solid #0b5cad;
      outline-offset: 3px;
    }
    .note {
      margin: 0;
      padding: 0.2rem 0.7rem;
      border-radius: 999px;
      font-size: 0.85rem;
      color: #2b2b33;
      background: rgba(255, 255, 255, 0.85);
    }
    .links {
      margin: 0.4rem 0 0;
      font-size: 0.9rem;
      text-align: right;
    }
    a {
      color: inherit;
    }
  `;

  class GtDemo extends HTMLElement {
    connectedCallback() {
      if (this.shadowRoot) {
        return;
      }
      const root = this.attachShadow({ mode: "open" });
      const label = this.getAttribute("label") || "The app";
      const size = this.getAttribute("size");
      const src = this.getAttribute("src") || "";
      const height = Number(this.getAttribute("height")) || 720;

      const style = document.createElement("style");
      style.textContent = STYLE;
      const frame = document.createElement("div");
      frame.className = "frame";
      frame.style.height = `${height}px`;

      const poster = document.createElement("img");
      poster.src = this.getAttribute("poster") || "";
      poster.alt = `${label}, as it looks once it's run`;
      poster.loading = "lazy";
      const start = document.createElement("div");
      start.className = "start";
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = `▶ ${this.getAttribute("action") || "Run this app"}`;
      const note = document.createElement("p");
      note.className = "note";
      note.textContent = `Runs Python in your browser${size ? `: about ${size} the first time` : ""}`;
      start.append(button, note);
      frame.append(poster, start);

      const links = document.createElement("p");
      links.className = "links";
      const full = document.createElement("a");
      full.href = src;
      full.target = "_blank";
      full.rel = "noopener";
      full.textContent = "Open full page ↗";
      links.append(full);

      button.addEventListener("click", () => {
        const app = document.createElement("iframe");
        app.src = src;
        app.title = `${label}, running in your browser`;
        frame.replaceChildren(app);
        app.focus();
      });
      root.append(style, frame, links);
    }
  }

  customElements.define("gt-demo", GtDemo);
})();
