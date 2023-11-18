from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
   d = sorted(d.items(), key=lambda item: item[1], reverse=True)
   res = [x[0] for x in d]
   return res


# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)
