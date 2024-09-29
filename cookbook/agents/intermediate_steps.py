from typing import Iterator
from rich.pretty import pprint
from phi.agent import Agent, AgentResponse
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
)

run_stream: Iterator[AgentResponse] = agent.run(
    "What is the stock price of NVDA", stream=True, stream_intermediate_steps=True
)
for chunk in run_stream:
    pprint(chunk.model_dump(exclude={"messages"}))
    print("---" * 20)