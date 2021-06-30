<template>
    <section id="footer" class="section has-green-bg">
        <div class="container has-text-centered">
            <a href="https://twitter.com" class="is-size-4 social-link">
                <i class="fab fa-twitter"></i>
            </a>
            <a href="https://github.com/" class="is-size-4 social-link">
                <i class="fab fa-github"></i>
            </a>
            <p class="has-text-white is-size-7">
                <i class="fas fa-copyright"></i> <b>{{msg}}, Gym Service</b>
            </p>
        </div>
    </section>
</template>
<script>
export default {
    name: 'Footer',
    props: {
        year: String
    }
}
</script>
