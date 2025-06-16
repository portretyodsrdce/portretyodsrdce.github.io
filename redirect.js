// redirect.js
(function() {
  if (window.location.hostname === "portretyodsrdce.github.io") {
    // redirect pouze pokud je hash prázdný (tedy uživatel právě přišel na základní stránku)
    if (!window.location.hash) {
      const langFragment = window.location.hash; // tady prázdné, ale pro jistotu
      const target = 'https://portretyodsrdce.cz/' + langFragment;
      window.location.replace(target);
    }
    // Pokud je fragment (#en, #cs), redirect neprovádět, už je na správné stránce
  }
})();
