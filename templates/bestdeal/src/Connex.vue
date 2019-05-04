<template>
  <div id="app">
    <v-app>
      <v-container> 
        <v-layout row>
          <div>
            <v-btn v-on:click="loadApi" color="primary">Load Data</v-btn>
          </div>
        </v-layout>
      </v-container>
      <v-container>
        <v-alert :value="dataLoaded==1" color="success" icon="check_circle">
          Data Loaded Successfully
        </v-alert>
        <v-alert :value="dataLoaded==2" color="error" icon="warning">
          Data Load Error
        </v-alert>
      </v-container>
    <pre>
      {{ $data }}  
    </pre> 
    </v-app>
    
  </div>
</template>


<script>
  export default {
    data () {
      return {
        dataLoaded: 0,
        apiData: 'undifined'
      }
    },
    methods: {
      loadApi: function() {
          this.dataLoaded = 0;
          this.$http.get('http://127.0.0.1:8000/bestdeal/deals/?format=json')
          .then(this.successCallBack, this.errorCallBack);
        },
        successCallBack: function(response){
          this.dataLoaded = 1;
          console.log('successCallback response:', response);
          this.apiData = response.data;
        },
        errorCallBack: function(response){
          this.dataLoaded = 2;
          console.log('errorCallback response:', response);
        }
    }
  }
</script>