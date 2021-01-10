<template>
    <v-container>
        {{notifications}}
<!--        <span-->
<!--            v-for="notif in notifications"-->
<!--            :key="notif.id"-->
<!--        >-->
<!--                {{ notif }}-->
<!--                <v-card v-if="notif.content_type === 'album'">-->
<!--                    <h5>{{ notif.content_object.artist.name }}</h5>-->
<!--                    <h4>{{ notif.content_object.name }}</h4>-->
<!--                    {{notif.content_object.cover}}-->
<!--                    <img :src="notif.content_object.cover">-->
<!--                </v-card>-->
<!--                <v-card v-else-if="notif.content_type === 'video'">-->
<!--                    pizda-->
<!--                </v-card>-->
<!--        </span>-->
    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: "Feed",
    data() {
        return {
            notifications: []
        }
    },
    created() {
        this.getNotifications()
    },
    methods: {
        getNotifications() {
            axios.get('notifications/')
                .then(response => {
                    this.notifications = response.data.results
                })
        }
    }
}
</script>

<style scoped>

</style>