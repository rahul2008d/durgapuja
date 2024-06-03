document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".tab");
    const items = document.querySelectorAll(".img");

    tabs.forEach(tab => {
        tab.addEventListener("click", function() {
            // Remove active class from all tabs
            tabs.forEach(tab => tab.classList.remove("tab-active"));
            // Add active class to the clicked tab
            this.classList.add("tab-active");

            const filter = this.getAttribute("data-filter");

            // Show/Hide items based on the selected tab
            items.forEach(item => {
                if (filter === "all") {
                    item.style.display = "block";
                } else {
                    if (item.classList.contains(filter)) {
                        item.style.display = "block";
                    } else {
                        item.style.display = "none";
                    }
                }
            });
        });
    });
});
