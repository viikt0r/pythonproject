new Vue(
    {
        el: '#simpleApp',
        data: {
            showAlert: false
        },
        methods: {
            loadApi: function () {
                this.$http.get('https://jsonplaceholder.typicode.com/posts').
                then(this.successCallback, this.errorCallback);
            },
            successCallback: function(response) {
                console.log('successCallback response:' , response);
            },
            errorCallback: function(response) {
                console.log('errorCallback response:' , response);
            }
        }
    }
    );