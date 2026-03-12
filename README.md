# a-lightweight-neural

Production-ready a-lightweight-neural toolkit for multi-agent orchestration and shared memory.

## Features
- Agent registry with task delegation
- Shared in-memory context store
- Deterministic planner for repeatable runs
- Test suite and CI workflow

## Install
```bash
pip install -e .
```

## Quickstart
```python
from a_lightweight_neural.orchestrator import Orchestrator
from a_lightweight_neural.agents import Agent

orch = Orchestrator()
orch.register(Agent(name='planner', skills=['plan']))
orch.register(Agent(name='executor', skills=['execute']))
result = orch.run(goal='Build a resilient task plan')
print(result.summary)
```

## Branches
- main: stable baseline
- develop: additional observability
- feature/experimental: adaptive scoring prototype