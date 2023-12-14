from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    specs_dict = defaultdict(list)
    for spec, name in specializations:
        specs_dict[spec].append(name)
    return dict(specs_dict)


# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
