<template>
    <section id="newsletter" class="section">
            <div class="container">
                <h3 class="has-text-green is-size-3">
                    Newsletter</h3>
                <p class="has-text-green">
                    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
                </p>
                <div class="field newsletter-field">
                    <div class="control">
                        <b-input v-model="email" placeholder='john@doe.com'></b-input>
                    </div>
                </div>
                <button rounded class="button is-medium" @click="success">
                    Subscribe
                </button>
            </div>
        </section>
</template>
<script>
export default {
    name: 'Newsletter',
    methods: {
        success() {
            this.$buefy.toast.open({
                message: 'We have sent you a confirmation email!',
                type: 'is-success'
            })
        },
        fail() {
            this.$buefy.toast.open({
                duration: 5000,
                message: `Something went wrong`,
                position: 'is-bottom',
                type: 'is-danger'
            })
        }
    }
}
</script>
