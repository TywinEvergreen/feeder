import router from '@/router'

const state = {
};

const getters = {
};

const mutations = {
};

const actions = {
    go: async (main, name) => {
        router.push({name: name})
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};