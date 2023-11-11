class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        map = {}
        res = []
        for [elm1, elm2] in adjacentPairs:
            if elm1 not in map:
                map[elm1] = []
            map[elm1].append(elm2)
            if elm2 not in map:
                map[elm2] = []
            map[elm2].append(elm1)
        print(map)
        
        firstElm = ''
        for elm in map:
            if(len(map[elm]) == 1):
                firstElm = elm
                break
        
        queue = []
        queue.append(firstElm)
        visited = set()
        while(queue):
            elm = queue.pop()
            res.append(int(elm))
            visited.add(elm)
            for adjElm in map[elm]:
                if adjElm not in visited:
                    queue.append(adjElm)
        return res
        