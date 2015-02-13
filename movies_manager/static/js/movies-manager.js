/* Project specific Javascript goes here. */
'use strict';
var app = angular.module('movies.app', []);

app.controller('AppController', function($scope, $http){
    $http.get('/api/films').success(function (newPost) {
        $scope.films = newPost;
        console.log(newPost)
    }).error(function (data, status) {
        console.log('Error code ' + status + ' ' + data);
    });

});