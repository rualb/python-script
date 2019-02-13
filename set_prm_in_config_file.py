
import sys
import getopt

import os
import shutil
from distutils import dir_util

__prod__ = 1

# script not started with -O (production) mode
if not __prod__:
    print("Prod mode:"+str(__prod__))


def main(argv):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    help = "script.py -p version -v 190201"
    prm = ""
    value = ""
    filename = ""
    if not __prod__:
        argv = ["-f", dir_path+"/ava.config", "-p", "version", "-v", "190212"]
    try:
        opts, args = getopt.getopt(
            argv, "hf:p:v:", ["file=", "prm=", "value="])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        ####
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-p", "--prm"):
            prm = arg
        elif opt in ("-v", "--value"):
            value = arg
        elif opt in ("-f", "--file"):
            filename = arg
        ####
    set_version(filename, prm, value)


def set_version(pFilename, pPrm, pValue):
    if not pFilename or not pPrm:
        print("Argument is empty")
        return

    content = None
    with open(pFilename) as f:
        content = f.readlines()

    changed = False
    content = [x.strip() for x in content]
    for indx, line in enumerate(content):  # i in range(len(content))
        if line.split(",")[0] == pPrm:
            changed = True
            if pValue:
                content[indx] = (pPrm+","+pValue)
                print("Parameter ["+line+"] changed to ["+content[indx]+"]")
            else:
                print("Parameter ["+line+"]")

    if not changed and pValue:
        content.append(pPrm+","+pValue)
        print("Parameter ["+content[-1]+"] added")

    with open(pFilename, "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main(sys.argv[1:])#script path first arg
