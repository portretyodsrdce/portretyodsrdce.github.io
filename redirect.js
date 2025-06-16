// redirect.js
(function () {
  // Redirect POUZE pokud jsme na GitHub Pages doméně
  if (window.location.hostname === "portretyodsrdce.github.io") {
    // Redirect jen pokud není žádný fragment (jazyk)
    if (!window.location.hash || window.location.hash === "#") {
      window.location.replace("https://portretyodsrdce.cz/");
    }
  }
})();
