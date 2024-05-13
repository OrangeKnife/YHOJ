import sys
import importlib.util
import json
class MainEntry:
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.info_json = None
    def run(self):
        spec = importlib.util.spec_from_file_location("module.name", self.file_path + "/entry.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    def info(self):
        if self.info_json == None:    
            with open( self.file_path + "/info.json", 'r') as file:
                self.info_json = json.load(file)
        return self.info_json
 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("requires folder name inside scripts")
        sys.exit(1)
    
    file_path = f"../scripts/{sys.argv[1]}"
    entry = MainEntry(file_path)
    #print(entry.info()["desc"], "by",entry.info()["author"])
    entry.run()