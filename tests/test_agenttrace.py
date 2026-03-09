from agenttrace import AgentTrace

def test_agent_trace():
    agent = AgentTrace("TestAgent")
    agent.think("Thinking")
    agent.act("Acting")
    agent.observe("Observing")
    
    assert len(agent.logs) == 3
    assert agent.logs[0][0] == "THINK"
    assert agent.logs[1][0] == "ACT"
    assert agent.logs[2][0] == "OBSERVE"
