var app = angular.module('App', []);

app.controller('fileController', ['$scope', '$http', '$timeout', '$q', 
function ($scope, $http, $timeout, $q) {
    
    $scope.file = '';
    
    $scope.getFile = function() {
        //return postFormData_xhr();
        return postFormData();
    };
    
    function postFormData() {
        var formData = new FormData();
        formData.append('file', $scope.file);
        
        return $http({
            method: 'POST',
            url: '/uploadCSV2',
            data: formData,
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        }).then(function successCallback(response) {
            //do stuff
            //console.log( response );
        }, function errorCallback(response) {
            // do stuff
            console.log( 'error response', response );
        });
    };
    
    // Originally I could get it to work with this function (XMLHttpRequest) while $http.post did not work.
    // Changing the headers for the post headers resolved this issue.
    function postFormData_xhr() {
        var deferred = $q.defer(),
        formdata = new FormData(),
        xhr = new XMLHttpRequest();
        formdata.append('file', $scope.file);
        
        xhr.onreadystatechange = function(r) {
            if (4 === this.readyState) {
                if (xhr.status == 200) {
                    deferred.resolve(xhr);
                } else {
                    deferred.reject(xhr);
                }
            }
        }
        xhr.open("POST", '/uploadCSV2', true);
        xhr.send(formdata);
        return deferred.promise;
    };
    
}]);

app.directive("ngFile",function(){
    return {
        link: function($scope,el){
            el.bind("change", function(e){
                $scope.file = (e.srcElement || e.target).files[0];
                $scope.getFile().then(function(){
                    (e.srcElement || e.target).value = '';
                });
            })
        }
    }
});
