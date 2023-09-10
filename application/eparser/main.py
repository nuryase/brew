import json
import time

from eparser import Parser
from handler import EPUBHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def epub_parser(data):
    handler = EPUBHandler(data["filepath"], data["filename"])

    handler.extract_epub()
    parser = Parser(handler.get_chapters(), handler.current_path())
    contents = parser.parse_xhtml()

    with open("./application/eparser/data.json", "r") as json_file:
        json_data = json.load(json_file)

    new_data = json_data[-1]

    new_data["contents"] = contents

    with open("./application/eparser/parsed_data.json", "r") as json_parsed_file:
        parsed_data = json.load(json_parsed_file)

    parsed_data.append(new_data)
    with open("./application/eparser/parsed_data.json", "w") as json_parsed_file:
        json.dump(parsed_data, json_parsed_file, indent=2)

    return


class MonitorJSON(FileSystemEventHandler):
    def on_modified(self, event):
        file = open(event.src_path)
        data = json.load(file)
        epub_parser(data[-1])
        print(data[-1])


if __name__ == "__main__":
    src_path = "./application/eparser/data.json"

    event_handler = MonitorJSON()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring...")
    observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
