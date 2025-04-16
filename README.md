
# mcp_server_example

This project demonstrates the implementation of building a custom MCP client-server solution, the client is developed using the Pydantic AI Framework, and it interacts with Brave Search MCP Server and a custom Send_Email server, all powered by the Gemini-2.0-Flash LLM. This approach eliminates the need for pre-built solutions like Claude Desktop, offering full flexibility and control over the client-server integration.


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
- `SENDER_EMAIL` -  Email address of the sender(the account for which you created the gmail_app_password).



### 7) Install the Brave Search MCP server

Install the MCP server. This will be called by the mcp_client using STDIO

```bash
npm install -g @modelcontextprotocol/server-brave-search
```


### 8) Run the server

Start the MCP server by running the following command in the `mcp_server` directory. This will be called by the mcp_client using SSE

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

### 10) Sample Prompt which invokes both the tools

find the most bizarre food combinations that actually taste good and email them to me with the subject 'Food Fusion Fiasco!' Add a fun note: 'Time to spice up your taste buds!'" to <email_id>
