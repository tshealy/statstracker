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

  var csrftoken = getCookie('csrftoken');

  $.ajax({
    headers: { "X-CSRFToken": csrftoken },
    url: '/api/activities/',
    method: 'GET',
    type: 'application/json'
  })
  .done(function(data) {
    console.log(data.length);
    for (var i = 0; i < data.length; i++) {
      var title = $(data[i]).attr('title');
      console.log(title);
      var contentHtml = '<li class="activity-li">' + title + '<a href="#instances"><span class="add-instance">+</span></a></li>'
      $('.activity-ul').append(contentHtml);
  }
    console.log('pass');
  })
  .fail(function() {
    alert( "error" );
  });

function getCookie(name) {
 var cookieValue = null;
 if (document.cookie && document.cookie != '') {
     var cookies = document.cookie.split(';');
     for (var i = 0; i < cookies.length; i++) {
         var cookie = $.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
         }
     }
 }
 return cookieValue;
}
var csrftoken = getCookie('csrftoken');

console.log(csrftoken)

});
