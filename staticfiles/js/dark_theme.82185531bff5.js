
  // Function to toggle dark theme
  function toggleDarkTheme() {
    document.body.classList.toggle("dark-theme");
    // Store user's preference in localStorage
    if (document.body.classList.contains("dark-theme")) {
      localStorage.setItem("darkTheme", "enabled");
    } else {
      localStorage.setItem("darkTheme", "disabled");
    }
  }

  // Add event listener to the button
  document.getElementById("darkThemeButton").addEventListener("click", toggleDarkTheme);

  // Check user's preference from localStorage and set dark theme if preferred
  if (localStorage.getItem("darkTheme") === "enabled") {
    toggleDarkTheme();
  }

