import json
import argparse
import os

parser = argparse.ArgumentParser(description='smpl to m3u')
parser.add_argument('filename',type=str,help='converting target(.smpl)')
args = parser.parse_args()
filename = args.filename
destination = os.path.splitext(filename)[0] + ".m3u8"
with open(filename,"r",encoding="utf-8") as json_file:
    jsstr = json.load(json_file)
    sorted_arr = sorted(jsstr["members"],key=lambda e:(e['order']))
with open(destination,"w",encoding="utf-8") as dest_file:
    dest_file.write("#EXTM3U\n")
    for i in sorted_arr:
        newstr = i["info"].replace("/storage/emulated/0/","D:\\").replace("/","\\")
        newstr += "\n"
        dest_file.write(newstr)