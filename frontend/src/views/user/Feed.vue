<template>
    <v-container>
        {{notifications}}
<!--        <span-->
<!--            v-for="notif in notifications"-->
<!--            :key="notif.id"-->
<!--        >-->
<!--                <AlbumNotificationCard-->
<!--                    v-if="notif.content_type === 'album'"-->
<!--                    :notification="notif"-->
<!--                />-->
<!--                <VideoNotificationCard-->
<!--                    v-else-if="notif.content_type === 'video'"-->
<!--                    :notification="notif"-->
<!--                />-->

<!--&lt;!&ndash;                    <h5>{{ notif.content_object.artist.name }}</h5>&ndash;&gt;-->
<!--&lt;!&ndash;                    <h4>{{ notif.content_object.name }}</h4>&ndash;&gt;-->
<!--&lt;!&ndash;                    {{notif.content_object.cover}}&ndash;&gt;-->
<!--&lt;!&ndash;                    <img :src="notif.content_object.cover">&ndash;&gt;-->
<!--        </span>-->
    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: "Feed",
    components: {
    },
    data() {
        return {
            notifications: []
        }
    },
    created() {
        this.getNotifications('album');
        this.getNotifications('video');
    },
    methods: {
        getNotifications(type) {
            axios.get(`notifications/${type}`)
                .then(response => {
                    this.notifications.concat(response.data.results)
                })
        }
    }
}
</script>

<style scoped>

</style>