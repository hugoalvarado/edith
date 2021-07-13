<template>

  <div class="hero-body">
    <div class="container has-text-centered">

      <div class="columns is-8 is-variable ">
        <div class="column is-full has-text-left">
          <h1 class="title is-1">Your open help requests</h1>
          <p class="is-size-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla eligendi soluta
            voluptate facere molestiae consequatur.</p>
        </div>
      </div>

      <div class="columns is-8 is-variable ">
        <div class="column is-full has-text-left">
          <b-table :data="data" :columns="columns"></b-table>
        </div>
      </div>

    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "ListHelpRequests",
  data() {
    return {
      data: [],
      columns: [
        {
          field: 'description',
          label: 'Description',
        },
        {
          field: 'created_at',
          label: 'Created At',
        },
        {
          field: 'completed',
          label: 'Completed',
        }
      ]
    }
  },
  mounted() {
    let url = 'http://0.0.0.0:8000/api/help-requests/'
    axios
      .get(url)
      .then(response => {this.data = response.data})
  }
}
</script>

<style scoped>

</style>
