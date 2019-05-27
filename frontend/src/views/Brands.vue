<template lang="html">
  <v-layout row wrap>
    <v-flex xs12 md4 v-for="brand in results" :key="brand.id">
      <v-card>
        <v-card-media :src="brand.photo" height="50px">
        </v-card-media>
        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">{{brand.name}}</h3>
            <div>{{brand.link}}</div>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-btn
            :to="{
              name: 'Brand',
              params: {
                id: brand.id
              }
            }"
            flat
            color="orange">View</v-btn>
        </v-card-actions>
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
  mounted() {
    this.load();
  },
  methods: {
    load() {
      API.marques()
        .then((results) => {
          this.results = results;
        });
    },
  },
};
</script>

<style lang="css">
</style>