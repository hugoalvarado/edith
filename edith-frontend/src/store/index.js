import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    helpRequests: [],
  },
  mutations: {
    SET_HELP_REQUESTS(state, requests) {
        state.helpRequests = requests
    }
  },
  actions: {
    createHelpRequest(context) {
      let url = 'http://0.0.0.0:8000/api/help-requests/'
      axios.post(url, {
        'description': 'test',
        'requestDate': '1/1/2020'
      }).then(response => {
        context.commit('SET_HELP_REQUESTS', response.data)
      })
    }
  },
  modules: {},
});
