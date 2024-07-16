import json
import re

class AutomationExecutor:
    def __init__(self, config, input_variables):
        config = self.replace_with_template_variables(config, input_variables)
        self.config = json.loads(config)
        self.input_variables = input_variables

    def exec(self):
        pass

    def replace_with_template_variables(self, template, variables):
        def replacer(match):
            variable_name = match.group(1).strip()
            return variables.get(variable_name, match.group(0)).replace('\\"', '"').replace('"', '\\"')
        pattern = r'\{\{(.*?)\}\}'
        result = re.sub(pattern, replacer, template)
        return result