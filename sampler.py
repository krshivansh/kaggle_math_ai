import pandas as pd
import numpy as np
import random

qb = pd.read_csv("./question_bank_3.csv")
print(qb.shape , qb.columns)

random.seed(42)

n=50

random_indices = random.sample(range(len(qb)), n)
random_rows = qb.iloc[random_indices]
random_rows['id'] = range(1, len(random_rows) + 1)
print(random_rows.columns)

random_rows.to_csv('./super50.csv',index=False)





print(random_rows.shape)
