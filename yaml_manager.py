import yaml
import sys

def read_yaml(path, all=True):
    try:
        with open(path, 'r') as f:
            contents = yaml.load_all(f, yaml.FullLoader) if all \
                else yaml.load(f, yaml.FullLoader)
            return list(contents) if all else [contents]
    except Exception as e:
        print e
        sys.exit(1)

def write_yaml(path, data, mode='a'):
    try:
        with open(path, mode) as f:
            yaml.dump(data, f, explicit_start=True)
    except Exception as e:
        print e
        sys.exit(1)
