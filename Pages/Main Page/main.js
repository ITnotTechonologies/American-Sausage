const arrowR = document.querySelector('.arrowR');
const arrowL = document.querySelector('.arrowL');
console.log(arrowL, arrowR);

const slides = document.querySelectorAll('.slides');
console.log(slides);

let counter = 0;

slides[counter].style.display = 'flex';

console.log(slides[counter]);

arrowL.onclick = function () {
	counter -= 1;
	
	if (counter < 0) {
		counter = slides.length - 1;
	}

	// alert(counter);

	for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	slides[counter].style.display = 'flex';

}

arrowR.onclick = function () {
	counter += 1;

	if (counter >= slides.length) {
		counter = 0;
	} 

	// alert(counter);
	for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	slides[counter].style.display = 'flex';
}