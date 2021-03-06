#Initial import of useful packages in Python
import pandas as pd 
import numpy as np 
import scipy as sp 
import scipy.stats.distributions as dist
from scipy import stats as st
from sklearn import linear_model
import statsmodels.api as sm

#Import .csv of dataset which was previously cleaned in PostgreSQL
df = pd.read_csv(r'C:\Users\Josh\Capstone_SQL.csv')
df

#Find play type counts in dataset
df.play_type.value_counts()

#Find percentage of plays of rush and pass type
rush_rate = df.play_type.value_counts().Rush / (df.play_type.value_counts().Rush + df.play_type.value_counts().Pass)
pass_rate = df.play_type.value_counts().Pass / (df.play_type.value_counts().Rush + df.play_type.value_counts().Pass)
print('Baseline Rush Rate:', rush_rate)
print('Baseline Pass Rate:', pass_rate)

#Determine baseline statistics by play type as well as teams
avg_ypp = df['yards_gained'].mean()
avg_ypp

df.groupby(['play_type']).yards_gained.mean()

df.groupby(['offense']).yards_gained.mean()

df.groupby(['offense', 'play_type']).yards_gained.mean()

df.groupby(['offense']).play_type.value_counts()

#Summary statistics for plays by down
df.groupby(['down']).yards_gained.mean()

df.groupby(['down']).yards_gained.median()

df.groupby(['down']).play_type.value_counts()

df.groupby(['down']).distance.mean()

df.groupby(['down']).distance.median()

df.groupby(['down', 'play_type']).yards_gained.mean()

df.groupby(['down', 'play_type']).yards_gained.median()

#Subdividing the dataset depending on if the offense is in the lead, trailing or tied
leading = df[df['offense_score'] > df['defense_score']]
leading

trailing = df[df['offense_score'] < df['defense_score']]
trailing

tied = df[df['offense_score'] == df['defense_score']]
tied

#Determining summary statistics for the new subsets of the data
lead_ypp = leading['yards_gained'].mean()
lead_ypp

lead_ypp_median = leading['yards_gained'].median()
lead_ypp_median

trail_ypp = trailing['yards_gained'].mean()
trail_ypp

trail_ypp_median = trailing['yards_gained'].median()
trail_ypp_median

tied_ypp = tied['yards_gained'].mean()
tied_ypp

tied_ypp_median = tied['yards_gained'].median()
tied_ypp_median

#Determining if the leading or trailing team calls more passing plays
print("Leading team play distribution:")
print(leading.play_type.value_counts())
print("Trailing team play distribution:")
print(trailing.play_type.value_counts())

print("Leading team calls passing plays", (18472 / (22831 + 18472)) * 100, "percent of the time.")
print("Trailing team calls passing plays", (21418 / (21418 + 17407)) * 100, "percent of the time.")

total_prop_pass = 47475 / (47475 + 47755)
num_lead = leading.play_type.count()
num_trail = trailing.play_type.count()

variance = total_prop_pass * (1 - total_prop_pass)
std_error = np.sqrt(variance * (1 / 18472 + 1 / 21418))
print("Sample Standard Error is", std_error)

best_est = (.4472314 - .5516548)
print("The best estimate is", best_est)
hypo_est = 0
test_stat = (best_est - hypo_est) / std_error
print("Test Statistic is", test_stat)

#Determines P-value for described passing rate attributes
pvalue = 2 * dist.norm.cdf(-np.abs(test_stat))
print("P-value is", pvalue)

#Determines if the team in the lead or the team that is trailing gains more yards per play
print("Leading team gains", lead_ypp, "yards per play")
print("Trailing team gains", trail_ypp, "yards per play")

#Determining significance of the difference in yards per play between leading and trailing team
rq2_data = [['leading', 6.89224], ['trailing', 5.53723]]
rq2_df = pd.DataFrame(rq2_data, columns = ['Team', 'YPP'])
rq2_df

rq2_a = rq2_df['YPP'].to_numpy()

#Returns P-value to determine significance
st.ttest_1samp(a = rq2_a, popmean = 6.12385)

#Determining how field position affects the type of plays called
yardline_dist = df.groupby(pd.cut(df['yard_line'], np.arange(0, 101, 10))).play_type.value_counts()
yardline_dist

#Determining how field position affects yards per play
yardline_ypp = df.groupby(pd.cut(df['yard_line'], np.arange(0, 101, 10))).yards_gained.mean()
yardline_ypp

