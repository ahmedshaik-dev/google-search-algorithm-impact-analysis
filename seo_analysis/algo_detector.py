import pandas as pd


def detect_impact(df: pd.DataFrame, threshold: float = 15.0) -> pd.DataFrame:
    """
    Flag keywords as algo-affected if impressions OR clicks changed by more than threshold%.
    Adds 'Algo_Affected' boolean column.
    """
    df = df.copy()
    df['Algo_Affected'] = (
        (df['Impressions_Pct'].abs() > threshold)
        | (df['Clicks_Pct'].abs() > threshold)
    )
    return df


def calculate_severity(df: pd.DataFrame) -> str:
    """Return LOW / MEDIUM / HIGH based on % of keywords flagged as algo-affected."""
    total = len(df)
    if total == 0:
        return 'LOW'
    affected_pct = df['Algo_Affected'].sum() / total * 100
    if affected_pct > 30:
        return 'HIGH'
    if affected_pct >= 10:
        return 'MEDIUM'
    return 'LOW'


def build_algo_summary(df: pd.DataFrame) -> dict:
    """Return summary stats dict for the Algorithm_Impact sheet header."""
    affected = df[df['Algo_Affected']]
    gained = affected[affected['Impressions_Pct'] > 0]
    lost = affected[affected['Impressions_Pct'] <= 0]
    return {
        'total_keywords': len(df),
        'affected_count': len(affected),
        'affected_pct': round(len(affected) / len(df) * 100, 1) if len(df) > 0 else 0,
        'positive_count': len(gained),
        'negative_count': len(lost),
        'total_impression_impact': int(affected['Impressions_Change'].sum()),
        'severity': calculate_severity(df),
    }
