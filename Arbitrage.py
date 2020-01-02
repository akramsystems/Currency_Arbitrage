'''
Currency Table where R[i][j]
represents the exchange from currency
c[i] to currency c[j]
'''
R = [   [1,         49,     90],\
        [1/50,      1,       2], \
        [0.0107,    0.4,     1]  ]


def bellmanford(s,R):
    dist,prev,edges = [],[],[]

    for u in range(len(R)):
        dist.append(1/(R[s][u]))
        prev.append(s)
        for v in range(len(R)):
            edges.append([u,v])

    for i in range(len(R)):
        for u,v in edges:
            if dist[v] > dist[u] * (1/(R[u][v])):
                dist[v] = dist[u] * (1/(R[u][v]))
                prev[v] = u


    conversion_list = []
    
    print(prev)
    if dist[s] < 1:
        v = s
        while v not in conversion_list:
            conversion_list.append(v)
            v = prev[v]
        print(conversion_list)

        while conversion_list[0]!= v:
            conversion_list.pop(0)

        conversion_list.append(v)
        print(conversion_list)




    return


bellmanford(0,R)
