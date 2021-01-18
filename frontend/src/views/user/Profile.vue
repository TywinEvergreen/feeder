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
                    <a @click="deleteSubscription(subscription.id)">x</a>
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
                    <a @click="deleteSubscription(subscription.id)">x</a>
                </h5>
            </v-col>
        </v-col>
    </v-row>
</template>

<script>
// import axios from 'axios'
import {mapState, mapActions} from 'vuex'

export default {
    name: "Profile",
    // data() {
    //     return {
    //         artist_subscriptions: [],
    //         channel_subscriptions: []
    //     }
    // },
    // created() {
    //     this.getSubscriptions()
    // },
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go']),
        // getArtistSubscriptions() {
        //     axios.get('subscriptions/artist')
        //         .then(response => {
        //             let subscriptions_to_artists = [];
        //             let subscriptions_to_channels = [];
        //
        //             response.data.results.forEach(subscription => {
        //                 if (subscription.content_type == 'artist') {
        //                     subscriptions_to_artists.push(subscription)
        //                 }
        //                 else if (subscription.content_type == 'channel') {
        //                     subscriptions_to_channels.push(subscription)
        //                 }
        //             })
        //
        //             this.subscriptions_to_artists = subscriptions_to_artists;
        //             this.subscriptions_to_channels = subscriptions_to_channels
        //         })
        // },
        // deleteSubscription(subscription_id) {
        //     axios.delete(`subscriptions/${subscription_id}`)
        //         .then(() => {
        //             this.getSubscriptions()
        //         })
        // },
    }
}
</script>

<style scoped>

</style>