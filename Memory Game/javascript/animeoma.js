window.addEventListener('load', function() {
  // Function to animate card rotation
  function roll() {
    const animaatio = document.querySelectorAll(".card")
    // Animation properties
    anime({
        targets: animaatio,
        translateY: -900,
        rotate: '1turn',
        easing: 'easeInOutSine',
        duration: 300
    });
  };
  roll()

  // Function to animate card hover
  function animateHover() {
    const hover = $(".card");
    // Create a function that takes four parameters:
    // a reference to the element, animation scale, duration, and elasticity
    function animateButton(el, scale, duration, elasticity) {
    // Remove previous animations
      anime.remove(el);
      anime({
        targets: el,
        scale: scale,
        duration: duration,
        elasticity: elasticity
      });
    };
    // Function for mouseenter with parameters
    function enterButton(el) {
      animateButton(el, 1.1, 50, 400);
    };
    // Function for mouseleave with parameters
    function leaveButton(el) {
      animateButton(el, 1.0, 50, 300);
    };
    // Call the enterButton() function on mouseenter
    hover.on('mouseenter', function() {
      enterButton(this);
    });
    // Call the leaveButton() function on mouseleave
    hover.on('mouseleave', function() {
      leaveButton(this);
    });
  };
  animateHover()
});
