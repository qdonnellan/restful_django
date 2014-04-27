var thingAppControllers = angular.module('thingAppControllers', []);

thingAppControllers.controller('ThingCtrl', ['$scope', 'Thing', 
    function ($scope, Thing) {
        $scope.things = Thing.query();
    }
]);