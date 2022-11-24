import pandas as pd


df = fb_blocked_users

df['block_duration'] = df['block_duration'].fillna(0)
#df['block_duration'] = df['block_duration'].astype('timedelta64')
#df['block_date'] = df['block_date'].astype('timedelta64')
#df['block_date'] = pd.to_datetime(df['block_date'])
#for x in df['block_duration']:
    #print(x)
df['blocked_until'] = pd.to_datetime(df['block_date']) + pd.to_timedelta(df['block_duration'] ,unit='d')

df.loc[(df['block_date']<'2021-12-31') & (df['block_date']>'2021-12-01') | ((df['blocked_until']<'2021-12-31') & (df['blocked_until']>'2021-12-01'))]
