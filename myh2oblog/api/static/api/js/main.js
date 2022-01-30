axios.interceptors.request.use(request => {
    if (request.method === 'post') {
        let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        request.headers['X-CSRFToken'] = csrf;
        console.log(csrf);
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
    console.log(editor)
});
const vue = new Vue({
    el: "#app",
    data() {
        return {
            activeNames: ['1', '2', '3', '4'],
            tabPosition: 'left',
            drawer: true,
            article: {
                title: '',
                description: '',
                content: '',
                cover: "http://pic.myh2o.top/favicon",
                category: '',
                tag: [],
            }
        }
    },
    methods: {
        open() {
            this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.$message({
                    type: 'success',
                    message: '删除成功!'
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
        },
    }
});