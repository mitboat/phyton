#!/usr/bin/env python3

import sys
import subprocess
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print("========= Phyton Compiler")
    print(sys.version)
    print()
    
    if len(sys.argv) != 2:
        print("  [!] Please specify the Phyton file to compile!")
        sys.exit(-1)

    try:
        subprocess.run(['unrtf', '--help'])
    except FileNotFoundError:
        print("  [!] unrtf needs to be installed on your system.")
        sys.exit(-1)
        
    html = subprocess.check_output(['unrtf', sys.argv[1]])
    src = BeautifulSoup(html, 'html.parser')
