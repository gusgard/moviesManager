(function(){
    'use strict';
    var app = angular.module('movies.app', []);

    app.config(function ( $httpProvider) {
        //$httpProvider.interceptors.push('myHttpRequestInterceptor');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });

    app.controller('AppController', function($scope, $http){
        $http.get('/api/movies').success(function (movies) {
            $scope.movies = movies;
            console.log('Movies ');
            console.log(movies);
        }).error(function (data, status) {
            console.log('Error code ' + status + ' ' + data);
        });

        $http.get('/api/films').success(function (films) {
            $scope.films = films;
            console.log('films ');
            console.log(films);
        }).error(function (data, status) {
            console.log('Error code ' + status + ' ' + data);
        });

        $http.get('/api/halls').success(function (hall) {
            $scope.halls = hall;
            console.log('hall ');
            console.log(hall);
        }).error(function (data, status) {
            console.log('Error code ' + status + ' ' + data);
        });

        $http.get('/api/hallfilms').success(function (hallfilms) {
            $scope.hallfilms = hallfilms;
            console.log('hallfilms')
            console.log(hallfilms);
        }).error(function (data, status) {
            console.log('Error code ' + status + ' ' + data);
        });

        $scope.halls = function(){


        }
    });

    app.controller('AppModal', function($scope, $http){
        // Simple POST request example (passing data) :

        $scope.saveHall = function(){
            console.log('aaaa');
            $http.post('/api/halls', {number:'123' , attendant:'gege'}).
                success(function(data, status, headers, config) {
                    // this callback will be called asynchronously
                    // when the response is available
                }).
                error(function(data, status, headers, config) {
                    // called asynchronously if an error occurs
                    // or server returns response with an error status.
                });
        }

    });
})();
