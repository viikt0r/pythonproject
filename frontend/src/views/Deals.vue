<template lang="html">
  <div class="deals">
  <h1>Deals</h1>
  <v-layout row wrap>
    <v-flex xs12 md4 v-for="res in results" :key="res.id">
      <v-card flat class="pa-7">
          <v-layout row wrap>
            <v-flex>
              <v-img
                height="100px"
                width="100px"
                src="res.photo"
                contain
               ></v-img>     
            </v-flex>

            <v-flex xs7>
              <v-card-title>
                <div>
                  <span class="headline"><router-link :to="'/Deals/' + res.id">{{res.title}}</router-link></span><br>
                  <span class="red--text">{{res.price_after}} </span>
                  <span class="grey--text" v-if="res.price_before > 0">{{res.price_before}} </span>
                  <span v-if="res.price_percent > 0 ">-{{res.price_percent}}% </span><br>
                  <span>Bons plans <router-link to="/Brands">{{res.brands.name}}</router-link></span><br>
                  <span>{{res.content| truncate(175)}}</span><br>
                </div>
              </v-card-title>
            </v-flex>

            <div>
              
              <v-btn icon><v-icon color="blue">thumb_down_alt</v-icon></v-btn>
              <span class="red--text" v-if="res.moyenne_vote > 0">{{res.moyenne_vote}}°</span>
              <span class="orange--text" v-if="res.moyenne_vote == null">0°</span>
              <span class="blue--text" v-if="res.moyenne_vote < 0">{{res.moyenne_vote}}°</span>
              <v-btn icon><v-icon color="red">thumb_up_alt</v-icon></v-btn>
            </div>  
            <v-btn small><v-icon>notifications_none</v-icon></v-btn>
            <v-btn small><v-icon left>chat_bubble</v-icon>{{res.nb_comment}}</v-btn>
            <v-btn small v-bind:href=res.link><v-icon>open_in_new</v-icon></v-btn>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
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
      API.deals().then(response => {
          this.results = response.data.results;
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