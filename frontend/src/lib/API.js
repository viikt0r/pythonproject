//import ezFetch from 'ez-fetch';
import axios from 'axios'
const API_URL = 'http://192.168.99.100:8000/bestdeal/';

export default {
    marques() {
        //return ezFetch.get(API_URL);
        return  axios.get(API_URL+'marques', 
        { 
          headers: 
          {
           "Authorization": "JWT "+localStorage.getItem('token') 
          }
        });
    },
};