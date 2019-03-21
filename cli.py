#!/usr/bin/python

import sys
import getopt
import colorama
from tlslabs.analyzer.connectivity import get_https_server_info
from tlslabs.analyzer.ciphers import ciphers_validator


if __name__ == "__main__":
    hostname = "google.com"
    server_info = get_https_server_info(hostname)
    colorama.init()
    ciphers_validator(server_info)
