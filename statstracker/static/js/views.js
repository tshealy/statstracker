require=(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"views":[function(require,module,exports){
var views={"activity":"<h1>Detail of activity instance</h1>\n<a href=\"#activity/:id/edit\">Edit</a>\n<a href=\"#activity/:id/add\">Add</a>\n","home":"<ul>\n  <li>This is an activity title <a href=\"#instances\"><span> + </span></a></li>\n</ul>\n","instances":"<h1>This is a page listing the instances of a specific activity</h1>\n","new-activity":"<div class=\"form-container\">\n  <h1> New activity: </h1>\n  <form class=\"login-form\">\n    <label class=\"input\">\n      <span class=\"focus-out\">Activity</span>\n      <input class=\"input-box\" type=\"email\">\n    </label>\n    <label class=\"input\">\n      <span class=\"focus-out\">Etc</span>\n      <input class=\"input-box\" type=\"text\">\n    </label>\n    <label class=\"input\">\n      <span class=\"focus-out\">etc</span>\n      <input class=\"input-box\" type=\"text\">\n    </label>\n    <button class=\"submit-btn\">Submit</button>\n  </form>\n</div>\n"};
if (typeof module !== "undefined" && module.exports) { module.exports = views; }
},{}]},{},[]);