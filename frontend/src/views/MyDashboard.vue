<template>


  <!--  <!DOCTYPE html>-->
  <!--<html lang="en">-->

  <!--<head>-->
  <!--	<meta charset="UTF-8">-->
  <!--	<meta http-equiv="X-UA-Compatible" content="IE=edge">-->
  <!--	<meta name="viewport" content="width=device-width, initial-scale=1">-->
  <!--	<title>Contact Form - Free Bulma template</title>-->
  <!--	<link rel="shortcut icon" href="../images/fav_icon.png" type="image/x-icon">-->
  <!--	&lt;!&ndash; Bulma Version 0.9.0&ndash;&gt;-->
  <!--	<link rel="stylesheet" href="https://unpkg.com/bulma@0.9.0/css/bulma.min.css" />-->
  <!--	<link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"-->
  <!--		integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">-->
  <!--	<link rel="stylesheet" href="../css/contact.css">-->
  <!--</head>-->

  <section class="hero is-fullheight">
    <NewHelpRequests></NewHelpRequests>
    <ListHelpRequests></ListHelpRequests>
  </section>


</template>

<script>
import NewHelpRequests from "@/components/NewHelpRequest.vue";
import ListHelpRequests from "@/components/ListHelpRequests.vue";

export default {
  name: "MyDashboard",
  components: {
    NewHelpRequests,
    ListHelpRequests
  },
  data() {
    return {
    };
  },
  methods: {
  }
};
</script>

<style scoped>

</style>
