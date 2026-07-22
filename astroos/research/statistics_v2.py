"""Strict statistical validation utilities for astronomical hypothesis research."""
import math,random

def fisher_z(r): return .5*math.log((1+r)/(1-r)) if abs(r)<1 else math.copysign(float('inf'),r)
def pearson(x,y):
    n=len(x); mx=sum(x)/n; my=sum(y)/n; a=sum((u-mx)*(v-my) for u,v in zip(x,y)); b=math.sqrt(sum((u-mx)**2 for u in x)*sum((v-my)**2 for v in y)); return a/b if b else 0

def permutation_correlation(x,y,iters=5000,seed=42):
    rng=random.Random(seed); observed=abs(pearson(x,y)); hits=0; yy=list(y)
    for _ in range(iters): rng.shuffle(yy); hits += abs(pearson(x,yy))>=observed
    return {'r':pearson(x,y),'p':(hits+1)/(iters+1),'iterations':iters,'seed':seed}

def bootstrap_effect(x,y,iters=5000,seed=42):
    rng=random.Random(seed); n=min(len(x),len(y)); effects=[]
    for _ in range(iters):
        idx=[rng.randrange(n) for _ in range(n)]; effects.append(sum(x[i]-y[i] for i in idx)/n)
    effects.sort(); return {'effect':sum(x[i]-y[i] for i in range(n))/n,'ci95_low':effects[int(.025*iters)],'ci95_high':effects[int(.975*iters)]}

def benjamini_hochberg(pvalues,q=.05):
    ranked=sorted(enumerate(pvalues),key=lambda z:z[1]); cutoff=-1
    for rank,(idx,p) in enumerate(ranked,1):
        if p<=q*rank/len(pvalues): cutoff=rank
    return [idx for rank,(idx,p) in enumerate(ranked,1) if rank<=cutoff]

def validate_oos(effect,p_value,ci_low,replications,regime_robust,correction_pass):
    return {'validated':effect>0 and p_value<.05 and ci_low>0 and replications>=3 and regime_robust and correction_pass}
