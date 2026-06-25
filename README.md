Project: AI Screenshot Analyzer & Coding Assistant

Built a desktop automation tool that captures screenshots, analyzes visual content using local vision-language models, and generates intelligent solutions in real time. The application uses screen capture, image preprocessing, OCR-like understanding, and large language models running locally through Ollama to identify coding problems, error messages, and technical content from screenshots. Qwen2.5-VL is used for visual understanding while Qwen Coder generates explanations, optimized approaches, and complete code solutions. The generated responses are automatically delivered to the user through a Telegram bot for instant access. The system operates entirely on local AI models, ensuring privacy, low latency, and offline capability. Qwen2.5-VL is specifically designed for understanding screenshots, documents, charts, and text within images, making it well-suited for this workflow.

Key Features

Automated screenshot capture using Python
Image resizing and preprocessing
Screenshot understanding with Qwen2.5-VL
Competitive programming and error analysis
AI-generated C++ solutions and explanations
Telegram bot integration for notifications
Fully local inference using Ollama
Privacy-focused architecture with no cloud dependency

Tech Stack

Python
Ollama
Qwen2.5-VL
Qwen Coder
PyAutoGUI
Pillow (PIL)
Telegram Bot API
Requests
