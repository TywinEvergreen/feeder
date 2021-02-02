<template>
    <v-row justify="center">
        <v-col cols="4">
            <v-col cols="12">
                <h1>Feeder</h1>
            </v-col>
            <v-col cols="12">
                <v-text-field
                        v-model="form.email"
                        @keydown.enter="login"
                        label="Почта"
                        outlined
                ></v-text-field>
                <v-text-field
                        v-model="form.password"
                        @keydown.enter="login"
                        label="Пароль"
                        type="password"
                        outlined
                ></v-text-field>
            </v-col>

            <ul>
                <li
                        v-for="error in errors"
                        :key="error"
                        style="color: red"
                >
                    {{ error }}
                </li>
            </ul>

            <v-btn
                    @click="login"
                    color="black white--text"
            >
                вход
            </v-btn>
            <a @click="go('user-register')">
                регистрация ->
            </a>
        </v-col>
    </v-row>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        data() {
            return {
                form: {
                    email: '',
                    password: ''
                },
                errors: []
            }
        },
        methods: {
            ...mapActions({
                'go': 'utils/go'
            }),
            async login() {
                try {
                    await this.$auth.loginWith('local', {data: this.form})
                    this.$store.dispatch('user/set_user');
                } catch (error) {
                    let login_errors = []
                    Object.entries(error.response.data).forEach(err => {
                        login_errors.push(`${err[0]}: ${err[1][0]}`)
                    });
                    this.errors = login_errors
                }
            },

            // login() {
            //     this.$axios('auth/token/login/', {
            //         method: 'POST',
            //         data: qs.stringify({
            //             email: this.form.email,
            //             password: this.form.password,
            //         })
            //     })
            //         .then(response => {
            //             Cookies.set('auth_token', response.data.auth_token);
            //             console.log(Cookies.get('auth_token'));
            //             this.$store.dispatch('user/set_authorization_header');
            //             this.$store.dispatch('utils/go', 'feed')
            //         })
            //         .catch(error => {
            //             let login_errors = []
            //             Object.entries(error.response.data).forEach(err => {
            //                 login_errors.push(`${err[0]}: ${err[1][0]}`)
            //             });
            //             this.errors = login_errors
            //         });
            // }
        }
    }
</script>

<style scoped>

</style>