#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  // Trying another method to get the header.
  const headerToUpdate = document.getElementsByTagName('header')[0];
  const headerContentSetter = document.getElementById('update_header');
  headerContentSetter.addEventListener(
    'click',
    () => { headerToUpdate.innerText = 'New Header!!!'; },
    { once: true } // Adding this because we don't need multiple times for the same result.
  );
}
/*
 * ===== SELF-TEACHING NOTES =====
 * document.getElementsByTagName
 * THIS is what I could (should?) have used in previous tasks when only tag used to search.
 * Although this has the same problem as getbyClassName, would pick the FIRST of all matching in page.
 * ALSO always returns an array so must target the first one, supposing a) it exists b) it's the one I want.
 */
