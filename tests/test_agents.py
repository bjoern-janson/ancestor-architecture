from src.agents import BaseAgent



def test_agent_exists():

    agent = BaseAgent()

    assert agent is not None
