document.addEventListener("DOMContentLoaded", () => {
  // Unix timestamp (in seconds) to count down to
  // var twoDaysFromNow = new Date().getTime() / 1000 + 86400 * 2 + 1;
    const targetDate = new Date('2024-10-09T00:00:00').getTime() / 1000 + 86400 * 2 + 1;;

  // Set up FlipDown
  var flipdown = new FlipDown(targetDate)

    // Start the countdown
    .start()

    // Do something when the countdown ends
    .ifEnded(() => {
      console.log("The countdown has ended!");
    });

  // Toggle theme
  var interval = setInterval(() => {
    let body = document.body;
    body.classList.toggle("light-theme");
    body.querySelector("#flipdown").classList.toggle("flipdown__theme-dark");
    body.querySelector("#flipdown").classList.toggle("flipdown__theme-light");
  }, 5000);

  var ver = document.getElementById("ver");
  ver.innerHTML = flipdown.version;
});
