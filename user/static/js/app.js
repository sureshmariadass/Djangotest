var app= angular.module("myApp",["ngRoute"]);
app.config(function($routeProvider){
  $routeProvider
  .when("/",{
    templateUrl:"<h1>Main</h1><p>Click on the links to change this content</p>"

  })
  .when("/cout",{
    templateUrl:"courses/ibm/cout.html"

  })
  .otherwise({
    redirectTo:"/"
  });
});
