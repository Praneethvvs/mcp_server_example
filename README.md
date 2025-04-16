
# mcp_server_example

This project demonstrates the implementation of a custom **MCP server** using **Pydantic AI** and integrates third-party services like **Brave Search** with **Server-Sent Events (SSE)**. Follow the steps below to set up and run the project.


## Prerequisites

To set up and run the custom MCP server, ensure you have the following:

- **Python 3.12**: Download and install the latest version from the [official Python website](https://www.python.org/downloads/).
  
- **Node.js 22.14.0**: Install this version from the [Node.js official site](https://nodejs.org/en/download/releases/).

- **Gemini API Key**: Sign up for a free API key at the [Google AI Studio](https://aistudio.google.com/app/apikey).

- **Brave Search API Key**: Obtain a free API key by visiting the [Brave Search API page](https://brave.com/search/api/) and registering for an account.

- **Gmail App Password**: Generate a 16-character app password for your Gmail account by following these steps:
  
  1. Navigate to [Google Account Security Settings](https://myaccount.google.com/apppasswords).
  2. Under "Signing in to Google," select "App passwords."
  3. Choose the app and device for which you need the password, then click "Generate."
  4. Copy the generated 16-character password for use in your application.

## Setup Instructions

### 1) Clone the project

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd mcp_server_example
```

### 2) Create a virtual environment

Create a Python virtual environment for the project:

```bash
python -m venv venv
```

### 3) Activate the virtual environment

Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\ctivate
  ```

- On MacOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4) Install the requirements for the MCP server

Navigate to the `mcp_server` directory and install the necessary dependencies:

```bash
cd mcp_server
pip install -r requirements.txt
```

### 5) Install the requirements for the MCP client

Next, navigate to the `mcp_client` directory and install the necessary dependencies:

```bash
cd mcp_client
pip install -r requirements.txt
```

### 6) Populate `.env` files

You need to configure the environment variables for both the server and client. Create `.env` files in both `mcp_server` and `mcp_client` directories and populate them with the following keys:

- `GEMINI_API_KEY` — Free API key from Google AI Studio.
- `BRAVE_API_KEY` — Free API key from Brave Search.
- `GMAIL_APP_PASSWORD` — Generated app password (not your Gmail password).

Refer to the project documentation for detailed instructions on how to get these keys.

### 7) Install the MCP server

Install the MCP server globally:

```bash
npm install -g @modelcontextprotocol/server-brave-search
```

### 8) Run the server

Start the MCP server by running the following command in the `mcp_server` directory:

```bash
cd mcp_server
python main.py
```

### 9) Run the client

Once the server is running, start the MCP client:

```bash
cd mcp_client
python main.py
```

---

### Additional Information

- The server uses **SSE** (Server-Sent Events) to handle real-time data transfer and communication.
- The MCP framework is used to create seamless interactions between your AI models and third-party data sources like Brave Search.

For more details on using the project and extending the MCP framework, please refer to the documentation.

