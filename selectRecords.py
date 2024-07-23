import pandas as pd

# Load the full dataset
df = pd.read_csv('accidents.csv')

# Select only the 'latitude' and 'longitude' columns
ll_df = df[['Start_Lat', 'Start_Lng']]

# Select the first 1000 rows
#subset_df = ll_df.head(1000)

subset_df = ll_df[(ll_df["Start_Lat"] >= 41) & (ll_df["Start_Lat"] <= 42) & (ll_df["Start_Lng"] <= -75) & (ll_df["Start_Lng"] >= -76)]
#subset_df =  = ll_df[(ll_df["LAT"] >= 41)]
# Save the subset to a new CSV file
subset_df.to_csv('local_accidents.csv', index=False)