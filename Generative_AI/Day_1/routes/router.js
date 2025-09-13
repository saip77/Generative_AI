const express = require("express");
const generateText = require("../controllers/openai");

const router = express.Router();

// Route for text generation
router.post("/generate", generateText);

module.exports = router;
