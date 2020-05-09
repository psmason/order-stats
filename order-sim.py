import numpy as np

# normal shape
DIST_AVG = 100
DIST_VAR = 10

# iterations
N = 100*1000

# top N sums to compute
TOP_N = [1, 2, 3, 5]

def simTopNSum(sampleSize):
    TOP_N_RESULTS = np.empty(shape=(0, len(TOP_N)))
    for i in range(N):
        a = np.sort(
            np.random.normal(loc=DIST_AVG,
                             scale=DIST_VAR,
                             size=sampleSize)
        )

        stats = np.empty(len(TOP_N))
        for j in range(len(TOP_N)):
            stats[j] = np.sum(a[-TOP_N[j]:])
        TOP_N_RESULTS = np.vstack((TOP_N_RESULTS, stats))

    # columnwise mean
    return TOP_N_RESULTS.mean(0)

def simTopNSumPareto(sampleSize):
    TOP_N_RESULTS = np.empty(shape=(0, len(TOP_N)))
    for i in range(N):
        a = np.sort(np.random.pareto(1, size=sampleSize))

        stats = np.empty(len(TOP_N))
        for j in range(len(TOP_N)):
            stats[j] = np.sum(a[-TOP_N[j]:])
        TOP_N_RESULTS = np.vstack((TOP_N_RESULTS, stats))

    # columnwise mean
    return TOP_N_RESULTS.mean(0)
    
print "30", simTopNSum(30)
print "60", simTopNSum(60)
print "100", simTopNSum(100)
print "200", simTopNSum(200)

print "pareto 30", simTopNSumPareto(30)
print "pareto 60", simTopNSumPareto(60)
print "pareto 100", simTopNSumPareto(100)
print "pareto 200", simTopNSumPareto(200)
                    

    
    
    
