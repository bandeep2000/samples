import yaml
import logging
import pytest

"""
parser = argparse.ArgumentParser()

parser.add_argument('-c', action='store', dest='configfile',required = True,
                        help='image uri to test')
results = parser.parse_args()
configfile = results.configfile
"""


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
def parse_yml(yaml_file_path):
    """
    Inputs: file path
    Returns:
    Dictionary parsed
    """
    try:
        config_details_stream = file(yaml_file_path, 'r') 
    except:
        logging.error("File doensn't seem to be  present in path '%s'"%yaml_file_path)
        raise
    config_details = yaml.load(config_details_stream)
    return config_details

def test_yaml_correct():
    """
     tests return value in dict
    """
    assert type(parse_yml('test.yml')) is dict


def test_yaml_correct1():
    """
    tests IOError exception is raised
    """
    with pytest.raises(IOError):
      parse_yml('test1.yml')


def test_yaml_correct2():
    """
     tests pytest excpeption is raised
    """
    with pytest.raises(AssertionError):
      assert type(parse_yml('test_incorrect.yml')) is dict
