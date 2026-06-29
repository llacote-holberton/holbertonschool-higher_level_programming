#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  // Grabbing the "list host".
  const titlesList = document.querySelector('ul#list_movies');

  // Using the "shortest syntax" for simplicity (avoids need to wrap in asyc/await functions)
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    // Fetch creates a Promise. THEN reacts on Promise being fulfilled.
    .then(response => response.json()) // Response headers are received before full content received hence another Promise.
    .then(data => { data.results.forEach(injectTitleInDedicatedList); })
  ;

  // Fun fact: code above will "know" about it, confer notes.
  function injectTitleInDedicatedList (jsonData) {
    const titleLi = document.createElement('li');
    titleLi.append(document.createTextNode(jsonData.title));
    titlesList.append(titleLi);
  }
}

/*
 * ===== INSTRUCTIONS =====
 * Write a JS script using Fetch API to retrieve the title for all movies
 * by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
 * AND inject them as li elements inside the ul#list_movies element.
 *
 * ===== SELF-TEACHING NOTES =====
 * Fetch API is asynchronous. Confer task 6 for detailed notes.
 *
 * Fun fact on functions definitions and use.
 *: Javascript being a half-decent language means you can
 *   define function wherever in file. Thanks to a process called "hoisting"...
 *   (let's summarize as "pre-reading of all script content to put some definitions on top")
 *  Code "above" can actually know the existence of a function defined below in code.
 */
