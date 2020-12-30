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
                <span
                    v-for="artist in user.user.followed_artists"
                    :key="artist.id"
                >
                    <h5>
                        {{artist.name}}
                        <a @click="removeArtist(artist)">x</a>
                    </h5>
                </span>
            </v-col>
            <v-col cols="6">
                <h2>
                    Youtube каналы
                    <a @click="go('AddChannel')">+</a>
                </h2>
                <span
                    v-for="channel in user.user.followed_channels"
                    :key="channel.id"
                >
                    {{channel}}
                </span>
            </v-col>
        </v-col>
    </v-row>
</template>

<script>
import {mapState, mapActions} from 'vuex'
import axios from 'axios'
import qs from 'qs'

export default {
    name: "Profile",
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        removeArtist(artist) {
            axios('user/', {
                method: 'PATCH',
                data: qs.stringify({
                    'artist': artist.spotify_id
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