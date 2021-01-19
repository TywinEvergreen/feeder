<template>
    <v-row>
        <v-col cols="12">
            <h2>{{ user.user.email }}</h2>
            {{user.user}}
        </v-col>
        <v-col cols="12">
            <v-col cols="6">
                <h2>
                    Исполнители
                    <a @click="go('AddArtist')">+</a>
                </h2>
                <h5
                    v-for="subscription in user.user.artist_subscriptions"
                    :key="subscription.id"
                >
                    {{ subscription.artist.name }}
                    <a @click="deleteSubscription('artist', subscription.id)">x</a>
                </h5>
            </v-col>
            <v-col cols="6">
                <h2>
                    Youtube каналы
                    <a @click="go('AddChannel')">+</a>
                </h2>
                <h5
                    v-for="subscription in user.user.channel_subscriptions"
                    :key="subscription.id"
                >
                    {{ subscription.channel.name }}
                    <a @click="deleteSubscription('channel', subscription.id)">x</a>
                </h5>
            </v-col>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import {mapState, mapActions} from 'vuex'

export default {
    name: "Profile",
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        deleteSubscription(type, id) {
            axios.delete(`subscriptions/${type}/${id}`)
                .then(() => {
                    this.set_user()
                })
        }
    }
}
</script>

<style scoped>

</style>