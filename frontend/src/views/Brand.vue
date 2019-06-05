<template lang="html">
  <v-layout row wrap>
    <v-flex xs12 md4 v-for="res in results" :key="res.id">
      <v-card>
        <v-card-media :src="res.photo" height="50px" width="50px">
        </v-card-media>
        <h3 class="headline mb-0">{{res.name}}</h3>
        </v-card-title>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import API from '@/lib/API';
export default {
  data() {
    return {
      results: [],
    };
  },
  created() {
    this.load();
  },
  methods: {
    load() {
      API.brands().then(response => {
          this.results = response.data.results;
        }).catch(error => {
          console.log(error.response)
        })
    },
  },
};
</script>

<style lang="css">
</style>