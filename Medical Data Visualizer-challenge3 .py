# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 00:20:20 2023

@author: kanoon
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/kanoon/Desktop/freecode camp/3/medical_examination.csv')
BMI=df['weight']/((df['height']/100)**2)

# binary kardan sottone ezafe vazn va ezafe kardane in sotoon be df
overweight=[]

for i in range(len(BMI)):
    if BMI[i]>25:
        overweight.append(1)
    else:
        overweight.append(0)
df['overweight']=overweight
    

gl=[]
ch=[]

for i in range(len(df)):
    if (df['cholesterol'][i]==1) :
        ch.append(0)
    else:
        # gl.append(1)
        ch.append(1)
        
for i in range(len(df)):
    if (df['gluc'][i]==1) :
        gl.append(0)
    else:
        gl.append(1)
        
df['gluc']=gl
df['cholesterol']=ch



x1=df.loc[df['cardio']==0, 'active']
x2=df.loc[df['cardio']==0, 'alco']
x6=df.loc[df['cardio']==0, 'smoke']
x4=df.loc[df['cardio']==0, 'gluc']
x3=df.loc[df['cardio']==0, 'cholesterol']
x5=df.loc[df['cardio']==0, 'overweight']

# len(x1[x1==1])  toole matris ba maghadir 1 ke as x1 estekhrag shode
y=[len(x1[x1==1]), len(x1[x2==1]), len(x1[x3==1]),len(x1[x4==1]), len(x1[x5==1]),len(x1[x6==1])]
x=[len(x1[x1==0]), len(x1[x2==0]), len(x1[x3==0]), len(x1[x4==0]), len(x1[x5==0]),len(x1[x6==0])]


Medical_data=pd.DataFrame({'ONES':x,
              'ZEROS':y},
              index=['active','alco','smoke','gluc', 'cholesterol','overweight'])




Medical_data.plot(kind="bar")
sns.catplot(df)

df_filter=df[(df['ap_lo']<=df['ap_hi'])&
             (df['height']>=df['height'].quantile(0.025))&
             (df['height']<=df['height'].quantile(0.975))&
             (df['weight']>=df['weight'].quantile(0.025))&
             (df['weight']<=df['weight'].quantile(0.975))
             ]

correlation=df_filter.corr()
mask = np.triu(np.ones_like(correlation, dtype=bool))

fig,ax=plt.subplots(figsize=(16,9))                        
sns.heatmap(correlation, mask=mask)

fig.savefig('heatmap.png')