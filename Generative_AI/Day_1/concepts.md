# Basic Concepts

## What is an SDK?

An SDK (Software Development Kit) is a collection of tools, libraries, and documentation that allows developers to build applications for a specific platform or technology.

## Why we need SDKs?

You want to build an app that uses OpenAI's API to generate text (like ChatGPT). Instead of manually crafting HTTP requests to the API, OpenAI gives you an SDK to make this easier.

The SDK:

- Handles authentication
- Formats API requests and responses
- Gives you clean, readable functions like openai.chat.completions.create()

// Without SDK
```
fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: {
    Authorization: `Bearer YOUR_API_KEY`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "gpt-4",
    messages: [{ role: "user", content: "Hello!" }],
  }),
});
```

// With SDK
```
const { OpenAI } = require("openai");

const openai = new OpenAI({
  apiKey: "YOUR_API_KEY",
});

const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: "Hello!" }],
});

console.log(response.choices[0].message.content);
```


## OpenAI class

while using 

const OpenAI = require("openai");

we are importing the OpenAI class from the openai package. Hence,the naming convention is to use the class name as the variable name.