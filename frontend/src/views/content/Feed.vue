<template>
    <v-container>
        <h4
                v-for="(release, index) in all_releases"
                :key="index"
        >
            {{release.name}} - {{release.release_datetime}}
<!--            <h5>{{release.cover}}</h5>-->
            <img :src="release.cover" alt="">
        </h4>
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
import {mapState} from 'vuex';
import {parse} from 'date-format-parse'
import axios from "axios";

export default {
    name: "Feed",
    components: {
    },
    data() {
        return {
            new_albums: [],
            new_videos: []
        }
    },
    created() {
        this.getNewAlbums();
        this.getNewVideos();
    },
    computed: {
        ...mapState(['conf']),
        all_releases() {
            let releases = [];

            releases.push(...this.new_albums);
            releases.push(...this.new_videos);

            const dt_format = this.conf.default_datetime_format
            let ordered_releases = releases.sort((a, b) => {
                return parse(b.release_datetime, dt_format) - parse(a.release_datetime, dt_format)
            })
            return ordered_releases
        },

    },
    methods: {
        getNewAlbums() {
            axios.get(`spotify/new-albums`)
                .then(response => {
                    this.new_albums = response.data.results;
                    // this.all_releases.push(...response.data.results);
                })
        },
        getNewVideos() {
            axios.get(`youtube/new-videos`)
                .then(response => {
                    this.new_videos = response.data.results;
                    // this.all_releases.push(...response.data.results);
                })
        },
    }
}
</script>

<style scoped>

</style>