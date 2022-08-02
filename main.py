import yaml_manager as ym

TEST_YAML_PATH = r'.\testyaml\ntfs.yaml'

def read_test():
    contents = ym.read_yaml(TEST_YAML_PATH)

    for content in contents:
        print content
        print "\n"

def test():
    read_test()
    return


if __name__ == "__main__":
    test()
