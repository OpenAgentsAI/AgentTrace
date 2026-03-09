""AgentTrace - Professional agent monitoring"""

import uuid

class AgentTrace:
    """Main tracer class"""
    
    def __init__(self, name="Agent"):
        self.name = name
        self.session_id = str(uuid.uuid4())
        self.logs = []
    
    def think(self, thought):
        """Log agent thinking process"""
        self.logs.append(("THINK", thought))
        
    def act(self, action):
        """Log agent action"""
        self.logs.append(("ACT", action))
        
    def observe(self, result):
        """Log observation results"""
        self.logs.append(("OBSERVE", result))
    
    def visualize(self):
        """Create simple ASCII visualization"""
        for log_type, content in self.logs:
            if log_type == "THINK":
                print(f"🤔 {content}")
            elif log_type == "ACT":
                print(f"⚡ {content}")
            elif log_type == "OBSERVE":
                print(f"👁️ {content}")
