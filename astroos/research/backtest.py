"""Purged walk-forward backtesting primitives."""
from dataclasses import dataclass
import math

@dataclass
class BacktestResult:
    folds:list; aggregate:dict

def walk_forward(dataset,train_size,test_size,step=None):
    step=step or test_size; folds=[]; i=train_size
    while i+test_size<=len(dataset):
        folds.append((dataset[i-train_size:i],dataset[i:i+test_size])); i+=step
    return folds

def evaluate_predictions(y_true,y_pred):
    n=len(y_true)
    if not n:return {'n':0}
    mse=sum((a-b)**2 for a,b in zip(y_true,y_pred))/n
    mae=sum(abs(a-b) for a,b in zip(y_true,y_pred))/n
    mean=sum(y_true)/n; var=sum((x-mean)**2 for x in y_true)/n
    return {'n':n,'mse':mse,'mae':mae,'r2':1-(mse/var if var else math.inf)}

def run_walk_forward(dataset,trainer,predictor,train_size,test_size):
    results=[]
    for train,test in walk_forward(dataset,train_size,test_size):
        model=trainer(train); results.append(evaluate_predictions([x[1] for x in test],[predictor(model,x[0]) for x in test]))
    return BacktestResult(results,{'folds':len(results),'mean_mae':sum(x['mae'] for x in results)/len(results) if results else None})
