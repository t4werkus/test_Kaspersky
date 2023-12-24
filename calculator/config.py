class Config:
    def __init__(self, agents: int = 0, storage: float = 0.0, traffic: float = 0, mail_traffic: float = 0, distributed: bool = False, nodes: int = 0):
        self.agents = agents
        self.storage = storage
        self.traffic = traffic
        self.mail_traffic = mail_traffic
        self.distributed = distributed
        self.nodes = nodes
