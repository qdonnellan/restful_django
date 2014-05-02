var thingAppControllers = angular.module('thingAppControllers', []);

thingAppControllers.controller('ThingCtrl', ['$scope', 'Thing',
    function ($scope, Thing) {
        $scope.things = Thing.query();

        $scope.saveThing = function() {
            Thing.save($scope.thing, function(data) {
                // a successful post!
                $scope.things.push(data);
            }, function(error) {
                // an unsuccessful post, womp womp
                $scope.errors = error.data;
            });
        };
    }
]);
