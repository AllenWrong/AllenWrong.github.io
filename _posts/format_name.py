import os
import re
import time


def get_md_files():
    files = os.listdir("./")
    md_files = []
    for file in files:
        if file.find(".md") != -1:
            md_files.append(file)
    return md_files
    
    
def check_match(md_files):
    pattern = "^\d{4}-\d{2}-\d{2}-(.*)$"
    not_match_name = []
    for file in md_files:
        if not re.match(pattern, file):
            not_match_name.append(file)
    return not_match_name
    
    
def time_stamp_to_time(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d',timeStruct)
    

def rename(md_files):
    
    not_match_names = check_match(md_files)
    
    for file in not_match_names:
        create_time = time_stamp_to_time(os.path.getmtime(file))
        new_name = create_time + "-" + file
        os.rename(file, new_name)
    print(f"format name done! changed {len(not_match_names)} names")


rename(get_md_files())