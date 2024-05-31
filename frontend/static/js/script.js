function openTab(tabName) {
    var i, tabContent;
    tabContent = document.getElementsByClassName("tabContent");
    for (i = 0; i < tabContent.length; i++) {
      tabContent[i].style.display = "none";
    }
    document.getElementById(tabName).style.display = "block";
  }
  document.getElementById("signIn").style.display = "block"; // Show sign in tab by default
  