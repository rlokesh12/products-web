 baseApp.controller('retailerEditController',['$scope','$http','$window',function ($scope,$http,$window) {
        $scope.productList = [];
        $scope.categories = [];
        $scope.showTable = false;
        $scope.productDetails = {};
        $scope.categoryDetails = {};
        $scope.categoryUrl;
        $scope.id =3;
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
        $scope.getProductDetails = function () {
            var path = location.pathname;
            var parts=path.split('/');
            console.log(parts);
            var url = '/api/v1/product/'+parts[2]+'/';
            $http({
                url: url,
                method: 'GET',
                params: {}
            })
                .then(function (response) {
                    if(response.data){
                        $scope.productDetails = response.data;
                        // console.log($scope.productDetails.image)
                        $scope.categoryUrl = $scope.productDetails.category;
                        $http({
                            url: $scope.categoryUrl,
                            method: 'GET',
                            params: {}
                        })
                            .then(function (urlresponse) {
                                if(urlresponse.data){
                                    $scope.categoryDetails = urlresponse.data;
                                    console.log("--->",$scope.categoryDetails.id)
                                }

                            })
                            .catch(function (urlresponse) {
                                console.log("err in category fetch")

                            })
                    }
                })
                .catch(function (response) {
                    console.log("err in product fetch")
                })
        }
        $scope.getProductDetails();
        $scope.getCategories();
    }])