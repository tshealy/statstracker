(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";var $=require("jquery"),_=require("underscore"),views=require("views"),router=require("../router");router.route("activity/:id",function(){var r=views.activity;$(".main-content").html(r)});

},{"../router":6,"jquery":"jquery","underscore":"underscore","views":"views"}],2:[function(require,module,exports){
"use strict";var $=require("jquery"),_=require("underscore"),views=require("views"),router=require("../router");router.route("","index",function(){var e=views.home;$(".main-content").html(e)}),$(function(){function e(e){var r=null;if(document.cookie&&""!=document.cookie)for(var n=document.cookie.split(";"),o=0;o<n.length;o++){var t=$.trim(n[o]);if(t.substring(0,e.length+1)==e+"="){r=decodeURIComponent(t.substring(e.length+1));break}}return r}var r=e("csrftoken");$.ajax({headers:{"X-CSRFToken":r},url:"/api/activities/",method:"GET",type:"application/json"}).done(function(e){console.log(e.length);for(var r=0;r<e.length;r++){var n=$(e[r]).attr("title");console.log(n);var o='<li class="activity-li">'+n+'<a href="#instances"><span class="add-instance">+</span></a></li>';$(".activity-ul").append(o)}console.log("pass")}).fail(function(){alert("error")});var r=e("csrftoken");console.log(r)});

},{"../router":6,"jquery":"jquery","underscore":"underscore","views":"views"}],3:[function(require,module,exports){
"use strict";var $=require("jquery"),_=require("underscore"),views=require("views"),router=require("../router");router.route("instances",function(){var e=views.instances;$(".main-content").html(e)});

},{"../router":6,"jquery":"jquery","underscore":"underscore","views":"views"}],4:[function(require,module,exports){
"use strict";var $=require("jquery"),_=require("underscore"),views=require("views"),router=require("../router");router.route("new-activity",function(){var t=views["new-activity"];$(".main-content").html(t)}),$(function(){function t(t){var i=null;if(document.cookie&&""!=document.cookie)for(var e=document.cookie.split(";"),n=0;n<e.length;n++){var o=$.trim(e[n]);if(o.substring(0,t.length+1)==t+"="){i=decodeURIComponent(o.substring(t.length+1));break}}return i}$("input").focusin(function(){$(this).siblings("span").addClass("focus-in")}),$("input").focusout(function(){var t=$(this).val();""===t&&$(this).siblings("span").removeClass("focus-in")});var i=t("csrftoken");$(".login-form").submit(function(t){t.preventDefault();var e=$(".activity-title").val();console.log(e),$.ajax({headers:{"X-CSRFToken":i},url:"/api/activities/",method:"POST",data:{id:50,profile:10,title:e}}).done(function(t){alert("posted"),console.log(t)}).fail(function(){alert("didnt post")}),window.location=""});var i=t("csrftoken")});

},{"../router":6,"jquery":"jquery","underscore":"underscore","views":"views"}],5:[function(require,module,exports){
"use strict";var router=require("./router");({controllers:{activity:require("./controllers/activity.js"),home:require("./controllers/home.js"),instances:require("./controllers/instances.js"),"new-activity-controller":require("./controllers/new-activity-controller.js")}}),router.init();

},{"./controllers/activity.js":1,"./controllers/home.js":2,"./controllers/instances.js":3,"./controllers/new-activity-controller.js":4,"./router":6}],6:[function(require,module,exports){
"use strict";var SortedRouter=require("./sorted-router");module.exports=new SortedRouter;

},{"./sorted-router":7}],7:[function(require,module,exports){
"use strict";var Backbone=require("backbone"),_=require("underscore"),SortedRouter=Backbone.Router.extend({sortedRoutes:{},route:function(){for(var e=arguments.length-1,t=arguments[arguments.length-1],r=0;e>r;++r)this.sortedRoutes[arguments[r]]=t},init:function(){var e=-1e6,t=this;_.chain(_.pairs(this.sortedRoutes)).sortBy(function(t){var r=t[0];return r.indexOf("*")>=0?e:-r.split(":").length}).each(function(e){Backbone.Router.prototype.route.apply(t,e)}),Backbone.history.start()}});module.exports=SortedRouter;

},{"backbone":"backbone","underscore":"underscore"}]},{},[5])


//# sourceMappingURL=app.js.map