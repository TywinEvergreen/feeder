<template>
    <v-row>
        <v-col cols="12">
            <v-text-field
                v-model="search_query"
                label="Поиск исполнителей"
                @keydown.enter="searchArtists"
            ></v-text-field>
            <v-btn @click="searchArtists">Поиск</v-btn>
        </v-col>
        <v-col cols="12">
            <ul>
                <li
                    v-for="artist in artists"
                    :key="artist.id"
                >
                    <h5>
                        {{ artist.name }}
                        <a @click="addArtist(artist)">+</a>
                    </h5>
                    <span
                        v-for="genre in artist.genres"
                        :key="genre.id"
                    >
                        {{ genre }}
                    </span>
                </li>
            </ul>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import SpotifyWebApi from 'spotify-web-api-js'
import {mapActions} from 'vuex'

export default {
    data() {
        return {
            SPOTIFY_CLIENT: new SpotifyWebApi(),

            search_query: '',
            artists: []
        }
    },
    created() {
        this.authorizeSpotify()
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        authorizeSpotify() {
            let base64_token = btoa(
                `${process.env.VUE_APP_SPOTIFY_CLIENT_ID}:${process.env.VUE_APP_SPOTIFY_CLIENT_SECRET}`
            );

            axios('https://accounts.spotify.com/api/token', {
                method: 'POST',
                headers: {
                    'Authorization': `Basic ${base64_token}`
                },
                data: qs.stringify({
                    'grant_type': 'client_credentials'
                })
            })
                .then(response => {
                    this.SPOTIFY_CLIENT.setAccessToken(response.data.access_token);
                })
        },
        searchArtists() {
            if (this.search_query) {
                this.SPOTIFY_CLIENT.searchArtists(this.search_query)
                    .then(response => {
                        this.artists = response.artists.items
                    })
            }
        },
        addArtist(artist) {
            axios('spotify/artist', {
                method: 'POST',
                data: qs.stringify({
                    'spotify_id': artist.id,
                    'name': artist.name
                })
            })
                .then(response => {
                    axios('subscriptions/artist', {
                        method: 'POST',
                        data: qs.stringify({
                            'artist': response.data.id
                        })
                    })
                        .then(() => {
                            this.set_user();
                        })
                })
        }
    }
}
</script>

<style scoped>

</style>