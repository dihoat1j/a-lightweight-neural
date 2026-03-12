from a_lightweight_neural.agents import Agent
from a_lightweight_neural.orchestrator import Orchestrator

orch = Orchestrator()
orch.register(Agent(name="planner", skills=["plan"]))
orch.register(Agent(name="executor", skills=["execute", "summarize"]))

result = orch.run(goal="Demo workflow")
print(result.summary)
print(result.steps)
