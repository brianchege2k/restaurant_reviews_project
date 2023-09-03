
// If the input checkbox is checked, activate dark mode by adding dark-class to the body
$('#toggle').change(() => {
   if ($('#toggle').is(":checked")) {
      $("body").addClass("dark-class");
   } else {
      $("body").removeClass("dark-class")
   }
})