yardline_ypp_median = df.groupby(pd.cut(df['yard_line'], np.arange(0, 101, 10))).yards_gained.median()
yardline_ypp_median

df.groupby(pd.cut(df['yard_line'], np.arange(0, 101, 10))).yards_gained.value_counts()

rq4_10 = df.loc[df['yard_line'].isin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])].yards_gained.tolist()
rq4_20 = df.loc[df['yard_line'].isin([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])].yards_gained.tolist()
rq4_30 = df.loc[df['yard_line'].isin([21, 22, 23, 24, 25, 26, 27, 28, 29, 30])].yards_gained.tolist()
rq4_40 = df.loc[df['yard_line'].isin([31, 32, 33, 34, 35, 36, 37, 38, 39, 40])].yards_gained.tolist()
rq4_50 = df.loc[df['yard_line'].isin([41, 42, 43, 44, 45, 46, 47, 48, 49, 50])].yards_gained.tolist()
rq4_60 = df.loc[df['yard_line'].isin([51, 52, 53, 54, 55, 56, 57, 58, 59, 60])].yards_gained.tolist()
rq4_70 = df.loc[df['yard_line'].isin([61, 62, 63, 64, 65, 66, 67, 68, 69, 70])].yards_gained.tolist()
rq4_80 = df.loc[df['yard_line'].isin([71, 72, 73, 74, 75, 76, 77, 78, 79, 80])].yards_gained.tolist()
rq4_90 = df.loc[df['yard_line'].isin([81, 82, 83, 84, 85, 86, 87, 88, 89, 90])].yards_gained.tolist()
rq4_100 = df.loc[df['yard_line'].isin([91, 92, 93, 94, 95, 96, 97, 98, 99, 100])].yards_gained.tolist()

df1 = pd.DataFrame(rq4_10)
df2 = pd.DataFrame(rq4_20)
df3 = pd.DataFrame(rq4_30)
df4 = pd.DataFrame(rq4_40)
df5 = pd.DataFrame(rq4_50)
df6 = pd.DataFrame(rq4_60)
df7 = pd.DataFrame(rq4_70)
df8 = pd.DataFrame(rq4_80)
df9 = pd.DataFrame(rq4_90)
df10 = pd.DataFrame(rq4_100)

#Determining P-value of the distribution to determine significance
rq4_f, rq4_p = st.f_oneway(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10) #ANOVA analysis
print(rq4_f, rq4_p)

#Determining which downs see the most yards per play
df.groupby(['down']).yards_gained.mean()

df.groupby(['down']).yards_gained.median()

rq5_1 = df.loc[df['down'].isin([1])].yards_gained.tolist()
rq5_2 = df.loc[df['down'].isin([2])].yards_gained.tolist()
rq5_3 = df.loc[df['down'].isin([3])].yards_gained.tolist()
rq5_4 = df.loc[df['down'].isin([4])].yards_gained.tolist()

rq5_df1 = pd.DataFrame(rq5_1)
rq5_df2 = pd.DataFrame(rq5_2)
rq5_df3 = pd.DataFrame(rq5_3)
rq5_df4 = pd.DataFrame(rq5_4)

rq5_f, rq5_p = st.f_oneway(rq5_df1, rq5_df2, rq5_df3, rq5_df4)
print(rq5_f, rq5_p)

#Determining whether passing or rushing plays result in more yards per play
df.groupby(['play_type']).yards_gained.mean()

df.groupby(['play_type']).yards_gained.median()

#Determining significance with T-test
rq6_data = [['Pass', 7.08998], ['Rush', 5.16338]]
rq6_df = pd.DataFrame(rq6_data, columns = ['Play Type', 'YPP'])

rq6_a = rq6_df['YPP'].to_numpy()

st.ttest_1samp(a = rq6_a, popmean = 6.12385)

#Determining factors correlating to yards per play
rq7_x = df[['offense_score', 'defense_score', 'yard_line', 'down', 'distance', 'quarter']]
rq7_y = df['yards_gained']

rq7_regr = LinearRegression()
rq7_regr.fit(rq7_x, rq7_y)

print('Intercept:', rq7_regr.intercept_)
print('Coefficients:', rq7_regr.coef_)

model = sm.OLS(rq7_y, rq7_x).fit()
print_model = model.summary()
print(print_model)