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

    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="columns is-8 is-variable ">
          <div class="column is-two-thirds has-text-left">
            <h1 class="title is-1">Edith can find the help you need</h1>
            <p class="is-size-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla eligendi soluta
              voluptate facere molestiae consequatur.</p>
            <!--            <div class="social-media">-->
            <!--              <a href="https://facebook.com" target="_blank" class="button is-light is-large"><i-->
            <!--                class="fa fa-facebook-square" aria-hidden="true"></i></a>-->
            <!--              <a href="https://instagram.com" target="_blank" class="button is-light is-large"><i-->
            <!--                class="fa fa-instagram" aria-hidden="true"></i></a>-->
            <!--              <a href="https://twitter.com" target="_blank" class="button is-light is-large"><i class="fa fa-twitter"-->
            <!--                                                                                                aria-hidden="true"></i></a>-->
            <!--            </div>-->
          </div>
          <div class="column is-one-third has-text-left">
            <b-field label="Help me with">
              <b-input
                v-model="description"
                maxlength="180"
                placeholder="Moving my couch..."
                type="textarea">
              </b-input>
            </b-field>
            <b-field label="When?">
              <b-datetimepicker
                v-model="completeByDate"
                placeholder="Tomorrow..."
                icon="calendar-today"
                horizontal-time-picker>
              </b-datetimepicker>
            </b-field>
            <div class="control">
              <button type="submit" @click="handleClick"
                      class="button is-link is-fullwidth has-text-weight-medium is-medium">Submit
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

  </section>


</template>

<script>

export default {
  name: "NewHelpRequest",
  data() {
    return {
      description: "",
      completeByDate: new Date()
    };
  },
  methods: {
    handleClick() {
      this.$store.dispatch('createHelpRequest',
        {
          'description': this.description,
          'completeByDate': this.completeByDate
        })
      // this.$router.push({ name: 'home' })
    }
  }
};
</script>

<style scoped>

</style>
