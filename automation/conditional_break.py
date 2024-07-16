from automation.automation_executor import AutomationExecutor


class ConditionalBreak(AutomationExecutor):
    def exec(self):
        result =  eval(self.config["expression"])
        return result