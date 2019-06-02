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
                  <span class="headline">{{res.title}}</span><br>
                  <span class="red--text">{{res.price_after}} </span>
                  <span class="grey--text">{{res.price_before}}</span>
                  <span>-50% </span>
                  <span>Bons plans {{res.brands.name}}</span><br>
                  <span>{{res.content}}</span><br>
                </div>
              </v-card-title>
            </v-flex>

            <div>
              <v-btn icon><v-icon color="blue">thumb_down_alt</v-icon></v-btn>
              <span class="red--text" v-if="res.moyenne_vote !== null">{{res.moyenne_vote}}°</span>
              <span class="red--text" v-if="res.moyenne_vote == null">0°</span>
              <v-btn icon><v-icon color="red">thumb_up_alt</v-icon></v-btn>
            </div>  
            <v-btn small><v-icon>notifications_none</v-icon></v-btn>
            <v-btn small><v-icon left>chat_bubble</v-icon>{{res.nb_comment}}</v-btn>
            <v-btn small><v-icon>open_in_new</v-icon></v-btn>
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
};
</script>
