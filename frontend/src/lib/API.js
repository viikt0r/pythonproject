import axios from 'axios'
const API_URL = 'http://localhost:8000/bestdeal/';

export default {
  marques(intId = "") {
    if (intId) {
      return axios.get(API_URL + 'marques/' + intId,
        {
          //headers:
          //{
          //  "Authorization": "JWT " + localStorage.getItem('token')
          //}
        });
    }
    else {
      return axios.get(API_URL + 'marques/');
    }
  },
  tags() {
    return axios.get(API_URL + 'tags');
  },

};