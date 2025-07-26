# 1~45까지 숫자 중 중복되지 않은 6개 숫자 출력

import random

def lotto_number():
    l = range(1,46)
    lotto = sorted(random.sample(l,6))
    return(lotto)