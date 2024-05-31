// Set the target date for the countdown (9th October 2024, 12:00 AM)
const targetDate = new Date('2024-10-09T00:00:00');

// Function to update the countdown display
function updateCountdown() {
  const currentDate = new Date();
  const timeDifference = targetDate.getTime() - currentDate.getTime();

  // Calculate days, hours, minutes, and seconds remaining
  const daysRemaining = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hoursRemaining = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutesRemaining = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const secondsRemaining = Math.floor((timeDifference % (1000 * 60)) / 1000);

  // Update the countdown display
  const countdownDisplay = document.getElementById('countdown');
  countdownDisplay.textContent = `${daysRemaining} days ${hoursRemaining} hours ${minutesRemaining} minutes ${secondsRemaining} seconds`;

  // If the countdown has reached zero, display a message
  if (timeDifference < 0) {
    countdownDisplay.textContent = 'Durga Puja 2024 has begun!';
    clearInterval(countdownInterval);
  }
}

// Initialize the countdown
const countdownInterval = setInterval(updateCountdown, 1000);

// Call the updateCountdown function immediately to display the initial countdown
updateCountdown();