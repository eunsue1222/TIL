import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/articles'

export const useArticleStore = defineStore('article', () => {
    const articles = ref([
        { id: 1, title: 'title 1', content: 'content1' },
        { id: 2, title: 'title 2', content: 'content2' },
    ])

    const getArticles = function() {
        axios({
                method: 'get',
                url: `${API_URL}/`
            })
            .then(res => {
                // console.log(res)
                articles.value = res.data
            })
            .catch(err => {
                console.log(err)
            })
    }
    return {
        articles,
        getArticles
    }
}, { persist: true })