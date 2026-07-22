"""Strict production promotion gate for research hypotheses."""
def strict_promotion_gate(metrics):
    required=['oos_effect','p_value','bootstrap_ci_low','bootstrap_ci_high','replications','regime_robust','multiple_testing_pass','permutation_pass','purged_split_pass']
    if any(k not in metrics for k in required): return {'status':'rejected','reason':'missing_validation_evidence'}
    passed=(metrics['oos_effect']>0 and metrics['bootstrap_ci_low']>0 and metrics['p_value']<.05 and metrics['replications']>=3 and metrics['regime_robust'] and metrics['multiple_testing_pass'] and metrics['permutation_pass'] and metrics['purged_split_pass'])
    return {'status':'validated' if passed else 'candidate','reason':'all_gates_passed' if passed else 'insufficient_robustness'}
