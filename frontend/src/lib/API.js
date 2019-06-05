import axios from 'axios'
const API_URL = 'http://localhost:8000/bestdeal/';

export default {
  brands(intId = "") {
    if (intId) {
      return axios.get(API_URL + 'brands/' + intId,
        {
          //headers:
          //{
          //  "Authorization": "JWT " + localStorage.getItem('token')
          //}
        });
    }
    else {
      return axios.get(API_URL + 'brands/');
    }
  },
  tags() {
    return axios.get(API_URL + 'tags');
  },
  deals(intId = "") {
    if (intId) {
      return axios.get(API_URL + 'deals/' + intId);
    }
    else {
      return axios.get(API_URL + 'deals');
    }

  },

};