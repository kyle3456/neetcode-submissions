class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for i in sorted(tickets, reverse = True):
            from_i, to_i = i
            d[from_i].append(to_i)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not d[curr]:
                res.append(stack.pop())
            else:
                stack.append(d[curr].pop())
        
        return res[::-1]
        

