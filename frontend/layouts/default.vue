<template>
    <v-container>
        <v-row
                v-if="isAuthenticated"
                justify="center"
        >
            <v-col cols="3">
                <v-row>
                    <v-col cols="3">
                        <a @click="go('feed')">Новинки</a>
                    </v-col>
                    <v-col cols="3">
                        <a @click="go('user-profile')">Профиль</a>
                    </v-col>
                    <v-col cols="3">
                        <a @click="signOut">Выйти</a>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
        <Nuxt/>
    </v-container>
</template>

<script>
    import Cookies from "js-cookie"
    import {mapActions, mapState} from "vuex"

    export default {
        // created() {
        //     this.$store.dispatch('user/set_authorization_header');
        //     this.$store.dispatch('user/set_user');
        // },
        computed: {
            ...mapState({
                isAuthenticated: state => state.user.isAuthenticated
            })
        },
        methods: {
            ...mapActions({
                'go': 'utils/go',
            }),
            signOut() {
                Cookies.remove('auth_token');
                this.$store.dispatch('user/set_authorization_header');
                this.$store.dispatch('user/set_user');
                this.go('user-login')
            }
        }
    }
</script>
