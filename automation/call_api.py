from automation.automation_executor import AutomationExecutor
import requests

class CallApi(AutomationExecutor):
    def exec(self):
        if "method" in self.config and self.config["method"].lower() == "post":
            resp = requests.post(
                self.config["url"],
                json=self.config.get("payload", {}),
                headers=self.config.get("headers", {}),
                params=self.config.get("params", {}),
            )
        else:
            resp = requests.get(
                self.config["url"],
                headers=self.config.get("headers", {}),
                params=self.config.get("params", {}),
            )
        if resp.text:
            self.input_variables[self.config["result_var"]] = resp.text
    