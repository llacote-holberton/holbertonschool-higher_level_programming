#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  const header = document.querySelector('header');
  // Favoring this syntax because more explicit on the fact we target a CSS ID.
  const triggerElement = document.getElementById('toggle_header');
  // Reminder: first argument is "which event", second is "what to do", third is "options"
  triggerElement.addEventListener(
    'click',
    // Our process does not require any parameter hence empty (), we could define "event"
    //   if we needed some information on the actually propagated event
    //   because it is always automatically passed.
    () => { header.classList.toggle('red'); header.classList.toggle('green'); }
    // { once: true } @warning: this time we want the Listener to stay active "indefinitely" to allow alternated toggles.
  );
}
