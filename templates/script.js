const imageUpload = document.getElementById('image-upload');
const imagePreview = document.getElementById('image-preview');

imageUpload.addEventListener('change', function() {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const image = new Image();
      image.src = e.target.result;
      image.style.maxWidth = '100%';
      image.style.maxHeight = '100%';
      image.onload = function() {
        const aspectRatio = image.width / image.height;
        const newHeight = 300;
        const newWidth = newHeight * aspectRatio;
        imagePreview.innerHTML = '';
        imagePreview.appendChild(image);
        imagePreview.style.width = newWidth + 'px';
        imagePreview.style.height = newHeight + 'px';
      };
    };
    reader.readAsDataURL(file);
  } else {
    imagePreview.innerHTML = 'No image selected';
  }
});
