
# Vision Chatbot & Image Preprocessing

This project integrates a **Vision-Language Model (VLM)** powered **chatbot** that interacts with images, answering questions and providing insights. It also includes **image preprocessing techniques** such as **Fourier Domain Filtering** and **Edge Detection** to prepare images for analysis.

## 1. Project Overview

### Vision Chatbot
- The chatbot utilizes LangChain and Ollama to interpret and respond to user queries related to images.
- It leverages a Vision-Language Model (VLM) to understand image content and answer questions, enabling an interactive experience with images.

### Image Preprocessing
- Implements techniques such as **Fourier Domain Filtering** and **Edge Detection** to process images before passing them to the chatbot for enhanced accuracy and analysis.

## 2. System Requirements

The machine used for this project has the following specifications:

- **GPU**: NVIDIA GPU with **6GB+ VRAM** (recommended for efficient chatbot functionality).
- **CUDA Version**: **12.6**.
- **RAM**: **16GB** (Higher RAM will improve performance).
- **Disk Space**: At least **5GB free** for the application and models.

### **Better Performance**
- A **more powerful GPU** (with more VRAM) will lead to faster processing and better chatbot performance, especially when dealing with large images or complex queries.
- **More RAM** (32GB or higher) can help improve overall system responsiveness, especially when running multiple applications alongside the chatbot.

## 3. Installation Steps

### 3.1 Step 1: Download Ollama
To enable chatbot functionality, first download and install **Ollama**. Visit the official website and follow the installation instructions.

- **Download Ollama**: [Here](https://www.ollama.com).

### 3.2 Step 2: Download Required Models
After installing Ollama, download the necessary models. For example, to download the `minicpm-v` model, run:
```bash
ollama pull minicpm-v
