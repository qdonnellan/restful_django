var thingApp = angular.module('thingApp', [
    'thingAppControllers', 'thingAppServices'
]);

thingApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

