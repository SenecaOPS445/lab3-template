#!/usr/bin/env python3
# AuthorID: ddelgado
import subprocess
import sys
import os

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    df_return = p.communicate()
    stdout = df_return[0].decode('utf-8').strip()
    return stdout 
    
print(free_space())
