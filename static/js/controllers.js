var thingAppControllers = angular.module('thingAppControllers', []);

thingAppControllers.controller('ThingCtrl', ['$scope', 'Thing',
    function ($scope, Thing) {
        $scope.things = Thing.query();

        $scope.saveThing = function() {
            Thing.save($scope.thing, function() {
                // a successful post!
                $scope.things = Thing.query();
            }, function(error) {
                // an unsuccessful post, womp womp
                $scope.errors = error.data;
            });
        };
    }
]);
