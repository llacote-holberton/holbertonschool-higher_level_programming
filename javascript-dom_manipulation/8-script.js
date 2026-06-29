#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  // This time no point in defining "after the user".
  function grabAndInjectHelloTranslation () {
    const helloHost = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
      .then(response => response.json()) // Response headers are received before full content received hence another Promise.
      .then(data => { helloHost.textContent = data.hello; })
    ;
  }

  // Cf self-teaching notes on why this attachment to an event.
  document.addEventListener(
    'DOMContentLoaded',
    () => grabAndInjectHelloTranslation(),
    { once: true } // Here again business specs don't imply any use for repeating process.
  );
}

/*
 * ===== INSTRUCTIONS =====
 * Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr
 *   and displays the value of hello from that fetch in the HTML element with id hello.
 * The translation of “hello” must be displayed in the HTML element with id hello
 * Your script must work when it is imported from the <head> tag

 * ===== SELF-TEACHING NOTES =====
 * Fetch API is asynchronous. Confer task 6 for detailed notes.
 * Making the "fetch & inject" run "at main script level" wouldn't work here (I tried xd)
 *   because the script is called and run in <head> tag...
 *   So would be executed before the HTML body had time to be loaded and parsed
 *   -> ending with 'undefined' element to inject into.
 * Hence why we put everything in a function and "attach it to a particular event"
 *   which is thrown by the document object *only when all DOM content has finished being parsed*.
 * Cf https://developer.mozilla.org/en-US/docs/Web/API/Document#events
 */
