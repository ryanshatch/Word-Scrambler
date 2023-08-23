<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1 align="center">Word Scrambler</h1>

  <p align="center">
    <strong>By: Ryan Hatch</strong><br>
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
       &copy; 2023 [ryan s hatch]<br>
       All Rights Reserved.
  </p>

  <h2 id="introduction">Introduction</h2>

  <p>
    The Word Scrambler is a Python program that allows you to rewrite user-provided text with perplexity and burstiness. Perplexity and burstiness are measures of how complex and variable the rewritten text will be. The goal is to generate text that closely resembles obfuscated writing while allowing for some level of variability and complexity.
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
    The scrambled text is: It aitn that bad. Could always be worse. Im running outta gas. maybe Id lay down for a little. Instead of always trying to figure everything out. And all I do is say sorry. Half the time I dont even know what Im singing about. Good news, good news, good news, thats all I wanna hear. No they dont like it when Im down..
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
  </p><br><br>

### License:

This software is the property of the copyright holder and is protected by copyright laws. All rights are reserved.

<code>The copyright holder grants no implied or express license for the use, copying, modification, distribution, or reproduction of this software, in whole or in part, without the prior written permission of the copyright holder.</code>

<code>Any unauthorized use, copying, modification, distribution, or reproduction of this software, in whole or in part, is strictly prohibited and constitutes a violation of copyright law. Such unauthorized use may result in civil and/or criminal penalties, including but not limited to legal action and monetary damages.</code>

To obtain permission for any use, copying, modification, distribution, or reproduction of this software, please contact the copyright holder at the following address:

```ryanshatch@gmail.com```
<br>
<br>
<br>
```By using this software, you acknowledge that you have read and understood the terms of this license and agree to comply with all applicable copyright laws. Failure to abide by the terms of this license may subject you to legal consequences.```

</body>
</html>
