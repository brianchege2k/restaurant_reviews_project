// If the input checkbox is checked, activate dark mode by adding dark-class to the body and container
$('#toggle').change(() => {
    if ($('#toggle').is(":checked")) {
       $("body").addClass("dark-class");
       $(".container").addClass("dark-class"); // Apply dark mode to the container
    } else {
       $("body").removeClass("dark-class");
       $(".container").removeClass("dark-class"); // Remove dark mode from the container
    }
 })
 