# ITF Chatbot with Groq API

This project is a Streamlit application that leverages the Groq API to provide an interactive chatbot experience for ITF-related information.

## Technologies

- Git
- Python 3.x
- Streamlit
- Groq API
- python-dotenv

## Prerequisites

- Python 3.11 or higher
- Git

## Installation

1. Clone the repository:
```
git clone https://github.com/pverhaert/itf-groq-chatbot-v2.git itf-chatbot`
cd itf-chatbot
```
2. (Optional) Create and activate a virtual environment:  
`python -m venv .venv`  
`source .venv/bin/activate`  # On Unix or MacOS  
`.venv\Scripts\activate.bat`  # On Windows
3. Install dependencies: `pip install -r requirements.txt`


## Configuration

### Groq API Key

Obtain a Groq API key from the [Groq API documentation](https://console.groq.com/docs/quickstart).

### Environment Setup

1. Rename `.env.example` to `.env`
2. Edit `.env`:
   - Replace `gsk_xxx` with your Groq API key
   - Set `PREFERRED_MODEL` to your desired model (see [supported models](https://console.groq.com/docs/models))

## Usage

Run the application: `streamlit run main.py` 
Alternatively, use the provided `run.bat` script on Windows.

## Deployment

This application is deployed on Streamlit Cloud:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://itf-chatbot.streamlit.app)

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome. Please open an issue or submit a pull request for any improvements.

## Support

For support, please open an issue in the GitHub repository.
