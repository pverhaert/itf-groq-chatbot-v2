# ITF Chatbot with Groq API
This project is a Streamlit application that interacts with the Groq API to provide information about the ITF Chatbot.

## Technologies Used
- Python 3.x
- Streamlit
- Groq API
- dotenv for environment management

## Getting Started

### Prerequisites
Ensure you have Python 3.11 or higher installed on your system. Streamlit and other required packages will be installed via the requirements file.

### Installation
1. Clone the repository: `git clone https://github.com/pverhaert/itf-groq-chatbot-v2.git itf-chatbot`
2. Navigate to the project directory: `cd itf-chatbot`
3. Set up a virtual environment (optional but recommended)
    - Open a command prompt (Windows: type `cmd` in the path bar at the top of the file explorer; Linux/macOS: open a terminal)
    - Create a virtual environment: `python -m venv .venv`
    - Activate the virtual environment:
        - Windows: `.venv\Scripts\activate.bat`
        - Linux/macOS: `source .venv/bin/activate`
4. Install the required Python packages: `pip install -r requirements.txt`

## Configuration
### Obtaining a Groq API Key
To use this application, you'll need an API key from Groq. Visit the [Groq API documentation](https://console.groq.com/docs/quickstart) to learn how to obtain one.

### Setting Up Your Environment
Once you have your API key, you need to set it in your environment:
- Rename `.env.example` to `.env`.
- Open the `.env` file and replace `gsk_xxx` with your Groq API key


## Running the Application
To run the application, activate your virtual environment (if you set one up) and use the following command: `streamlit run main.py`


