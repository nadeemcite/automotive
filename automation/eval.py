from automation.automation_executor import AutomationExecutor


class Eval(AutomationExecutor):
    def exec(self):
        result = eval(self.config["expression"])
        self.input_variables[self.config["result_var"]] = result
