axios.interceptors.request.use(request => {
    if (request.method === 'post') {
        let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        request.headers['X-CSRFToken'] = csrf;
        // console.log(csrf);
    }
    return request
})

axios.interceptors.response.use(response => {
    return response.data
})

$(function () {
    var editor = editormd("article-content-area", {
        width: "100%",
        height: "90%",
        path: "https://cdn.jsdelivr.net/gh/yremp/editormd/lib/",
        gotoLine: true,
        codeFold: true,
        // emoji: true,
        toolbarIcons: function () {
            return ["||", "watch", "fullscreen", "preview", "testIcon"]
        },
    });
});
const vue = new Vue({
    el: "#app",
    data() {
        return {
            activeNames: ['1', '2', '3', '4'],
            tabPosition: 'left',
            drawer: false,
            article: {
                title: '',
                description: '',
                content: '',
                cover: "https://pic.myh2o.top/defaultCover",
                category: '',
                tag: [],
            }
        }
    },
    methods: {
        open() {
            this.$confirm('确认发布此文章吗？', '操作确认', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'info'
            }).then(() => {
                this.post_article();
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消发布'
                });
            });
        },
        post_article() {
            const data = {
                title: this.article.title,
                category: this.article.category,
                description: this.article.description,
                content: this.$refs.article_content.value,
                cover: this.article.cover,
                tag: this.article.tag,
            };
            // console.log(data);
            let url = location.href.split('/api/')[1];
            url = `/api/${url}`;
            axios.post(`${url}`, data).then(res => {
                // console.log(res);
                if (res.code) {
                    this.$message.error(res.msg);
                    return
                }
                this.$message.success(res.msg);
                setTimeout(() => {
                    location.href = `/article/${res.id}`;
                }, 1000)
            })
        },
    }
});