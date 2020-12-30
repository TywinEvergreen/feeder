<template>
    <v-row>
        <v-col cols="12">
            <v-text-field
                v-model="search_query"
                label="Поиск youtube каналов"
                @keydown.enter="searchChannels"
            ></v-text-field>
            <v-btn @click="searchChannels">Поиск</v-btn>
        </v-col>
        <v-col cols="12">
<!--            <ul>-->
<!--                <li-->
<!--                    v-for="channel in channels"-->
<!--                    :key="channel.id"-->
<!--                >-->
<!--                    <h5>-->
<!--                        {{channel.name}}-->
<!--                        <a @click="addArtist(artist)">+</a>-->
<!--                    </h5>-->
<!--                </li>-->
<!--            </ul>-->
        </v-col>
    </v-row>
</template>

<script>
import {mapActions} from 'vuex'
import axios from 'axios'
import qs from 'qs'
import YouTube from 'youtube-sr'

export default {
    name: "AddChannel",
    data() {
        return {
            search_query: '',
            channels: []
        }
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        searchChannels() {
            // if (this.search_query) {
            //     this.SPOTIFY_CLIENT.searchArtists(this.search_query)
            //         .then(response => {
            //             this.artists = response.artists.items
            //         })
            // }
        },
        addChannel(channel) {
            // axios('spotify/artist/', {
            //     method: 'POST',
            //     data: qs.stringify({
            //         'spotify_id': spotify_artist.id,
            //         'name': spotify_artist.name
            //     })
            // })
            //     .then(response => {
            //         axios('user/', {
            //             method: 'PATCH',
            //             data: qs.stringify({
            //                 'artist': response.data.spotify_id
            //             })
            //         })
            //             .then(() => {
            //                 this.set_user();
            //             })
            //     })
        }
    }
}
</script>

<style scoped>

</style>