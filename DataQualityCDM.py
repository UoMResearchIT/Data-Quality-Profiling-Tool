import pandas as pd
from checks_onco import ALL_ONCO_CHECKS

class DataQualityCDM:
    """Runs core DataQuality on every table + extra oncology rules."""
    def __init__(self, tables: dict[str,pd.DataFrame], dq_cls):
        self.tables = tables
        self.dq_cls = dq_cls       # existing DataQuality class

        prefixed = []
        for tbl, df in tables.items():
            df2 = df.copy()
            df2.columns = [f"{tbl}_{col}" for col in df.columns]
            prefixed.append(df2)
        flat = pd.concat(prefixed, axis=1) if prefixed else pd.DataFrame()
        self.base = dq_cls(flat)
        self.onco_results = None
    
    def set_test_params(self, *args, **kwargs):
        """Pass test-parameter calls straight through to the underlying DataQuality."""
        return self.base.set_test_params(*args, **kwargs)

    def run_all_metrics(self):
        self.base.run_all_metrics()
        self.onco_results = {name: fn(self.tables) for name, fn in ALL_ONCO_CHECKS}

    # expose what the UI already expects
    def raw_results(self):
        return self.base.raw_results()

    def aggregate_results(self, *a, **kw):
        base = self.base.aggregate_results(*a, **kw)
        # append oncology rules as extra rows
        onco_df = pd.DataFrame({
            "field": ["episode_level"]*len(self.onco_results),
            **{k:[v] for k,v in self.onco_results.items()}
        })
        return pd.concat([base, onco_df], ignore_index=True)
