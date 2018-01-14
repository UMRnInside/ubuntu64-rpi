#!/usr/bin/python3
#Filename:build.py
import os
print('updating list')
os.popen('apt update')
print('installing software')
os.popen('apt install git')
print('clone sources')
os.system('bash build_kernel.sh')
print('build finish, please run install.py')
