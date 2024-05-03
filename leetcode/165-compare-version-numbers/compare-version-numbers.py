class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def get_list(version):
            return list(map(int,version.split(".")))
        
        v1 = get_list(version1)
        v2 = get_list(version2)

        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)
        
        for n1, n2 in zip(v1,v2):
            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        return 0