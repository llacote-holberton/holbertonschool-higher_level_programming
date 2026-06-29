#!/usr/bin/node

// @warning: "IF WRAPPER" is SPECIFIC TO MY ENVIRONMENT because my pre-commit
//   tries to run all scripts as Node apps.
if (typeof document !== 'undefined') {
  const header = document.querySelector('header');
  const recolor = '#FF0000'; // Pure Red in RGB.
  // Each HTMLElement has a "style" property which allows to read/define "inline styles".
  //   For this we must use the name of the CSS property converted into camelCase for composed names
  //   ex background-color (CSS stylesheet) -> style.backgroundColor (Javascript)
  header.style.color = recolor;
}
