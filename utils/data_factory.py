import json
class JsonReader:

    def read_json_file(self, file):
        with open(file) as data_file:
            return json.load(data_file)