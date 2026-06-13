import pandas as pd
import numpy as np


def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add change, % change, and composite Impact_Score columns.

    Input columns required: Clicks_Before/After, Impressions_Before/After,
                            CTR_Before/After, Position_Before/After
    Added columns: *_Change, *_Pct, Pos_Score, Impact_Score
    """
    df = df.copy()

    for metric in ['Clicks', 'Impressions', 'CTR']:
        before = df[f'{metric}_Before'].astype(float)
        after = df[f'{metric}_After'].astype(float)
        df[f'{metric}_Change'] = (after - before).round(4)
        safe_before = before.replace(0, np.nan)
        df[f'{metric}_Pct'] = ((after - before) / safe_before * 100).fillna(0).round(2)

    pos_before = df['Position_Before'].astype(float)
    pos_after = df['Position_After'].astype(float)
    df['Pos_Change'] = (pos_after - pos_before).round(2)
    safe_pos = pos_before.replace(0, np.nan)
    df['Pos_Pct'] = ((pos_after - pos_before) / safe_pos * 100).fillna(0).round(2)
    df['Pos_Score'] = (-df['Pos_Pct']).round(2)  # Inverted: lower position number = positive

    df['Impact_Score'] = (
        df['Clicks_Pct'] * 0.40
        + df['Impressions_Pct'] * 0.30
        + df['Pos_Score'] * 0.20
        + df['CTR_Pct'] * 0.10
    ).round(2)

    return df
