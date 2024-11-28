# Vision Chatbot & Image Preprocessing

This project integrates a **Vision-Language Model (VLM)** powered **chatbot** that interacts with images, answering questions and providing insights. It also includes **image preprocessing techniques** such as **Fourier Domain Filtering** and **Edge Detection** to prepare images for analysis.

## Table of Contents
1. [Project Overview](#1-project-overview)
   - [Vision Chatbot](#vision-chatbot)
   - [Image Preprocessing](#image-preprocessing)
2. [System Requirements](#2-system-requirements)
3. [Installation Steps](#3-installation-steps)
   - [Step 1: Download Ollama](#31-step-1-download-ollama)
   - [Step 2: Download Required Models](#32-step-2-download-required-models)
   - [Step 3: Run the Application](#33-step-3-run-the-application)
4. [Offline Usage](#4-offline-usage)
5. [Contributing](#5-contributing)
6. [License](#6-license)
7. [Troubleshooting](#7-troubleshooting)
   - [Issue 1: Model download failure](#issue-1-model-download-failure)

## 1. Project Overview

### Vision Chatbot
- The chatbot utilizes LangChain and Ollama to interpret and respond to user queries related to images.
- It leverages a **Vision-Language Model (VLM)** to understand image content and answer questions, enabling an interactive experience with images.
- **Key Features**:
  - Real-time image analysis.
  - Multimodal interactions: text and images.
  ## Screenshot of the Chatbot in Action
 ### 💪 Strong OCR Capability
![Chatbot Screenshot](Chatbot-Screenshot)
### 🚀 Superior Efficiency
[![Chatbot-Screenshot 1](Chatbot-Screenshot 1)](https://github.com/Hicham-T/Vision-Chatbot-Image-Preprocessing/blob/b9ed2aa2de13064f811b4ec53ff4a58d73eed583/Chatbot-Screenshot%201)
### 🔥 Leading Performance
![Chatbot Screenshot](images/Screenshot-code.png)
### Image Preprocessing
- Implements techniques such as **Fourier Domain Filtering** and **Edge Detection** to process images before passing them to the chatbot for enhanced accuracy and analysis.
- **Use Cases**: 
  - Image enhancement for AI-based recognition tasks.
  - Preparing images for analysis or classification.

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
