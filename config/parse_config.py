from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import yaml
from easydict import EasyDict as easydict

# TODO: Add in default values
def add_defaults(cfg):
    return cfg

def parse_config_file(path_to_config):

    with open(path_to_config) as f:
        cfg = yaml.load(f)

    return easydict(cfg)