<template>
    <v-row justify="center">
        <v-col cols="12">
            <v-col cols="12">
                <h1>Feeder</h1>
                <h5>пройдите регистрацию</h5>
            </v-col>
            <v-col cols="12">
                <v-text-field
                    v-model="form.email"
                    label="Почта"
                    outlined
                ></v-text-field>
                <v-text-field
                    v-model="form.password"
                    label="Пароль"
                    type="password"
                    outlined
                ></v-text-field>

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
                    @click="register"
                    color="black white--text"
                >
                    регистрация
                </v-btn>
            </v-col>
        </v-col>
    </v-row>
</template>

<script>
import qs from 'qs'

export default {
    auth: false,
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
        register() {
            this.$axios('auth/users/', {
                method: 'POST',
                data: qs.stringify({
                    email: this.form.email,
                    password: this.form.password,
                })
            })
                .then(() => {
                    this.$store.dispatch('utils/go', 'user-login')
                })
                .catch(error => {
                    let register_errors = []
                    Object.entries(error.response.data).forEach(error => {
                        register_errors.push(`${error[0]}: ${error[1][0]}`)
                    });
                    this.errors = register_errors
                });
        }
    }
}
</script>

<style scoped>

</style>