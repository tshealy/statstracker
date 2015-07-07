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

  var csrftoken = getCookie('csrftoken');

  $('.login-form').submit(function(e) {
    e.preventDefault();

    var title = $('.activity-title').val();
    console.log(title);

    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url: '/api/activities/',
      method: 'POST',
      data: ({
        id: 50,
        profile: 10,
        title: title
      }),
    })
    .done(function(data){
      alert('posted');
      console.log(data);
    })
    .fail(function() {
      alert('didnt post');
    });
    window.location = '';
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



});
