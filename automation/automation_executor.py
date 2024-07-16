import json
import re

class AutomationExecutor:
    def __init__(self, config, input_variables):
        self.input_variables = input_variables
        config = self.replace_with_template_variables(config, input_variables)
        print(config)
        self.config = json.loads(config)

    def exec(self):
        pass

    def replace_with_template_variables(self, template, variables):
        def replacer(match):
            variable_name = match.group(1).strip()
            return variables.get(variable_name, match.group(0)).replace('"', '\\"')
        
        # Regex pattern to find all occurrences of {{<var_name>}}
        pattern = r'\{\{(.*?)\}\}'
        
        # Replace all matches with their corresponding values
        result = re.sub(pattern, replacer, template)
        
        return result