// JavaScript code
document.addEventListener('DOMContentLoaded', () => {
  const userImage = document.getElementById('userImage');
  const imageUpload = document.getElementById('imageUpload');
  const userName = document.getElementById('userName');
  const welcomeMessage = document.getElementById('welcomeMessage');
  const logoutBtn = document.getElementById('logoutBtn');
  
  // Set the user's name
  const currentUser = '{{ user.owner_name }}';
  userName.textContent = currentUser;
  welcomeMessage.textContent = `Welcome, ${currentUser}`;
  
  // Handle user image upload
  imageUpload.addEventListener('change', (event) => {
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
  logoutBtn.addEventListener('click', () => {
    // Perform logout logic here
    alert('You have been logged out.');
  });
  
  // Set subscription and schedule details
  const day1Date = document.getElementById('day1Date');
  const day1Food = document.getElementById('day1Food');
  const day1Charges = document.getElementById('day1Charges');
  const day1ScheduleDate = document.getElementById('day1ScheduleDate');
  
  day1Date.textContent = 'June 1, 2024';
  day1Food.textContent = 'Vegetarian Thali';
  day1Charges.textContent = '$20';
  day1ScheduleDate.textContent = 'June 1, 2024';
});
