<template>
    <v-container>

    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: "Feed",
    created() {
        this.getNotifications()
    },
    methods: {
        getNotifications() {
            axios.get('notifications/')
                .then(response => {
                    console.log(response.data)
                })
        }
    }
}
</script>

<style scoped>

</style>