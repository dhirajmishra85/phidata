from phi.agent import Agent
from phi.tools.github import GithubToolkit

# Replace 'your_access_token' with your actual GitHub access token
access_token = ""

# Initialize the GitHub toolkit
github_toolkit = GithubToolkit(access_token=access_token)

# Create an agent with the GitHub toolkit
agent = Agent(
    instructions=[
        "Use your tools to answer questions about the repo: phidatahq/phidata",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[github_toolkit],
    debug_mode=True,
    show_tool_calls=True,
)

# Example usage: List open pull requests
agent.print_response("List open pull requests", markdown=True)

# Example usage: Get pull request details
agent.print_response("Get details of #1239", markdown=True)

# # Example usage: Get pull request changes
agent.print_response("Show changes for #1239", markdown=True)

# Example usage: List open issues
agent.print_response("What is the latest opened issue?", markdown=True)

# Example usage: Create an issue
agent.print_response("Explain the comments for the most recent issue", markdown=True)