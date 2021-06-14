class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = {}
        count = 0
        for i in list1:
            d1[i] = count
            count += 1
        count = 0
        for i in list2:
            if i in d1:
                d2[i] = count + d1[i]
            count +=1

        temp = min(d2.values())
        res = [key for key in d2 if d2[key] == temp]
        # res.append(min(d2.keys(), key=lambda k: d2[k]) <- this could only take one item of min
        return res