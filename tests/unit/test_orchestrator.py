from a_lightweight_neural.agents import Agent
from a_lightweight_neural.orchestrator import Orchestrator

def test_orchestrator_run() -> None:
    orch = Orchestrator()
    orch.register(Agent(name="planner", skills=["plan"]))
    out = orch.run("ship release")
    assert len(out.steps) == 3
