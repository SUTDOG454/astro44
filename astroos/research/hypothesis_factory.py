"""Ray-compatible hypothesis experiment factory."""
try:
    import ray
except ImportError:
    ray=None

def evaluate_hypothesis(hypothesis, dataset, evaluator):
    return evaluator(hypothesis,dataset)

def build_ray_task(evaluator):
    if ray is None:
        return evaluator
    return ray.remote(evaluator)

class HypothesisFactory:
    def __init__(self,evaluator): self.evaluator=evaluator
    def run(self,hypotheses,datasets):
        if ray is None:
            return [evaluate_hypothesis(h,d,self.evaluator) for h,d in zip(hypotheses,datasets)]
        remote_eval=ray.remote(self.evaluator)
        refs=[remote_eval.remote(h,d) for h,d in zip(hypotheses,datasets)]
        return ray.get(refs)
