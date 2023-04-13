import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest

chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p = 0.01
    z_stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], value=0, alternative='smaller')
    z_crit = np.abs(norm.ppf(p))
    if z_stat < -z_crit:
        return True
    else:
        return False
