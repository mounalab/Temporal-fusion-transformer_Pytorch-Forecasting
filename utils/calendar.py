from typing import List, Union
import numpy as np
import pandas as pd

CALENDAR_CYCLES = {
    "weekday": 7,
    "week": 52,
    "month": 12,
}

def add_cyclical_calendar_features(df: pd.DataFrame, features: Union[str, List[str]]):
    """Cyclical encoding of calendar features
    NOTE datetime column must be set as index """

    if isinstance(features, str):
        features = [features]

    for feat in features:
        assert (
            feat in CALENDAR_CYCLES.keys()
        ), f"Cyclical encoding is not available for {feat}"
       
        values = getattr(df.index, feat)
        df[f"{feat}_sin"] = np.sin(2 * np.pi * values / CALENDAR_CYCLES[feat])
        df[f"{feat}_cos"] = np.cos(2 * np.pi * values / CALENDAR_CYCLES[feat])

    return df