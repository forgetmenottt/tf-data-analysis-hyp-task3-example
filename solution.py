import pandas as pd
import numpy as np
from statsmodels. stats.weightstats import ztest as ztest


chat_id = 1372197133 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.1
    test_stat, p_value = ztest(x, value= 500 )
    if (p_value < alpha):
        a = True
    else:
        a = False
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return a # Ваш ответ, True или False
