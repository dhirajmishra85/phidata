from phi.assistant import Assistant
from phi.llm.aws.claude import Claude
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Claude(model="anthropic.claude-3-5-sonnet-20240620-v1:0"),
    tools=[DuckDuckGo()],
    instructions=["use your tools to search internet"],
    debug_mode=True,
)


res = assistant.run(
    "you need to preform multiple searches. first list top 5 college football teams. then search for the mascot of the team with the most wins",
    stream=False,
)
print(res)