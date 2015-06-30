'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('', 'index', function () {
  var activityHTML = views['home'];

  $('.main-content').html(activityHTML);

});

$(function() {

  $.ajax({
    url: 'api/',
    method: 'GET',
    type: 'application/json'
  })
  .done(function() {
    alert( "success" );
  })
  .fail(function() {
    alert( "error" );
  });

});
