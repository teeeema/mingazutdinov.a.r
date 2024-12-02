import csv
import subprocess
import sys
from dependency_visualizer import visualize_dependencies

def load_config(file_path):
    with open(file_path, 'r') as config_file:
        reader = csv.DictReader(config_file)
        return next(reader)

def main(config_path):
    config = load_config(config_path)
    
    visualize_dependencies(
        package_name=config['package_name'],
        output_file=config['output_file'],
        max_depth=int(config['max_depth']),
        visualization_tool_path=config['visualization_tool_path'],
        repo_url=config['repo_url']
    )

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config.csv>")
        sys.exit(1)

    main(sys.argv[1])
