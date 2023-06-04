;(function() {
	'use strict';

	class Gallery {
		constructor(gallery) {
			this.thumbsBox = gallery.querySelector('.thumbs');
			this.thumbs = this.thumbsBox.querySelectorAll('img');
			this.image = gallery.querySelector('.photo-box img');
			this.control = gallery.querySelector('.control-row');
			this.count = this.thumbs.length;
			this.current = 0;
			this.registerEventsHandler();
		}

		registerEventsHandler(e) {
			this.control.addEventListener('click', this.buttonControl.bind(this));
			this.image.addEventListener('click', this.imageControl.bind(this));
			this.image.addEventListener('wheel', this.wheelControl.bind(this));
			document.addEventListener('keydown', this.keyControl.bind(this));
			this.thumbsBox.addEventListener('click', this.thumbControl.bind(this));
		}

		buttonControl(e) {
			if (e.target.tagName != 'BUTTON') return;
			const ctrl = e.target.dataset.control;
			let argControl = {
				first: 0,
				last: this.count - 1,
				prev: (this.count + this.current - 1) % this.count,
				next: (this.current + 1) % this.count
			};
			const i = argControl[ctrl];
			this.showPhoto(i);
		}

		imageControl(e) {
			this.showPhoto((this.current + 1) % this.count);
		}

		wheelControl(e) {
			e.preventDefault();

			let i = (e.deltaY > 0) ? (this.current + 1) % this.count : (this.count + this.current - 1) % this.count;
			this.showPhoto(i)
		}

		keyControl(e) {
			e.preventDefault();
			const code = e.which;
			if (code != 37 && code != 39) return;
			let argControl = {
				37: (this.count + this.current - 1) % this.count,
				39: (this.current + 1) % this.count
			}
			this.showPhoto(argControl[e.which]);
		}

		thumbControl(e) {
			const target = e.target;
			if (target.tagName != 'IMG') return;
			const i = [].indexOf.call(this.thumbs, target);
			this.showPhoto(i);
		}

		showPhoto(i) {
			const src = this.thumbs[i].getAttribute('src');
			this.image.setAttribute('src', src.replace('thumbnails', 'photos'));
			this.current = i;
		}
	}

	const galleries = document.querySelectorAll('[data-gallary]');
	for (let gallery of galleries) {
		const goodsgallery = new Gallery(gallery);
	}
})();
