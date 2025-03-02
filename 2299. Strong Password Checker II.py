class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        low = False
        upp = False
        dig = False
        spec = False
        dup = False
        for i,val in enumerate(password):
            asc = ord(val)
            if i < len(password)-1:
                if val == password[i+1]:
                    return False
            if asc >= 97  and asc<=122:
                low = True
            elif asc >=65 and asc <= 90:
                upp = True
            elif asc >=48 and asc <= 57:
                dig = True
            elif val in '!@#$%^&*()-+':
                spec = True
        if password[-1]==password[-2]:
            return False
        return low and upp and dig and spec
