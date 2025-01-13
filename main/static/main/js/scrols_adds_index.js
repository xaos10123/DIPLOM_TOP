const scrollable = document.querySelector('.scrollable');
const content = document.querySelector('.content');
const scrollLeftButton = document.getElementById('scrollLeft');
const scrollRightButton = document.getElementById('scrollRight');

scrollLeftButton.addEventListener('click', () => {
    content.scrollBy({
        top: 0,
        left: 500, 
        behavior: 'smooth'
    });
});

scrollRightButton.addEventListener('click', () => {
    content.scrollBy({
        top: 0,
        left: -500, 
        behavior: 'smooth' 
    });
});