"""Unified AFM/AFA feature fusion layer."""
def build_feature_tensor(core=None,predictive=None,synastry=None,financial=None):
    return {
        "core": core or {},
        "predictive": predictive or {},
        "synastry": synastry or {},
        "financial": financial or {},
    }
