class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        conditionsmet = 0
        chars = [['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'], ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'], ['0','1','2','3','4','5','6','7','8','9'], ["!","@","#","$","%","^","&","*","(",")","-","+"]]
        if len(password) >= 8:
            conditionsmet += 1
        lowerSwitch = False
        upperSwitch = False
        digitSwitch = False
        specialSwitch = False
        for i in range(len(password)):
            if password[i] in chars[0] and lowerSwitch == False:
                conditionsmet +=1
                lowerSwitch = True
            if password[i] in chars[1] and upperSwitch == False:
                conditionsmet +=1
                upperSwitch = True
            if password[i] in chars[2] and digitSwitch == False:
                conditionsmet +=1
                digitSwitch = True
            if password[i] in chars[3] and specialSwitch == False:
                conditionsmet +=1
                specialSwitch = True
            if i < len(password) -1:
                if password[i] == password[i+1]:
                    return False
        if conditionsmet >= 5:
            return True
        return False