# Tag: string
class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        pre = " "
        # only when the previous element is not " ", the current " " can count
        for i in s:
            if i ==" " and (pre != " "):
                count += 1
            pre = i

        t = s.replace(" ","")
        # t to judge if it is all space 
        # pre in elif, to judge the last element whether it is " "
        if not t:
            return 0
        elif pre is not " ":
            return count + 1
        else:
            return count