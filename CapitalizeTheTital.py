class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        new = []
        for i in title:
            if len(i)<3:
                i = i.lower()
                new.append(i)
            else:
                i = i.lower()
                val = i[0]
                val = val.upper()
                i = val + i[1:]
                new.append(i)
        return ' '.join(new)
