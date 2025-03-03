import json

from automation.automation_executor import AutomationExecutor


class ArrayJoin(AutomationExecutor):

    def exec(self):
        self.input_variables[self.config["result_var"]] = json.dumps(
            self.config["join_key"].join(json.loads(self.config["source"]))
        )
