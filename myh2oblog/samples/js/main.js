// 点击首页的下滑图标
// const scroll_down = document.querySelector(".web-scroll-down");
const header = document.querySelector(".web-header");
// scroll_down.onclick = function() {
// 	let bottom = header.getBoundingClientRect().bottom;
// 	console.log(bottom);
// 	window.scrollBy(0, bottom);
// }


// 往上滑动，出现导航栏
const navbar = document.querySelector(".navbar");

function navbar_show() {
	navbar.classList.add('navbar-fixed');
}

function navbar_unshow() {
	navbar.classList.remove('navbar-fixed');
}

window.onmousewheel = (event) => {
	if (event.wheelDelta >= 0) {
		if (header.getBoundingClientRect().top < 0) {
			navbar_show();
		} else {
			navbar_unshow();
		}
	} else {
		navbar_unshow();
	}
}

// 后续改进一下鼠标滑动滚动条，导航栏不会出现的情况
// window.addEventListener('scroll', (event) => {
// 	console.log(event);
// })
