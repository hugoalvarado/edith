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
    createHelpRequest(context, params) {
      let url = 'http://0.0.0.0:8000/api/help-requests/'
      axios.post(url, {
        'description': params.description,
        'complete_by': params.completeByDate
      }).then(response => {
        console.log(response)
        context.commit('SET_HELP_REQUESTS', response.data)
      })
    }
  },
  modules: {},
});
