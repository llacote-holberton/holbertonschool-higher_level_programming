#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT so my pre-commit doesn't block.
if (typeof document !== 'undefined') {
  // Using the "shortest syntax" for simplicity (avoids need to wrap in asyc/await functions)
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    // Fetch creates a Promise. THEN reacts on Promise being fulfilled.
    .then(response => response.json()) // Response headers are received before full content received hence another Promise.
    .then(data => { document.querySelector('#character').textContent = data.name; })
  ;
}

/*
 * ===== SELF-TEACHING NOTES =====
 * Fetch API is asynchronous. Making a request creates a Promise.
 * Receiving response headers and finishing receiving response body are technically
 *   two separate steps (because the second can take a LONG time depending on request type and content size)
 *   and we cannot "skip one" so we always need to write "fetch(...).then"
 * Here we need another .then() to exploit the parsed json because
 *   while technically only the "stream reception" is really asynchronous,
 *   the method response.json includes the JSON parsing in the same Promise by simplicity.
 * In opposition if we read XML, we would use raw_data =  response.text() as a Promise to get full response body
 * then we'd make a "synchronous call" (= classic call) like xml = DomParser(raw_data) (NOTE: pseudo code probably not valid).
 */
