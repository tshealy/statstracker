'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('new-activity', function () {
  var activityHTML = views['new-activity'];

  $('.main-content').html(activityHTML);

});

$(function() {
  $('input').focusin(function() {
    $(this).siblings('span').addClass('focus-in');
  });

  $('input').focusout(function() {
    var characters = $(this).val();
    if (characters === '') {
    $(this).siblings('span').removeClass('focus-in');
  }
  });

});
