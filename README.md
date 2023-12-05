# GPTsDataCollector

## Overview

GPTsDataCollector is a proof of concept that demonstrates interactive form filling through conversations with ChatGPT. Users can engage with ChatGPT to fill out forms in a conversational manner, making data collection more intuitive and user-friendly.

**Note:** Before deploying this tool, it is recommended to configure Nginx and set up HTTPS for secure data transmission.

**Demo:** [ChatGPT Interactive Form Collector](https://chat.openai.com/g/g-m5IFwo2Q0-info-collector)

## Setup and Usage

This section guides you through setting up and using the GPTsDataCollector.

### ChatGPT Setup

1. Create ChatGPT Chatbot:
   - Use the provided prompt in `prompt.txt` as a base to create a new GPTs chatbot.
   - Add Actions using the OpenAPI specification in `openapi.yml`.
   - **Important:** Update the URL in `openapi.yml` to point to your server.

### Server Setup

1. Install Dependencies:
   - Run the command `pip install -r requirements.txt` to install necessary Python packages.
2. Start the Server:
   - Launch the server by executing `python wsgi.py`.