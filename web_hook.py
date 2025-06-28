import pymsteams

from config.config import web_hook

teams_message = pymsteams.connectorcard(web_hook)
# teams_message.text("Hi! :) - Diana Rojas")
with open("reports/markdown/md_report.md") as f:
    report = f.read()

print(report)

teams_message.text(report)
teams_message.send()