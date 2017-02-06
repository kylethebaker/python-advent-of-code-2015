import re

input_re = re.compile(r""
                      r"^(?P<action>turn on|turn off|toggle) "
                      r"(?P<start>\d*,\d*) "
                      r"through "
                      r"(?P<end>\d*,\d*)$")

patterns = [
    "turn on 0,0 through 999,999",
    "toggle 0,0 through 999,0",
    "turn off 499,499 through 500,500"
]

for line in patterns:
    matches = input_re.match(line)
    print(matches.group("action"))
    print(matches.group("start"))
    print(matches.group("end"))
    print("----------------")
