#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT because my pre-commit
//   tries to run all scripts as Node apps.
if (typeof document !== 'undefined') {
  const recolor = '#FF0000'; // How to recolor.
  const header = document.querySelector('header');
  const triggerElement = document.getElementById('red_header');
  // Most recommended syntax, although .onclick() should work if I understood correctly.
  triggerElement.addEventListener('click', () => {
    header.style.color = recolor;
  }, { once: true });
  //  IMPORTANT: "once: true" is one of the keys of an "options" object to alter event Listener behaviour.
  //  It ensures that the associated behaviour/processing is only executed ONCE (first time Event is thrown)
  //    after that Javascript automatically removes this listener.
  //  => Good practice for alterations we want only applied once.
}
