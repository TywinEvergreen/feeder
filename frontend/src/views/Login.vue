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
            <a @click="go('Register')">
                регистрация ->
            </a>
        </v-col>
    </v-row>
</template>

<script>
import {mapActions} from 'vuex'

import axios from 'axios'
import qs from 'qs'
import Cookies from 'js-cookie'

export default {
    name: "Login",
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
        ...mapActions(['go', 'set_authorization_header', 'set_user']),
        login() {
            console.log(this.form);
            axios('auth/token/login/', {
                method: 'POST',
                data: qs.stringify({
                    email: this.form.email,
                    password: this.form.password,
                })
            })
                .then(response => {
                    Cookies.set('auth_token', response.data.auth_token);
                    this.set_authorization_header();
                    this.set_user();
                    this.go('Feed');
                })
                .catch(error => {
                    let login_errors = []
                    Object.entries(error.response.data).forEach(error => {
                        login_errors.push(`${error[0]}: ${error[1][0]}`)
                    });
                    this.errors = login_errors
                });
        }
    }
}
</script>

<style scoped>

</style>