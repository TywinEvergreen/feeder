<template>
    <v-row>
        <v-col cols="12">
            <h2>{{ user.user.email }}</h2>
        </v-col>
        <v-col cols="12">
            <v-col cols="6">
                <h2>
                    Исполнители
                    <a @click="go('AddArtist')">+</a>
                </h2>
<!--                <h5-->
<!--                    v-for="artist in user.user.followed_artists"-->
<!--                    :key="artist.id"-->
<!--                >-->
<!--                    {{ artist.name }}-->
<!--                    <a @click="updateUser('artist', artist.spotify_id)">x</a>-->
<!--                </h5>-->
            </v-col>
            <v-col cols="6">
                <h2>
                    Youtube каналы
                    <a @click="go('AddChannel')">+</a>
                </h2>
<!--                <h5-->
<!--                    v-for="channel in user.user.followed_channels"-->
<!--                    :key="channel.id"-->
<!--                >-->
<!--                    {{ channel.name }}-->
<!--                    <a @click="updateUser('channel', channel.youtube_id)">x</a>-->
<!--                </h5>-->
            </v-col>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import {mapState, mapActions} from 'vuex'

export default {
    name: "Profile",
    data() {
        return {
            subscriptions_to_artists: [],
            subscriptions_to_channels: []
        }
    },
    created() {
        this.getSubscriptions()
    },
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        getSubscriptions() {
            axios.get('subscriptions/')
                .then(response => {
                    console.log(response.data)
                })
        },
        updateUser(key, value) {
            axios('user/', {
                method: 'PATCH',
                data: qs.stringify({
                    [key]: value,
                })
            })
                .then(() => {
                    this.set_user()
                })
        }
    }
}
</script>

<style scoped>

</style>