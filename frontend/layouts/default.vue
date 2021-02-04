<template>
    <v-app>
        <v-row>
            <v-col cols="2">
                <v-card
                        class="mx-auto rounded-0" fill-height height="100vh"
                >
                    <v-navigation-drawer
                            class="accent-4 rounded-0"
                            dark
                            permanent
                            width="100%"
                    >
                        <v-list>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title class="title">
                                        Feeder
                                    </v-list-item-title>
                                    <v-list-item-subtitle>
                                        {{page_names[$route.name]}}
                                    </v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item
                                    v-for="item in items"
                                    :key="item.name"
                                    link
                                    @click="go(item.route_name)"
                            >
                                <v-list-item-icon>
                                    <v-icon>{{ item.icon }}</v-icon>
                                </v-list-item-icon>

                                <v-list-item-content>
                                    <v-list-item-title>{{ item.name }}</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>

                        <template v-slot:append>
                            <div class="pa-2">
                                <v-btn block @click="signOut">
                                    Logout
                                </v-btn>
                            </div>
                        </template>
                    </v-navigation-drawer>
                </v-card>
            </v-col>
            <v-col cols="10">
                <Nuxt/>
            </v-col>
        </v-row>

    </v-app>


    <!--    <v-container id="dolboeb">-->
    <!--        <v-row-->
    <!--                v-if="isAuthenticated"-->
    <!--                justify="center"-->
    <!--                align="center"-->
    <!--        >-->
    <!--            <v-col cols="3">-->
    <!--                <v-row>-->
    <!--                    <v-col cols="3">-->
    <!--                        <a @click="go('index')">Новинки</a>-->
    <!--                    </v-col>-->
    <!--                    <v-col cols="3">-->
    <!--                        <a @click="go('user-profile')">Профиль</a>-->
    <!--                    </v-col>-->
    <!--                    <v-col cols="3">-->
    <!--                        <a @click="signOut">Выйти</a>-->
    <!--                    </v-col>-->
    <!--                </v-row>-->
    <!--            </v-col>-->
    <!--        </v-row>-->
    <!--        <Nuxt/>-->
    <!--    </v-container>-->
</template>

<script>
    import {mapActions, mapState} from "vuex"

    export default {
        middleware: ['setUser'],
        data() {
            return {
                page_names: {
                    'index': 'Главная',
                    'user-profile': 'Профиль',
                    'content-add-artist': 'Добавить исполнителя',
                    'content-add-channel': 'Добавить youtube канал'
                },
                items: [
                    {
                        name: 'На главную',
                        icon: 'fa-home',
                        route_name: 'index'
                    },
                    {
                        name: 'Профиль',
                        icon: 'fa-profile',
                        route_name: 'user-profile'
                    }
                ]
            }
        },
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
                this.$auth.logout()
                this.$store.dispatch('user/set_authorization_header');
                this.$store.dispatch('user/set_user');
                this.go('user-login')
            }
        }
    }
</script>
<style>
    #navigation {
        height: 100vh;
        width: 40vh;
    }
</style>
