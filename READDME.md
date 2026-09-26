# AI Email Assistant

AI Email Assistant is a simple AI-powered web application that generates emails based on user-provided information such as recipient, purpose, details, tone, and desired email length.

The project was built as a practical introduction to working with APIs, Large Language Models (LLMs), environment variables, and Streamlit.

## Features

- Generate complete emails using AI
- Enter recipient and purpose
- Add important details to include in the email
- Select email tone: Professional, Friendly, Formal, or Casual
- Select email length: Short, Medium, or Detailed
- Input validation to prevent empty fields
- Error handling for API-related problems
- Secure API key storage using environment variables
- Simple web interface built with Streamlit

## Technologies Used

- Python
- Streamlit
- OpenRouter API
- OpenAI Python SDK
- python-dotenv

## How It Works

1. The user enters the required email information through the Streamlit interface.
2. The application validates the user input.
3. Python builds a structured prompt using the provided information.
4. The prompt is sent to an LLM through the OpenRouter API.
5. The API returns the generated response.
6. The application extracts the generated email from the response.
7. Streamlit displays the final email to the user.

## Installation

Clone the repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Streamlit application with:

```bash
streamlit run Aiemail.py
```

## Environment Variables

The application requires an OpenRouter API key.

Create a `.env` file in the project directory and add:

```text
OPENROUTER_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore` so that the API key is not exposed publicly.

## Project Structure

```text
AI-Email-Assistant/
│
├── Aiemail.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` is used locally and should not be uploaded to GitHub.

## Future Improvements

Possible future improvements include:

- Email refinement and rewriting
- Copy-to-clipboard functionality
- Additional tone options
- Email history
- Improved user interface
   
## Author

Muhammad Zoraiz