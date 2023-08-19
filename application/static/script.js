//wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Get a reference to the arrow element
    const arrow = document.querySelector('.arrow');

    // Get a reference to the element you want to toggle the class of
    const targetElement = document.querySelector('.inner-post');

    // Add a click event listener to the arrow element
    arrow.addEventListener('click', function() {
      // Toggle the desired class on the target element
      targetElement.classList.toggle('display');
    });
});