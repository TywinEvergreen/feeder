<template>
    <v-row>
        <v-col cols="12">
            <v-text-field
                v-model="search_query"
                @keydown.enter="searchArtist"
            ></v-text-field>
            <v-btn @click="searchArtist">Поиск</v-btn>
        </v-col>
        <v-col cols="12">
            <ul>
                <li
                    v-for="artist in artists"
                    :key="artist.id"
                >
                    {{artist}}
                </li>
            </ul>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import SpotifyWebApi from 'spotify-web-api-js'

export default {
    name: "AddArtist",
    data() {
        return {
            SPOTIFY_CLIENT: new SpotifyWebApi(),

            search_query: '',
            artists: []
        }
    },
    beforeCreate() {
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
            .catch(() => {
                alert('Не удалось аутентифицировать клиент Spotify')
            })
    },
    methods: {
        searchArtist() {
            if (this.search_query) {
                this.SPOTIFY_CLIENT.searchArtists(this.search_query)
                    .then(response => {
                        this.artists = response.artists.items
                    })
            }
        }
    }
}
</script>

<style scoped>

</style>