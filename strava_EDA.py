import matplotlib.pyplot as plt
import pandas as pd

############### READ STRAVA DATA CSV ###############
df = pd.read_csv('Strava_data.csv')     # update file as needed

############### CREATE DATAFRAME: Avg Altitude by Month ###############
avg_alt = df.loc[: ,'Elev_high' : 'Elev_low']
df['avg_alt'] = avg_alt.mean(axis=1)
df_alt_month = df.groupby(['Month'])['avg_alt'].mean()
df_x_month = df_alt_month[['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December']]

############### CREATE PLOT: Avg Altitude of Activity by Month ###############

df_alt_month.plot.bar(title = 'Average Altitude of Activity by Month',
              ylim = (3000, 7000), color= (0.988, 0.38, 0))
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average Altitude")
plt.tight_layout()
plt.show()

##############################################################################

############### CREATE DATAFRAME: Shoes by Moving Duration ###############
time = pd.DatetimeIndex(df['Moving time'])                               
time = time.hour * 60 + time.minute
df['time'] = time
df_shoes = df.groupby(['Gear'])['time'].sum()
df_shoes = df_shoes.drop(['BMC', 'Rock Hopper'])

############### CREATE PLOT: Shoes by Moving Duration ###############
df_shoes.plot.bar(title = 'Total Duration by Shoe', yticks = range(0, 6000, 1000),
             color= (0.988, 0.38, 0))
plt.xticks(rotation=45, ha='right')
plt.ylabel("Hours")
plt.tight_layout()
plt.show()

##############################################################################

############### CREATE DATAFRAME: Shoes by Avg HR ###############
df = df[df['Average heartrate'] != 0]
df_shoes_hr = df.groupby(['Gear'])['Average heartrate'].mean()
df_shoes_hr = df_shoes_hr.drop(['BMC', 'Rock Hopper'])
df_shoes_hr.plot.bar(title = 'Average HR by Shoe', ylim = (120, 160), color= (0.988, 0.38, 0))

############### CREATE PLOT: Shoes by Avg HR ###############
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average Heartrate")
plt.tight_layout()
plt.show()

##############################################################################

############### CREATE DATAFRAME: Heart Beats by Month ###############
df_hr_month = df.groupby(['Month'])['HeartBeats'].sum()
df_hr_month = df_hr_month[['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December']]

############### CREATE PLOT: Total Heartbeats by Month ###############
df_hr_month.plot.bar(title = 'Total Heart Beats per Month',
             ylim = (300000, 900000), color= (0.988, 0.38, 0))
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total Heart Beats")
plt.tight_layout()
plt.show()
