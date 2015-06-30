'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('activity/:id', function () {
  var activityHTML = views['activity'];

  $('.main-content').html(activityHTML);

});
