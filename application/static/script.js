//wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
  // Get references to all arrow elements
  const arrows = document.querySelectorAll('.arrow');

  // Loop through each arrow element
  arrows.forEach(function(arrow) {
    // Find the post element that contains this arrow
    const post = arrow.closest('.post');
    // Find the corresponding target element within the post
    const targetElement = post.querySelector('.inner-post');
    // Add a click event listener to the arrow element
    arrow.addEventListener('click', function() {
      // Toggle the desired class on the target element
      targetElement.classList.toggle('display');

      // Toggle the src attribute of the arrow image
      const altSrc = arrow.getAttribute('data-alt-src');
      if (altSrc) {
        const currentSrc = arrow.getAttribute('src');
        arrow.setAttribute('src', altSrc);
        arrow.setAttribute('data-alt-src', currentSrc);
      }
    });

  });

});
