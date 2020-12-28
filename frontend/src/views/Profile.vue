<template>
    <v-row>
        <v-col cols="12">
            <h2>{{ user.user.email }}</h2>
        </v-col>
        <v-col cols="12">
            <v-col cols="6">
                <h3>
                    Исполнители
                    <a @click="go('AddArtist')">+</a>
                </h3>
                <span
                    v-for="artist in user.user.followed_artists"
                    :key="artist.id"
                >
                    {{artist}}
                </span>
            </v-col>
            <v-col cols="6">
                <h3>
                    Youtube каналы
                    <a @click="go('AddChannel')">+</a>
                </h3>
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

export default {
    name: "Profile",
    computed: {
        ...mapState(['user'])
    },
    methods: {
        ...mapActions(['go'])
    }
}
</script>

<style scoped>

</style>