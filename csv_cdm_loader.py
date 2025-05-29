import pandas as pd
import zipfile
import tempfile
import pathlib

# Full set of CDM + Oncology Extension tables to load
TABLES = [
    "person",
    "visit",                  # your existing visit table
    "condition",              # condition_occurrence
    "drug_exposure",
    "measurement",
    "procedure_occurrence",   # for RT start/end events
    "observation",            # for TNM, performance status, etc.
    "care_site",              # for reporting_site
    "death",                  # for death_date
    "episode",                # oncology courses
    "episode_event",          # links courses → events
]

def load_zip(path: str) -> dict[str, pd.DataFrame]:
    """Extract a CDM .zip and return a dict of {table_name: DataFrame}."""
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        z.extractall(tmp)

    folder = pathlib.Path(tmp)
    dfs: dict[str, pd.DataFrame] = {}
    for tbl in TABLES:
        fp = folder / f"{tbl}.csv"
        if fp.exists():
            # read everything in as strings to avoid dtype surprises
            dfs[tbl] = pd.read_csv(fp, dtype=str)
        else:
            # if the file is missing, create an empty frame
            dfs[tbl] = pd.DataFrame()
    return dfs
