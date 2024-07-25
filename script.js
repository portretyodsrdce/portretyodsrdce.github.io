// script.js
function switchLanguage(lang) {
    var csElements = document.querySelectorAll('.cs');
    var enElements = document.querySelectorAll('.en');

    if (lang === 'cs') {
        csElements.forEach(element => element.style.display = '');
        enElements.forEach(element => element.style.display = 'none');
    } else if (lang === 'en') {
        csElements.forEach(element => element.style.display = 'none');
        enElements.forEach(element => element.style.display = '');
    }
}

function showModal(imageSrc, captionText) {
    var modal = document.getElementById('imageModal');
    var modalImg = document.getElementById('largeImage');
    var caption = document.getElementById('imageCaption');
    modal.style.display = 'block';
    modalImg.src = imageSrc;
    caption.textContent = captionText;
}

function closeModal() {
    var modal = document.getElementById('imageModal');
    modal.style.display = 'none';
}
