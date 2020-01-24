#!/usr/bin/python3

## http://xahlee.info/python/system_calls.html

import subprocess

output = subprocess.check_output(['ls', '-all'])
print(output.decode("utf-8"))

exitCode = subprocess.check_output(['ls', '-all'])
print(exitCode)