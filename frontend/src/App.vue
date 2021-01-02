<template>
    <v-app>
        <Header>
            <base href="/">
            <router-view/>
        </Header>
    </v-app>
</template>

<script>
import Header from '@/components/Header'
import {mapGetters, mapActions, mapState} from 'vuex'

export default {
    name: 'App',
    components: {
        Header
    },
    computed: {
        ...mapGetters(['auth_token_in_cookies']),
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['set_authorization_header', 'set_user']),
    },
    created() {
        if (this.auth_token_in_cookies) {
            this.set_authorization_header();
        }
        this.set_user()
    }
};
</script>
<style>
.clickable {
    cursor: pointer;
}
</style>