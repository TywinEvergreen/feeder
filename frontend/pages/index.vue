<template>
    <v-container>
        <h4
                v-for="(release, index) in all_releases"
                :key="index"
        >
            {{release.name}} - {{release.release_datetime}}
            <img :src="release.cover" alt="">
        </h4>
    </v-container>
</template>

<script>
import {mapState} from 'vuex';
import {parse} from 'date-format-parse'

export default {
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
        all_releases() {// Фильтерит релизы по дате и складывает их в один массив
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
            this.$axios.get(`spotify/new-albums`)
                .then(response => {
                    this.new_albums = response.data.results;
                })
        },
        getNewVideos() {
            this.$axios.get(`youtube/new-videos`)
                .then(response => {
                    this.new_videos = response.data.results;
                })
        },
    }
}
</script>