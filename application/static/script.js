//wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
  // Get references to all arrow elements
  const arrows = document.querySelectorAll('.arrow');

  // Loop through each arrow element
  arrows.forEach(function(arrow) {
    // Find the corresponding target element for this arrow
    const targetElement = arrow.parentElement.querySelector('.inner-post');

    // Add a click event listener to the arrow element
    arrow.addEventListener('click', function() {
      // Toggle the desired class on the target element
      targetElement.classList.toggle('display');
    });
  });
});
