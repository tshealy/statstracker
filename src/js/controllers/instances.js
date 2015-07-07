'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('instances', function () {
  var activityHTML = views['instances'];

  $('.main-content').html(activityHTML);

});
