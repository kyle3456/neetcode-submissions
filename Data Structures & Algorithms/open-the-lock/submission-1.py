class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque([("0000", 0)])
        s = set(deadends)
        def do(lock):
            res = []
            for i in range(4):
                curr = int(lock[i])
                if curr == 9:
                    curr = 0
                else:
                    curr += 1
                tmp = lock[:i] + str(curr) + lock[i + 1:]
                res.append(tmp)
                curr = int(lock[i])
                if curr == 0:
                    curr = 9
                else:
                    curr -= 1
                tmp = lock[:i] + str(curr) + lock[i + 1:]
                res.append(tmp)

            return res
        

        while q:
            for i in range(len(q)):
                curr, turn = q.popleft() 
                if curr == target:
                    return turn
                r = do(curr)
                for j in r:
                    if j not in s:
                        s.add(j)
                        q.append([j, turn + 1])
        
        return -1