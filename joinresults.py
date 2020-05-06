import sys
import os

path = sys.argv[1]

out_filename = "wos\\2020-05\\WoS_" + sys.argv[2] + "_final.txt"

file_list = os.listdir(path)

with open(out_filename, "wb") as outfile:
    for f in file_list:
        with open((path + "\\" + f), "rb") as infile:
            outfile.write(infile.read())