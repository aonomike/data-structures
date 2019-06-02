attendance =  ('A', 'L', 'P')

def checkRecord(n: int) -> int:
        attendance = ('A', 'L', 'P')
        if n == 1:
            return len(attendance)
        a = []
        [ a.append(attendance) for i in range(n) ]
        import itertools
        possible = list(itertools.product(*a))
        unique_possible = list(map(lambda x: ''.join(x), possible))
        att = list(filter(lambda x: x.count('LLL') == 0 and x.count('A') < 2 , unique_possible))
        return (len(att)%(10**9+7))