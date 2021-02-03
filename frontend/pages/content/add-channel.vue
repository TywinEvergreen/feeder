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
            <ul>
                <li
                    v-for="channel in channels"
                    :key="channel.id"
                >
                    <h5>
                        {{ channel.title }}
                        <a @click="addChannel(channel)">+</a><br>
                    </h5>
                    <span>{{ channel.description }}</span>
                </li>
            </ul>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import {mapActions} from 'vuex'
import {YTSearcher} from 'ytsearcher'

export default {
    data() {
        return {
            YOUTUBE_CLIENT: new YTSearcher(process.env.VUE_APP_YOUTUBE_CLIENT_SECRET),

            search_query: '',
            channels: []
        }
    },
    methods: {
        ...mapActions(['go', 'set_user']),
        searchChannels() {
            if (this.search_query) {
                this.YOUTUBE_CLIENT.search(this.search_query, {type: 'channel', maxResults: 30})
                    .then(response => {
                        this.channels = response.currentPage
                    })
            }
        },
        addChannel(channel) {
            this.$axios('youtube/channel', {
                method: 'POST',
                data: qs.stringify({
                    'youtube_id': channel.id,
                    'name': channel.title
                })
            })
                .then(response => {
                    this.$axios('subscriptions/channel', {
                        method: 'POST',
                        data: qs.stringify({
                            'channel': response.data.id
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