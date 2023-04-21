import pandas as pd

def check_na(df):
    """
    percentage of rows containing NaN data
    """
    return df.isna().sum() * 100 / len(df)

def get_missing_dates(df, freq= None, start_date=None, end_date=None):
    """
    get dates which are missing in the series
    """
    if start_date is None:
        start_date = df.index[0]

    if end_date is None:
        end_date = df.index[-1]

    if freq is None:
        freq = df.index.freq

    return pd.date_range(start=start_date, end=end_date, freq=freq).difference(df.index)
