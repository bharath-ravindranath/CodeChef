def cleanup(case):
    n, m = map(int, input().split())
    cJobs = {int(x) for x in input().split()}
    tJobs = {x for x in range(1,n+1)}
    rJobs = tJobs.difference(cJobs)
    chefJobs = []
    assistJobs = []
    for i, x in enumerate(rJobs):
        if i%2 == 1:
            assistJobs.append(x)
        else:
            chefJobs.append(x)
    
    print(*chefJobs, sep=' ')
    print(*assistJobs, sep=' ')

T = int(input())
for i in range(T):
    cleanup(i)
