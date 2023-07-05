Counting the number of links on the page:

```js
const links = document.querySelectorAll('a');
console.log(links.length);
```

Ouput links in nice format
```js
const links = document.querySelectorAll('a');
const linkArray = Array.from(links); // convert NodeList to Array

linkArray.forEach(link => {
  console.log(link.getAttribute('href'));
});
```

Counting the number of images on the page:
```js
const images = document.querySelectorAll('img');
console.log(images.length);
```

Finding the largest heading on the page:
```js
const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
let largestHeading = headings[0];
headings.forEach(heading => {
  if (heading.getBoundingClientRect().height > largestHeading.getBoundingClientRect().height) {
    largestHeading = heading;
  }
});
console.log(largestHeading.innerText);
```

Finding the most frequently used color on the page:
```js
const elements = document.querySelectorAll('*');
const colors = {};
elements.forEach(element => {
  const color = window.getComputedStyle(element).getPropertyValue('color');
  if (colors[color]) {
    colors[color]++;
  } else {
    colors[color] = 1;
  }
});
let mostFrequentColor = Object.keys(colors)[0];
Object.keys(colors).forEach(color => {
  if (colors[color] > colors[mostFrequentColor]) {
    mostFrequentColor = color;
  }
});
console.log(mostFrequentColor);
```

Counts the frequency of each word on a webpage and logs the results to the console
```js
// Get all the text on the webpage
const text = document.body.innerText;

// Split the text into an array of words
const words = text.split(/\s+/);

// Create an empty object to store the word frequencies
const wordFrequencies = {};

// Loop through each word and update its frequency in the object
words.forEach(word => {
  // Ignore small words (less than 3 characters)
  if (word.length < 3) {
    return;
  }

  // Convert the word to lowercase
  const lowercaseWord = word.toLowerCase();

  // If the word is already in the object, increment its frequency
  if (wordFrequencies[lowercaseWord]) {
    wordFrequencies[lowercaseWord]++;
  }
  // Otherwise, add the word to the object with a frequency of 1
  else {
    wordFrequencies[lowercaseWord] = 1;
  }
});

// Log the word frequencies to the console
console.log(wordFrequencies);
```
Copy Paste Text
```js
const words = 'This is the text to be copied to the clipboard.';

navigator.clipboard.writeText(words)
  .then(() => {
    console.log('Text copied to clipboard.');
  })
  .catch(error => {
    console.error('Failed to copy text: ', error);
  });
```
Print Out All Heading 
```js
const h2Elements = document.querySelectorAll('h2');

// Loop through h2 elements and extract text content
for (let i = 0; i < h2Elements.length; i++) {
  const h2Text = h2Elements[i].textContent;
  console.log(h2Text);
}
```
___

Scan Entered Text for Email and Password
this code can only be implemented for email , change the id values according to website Id
```js
const emailField = document.getElementById('email');
const passwordField = document.getElementById('passContainer');

// Copy the values of the fields
const emailValue = emailField.value;
const passwordValue = passwordField.value;

// Log the values to the console
console.log(`Email: ${emailValue}, Password: ${passwordValue}`);
```

How to get recent time in without API from https://www.google.com/search?client=opera-gx&q=malaysia+time+now&sourceid=opera&ie=UTF-8&oe=UTF-8
```js
const timeStr = document.querySelector('.gsrt.vk_bk.FzvWSb.YwPhnf').textContent.trim();

```
