// JavaScript code
document.addEventListener("DOMContentLoaded", () => {
  const userImage = document.getElementById("userImage");
  const imageUpload = document.getElementById("imageUpload");
  // const userName = document.getElementById('userName');
  // const welcomeMessage = document.getElementById('welcomeMessage');
  const logoutBtn = document.getElementById("logoutBtn");

  // Fixed start date for calculation
  const fixedStartDate = new Date("2024-06-04"); // Example date, replace with your fixed start date

  // Current system date
  const currentDate = new Date();

  // Calculate the difference in days between current date and fixed start date
  const diffInDays = Math.ceil(
    (currentDate - fixedStartDate) / (1000 * 60 * 60 * 24)
  );

  // Subscription details for each day
  const subscriptionDetails = [
    { day: 1, name: "ষষ্ঠী", food: "Food A", charges: 10 },
    { day: 2, name: "সপ্তমী", food: "Food B", charges: 15 },
    { day: 3, name: "অষ্টমী", food: "Food C", charges: 20 },
    { day: 4, name: "নবমী", food: "Food D", charges: 25 },
    { day: 5, name: "দশমী", food: "Food E", charges: 30 },
  ];

  // Find the subscription details for the current day
  const currentSubscription = subscriptionDetails.find(
    (subscription) => subscription.day === diffInDays
  );

  if (currentSubscription) {
    const dayElement = document.getElementById("day");
    const dayDateElement = document.getElementById("dayDate");
    const dayFoodElement = document.getElementById("dayFood");
    const dayChargesElement = document.getElementById("dayCharges");

    dayElement.textContent = currentSubscription.name;
    dayDateElement.textContent = formatDate(currentDate); // Format date
    dayFoodElement.textContent = currentSubscription.food;
    dayChargesElement.textContent = "INR " + currentSubscription.charges;
  }
});

// Function to format date (e.g., "June 1, 2024")
function formatDate(date) {
  const options = { month: "long", day: "numeric", year: "numeric" };
  return date.toLocaleDateString("en-US", options);
}

// Handle user image upload
imageUpload.addEventListener("change", (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = () => {
    userImage.src = reader.result;
  };

  if (file) {
    reader.readAsDataURL(file);
  }

  // Submit the form when a file is selected
  uploadImageForm.submit();
});

// Handle logout button click
logoutBtn.addEventListener("click", () => {
  // Perform logout logic here
  alert("You have been logged out.");
});
