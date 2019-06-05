<template lang="html">
  <div class="deals">
  <h1>Deals</h1>
      <v-card flat class="pa-7">
          <v-layout row wrap>
            <v-flex>
              <v-img
                height="100px"
                width="100px"
                src="results.photo"
                contain
               ></v-img>     
            </v-flex>

            <v-flex xs7>
              <v-card-title>
                <div>
                  <span class="headline">{{results.title}}</span><br>
                  <span class="red--text">{{results.price_after}} </span>
                  <span class="grey--text" v-if="results.price_before > 0">{{results.price_before}} </span>
                  <span v-if="results.price_percent > 0 ">-{{results.price_percent}}% </span><br>
                  <span>Bons plans <router-link to="/Brands">{{results.brands.name}}</router-link></span><br>
                  <span>{{results.content| truncate(175)}}</span><br>
                </div>
              </v-card-title>
            </v-flex>

            <div>
              
              <v-btn icon><v-icon color="blue">thumb_down_alt</v-icon></v-btn>
              <span class="red--text" v-if="results.moyenne_vote > 0">{{results.moyenne_vote}}°</span>
              <span class="orange--text" v-if="results.moyenne_vote == null">0°</span>
              <span class="blue--text" v-if="results.moyenne_vote < 0">{{results.moyenne_vote}}°</span>
              <v-btn icon><v-icon color="red">thumb_up_alt</v-icon></v-btn>
            </div>  
            <v-btn small><v-icon>notifications_none</v-icon></v-btn>
            <v-btn small><v-icon left>chat_bubble</v-icon>{{results.nb_comment}}</v-btn>
            <v-btn small v-bind:href=results.link><v-icon>open_in_new</v-icon></v-btn>
          </v-layout>
        </v-card>
  </div>
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
      API.deals(this.$route.params.id).then(response => {
          this.results = response.data;
        }).catch(error => {
          console.log(error.response)
        })
    },
  },
  filters: { 
    truncate: function(string, value) {
        return string.substring(0, value) + '...';
    }
  },
};
</script>