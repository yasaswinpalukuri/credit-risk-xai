import pandas as pd
import numpy as np

def calc_woe_iv(df, feature, target):
    lst = []
    for val in df[feature].unique():
        total = df[df[feature] == val].shape[0]
        good = df[(df[feature] == val) & (df[target] == 0)].shape[0]
        bad = df[(df[feature] == val) & (df[target] == 1)].shape[0]

        dist_good = good / (df[target] == 0).sum()
        dist_bad = bad / (df[target] == 1).sum()

        woe = np.log((dist_good + 0.0001) / (dist_bad + 0.0001))
        iv = (dist_good - dist_bad) * woe

        lst.append({
            'Value': val,
            'Good': good,
            'Bad': bad,
            'WoE': woe,
            'IV': iv
        })

    df_woe = pd.DataFrame(lst)
    total_iv = df_woe['IV'].sum()
    return df_woe.sort_values(by='WoE'), total_iv