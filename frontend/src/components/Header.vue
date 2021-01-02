<template>
    <v-container>
        <v-row
            v-if="user.authenticated"
            justify="center"
        >
            <v-col cols="3">
                <v-row>
                    <v-col cols="3">
                        <a @click="go('Feed')">Новинки</a>
                    </v-col>
                    <v-col cols="3">
                        <a @click="go('Profile')">Профиль</a>
                    </v-col>
                    <v-col cols="3">
                        <a @click="signOut">Выйти</a>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
        <slot></slot>
    </v-container>
</template>

<script>
import Cookies from "js-cookie"
import {mapActions, mapState} from "vuex"

export default {
    name: "Header",
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go', 'set_authorization_header', 'set_user']),
        signOut() {
            Cookies.remove('auth_token');
            this.set_authorization_header();
            this.set_user();
            this.go('Login')
        }
    }
}
</script>

<style scoped>

</style>