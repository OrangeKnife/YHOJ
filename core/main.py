import sys
import importlib.util
class MainEntry:
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    def run(self):
        spec = importlib.util.spec_from_file_location("module.name", self.file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

if __name__ == "__main__":
    ##sys.argv  = ["test","scripts/print.py"]
    if len(sys.argv) != 2:
        sys.exit(1)
    
    entry = MainEntry(sys.argv[1])
    entry.run()