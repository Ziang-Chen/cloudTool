# author: Ziang Chen
# this module is a built in path mapper system
# it can be used to map the path from one system to another
# the mapping rule is defined in the argument list

import re
from src.argument_list import arguments


class mapper:
    # address mapper class
    # this class is used to map the address from one system to another
    def __init__(self, args: arguments):
        self.rule = ruler(args.mappingRule, args)

    def map(self, src):
        # map the address
        return self.rule.getHandler()(src)

    def batchMapping(self, src_list):
        # batch mapping
        # src_list: list of source address
        # return: list of target address
        handler = self.rule.getHandler()
        r = list()
        for s in src_list:
            r.append(handler(s))
        return r


class ruler:
    # rule class
    def __init__(self, name, args: arguments):
        ### map with different rul system
        self.name = name
        if name == "regExp":
            #  P(S)/O -> T

            # storage pattern
            self.src = args.sourcePattern
            self.tgt = args.subs

            # compile and return enclose function
            self.pattern = re.compile(self.src)

            def handler(sr_str):
                return self.pattern.sub(self.tgt, sr_str)

            self.handler = handler

        elif name == "dualReg":
            # P_1(S)/ P_2(s) -> T
            

            self.src_pattern = args.sourcePattern
            self.tgt_pattern = args.targetPattern
            self.srcP = re.compile(self.src_pattern)
            self.tgtP = re.compile(self.tgt_pattern)

            def handler(sr_str):
                return self.srcP.sub(
                    lambda a: re.match(self.tgt_pattern, a).group(), sr_str
                )

            self.handler = handler
        elif name == "super":
            # P_1(S)  / P_2 (S)  --> P_3 (S)
            # pattern 1 (source pattern) using to locate
            # pattern 2 (sub pattern) using to replace
            # pattern 3 (target pattern) using as axuliary

            def handler(sr_str: str):
                P1 = re.compile(args.sourcePattern)
                P2 = re.compile(args.subsPattern)
                P3 = args.targetPattern

                return sr_str.replace(
                    t := re.search(P1, sr_str).group(), re.sub(P2, P3, t)
                )

            self.handler = handler

        elif name == "direct":

            # direct mapping
            # P(S) -> T
            # P is the pattern
            # S is the source string
            # T is the target string
            def handler(sr_str):
                return args.targetPattern

            self.handler = handler

        elif name == "nothing":

            def handler(sr_str):
                return sr_str

            self.handler = handler

        else:
            raise UnboundLocalError

    def getHandler(self):
        # return the handler
        return self.handler

    def convert(self, source_str):
        # convert the source string
        return self.handler(source_str)
