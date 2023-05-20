// Desc: Preview image before uploading
const input = document.querySelector('input[type="file"]');
const container = document.querySelector('#image-container');
const dropZone = document.getElementById('drop-zone');
const clearImageButton = document.querySelector('#clear-image');

// Function to handle file selection
function handleFileSelect(file) {
    container.innerHTML = '';
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.id = 'image-preview';
            container.appendChild(img);

            // Save the base64 representation of the image in session storage
            sessionStorage.setItem('imagePreview', e.target.result);
        }
        reader.readAsDataURL(file);
    }
}

input.addEventListener('change', function () {
    handleFileSelect(this.files[0]);
});

// Drag and drop events
dropZone.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', function (e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', function (e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    input.files = e.dataTransfer.files;
    handleFileSelect(file);
});


// clearImageButton.addEventListener('click', function() {
//     // Clear the file input
//     input.value = '';

//     // Clear the image preview from the container
//     container.innerHTML = '';

//     // Remove the image preview from session storage
//     sessionStorage.removeItem('imagePreview');
// });


// Load the image preview from session storage when the page is reloaded
// Clear the file input when the page is refreshed
window.addEventListener('DOMContentLoaded', function() {

    // Your existing code for loading the image preview from session storage
    const imagePreviewSrc = sessionStorage.getItem('imagePreview');
    if (imagePreviewSrc) {
        const img = document.createElement('img');
        img.src = imagePreviewSrc;
        img.id = 'image-preview';
        container.appendChild(img);
    }
});



