export default {
    actions: {
        async go(context, name) {
            $nuxt.$router.push({
                name: name
            })
        },
    }
}
