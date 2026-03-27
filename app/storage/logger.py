


import json
import os

LOG_PATH = "data/logs.json"

class Logger:

    def log(self, data):
        if not os.path.exists(LOG_PATH):
            with open(LOG_PATH, "w") as f:
                json.dump([], f)

        with open(LOG_PATH, "r") as f:
            logs = json.load(f)

        logs.append(data)

        with open(LOG_PATH, "w") as f:
            json.dump(logs, f, indent=2)