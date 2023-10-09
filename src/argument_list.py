from dataclasses import dataclass

@dataclass
class arguments:

    mappingRule  = "direct"
    sourcePattern  = "*"
    targetPattern  = "*"
    sourceFolder = "./"
    targetFolder = "./"
    subs = ""
    subsPattern= ""