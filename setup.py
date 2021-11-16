#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Harvey Wu

import os
import sys
import toml

name = r''
version = r''
edition = r''

# Read configuration file


def Read():
    global name, version, edition
    cfg = 'Cargo.toml'
    if not os.path.exists(cfg):
        input(cfg + ' not found')
        sys.exit(-1)
    with open(cfg, mode='rb') as f:
        content = f.read()
    dic = toml.loads(content.decode('utf8'))

    name = dic['name'].strip()
    if not os.path.exists(name):
        print('Error: not exists %s' % name)
        sys.exit(-1)
    print('name: %s' % name)

    version = dic['version'].strip()
    if not os.path.exists(version):
        print('Error: not exists %s' % version)
        sys.exit(-1)
    print('version: %s' % version)

    edition = dic['edition'].strip()
    if not os.path.exists(edition):
        print('Error: not exists %s' % edition)
        sys.exit(-1)
    print('edition: %s' % edition)

    print('Read config.toml successed!')


if __name__ == '__main__':
    Read()
