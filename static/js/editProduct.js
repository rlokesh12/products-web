 baseApp.controller('retailerEditController',['$scope','$http','$window',function ($scope,$http,$window) {
        $scope.productList = [];
        $scope.categories = [];
        $scope.showTable = false;
        // $scope.selectedCategory = selectedCategory.category;
        console.log("edit::",$scope.selectedCategory);
        $scope.getCategories = function () {
            var url = '/api/v1/category/';
             $http({
                url: url,
                method: 'GET',
                data: {}
            })
                .then(function (response) {

                    $scope.categories = response.data.objects;
                })
                .catch(function (response) {
                    console.log("err");
                })
        };
        $scope.getCategories();
    }])