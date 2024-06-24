# Travel_Assistant_Bot
Travel_Assistant_Bot

Certainly! Here's a README template for a travel bot that compares the performance of Ollama (Llama3, Gemma:2b) and OpenAI GPT models:

---

# Travel Bot: Comparing Ollama (Llama3, Gemma:2b) and OpenAI GPT Models

Welcome to Travel Bot! This README provides an overview of the project, which compares the performance of Ollama's Llama3 (Gemma:2b) and OpenAI's GPT models in the context of generating travel-related content. This includes creating travel itineraries, answering travel-related questions, and providing travel tips, with a special focus on global destinations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Model Comparison](#model-comparison)
  - [Ollama Llama3 (Gemma:2b)](#ollama-llama3-gemma2b)
  - [OpenAI GPT Models](#openai-gpt-models)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Travel Bot is designed to leverage the capabilities of advanced language models to assist with travel planning and advice. By comparing Ollama's Llama3 (Gemma:2b) and OpenAI's GPT models, we aim to identify which model offers superior performance in generating accurate, useful, and creative travel content.

## Features
- **Itinerary Generation**: Create new and unique travel itineraries based on given preferences or destinations.
- **Travel Q&A**: Answer travel-related questions with detailed explanations.
- **Travel Tips**: Provide useful tips and tricks for traveling.

## Model Comparison

### Ollama Llama3 (Gemma:2b)
- **Architecture**: Based on the Llama3 architecture, specifically the Gemma:2b variant.
- **Strengths**:
  - Excels in understanding and generating text related to travel.
  - Provides creative and diverse itinerary suggestions.
  - Efficient in handling complex travel queries.
- **Weaknesses**:
  - May require more fine-tuning for highly specialized travel knowledge.
  - Limited availability of training data compared to OpenAI models.

### OpenAI GPT Models
- **Architecture**: Various versions of the Generative Pre-trained Transformer (GPT) architecture.
- **Strengths**:
  - Extensive training on diverse datasets, including travel content.
  - High accuracy in answering travel-related questions.
  - Robust and reliable performance in generating detailed itineraries and tips.
- **Weaknesses**:
  - Can occasionally produce overly complex or impractical itineraries.
  - Higher computational resource requirements.

## Installation
To install and set up Travel Bot, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/travel-bot.git
    cd travel-bot
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install Ollama Llama3 and Gemma:2b models:
    - Follow the instructions at [Ollama GitHub repository](https://github.com/ollama) to install the models locally.
    - Run the following commands to set up the models:
      ```sh
      ollama run llama3
      ollama run gemma:2b
      ```

4. Create model files:
    - Create `Modelfile` and add the following content for Llama3:
      ```
      FROM llama3

      # set the temperature to 1 [higher is more creative, lower is more coherent]
      PARAMETER temperature 1

      # set the system message
      SYSTEM """
      You are a travel expert. Answer as Travel Bot, the assistant, only.
      """
      ```

    - Create `Modelfile2` and add the following content for Gemma:2b:
      ```
      FROM gemma

      # set the temperature to 1 [higher is more creative, lower is more coherent]
      PARAMETER temperature 1

      # set the system message
      SYSTEM """
      You are a travel expert. Answer as Travel Bot, the assistant, only.
      """
      ```

5. Set up API keys:
    - Obtain an API key for OpenAI.
    - Create a `.env` file in the root directory and add your OpenAI API key:
      ```sh
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage
To run the Streamlit app, use this command:
```sh
streamlit run app.py
```
You can interact with the bot via the command line or through the Streamlit web application.

## Examples
Here are some examples of what Travel Bot can do:

- **Generate an Itinerary**:
  - **Input**: "Create a 7-day itinerary for Paris."
  - **Output**: "Here is a 7-day itinerary for Paris: [detailed itinerary]"

- **Answer a Travel Question**:
  - **Input**: "What are the best travel tips for Tokyo?"
  - **Output**: "Here are some travel tips for Tokyo: [detailed tips]"

- **Provide a Travel Tip**:
  - **Input**: "What's a good tip for saving money while traveling?"
  - **Output**: "To save money while traveling, consider these tips: [detailed tips]"

## Contributing
We welcome contributions to Travel Bot! Please see our contributing guidelines for more information.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to adjust any sections as needed!

---
