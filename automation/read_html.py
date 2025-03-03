import json

import requests
from bs4 import BeautifulSoup
from lxml import etree

from automation.automation_executor import AutomationExecutor


class ReadHtml(AutomationExecutor):

    def exec(self):
        response = requests.get(self.config["url"])
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        dom = etree.HTML(str(soup))
        if "extracts" in self.config:
            results = []
            for extract in self.config["extracts"]:
                results.append(self.extract_xpath(dom, extract))
            self.input_variables[self.config["result_var"]] = json.dumps(results)
        elif "extract" in self.config:
            result = self.extract_xpath(dom, self.config["extract"])
            self.input_variables[self.config["result_var"]] = result

    def extract_xpath(self, dom, xpath):
        elements = dom.xpath(xpath)
        text_content = ""
        for element in elements:
            text_content = "".join(element.itertext())
        return text_content
