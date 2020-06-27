'''
Power Analysis - Part I
'''
import numpy as np
import scipy.stats as st

# init
effect_size, sample_size, control_mean, control_sd = .05, 50, 1, .5
print(control_mean*(1+effect_size))
control_time_spent = np.random.normal(
    loc=control_mean,
    scale=control_sd,
    size=sample_size
)
treatment_time_spent = np.random.normal(
    loc=control_mean*(1+effect_size),
    scale=control_sd,
    size=sample_size
)
t_stat, p_value = st.ttest_ind(control_time_spent, treatment_time_spent)
stat_sig = p_value < .05
print("P-value: {}, Statistically Significant? {}".format(p_value, stat_sig))

'''
Power Analysis - Part II
'''
sample_size = 50
sims = 1000

while True:
    control_time_spent = np.random.normal(
        loc=control_mean,
        scale=control_sd,
        size=(sample_size, sims)
    )
    treatment_time_spent = np.random.normal(
        loc=control_mean*(1+effect_size),
        scale=control_sd, 
        size=(sample_size, sims)
    )
    t, p = st.ttest_ind(control_time_spent, treatment_time_spent)
    '''
    st.ttest_ind(a, b)
    This is a two-sided test for the null hypothesis that 2 independent 
    samples have identical average (expected) values. This test assumes 
    that the populations have identical variances by default.
    '''
    power = (p < .05).sum()/sims
    if power >= .8:
        break
    else:
        sample_size += 10

print('For 80% power, sample size required = {}'.format(sample_size))
