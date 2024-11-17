import config
import os
from os import system as cmd
import subprocess
import re
from sys import argv

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

INFO = '\x1b[34m[INFO]\x1b[0m'
ERROR = '\x1b[31m[ERROR]\x1b[0m'
WARNING = '\x1b[33m[WARNING]\x1b[0m'

if len(argv) != 2:
    print(f'{ERROR} Invalid command usage: leosync <pull | push>')
    exit(-1)

git_output = run(['git', '-v'])

if git_output.returncode != 0:
    print(f'{ERROR} Please install git: \x1b[4mhttps://git-scm.com\x1b[0m')
    exit(-1)

git_version = re.findall(r'\d.\d+.\d', git_output.stdout)[0]

print(f'{INFO} Using Git version \x1b[32m{git_version}\x1b[0m')

def pull():
    if os.path.exists(config.PATH):
        print(f'{INFO} Pulling')
        prev = os.getcwd()
        os.chdir(config.PATH)
        os.chdir(prev)
        run(['git', 'pull'])
    else:
        print(f'{INFO} Cloning')
        run(['git', 'clone', config.REPO])

def push():
    print(f'{INFO} Pushing')
    prev = os.getcwd()
    os.chdir(config.PATH)
    os.chdir(prev)
    cmd('git add -A')
    cmd('git commit -am "Sync"')
    cmd('git push')

if argv[1] == 'pull':
    pull()
elif argv[1] == 'push':
    push()
elif argv[1] == 'sync':
    print(f'{INFO} Syncing')
    pull()
    push()
else:
    print(f'{ERROR} Invalid command usage: leosync <pull | push>')
    exit(-1)