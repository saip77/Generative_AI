const OpenAI = require("openai");
require("dotenv").config();  // Load environment variables from .env file

// Create a new instance of the OpenAI class
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
})

// Define a function to generate text using the OpenAI API
const generateText = async (req, res) => {
    try {
      const { prompt } = req.body;
  
      if (!prompt) {
        return res.status(400).json({ error: "Prompt is required" });
      }
  
      const response = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [{ role: "user", content: prompt }],
        temperature: 0.7,
        max_tokens: 100,
      });
  
      res.json({
        reply: response.choices?.[0]?.message?.content || "No reply generated",
      });
    } catch (error) {
      console.error("OpenAI API Error:", error);
      res.status(500).json({ error: error.message });
    }
  };
  
module.exports = generateText;