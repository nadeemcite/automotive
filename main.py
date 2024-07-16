from cron.cron_executer import cron_execute


def run():
    cron_execute(
        [
            "1467148511",
            '["a","b"]',
            "Read HTML", '{ "url": "https://www.bhaskar.com", "extracts": ["(//ul)[4]/div[1]/div/li//h3", "(//ul)[4]/div[2]/div/li//h3", "(//ul)[4]/div[3]/div/li//h3"], "result_var": "a" }',
            "Array Join", '{ "source": "{{a}}", "join_key": "\\n\\n",  "result_var": "b" }',
            "Call API", '{"url": "https://discord.com/api/webhooks/1262716477182836806/_2bcN6h7NgwN9QTdFBf3rRaV39vksClOSAiee4UzMp0l3XvJTnfIR6larFsaNWCWWfgv", "method": "post", "payload": {"content": "{{b}}" }, "result_var": "b" } ',
            "End"
        ]
    )

run()