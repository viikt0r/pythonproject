<template>
  <v-toolbar dense>
    <v-toolbar-side-icon></v-toolbar-side-icon>
    <v-toolbar-title>Title</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-flex md10><v-text-field label="Search" placeholder="Search" solo></v-text-field></v-flex>

      <v-btn large :loading="loading" :disabled="loading" color="secondary" @click="loader = 'loading'"><v-icon>account_circle</v-icon>Login</v-btn>
      
      <v-btn large :loading="loading" :disabled="loading" color="red" @click="loader = 'loading'"><v-icon>add_circle</v-icon>Post</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<template>
  <v-layout>
    <v-flex xs10 sm4 offset-sm1>
      <v-card>
              <v-layout row>
                <v-flex xs3>
                  <v-img
                    height="100px"
                    width="100px"
                    src="https://www.media-rdc.com/medias/4fa8bd9787ce32b7a903b371d14626a9/p_580x580/3ff6287ff95f3c2496e44aee13a3ff9c.jpg"
                    contain
                  ></v-img>     
                </v-flex>

                <v-flex xs10>
                  <v-card-title>
                    <div>
                      <span class="headline">Nom article</span><br>
                      <span class="red--text">5,49€ </span>
                      <span class="grey--text">10,99€ </span>
                      <span>-50% </span>
                      <span>Bons plans Carrefour </span><br>
                      <span>Super prix pour la version à 8Go (party) Prix Fnac ici à 1092 euros en exemple Type de produit Ultra portable - Sub Notebook Taille de l'écran 13,5 " Taille d'écran</span><br>
                    </div>
                  </v-card-title>
                  
                </v-flex>
                
              </v-layout>
              <v-card-actions>
                <v-layout justify-space-around>
                  <div>
                    <v-btn icon><v-icon color="blue">thumb_down_alt</v-icon></v-btn>
                    <span class="red--text">330°</span>
                    <v-btn icon><v-icon color="red">thumb_up_alt</v-icon></v-btn>
                  </div>  
                    <v-btn small><v-icon>notifications_none</v-icon></v-btn>
                    <v-btn small><v-icon left>chat_bubble</v-icon>99</v-btn>
                    <v-btn small><v-icon>open_in_new</v-icon></v-btn>
                  
                </v-layout>
              </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>


<script>
export default {
  name: 'App',
  data() {
    return {
      //
    };
  },
};
</script>