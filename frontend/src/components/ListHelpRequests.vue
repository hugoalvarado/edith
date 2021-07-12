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
export default {
  name: "ListHelpRequests",
  data() {
    return {
      data: [
        {'id': 1, 'first_name': 'Jesse', 'last_name': 'Simmons', 'date': '2016-10-15 13:43:27', 'gender': 'Male'},
        {'id': 2, 'first_name': 'John', 'last_name': 'Jacobs', 'date': '2016-12-15 06:00:53', 'gender': 'Male'},
        {'id': 3, 'first_name': 'Tina', 'last_name': 'Gilbert', 'date': '2016-04-26 06:26:28', 'gender': 'Female'},
        {'id': 4, 'first_name': 'Clarence', 'last_name': 'Flores', 'date': '2016-04-10 10:28:46', 'gender': 'Male'},
        {'id': 5, 'first_name': 'Anne', 'last_name': 'Lee', 'date': '2016-12-06 14:38:38', 'gender': 'Female'}
      ],
      columns: [
        {
          field: 'id',
          label: 'ID',
          width: '40',
          numeric: true
        },
        {
          field: 'first_name',
          label: 'First Name',
        },
        {
          field: 'last_name',
          label: 'Last Name',
        },
        {
          field: 'date',
          label: 'Date',
          centered: true
        },
        {
          field: 'gender',
          label: 'Gender',
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
