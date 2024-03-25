class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dlog, llog = [], []
        lexdict = defaultdict(list)
        for l in logs:
            log = l.split(" ")
            idf = log[0]
            if log[1].isdigit():
                dlog.append(l)
            else:
                del log[0]
                m = " ".join(log)
                lexdict[m].append(l)
                llog.append(m)
        llog.sort()
        res = []
        for s in llog:
            if len(lexdict[s]) > 1:
                lexdict[s].sort(key = lambda x:x[0])
                res.append(lexdict[s][0])
                del lexdict[s][0]
            else:
                res.append(lexdict[s][0])
        for d in dlog:
            res.append(d)
        return res