
# Cloud Tools CLI detail defination
# this file define the cli interface

import argparse



parser = argparse.ArgumentParser(
    prog="cloud automator", description="v 0.09 by Ziang Chen"
)
parser.add_argument(
    "--mappingRule",
    "--mR",
    "-r",
    default="direct",
    help=" select the mapping rule [refExp/dualReg] ",
    choices=["regExp", "dualReg", "direct", "super", "nothing"],
)

parser.add_argument(
    "--sub", "--subsition", default="new_name.mp4", help="substition word"
)

parser.add_argument("--bP", "--p2", 
                    "--SubstitionPattern", default=".*.mp4", help="substition pattern")

parser.add_argument("--sP", "--p1", 
                    "--SourcePattern", default=".*.mp4", help="source pattern ")

parser.add_argument("--tP", "--p3", 
                    "--TargetPattern", default="new.mp4", help="target pattern ")

parser.add_argument("--tF",
                    "--TargetFolder", default="./", help="target Folder ")

parser.add_argument("--sF", 
                    "--SourceFolder", default="./", help="source Folder ")


# parser.add_argument("-tgt_pattern", help="target pattern")
