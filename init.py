#!/usr/bin/python3
import os

def make_exec(file_name):
 exec_string = 'chmod +x '
 cwd = os.getcwd() + '/'
 cmd = exec_string + '"' + cwd + file_name + '"'
 os.system(cmd)

make_exec("install_dependencies.sh")
make_exec('install_dependencies.sh')
make_exec('uninstall_dependencies.sh')
make_exec('installer.sh')
make_exec('uninstaller.sh')
make_exec('run.sh')
make_exec('fdk.py')
make_exec('init.py')
make_exec('exit.py')

def first_run(file_name):
 cmd = "./" + file_name 
 os.system(cmd)

first_run("installer.sh")

def sec_run(file_name):
 cmd = "/usr/local/bin/" + file_name 
 os.system(cmd)

sec_run("install_dependencies.sh")

