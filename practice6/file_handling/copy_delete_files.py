from shutil import copy
import os
# os.mkdir("reserve")
os.remove("../demofile.txt")
copy("../demofile.txt", "reserve/demofile.txt")
