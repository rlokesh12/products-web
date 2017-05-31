'use strict';
angular.module('showProductsApp', [])
    .config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('{(');
        $interpolateProvider.endSymbol(')}');
    }])

    .controller('showProductsController',['$scope','$http','$window',function ($scope,$http,$window) {
        $scope.productList = [];
        $scope.categories = [];
        $scope.selectedCategory;
        $scope.getCategories = function () {
            var url = '/api/v1/category/';
             $http({
                url: url,
                method: 'GET',
                data: {}
            })
                .then(function (response) {
                    // console.log("Got em");
                    $scope.categories = response.data.objects;
                })
                .catch(function (response) {
                    console.log("err");
                })
        };
        $scope.getProductList = function (category) {
            if(category == 'all')
                var url = '/api/v1/product/?format=json';
            else
                var url = '/api/v1/product/?format=json&category__name='+category;
            $http({
                url: url,
                method: 'GET',
                params: {}
            })
                .then(function (response) {
                    // console.log(response.data.objects);
                    if(category=='all')
                        $scope.selectedCategory = 'All Products';
                    else
                        $scope.selectedCategory = category;
                    $scope.productList = response.data.objects;
                })
                .catch(function (response) {
                    console.log("err");
                })

        }
        $scope.getProductList("all");
        $scope.getCategories();
    }])