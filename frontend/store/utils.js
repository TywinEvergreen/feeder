export const actions = {
    go: async ({ app }, name) => {
        app.router.push({name: name})
    },
};
