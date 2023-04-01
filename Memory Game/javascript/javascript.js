$(document).ready(function() {
  // Calls functions when the page is ready
  shuffle();
  countCards();
  reloadPage();
});

// "New game" is implemented by attaching a function to the 
// button that simply refreshes the page and shuffles the cards
function reloadPage() {
  // Click event listener to "New Game" button
  $('#reload').click(function() {
  // Reloads the page
    location.reload();
  });
};

// Function to shuffle the deck of cards
function shuffle() {
  let card = $(".card");
  // For loop for each element
  for (let i = 0; i < card.length; i++) {
      // Picks a random element from all the card divs
      let targetOne = Math.floor(Math.random() * card.length);
      // Picks another random element from all the card divs
      let targetTwo = Math.floor(Math.random() * card.length);
      // Eq selects the chosen cards and places them one after the other
      card.eq(targetOne).before(card.eq(targetTwo));
  };
};

// Function to check for pairs
function countCards() {
  // Variable to keep track of how many cards have been selected (either 1 or 2)
  let counter = 0;
  // Variable for the first selection
  let firstChoice = "";
  // Variable for the second selection
  let secondChoice = "";

  let clickCount = 0;
  const cards = $(".card");

  // Click event listener for the cards
  cards.on("click", function() {
    // Checks if the clicked card is checked, i.e. if it has a pair
    if ($(this).hasClass("checked")) {
      // If it doesn't have a pair, return
      return;
    }
    // Checks if the card has already been clicked, clarification:
    //   --the program found another card with the same "animal" by
    //     clicking the same card twice, this prevents it
    if ($(this).hasClass("clicked") || counter === 2) {
      return;
    };

    // Add "clicked" class to the clicked card
    $(this).addClass("clicked");
    // Add one to the clickCount variable
    clickCount++;
    // Update the click count display
    $("#clicks").text(`Clicks: ${clickCount}`);

    // Check if it is the first or second click
    if (counter === 0) {
      // Check the "animal" attribute value
      firstChoice = $(this).attr("animal");
      // If it is the first click, add one to the counter
      counter++;

    } else {
      // Check the "animal" attribute value
      secondChoice = $(this).attr("animal");
      // It is the second click, change counter to zero
      counter = 0;

      // Check if the first selection is the same as the second selection
      if (firstChoice === secondChoice) {
      // Assigns the cards with the same "animal" value to a variable
        const oikeatKortit = $(".card[animal='" + firstChoice + "']");
        // Adds the "checked" class to the selected cards
        oikeatKortit.addClass("checked");
        // Removes the "clicked" class
        oikeatKortit.removeClass("clicked");

        // Congratulatory message
        const checkdCards = $(".card.checked");
        // Checks if all cards are checked by comparing the length of the cards and the "checked" class of the cards
        if (checkdCards.length === cards.length) {
          // Sends an alert congratulatory message with a 500ms delay showing the total click count
          if (clickCount <= 30) {
              setTimeout(function() {alert("Erinomainen suoritus! Selvitit muistipelin " + `${clickCount}`+ " painalluksella!");},500);
          } else if ((clickCount > 30) && (clickCount < 50)) {
              setTimeout(function() {alert("Hyvää työtä! Selvitit muistipelin " + `${clickCount}`+ " painalluksella!");},500);
          } else {
              setTimeout(function() {alert("Selvitit muistipelin " + `${clickCount}`+ " painalluksella. Paremmin ensi kerralla :)");},500);
          };
        };
      } else {
        const wrongCards = $(".card.clicked");
        // If the cards do not match, adds the "wrong" class which colors the background red
        wrongCards.addClass("wrong");
        // Removes the "wrong" class to remove the red color after 600ms
        setTimeout(function() {
          wrongCards.removeClass("wrong");
        },600)

        // Removes the "clicked" class after a 600ms delay
        setTimeout(function() {
          wrongCards.removeClass("clicked");
        }, 600)
      };
    };
  });
};

