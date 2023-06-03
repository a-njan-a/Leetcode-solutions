class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i in range(n):
            if manager[i] != -1 :
                graph[manager[i]].append(i)

        result = 0
        minutes = [(headID, 0)]

        while(minutes):
            node, curr = minutes.pop()
            curr += informTime[node]

            result = max(result, curr)

            for c in graph[node]:
                minutes.append((c, curr))

        return result


            
