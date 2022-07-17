const image = document.querySelectorAll('.activ')
const link = document.querySelectorAll('.bobbly')
const main = document.querySelectorAll('.main')



link[0].onclick = () => {
image.style.backgroundPosition = "-64px 0px"

}


function checking(ins, ln) {
	if (ins.className.includes('passive')) {
		ins.style.border= "0px solid #121212";
		ln.href='#';
		ln.remove()
		return true
	}
}

for (node of main){
	let ins = node.querySelector('ins')
	let ln = node.querySelector('.bobbly')

	let flag = checking(ins, ln)

	if (flag) {
		console.log(flag);

		continue;
	};

	ln.onmouseover = () => {
		ins.style.borderColor = "#7f0af5"
	}
	ln.onmouseout = () => {
		ins.style.borderColor = "#121212"
	}
	ln.onclick = () => {
		ins.style.filter = "grayscale(0%)"
	}
}


