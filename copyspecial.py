#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "knmarvel"


def get_special_paths(dir):
    """takes a directory and returns a list of the absolute
    paths of the special files in the given directory"""
    spec_paths = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if re.search("__(.+?)__", name):
                if os.path.join(os.path.abspath(dir), name) not in spec_paths:
                    spec_paths.append(os.path.join(os.path.abspath(dir), name))
                else:
                    return "ERROR"
    return spec_paths


def copy_to(paths, dir):
    """given a list of the paths, copy those files into the
    given directory"""
    for file in paths:
        shutil.copy(file, dir)


def zip_to(paths, dir):
    """given a list of paths, zip those files up into the
    given zipfile"""
    cmd = ["zip", "-j", dir] + paths
    subprocess.call(cmd)


def parsing():
    """parses arguments given as parameters in calling function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--fromdir', default='./')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    return parser.parse_args()


def main():
    """Calls all functions to return above listed results"""
    args = parsing()
    spec_paths = get_special_paths(args.fromdir)
    if spec_paths == "ERROR":
        print("Error: duplicate special files.")
        return "Error: duplicate special files."
    print("\n".join(spec_paths))

    if args.todir:
        copy_to(spec_paths, args.todir)

    if args.tozip:
        zip_to(spec_paths, args.tozip)


if __name__ == "__main__":
    main()
