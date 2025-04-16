from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio, MCPServerHTTP
from dotenv import load_dotenv
import asyncio
import os


load_dotenv()

brave_search_mcp_server = MCPServerStdio(
    command= "npx",
    args=[
          "-y",
          "@modelcontextprotocol/server-brave-search"
        ],
    env= {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
)


mail_server = MCPServerHTTP(url='http://localhost:8000/sse')  

#stdio mode
# mail_server = MCPServerStdio(
#     command= "/Users/praneethvvs/.local/bin/uv",
#     args= [
#         "run",
#         "--with",
#         "mcp[cli]",
#         "mcp",
#         "run",
#         "/Users/praneethvvs/Desktop/Praneeth/Projects/mcp_server_example/main.py"
#       ]
# )


agent = Agent(model="gemini-2.0-flash", mcp_servers=[brave_search_mcp_server, mail_server])



async def main():
    async with agent.run_mcp_servers():
        while True:
            command = input("You: ")
            if command == "exit":
                break
            agent_response = await agent.run(command)
            print(f"Agent: {agent_response}")


if __name__ == "__main__":
    asyncio.run(main())