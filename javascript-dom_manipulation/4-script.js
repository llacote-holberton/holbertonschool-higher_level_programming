#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  // Creating a dedicated function to cleanly separate
  //   the "do something on a click" and "what is actually done"
  function injectNewLiElement () {
    // For now we "get" the list to expand directly here because simpler.
    const listToExpand = document.querySelector('ul.my_list');
    const newLi = document.createElement('li');
    newLi.appendChild(document.createTextNode('Item'));
    listToExpand.appendChild(newLi);
  }

  const elementAdder = document.getElementById('add_item');
  elementAdder.addEventListener(
    'click',
    () => { injectNewLiElement(); }
  );
}

/*
 * ===== SELF-TEACHING NOTES =====
 * === About selecting the Unordered List we want to enrich.
 * @note: can use "const" because adding an element is mutating the object,
 *   NOT changing the reference variable points to.
 * @note: querySelector('ul.my_list') will pick the FIRST matching element.
 * No other way since we only have a class to "filter" instead of an id.
 * So if several ul with that class, only first will be updated.
 * @important: it is also why we use querySelector so we can at least restrict on ul tags with that class.
 * If we instead used getElementByClassName we would get the first tag with that class, whether ul or not.
 *
 * === About creating and "attaching" a new Element
 * CF https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement
 *
 * === About having the "list to expand" statically identified and retrieved inside the "adder function" ===
 * Best practice would have been to make that function parameterized (ex injectNewLiElementInside(parentListElement))
 *   but it's not intuitive at all to provide arguments to a function which is itself a parameter of addEventListener.
 * So will be experimented in a later task, probably. :)
 */
