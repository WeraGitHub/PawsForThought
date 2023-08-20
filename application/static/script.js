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


  // Get references to the clickable images, modal, modal image, and close button
  const clickableImages = document.querySelectorAll('.clickable-image');
  const modal = document.getElementById('modal');
  const modalImage = document.getElementById('modal-image');
  const closeButton = document.querySelector('.close-button');

  // Add click event listeners to each clickable image
  clickableImages.forEach(function(image) {
    image.addEventListener('click', function() {
      // Set the source of the modal image to the clicked image's source
      modalImage.src = image.getAttribute('src');
      // Display the modal
      modal.style.display = 'block';
    });
  });

  // Add click event listener to the close button
  closeButton.addEventListener('click', function() {
    // Hide the modal when the close button is clicked
    modal.style.display = 'none';
  });

  // Add click event listener to the window
  window.addEventListener('click', function(event) {
    // Close the modal if the user clicks outside the modal content
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });

});
