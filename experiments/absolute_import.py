import importlib.util 

def import_from_path(module_name, file_path):
    # Load the module specification
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    # Create a new module based on the specification
    module = importlib.util.module_from_spec(spec)
    # Execute the module in its own namespace
    spec.loader.exec_module(module)
    return module

# Absolute path to the Python file
file_path = "/home/jf01/dev/misc/python/example_module.py"

# Import the module
my_script = import_from_path("example_module", file_path)

# Use the imported module
my_script.greet()


