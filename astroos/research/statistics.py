"""Research-grade statistical controls for hypothesis evaluation."""
import random,math

def benjamini_hochberg(pvalues,q=.05):
    order=sorted(range(len(pvalues)),key=lambda i:pvalues[i]); m=len(pvalues); cutoff=None
    for rank,i in enumerate(order,1):
        if pvalues[i] <= q*rank/m: cutoff=i
    return {'rejected':[i for i,p in enumerate(pvalues) if cutoff is not None and p<=pvalues[cutoff]],'q':q}

def permutation_test(x,y,iterations=2000,seed=42):
    rng=random.Random(seed); observed=abs(sum(x)/len(x)-sum(y)/len(y)); pooled=x+y; n=len(x); count=0
    for _ in range(iterations):
        rng.shuffle(pooled); count += abs(sum(pooled[:n])/n-sum(pooled[n:])/len(y))>=observed
    return {'observed':observed,'p_value':(count+1)/(iterations+1),'iterations':iterations,'seed':seed}

def bootstrap_mean(values,iterations=2000,seed=42):
    rng=random.Random(seed); n=len(values); means=[]
    for _ in range(iterations): means.append(sum(rng.choice(values) for _ in range(n))/n)
    means.sort(); return {'mean':sum(values)/n,'ci95':(means[int(.025*iterations)],means[int(.975*iterations)])}

def purged_embargo_split(n,train_end,test_start,test_end,embargo=0):
    train=list(range(0,max(0,train_end))); test=list(range(test_start,min(n,test_end))); train=[i for i in train if i<test_start-embargo]; return train,test

def regime_metrics(records,regime_key='regime'):
    out={}
    for r in records: out.setdefault(r[regime_key],[]).append(r)
    return {k:{'n':len(v),'mean_effect':sum(x.get('effect',0) for x in v)/len(v)} for k,v in out.items()}
