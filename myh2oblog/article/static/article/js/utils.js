const constants = {scrollListened: true};
const tools = {
    getEleTop: (ele) => {
        let actualTop = ele.offsetTop
        let current = ele.offsetParent

        while (current !== null) {
            actualTop += current.offsetTop
            current = current.offsetParent
        }

        return actualTop
    }
}