import pandas as pd


def classify_keywords(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add Status and Category columns.

    Status: GAINED | LOST | IMPROVED | DECLINED | FLAT  (based on clicks)
    Category: STRONG_POSITIVE | POSITIVE | WATCH | NEGATIVE  (based on Impact_Score)
    """
    df = df.copy()

    def _status(row) -> str:
        b, a = row['Clicks_Before'], row['Clicks_After']
        if b == 0 and a > 0:
            return 'GAINED'
        if b > 0 and a == 0:
            return 'LOST'
        if a > b:
            return 'IMPROVED'
        if a < b:
            return 'DECLINED'
        return 'FLAT'

    def _category(score: float) -> str:
        if score > 30:
            return 'STRONG_POSITIVE'
        if score >= 5:
            return 'POSITIVE'
        if score >= -10:
            return 'WATCH'
        return 'NEGATIVE'

    df['Status'] = df.apply(_status, axis=1)
    df['Category'] = df['Impact_Score'].apply(_category)
    return df
