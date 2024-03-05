document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector('.carousel');
    const inner = carousel.querySelector('.carousel-inner');
    const prevButton = carousel.querySelector('.carousel-prev');
    const nextButton = carousel.querySelector('.carousel-next');
    const totalItems = inner.querySelectorAll('.carousel-item').length;
    let currentIndex = 0;
  
    function updateCarousel() {
      inner.style.transform = `translateX(-${currentIndex * 100}%)`;
    }
  
    prevButton.addEventListener('click', function() {
      currentIndex = (currentIndex - 1 + totalItems) % totalItems;
      updateCarousel();
    });
  
    nextButton.addEventListener('click', function() {
      currentIndex = (currentIndex + 1) % totalItems;
      updateCarousel();
    });
  });
  