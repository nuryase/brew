import json
import logging
import time
import sys
from eparser import Parser
from handler import EPUBHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Read from data.json
# Parse using the filename + filepath --> First check if the name folder exists in epubs
# If so, go to the next filename + filepath in the JSON


# After parsing, update the .JSON file line with the parsed contents
def epub_parser(data):
    handler = EPUBHandler(data["filepath"], data["filename"])

    handler.extract_epub()
    parser = Parser(handler.get_chapters(), handler.current_path())
    contents = parser.parse_xhtml()

    # Update data
    # data.update({"contents": contents})

    with open("./application/eparser/data.json", "r") as json_file:
        json_data = json.load(json_file)

    new_data = json_data[-1]

    new_data["contents"] = contents

    with open("./application/eparser/parsed_data.json", "r") as json_parsed_file:
        parsed_data = json.load(json_parsed_file)

    parsed_data.append(new_data)
    with open("./application/eparser/parsed_data.json", "w") as json_parsed_file:
        json.dump(parsed_data, json_parsed_file, indent=2)
    # Update JSON
    # for index in range(len(json_data)):
    # print("Second Test: ", json_data[index])
    # if json_data[index]["filename"] == data["filename"]:
    # print("Test 1: ", json_data[index]["filename"])
    # print("Test 2: ", data["filename"])
    # json_data[index]["contents"] = contents
    # with open("./application/backend/data.json", "w") as json_data_file:
    # json.dump(json_data, json_data_file, indent=2)
    # with open(
    # "./application/backend/parsed_data.json", "w"
    # ) as json_parsed_file:
    # json.dump(json_data, json_parsed_file, indent=2)
    # print(json_data)
    # json.dump(json_data[i].update({"contents": contents}), file)
    # file.close()
    # json_data[i].update({"contents": contents})
    # print("Third Test: ", json_data[0])
    # Add to the specific file --> if filename == data['filename], output = {filename: ORV, filepath: path, contents: --}
    # json_file.close()
    return  # contents


class MonitorJSON(FileSystemEventHandler):
    def on_modified(self, event):
        file = open(event.src_path)
        data = json.load(file)
        epub_parser(data[-1])
        print(data[-1])
        # print(event.src_path, event.event_type)
        # print("ADDITION: ", data[-1])


if __name__ == "__main__":
    src_path = "./application/eparser/data.json"

    event_handler = MonitorJSON()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started...")
    observer.start()
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
