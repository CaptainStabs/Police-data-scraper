import os
mydir = os.getcwd()
filelist = [ f for f in os.listdir(mydir) if f.endswith(".bak") ]
for f in filelist:
    os.remove(os.path.join(mydir, f))