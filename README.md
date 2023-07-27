<!DOCTYPE html>
<html>
<head>
  <title>Word Scrambler</title>
</head>
<body>
  <h1 align="center">Word Scrambler</h1>

  <p align="center">
    <strong>By: Your Name Here</strong><br>
  </p>

  <p align="center">
    <a href="#introduction">Introduction</a> •
    <a href="#how-to-use">How to Use</a> •
    <a href="#implementation-details">Implementation Details</a> •
    <a href="#example-usage">Example Usage</a> •
    <a href="#customization">Customization</a>
  </p>

  *****************************************************

  <p align="center">
       &copy; [Year] [Your Name Here]<br>
       All Rights Reserved.
  </p>

  <h2 id="introduction">Introduction</h2>

  <p>
    The Word Scrambler is a Python program that allows you to rewrite user-provided text with the most human-like perplexity and burstiness. Perplexity and burstiness are measures of how complex and variable the rewritten text will be. The goal is to generate text that closely resembles natural human writing while allowing for some level of variability and complexity.
  </p>

  <h2 id="how-to-use">How to Use</h2>

  <ol>
    <li>Run the script.</li>
    <li>Enter the text you want to rewrite when prompted.</li>
    <li>Input the desired perplexity and burstiness values on a scale of 0 to 100. Higher values increase complexity and variability.</li>
  </ol>

  <h2 id="implementation-details">Implementation Details</h2>

  <p>
    The script utilizes a language model to rewrite the text. It iterates through each word in the input text and applies the following rules:
  </p>

  <ol>
    <li>If the random number falls below the burstiness value, replace the word with a random lowercase letter.</li>
    <li>If the random number falls below the perplexity value, replace the word with a random combination of lowercase letters, digits, and spaces. Non-alphanumeric characters are removed to maintain readability.</li>
  </ol>

  <h2 id="example-usage">Example Usage</h2>

  <pre><code>
    Enter the text you want to scramble: The Evaluation section evaluates different operating platforms and their suitability for the requirements of the gaming application.
    Enter the perplexity: 50
    Enter the burstiness: 50
    The scrambled text is: cbcbaaaaabaaaaa acaaaaaaaaaaaa aabcaacaaaa aacabaaaaaaaa aacaaaaaaaaaa aaaaaaaaaaaaaaa.
  </code></pre>

  <h2 id="customization">Customization</h2>

  <p>
    You can adjust the perplexity and burstiness levels to control the complexity and variability of the rewritten text. Higher values will result in more complex and variable output, while lower values will lead to more straightforward and consistent output.
  </p>

  <p>
    Please note that this code uses a simple language model for demonstration purposes. You can replace it with a more advanced model for better results.
  </p>

  <h2>Caution</h2>

  <p>
    Using very high perplexity and burstiness values may result in extremely convoluted and hard-to-understand text. Carefully select the values to generate human-like yet coherent output.
  </p>
</body>
</html>