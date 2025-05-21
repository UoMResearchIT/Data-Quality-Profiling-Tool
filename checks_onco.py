def duplicate_episode_event(dfs):
    ee = dfs["episode_event"]
    if ee.empty:
        return 0
    return ee.duplicated(["episode_id","event_table","event_id"]).sum()

def orphan_episode_event(dfs):
    ee, ep = dfs["episode_event"], dfs["episode"]
    if ee.empty or ep.empty:
        return 0
    return (ee.merge(ep[["episode_id"]],on="episode_id",how="left",indicator=True)
              .query("_merge=='left_only'").shape[0])

def episode_without_events(dfs):
    ee, ep = dfs["episode_event"], dfs["episode"]
    if ep.empty:
        return 0
    linked = set(ee["episode_id"])
    return ep[~ep["episode_id"].isin(linked)].shape[0]

ALL_ONCO_CHECKS = [
    ("Duplicate episode links", duplicate_episode_event),
    ("Orphan links", orphan_episode_event),
    ("Episodes with zero events", episode_without_events),
]
