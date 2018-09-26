import glob
import os


read_files = glob.glob(os.path.join("local/*.txt"))

with open("2018.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
    filelist = [ f for f in os.listdir("local") if f.endswith(".txt") ]
    for f in filelist:
        os.remove(os.path.join("local", f))
