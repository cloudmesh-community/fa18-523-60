import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from collections import Counter
from datetime import datetime
import pymongo
from pymongo import MongoClient
from wordcloud import WordCloud
import time
import re
from   datetime import datetime
import logging 


def load_data():
    #client = MongoClient()
    #db = client.kickstarter
    #collection = db.projects
    #df = pd.DataFrame(list(collection.find()))
      
    client = MongoClient('mongodb+srv://nishad:****@cluster0-4fgwj.azure.mongodb.net/test?retryWrites=true')
    db = client.kick
    collection = db.project
    df = pd.DataFrame(list(collection.find()))
    
    
    '''Data Cleaning Features '''
    df.drop(['usd pledged'], axis=1, inplace=True)
    df.replace('N,0"','NO',inplace=True)
    
    '''extract features'''
    
    ''' Launched date conversion to day,year,month,time'''
    df['year'] = df['launched'].apply(lambda x:x[0:4])                                                                                                                                                                                                                                          
    df['month'] = df['launched'].apply(lambda x:x[5:7])
    df['day'] = df['launched'].apply(lambda x:x[8:10])
    df['time'] = df['launched'].apply(lambda x:x[11:])
    
    ''' Deadline date conversion to day,year,month,time'''
    df['year_d'] = df['deadline'].apply(lambda x:x[0:4])                                                                                                                                                                                                                                          
    df['month_d'] = df['deadline'].apply(lambda x:x[5:7])
    df['day_d'] = df['deadline'].apply(lambda x:x[8:10])
    df['time_d'] = df['deadline'].apply(lambda x:x[11:])
    
    ''' Adding Duration Column '''
    df['A'] = pd.to_datetime(df['deadline'])
    df['B'] = pd.to_datetime(df['launched'])
    df['duration'] = df['A'] - df['B']
    df.duration = df.duration.dt.days
    
    return df
    
def show_wordcloud(data, title = None):
    '''Split names by space and generate word counts.'''
    wordcloud = WordCloud(
        background_color='white',
        max_words=100,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    return plt.imshow(wordcloud)
    
def main():
    
    '''measure Performance'''
    perflog = open('performance.log','w')
    start_time = time.time()
    perflog.write("Program started at: ")
    perflog.write(str(start_time))
    
    df = load_data()
    #plt.style.use('ggplot')
    plt.figure(figsize=(12,8))
    sns.set(style="white")
    
  
    ''' Projects statuses '''
    df['state'].value_counts().plot(kind='bar')
    plt.savefig('Project states.png')
    
    '''Top Countries with goal'''
    sns.set(style="white")
    df_ggsf = df[(df['state'] == 'successful') | (df['state'] =='failed') ]
    df_gg = df_ggsf[['goal','state','main_category']]
    df_ggrp= df_gg.groupby(['main_category','state'],as_index=False).mean().sort_values(by='goal',ascending=False)
    plt.figure(figsize=(15,9))
    sns.barplot(x='goal',y='main_category',data=df_ggrp,hue='state',palette='viridis')
    plt.legend(loc='center right')
    plt.savefig('Top countries average goal for Success and failed.png')
 
    ''' Year wise successful and failed project '''
    df3 = df[(df['state']=='successful')| (df['state']=='failed')].sort_values(by='pledged',ascending=True)
    sns.countplot(x='year',hue='state',data=df3)
    plt.title('Project_count_across_different_states')
    plt.savefig('Project_count_across_different_states.png')
    
    '''Project status across categories'''
    df[['main_category', 'state']].pivot_table(columns='state', index='main_category', aggfunc=np.size).plot(kind='bar', figsize=(12, 8), stacked=True)
    plt.savefig('Project_count_across_different_states.png')
    
    ''' Top Markets ''' 
    df_s = df[(df['state']=='successful')| (df['state']=='failed')]
    df_c = df_s[['pledged','state','country']]
    df_cp = df_c.groupby(['country','state'],as_index=False).mean().sort_values(by='pledged',ascending=False)
    sns.barplot(x='country',y='pledged',data=df_cp,hue='state',palette='muted')
    plt.savefig('Top Markets.png')
    
    '''Heatmap of pledge amount'''
    df_gn = df[['pledged','state','main_category']]
    df_gn_g = df_gn.groupby(['main_category','state'],as_index=False).mean()
    df_pivot = df_gn_g.pivot(index='state',columns='main_category')
    df_pivot.dropna(inplace=True)
    plt.figure(figsize=(15,8))
    sns.heatmap(df_pivot,cmap='viridis')

    ''' Average Pledged Amount for Success and Failed Projects'''
    df_sf = df[(df['state']=='successful')| (df['state']=='failed')]
    df_g = df_sf[['pledged','state','main_category']]
    df_grp= df_g.groupby(['main_category','state'],as_index=False).mean().sort_values(by='pledged',ascending=False)
    sns.barplot(x='main_category',y='pledged',data=df_grp,hue='state',palette='muted')
    plt.savefig('Pledge_Amount_Average.png')
    
    ''' SNS dist plots continuous variables '''
    '''goal'''
    dims = (14, 8)
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False, figsize=dims)
    sns.distplot(df.goal, ax=ax1)
    sns.distplot(np.log1p(df.goal), ax=ax2)
    plt.savefig('Dist_plot_goal.png')
    
    '''pledged''' 
    dims = (14, 8)
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False, figsize=dims)
    sns.distplot(df.pledged, ax=ax1)
    sns.distplot(np.log1p(df.pledged), ax=ax2)
    plt.savefig('Dist_plot_pledged.png')
    
    '''Amount Remaining in failed categories'''
    df = df.loc[df['state'] == 'failed'] 
    df['remain'] = df['goal']-df['pledged']
    df8 = (df.groupby(['main_category']).agg({'goal':'sum', 'pledged':'sum', 'remain':'sum'}).reset_index())
    ax = plt.axes()
    ax.bar(df8.main_category, df8['remain'], width=0.4, color='r',label = 'Remaining')
    ax.bar(df8.main_category, df8['pledged'], width=0.4, color='g', label = 'Pledged')
    plt.xticks(rotation=90)
    ax.legend(fontsize = 10)
    plt.title('Amount Remaining in failed categories')
    plt.savefig('Amount_Remaining_in_failed_categories.jpg')
   
    
    '''WordCloud''' 
    show_wordcloud(df[df.state == 'successful']['category'])
    start_time = time.time()
    
    ''' boxplot '''
    df4 = df.groupby('state').duration.mean().sort_index()
    df4.plot(kind='box')
    
    end_time= time.time() - start_time
    perflog.write("Program ended with: ")
    perflog.write(str(end_time))
    perflog.close()
    
if __name__ == "__main__":
   e_logger = logging.getLogger('exceptionlogger')
   e_logger.setLevel(logging.DEBUG) 
   formatter = logging.Formatter("%(asctime)s:%(message)s")
   e_handler = logging.handlers.RotatingFileHandler("exception.log",maxBytes=10000,backupCount=5)
   e_handler.setFormatter(formatter)
   e_logger.addHandler(e_handler)
   try:
        main()
   except Exception:
        e_logger.exception("message")
