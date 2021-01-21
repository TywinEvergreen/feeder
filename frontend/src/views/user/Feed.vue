<template>
    <v-container>
        <h3>{{all_releases}}</h3>
        <h4>{{new_albums}}</h4>
        <h5>{{new_videos}}</h5>
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
            all_releases: [],

            new_albums: [],
            new_videos: []
        }
    },
    created() {
        this.getNewAlbums();
        this.getNewVideos();
        this.setAllReleases(this.new_albums, this.new_videos);
    },
    methods: {
        async getNewAlbums() {
            await axios.get(`spotify/new-albums`)
                .then(response => {
                    this.new_albums = response.data.results
                })
        },
        async getNewVideos() {
            await axios.get(`youtube/new-videos`)
                .then(response => {
                    this.new_videos = response.data.results
                })
        },
        setAllReleases() {
            console.log(this.new_videos, this.new_albums);
            let releases = [];
            releases.push(...this.new_albums, ...this.new_videos);
            this.all_releases = releases
        },
    }
}
</script>

<style scoped>

</style>