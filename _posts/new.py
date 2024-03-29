import sys
import time


def time_stamp_to_time(timestamp, more=False):
    timeStruct = time.localtime(timestamp)
    if more:
        return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
    return time.strftime('%Y-%m-%d',timeStruct)

    
def mkfile(file_name):
    header = f'---\n\
title: "{file_name}"\n\
excerpt: ""\n\
mathjax: false\n\
tags: "新文章在写"\n\
---'
    file_name = time_stamp_to_time(time.time()) + "-" + file_name + ".md"
    with open(file_name, "w") as f:
        print(header, file=f)
    print(f"'{file_name}' File created!")
    
    
def mkfiles(file_names):
    for file in file_names:
        mkfile(file)
        
        
mkfiles(sys.argv[1:])