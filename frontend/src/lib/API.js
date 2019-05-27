import ezFetch from 'ez-fetch';

const API_URL = 'http://192.168.99.100:8000/bestdeal/';

export default {
    marques() {
        return ezFetch.get(API_URL);
    },
};