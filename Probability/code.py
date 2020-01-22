# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)

p_a = df[df.fico > 700] 
p_a = len(p_a) / df.purpose.count()
p_b = df[df.purpose == 'debt_consolidation'] 
p_b = len(p_b) / df.purpose.count()
df1 = df[df.purpose == 'debt_consolidation']
p_a_b = df[(df.purpose == 'debt_consolidation') & (df.fico > 700)]
p_a_b = len(p_a_b) / df.purpose.count()
result = p_a_b == p_a
print(result)
# code ends here


# --------------
# code starts here

prob_lp = df[df['paid.back.loan'] == 'Yes'] 
prob_lp = len(prob_lp) / df.purpose.count()

prob_cs = df[df['credit.policy'] == 'Yes'] 
prob_cs = len(prob_cs) / df.purpose.count()

new_df = df[df['paid.back.loan'] == 'Yes'] 

prob_pd_cs =  (new_df[new_df['credit.policy'] == 'Yes']).shape[0] / new_df.purpose.count()

bayes = (prob_pd_cs * prob_lp) / prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind = 'bar')
plt.show()
df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts(normalize=True).plot(kind = 'bar')
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df.installment.median()

inst_mean = df.installment.mean()
df.installment.plot(kind = 'hist')
plt.show()
df['log.annual.inc'].plot(kind = 'hist')
plt.show()
# code ends here


