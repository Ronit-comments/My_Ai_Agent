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


    def get_step_result(
        self,
        step_number
    ):

        for item in self.results:

            if item["step"] == step_number:

                return item["result"]


        return None