import yaml_manager as ym
import random

TEST_YAML_PATH = r'.\testyaml\ntfs.yaml'
TEST_YAML_OUTPUT_PATH = r'.\testyaml\test'

TEST_DICT = [{
    'hello': 'world',
    'hi': ['123', '456', '789']
}, {
    'hello': 'world',
    'hi': ['123', '456', '789']
}]

def read_test():
    contents = ym.read_yaml(TEST_YAML_PATH)

    for content in contents:
        print content
        print "\n"

def write_test():
    path = TEST_YAML_OUTPUT_PATH + str(random.randrange(1,100)) + ".yaml"
    
    for d in TEST_DICT:
        ym.write_yaml(path, d)
        print d

def test():
    read_test()
    write_test()

if __name__ == "__main__":
    test()
