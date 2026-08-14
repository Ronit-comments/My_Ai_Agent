class AgentState:

    def __init__(self):

        self.results = []


    def add_result(
        self,
        step,
        action,
        result
    ):

        self.results.append({

            "step": step,

            "action": action,

            "result": result
        })


    def get_results(self):

        return self.results