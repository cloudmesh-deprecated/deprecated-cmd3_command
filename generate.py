#! /usr/bin/env python

import os


data = {'command': 'uebercool',
        'module': 'cloudmesh_uebercool'}


def replace(filename, data):
    if filename is None or filename == "":
        return
    print "Converting:", filename
    # read content
    with open(filename, 'r') as f:
        content = str(f.readlines())
    # replace content
    content = content.format(**data)
    # write content back to file
    with open(filename, 'w') as f:
        f.write(content)

def replace_string(filename, data):
    if filename is None or filename == "":
        return
    print "Converting:", filename
    # read content
    with open(filename, 'r') as f:
        content = str(f.readlines())
    # replace content
    for key in data:
        old = "{" + key +"}"
        new = data[key]
    content = content.replace(old, new)
    # write content back to file
    with open(filename, 'w') as f:
        f.write(content)


# BUG check if dir exists
script = """
    rm -rf {module}
    cp -rf cmd3_template {module}
    mv {module}/cmd3_template {module}/{module}
    mv {module}/{module}/command_command.py {module}/{module}/command_{command}.py
    mv {module}/{module}/plugins/cm_shell_command.py {module}/{module}/plugins/cm_shell_{command}.py
    """.format(**data)

for line in script.split("\n"):
    line = line.strip()
    print line
    os.system(line)

files = """
   {module}/setup.py
   {module}/Makefile
   {module}/{module}/plugins/cm_shell_{command}.py
   {module}/{module}/command_{command}.py
   """.format(**data)

for filename in files.split("\n"):
    filename = filename.strip()
    print filename
    replace_string(filename, data)

