from automation.automation_executor import AutomationExecutor
from bs4 import BeautifulSoup
import requests
from lxml import etree
import json


class ReadHtml(AutomationExecutor):

    def exec(self):
        response = requests.get(self.config["url"])
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        dom = etree.HTML(str(soup))
        results = []
        for extract in self.config["extracts"]:
            xpath = extract
            elements = dom.xpath(xpath)
            text_content = ""
            for element in elements:
                text_content = "".join(element.itertext())
            results.append(text_content)
        self.input_variables[self.config["result_var"]] = json.dumps(results)
        # print(self.input_variables)
