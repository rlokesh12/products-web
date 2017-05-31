
    baseApp.controller('retailerDashController',['$scope','$http','$window','toaster',function ($scope,$http,$window,toaster) {
        $scope.productList = [];
        $scope.categories = [];
        $scope.showTable = false;
        $scope.selectedCategory;
        $scope.getCategories = function () {
            var url = '/api/v1/category/';
             $http({
                url: url,
                method: 'GET',
                data: {}
            })
                .then(function (response) {
                    console.log("Got em");
                    $scope.categories = response.data.objects;
                })
                .catch(function (response) {
                    console.log("err");
                })
        };
        $scope.getProductList = function (category) {
            // if(category == 'all')
            //     var url = '/api/v1/product/?format=json';
            // else
            var url = '/api/v1/category/?format=json&id='+category;
            $http({
                url: url,
                method: 'GET',
                params: {}
            })
                .then(function (response) {
                    console.log("yup");
                    $scope.selectedCategoryName = response.data.objects[0].name;
                })
                .catch(function (response) {
                    console.log("err");
                })
            var url = '/api/v1/product/?format=json&category__id='+category;
            $http({
                url: url,
                method: 'GET',
                params: {}
            })
                .then(function (response) {
                    $scope.showTable = true;
                    // $scope.selectedCategory = category;
                    // console.log(response.data.objects);
                    $scope.selectedCategory = category;
                    $scope.productList = response.data.objects;
                })
                .catch(function (response) {
                    console.log("err");
                })

        }
        $scope.editProduct = function (productId,categoryId) {

            var url = '/retailer/editProduct/';
            $window.location.href = url;
        };
        $scope.removeProduct = function (productId,categoryId) {
            var url = '/removeProduct/';
            $http({
                url: url,
                method: "POST",
                data:{"productId": productId}
            })
                .then(function (response) {
                    console.log("removed")
                    console.log(response.data.msg)
                    if(response.data.msg == "Success"){
                        console.log(response.data.msg)
                        toaster.pop("success","success","Product Removed")
                        $scope.getProductList(categoryId)

                    }
                })
                .catch(function (response) {
                    console.log("error")
                })
        }
        $scope.getCategories();
    }])