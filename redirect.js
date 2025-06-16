// redirect.js
(function() {
  const langFragment = window.location.hash; // zachytí #en, #cs, nebo prázdné
  const target = 'https://portretyodsrdce.cz/' + langFragment;
  window.location.replace(target);
})();
