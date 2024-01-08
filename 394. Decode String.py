class Solution:
    def decodeString(self, s: str) -> str:
        stacks = []
        string = ""
        value = 0
        for val in (s):
            if val == "[":
                stacks.append(string)
                stacks.append(value)
                string = ""
                value = 0
            elif val == "]":
                num = stacks.pop()
                prev = stacks.pop()
                string = prev + num * string
            elif val.isdigit():
                value = value*10 + int(val)
            else:
                string += val
        return string
