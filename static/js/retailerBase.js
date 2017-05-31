'use strict';
var baseApp = angular.module('retailerBaseApp', ['toaster'])
    .config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('{(');
        $interpolateProvider.endSymbol(')}');
    }])

    // baseApp.service('selectedCategory', function () {
    //     var category = '';
    //     this.category = category;
    //
    // });

    baseApp.controller('retailerBaseController',['$scope','$window',function ($scope,$window) {

        
    }])