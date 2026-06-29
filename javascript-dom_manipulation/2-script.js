#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  const header = document.querySelector('header');
  // Using the "generic" method to show syntax difference compared to task 1.
  // getElementById expects CSS id WITHOUT the '#' while querySelector REQUIRES IT.
  const triggerElement = document.querySelector('#red_header');
  // Reminder: first argument is "which event", second is "what to do", third is "options"
  triggerElement.addEventListener(
    'click',
    // Our process does not require any parameter hence empty (), we could define "event"
    //   if we needed some information on the actually propagated event
    //   because it is always automatically passed.
    () => { header.classList.add('red'); }, // Specific "sub-object" with defined methods add/remove/toggle.
    { once: true }
  );
}
