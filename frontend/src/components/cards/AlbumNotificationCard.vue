<template>
    <v-card>
        {{notification.content_object}}
        <h3>{{}}</h3>
    </v-card>
</template>

<script>
export default {
    name: "AlbumNotificationCard",
    props: ['notification']
}
</script>

<style scoped>

</style>