class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(set)
        f = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                value = accounts[i][j]
                d[i].add(value)
                f[value].append(i)
        visited = set()
        
        def dfs(i, emails):
            visited.add(i)
            for email in d[i]:
                emails.add(email)
                for j in f[email]:
                    if j not in visited:
                        dfs(j, emails)

        res = []
        for i in range(len(accounts)):
            if i not in visited:
                emails = set()
                dfs(i, emails)
                res.append([accounts[i][0]] + sorted(emails))
        return res

