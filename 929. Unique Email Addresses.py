class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = {}
        for email in emails:
            [local,domain] = email.split("@")
            local.replace(".", "")
            i = 0
            uniq = ""
            while i < len(local):
                if(local[i]=="+"):
                    break
                elif local[i] != ".":
                    uniq+= local[i]
                i+=1
            actual = uniq +"@" + domain
            if l.get(actual,0) == 0:
                l[actual] = 1
        return sum(l.values())
