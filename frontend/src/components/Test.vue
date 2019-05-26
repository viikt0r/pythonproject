<template>
  <v-app>
    <v-content>
      <div>
        <div class="text-xs-center">
        <v-btn color="primary" v-on:click="loadApi" @click="alert = !alert">Toggle</v-btn>
        </div>
        <v-alert :value="alert" type="success" transition="scale-transition">
          This is a success alert.
        </v-alert>
      </div>
    </v-content>  
  </v-app>
</template>

<script>
import Test from './components/Test'
import Index from './components/Index'

export default {
  name: 'App',
  components: {
    Home,Index
  },
  methods: {
		loadApi: function () {
			this.dataLoaded = 0;
			this.$http.get('http://127.0.0.1:8000/bestdeal/deals/?format=json').
			then(this.successCallback, this.errorCallback);
		},
		successCallback: function(response) {
			this.dataLoaded = 1;
			console.log('successCallback response:' , response);
			this.apiData = response.data;
		},
		errorCallback: function(response) {
			this.dataLoaded = 2;
			console.log('errorCallback response:' , response);
		}
	},
  data () {
    return {
        alert: true,
		    dataLoaded: 0,
        apiData: undefined
    }
  }
}
</script>
