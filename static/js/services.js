var thingAppServices = angular.module('thingAppServices', [
    'ngResource'
]);

thingAppServices.factory('Thing', ['$resource', function ($resource){
    return $resource('api/things/:thingId', {thingId: '@id'});
}])