let active = 0;
const cardCount = $('.card-container').length;

function prevSlide() {
  active = (active - 1 + cardCount) % cardCount;
  updateCarousel();
}

function nextSlide() {
  active = (active + 1) % cardCount;
  updateCarousel();
}

function updateCarousel() {
  $('.card-container').each(function(index) {
    const offset = (index - active) * -100;
    $(this).css('transform', 'translateX(' + offset + '%)');
  });
}

$(document).ready(function() {
  updateCarousel();
});
