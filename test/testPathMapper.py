
#  Arg Test

import utlis.pathmap as pm

args_1 = {
    "mappingRule": "direct",
    "src": "*",
    "tgt": "/a/b/c",
    "src_pattern": None,
    "tgt_pattern": None,
}


print(pm.mapper(args_1).map("some_address"))

