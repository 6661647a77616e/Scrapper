// Define the starting and ending values for X
var start = 7;
var end = 100;

// Iterate through the range of X values using a for loop
for (var x = start; x <= end; x++) {
  // Construct the CSS selector with the dynamic X value
  var selector = 'h2[data-automation-id="homepage:main_list:article:title:' + x + '"]';

  // Extract the text from the specified <h2> element
  var element = document.querySelector(selector);
  var text = element.textContent;

  // Print the extracted text
  console.log(text);
}
