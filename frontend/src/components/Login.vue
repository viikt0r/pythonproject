<template>
  <v-flex xs4 class="grey lighten-4">
    <v-container style="position: relative;top: 13%;" class="text-xs-center">
      <v-card flat>
        <v-card-title primary-title>
          <h4>Login</h4>
        </v-card-title>
        <v-form @submit.prevent="login">
          <v-text-field
            prepend-icon="person"
            v-model="username"
            label="Username"
          ></v-text-field>
          <v-text-field
            prepend-icon="lock"
            v-model="password"
            label="Password"
            type="password"
          ></v-text-field>
          <v-card-actions>
            <v-btn type="submit" primary large block>Login</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-container>
  </v-flex>
</template>


<script>
	export default {
		data(){
			return {
				username : "",
        password : ""
      }
		},
		methods: {
			login: function () {
					let username = this.username 
					let password = this.password
					this.$store.dispatch('login', { username, password })
					.then(() => this.$router.push('/'))
					.catch(err => console.log(err))
			}
		}
	}
</script>