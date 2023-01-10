#!/usr/bin/env python3

import os
import sys
from configparser import ConfigParser

config_file = sys.argv[1]
config_section = sys.argv[2]

config = ConfigParser()
config.read(config_file)
for config_var in sys.argv[3:]:
    config.set(config_section, config_var, os.environ[config_var])

with open(config_file, 'w') as config_file_handler:
    config.write(config_file_handler)
