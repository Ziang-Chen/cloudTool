# Automator CLI entrence
# Author: Zhang Chen
# CLI: python automator.py --help for more information


from src.setting import *
from tools.rename_cli import parser
from utlis.pathmap import mapper
from src.fileoperation import file, folder
from src.path import path

from src.argument_list import arguments


def rename(args: arguments):
    #this is the rename function
    # 1. get the file list
    # 2. map the file list
    # 3. rename the file list
    # 4. return
    if args.mappingRule == "nothing":
        return
    baseFolder = folder(arguments.sourceFolder)
    fs = baseFolder.path.iterator_on_same_level(arguments.sourcePattern)
    m = mapper(args)

    if IS_DEBUG:
        for f_ in fs:
            f = str(f_)
            print("file name:", f)
            print("renamed to:", m.map(f))
            return
    #### after debugg correct using file object to rename


def deliver(args: arguments):
    # first copy then rename
    # 1. get the file list
    # 2. copy the file list
    # 3. rename the file list
    # 4. return
    baseFolder = folder(arguments.sourceFolder)
    fs = baseFolder.path.iterator_on_same_level(arguments.sourcePattern)

    for f_ in fs:
        file(f_).deliver(path(args.targetFolder))

    args.sourceFolder = args.targetFolder
    rename(args)


def main():
    # main function
    # 1. get the arguments
    args_ = parser.parse_args()
    arguments.sourcePattern = args_.sP
    arguments.targetPattern = args_.tP
    arguments.mappingRule = args_.mappingRule
    arguments.sourceFolder = args_.sF
    arguments.targetFolder = args_.tF
    arguments.subs = args_.sub
    arguments.subsPattern = args_.bP

    # 2. rename or deliver
    if IS_DEBUG:
        import pprint

        pprint.pp(args_)
        # return 0
    if arguments.sourceFolder == arguments.targetFolder:
        rename(arguments)
    else:
        deliver(arguments)

    # sF = folder(arguments.sourceFolder)
    # tF = folder(arguments.targetFolder)


if __name__ == "__main__":
    main()
