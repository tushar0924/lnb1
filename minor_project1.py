#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


books=pd.read_csv(r'D:/books.csv')


# In[3]:


books_df=pd.DataFrame(books)
books_df


# In[4]:


books_df.info()


# In[5]:


books_df.set_index('bookID',inplace=True)


# In[43]:


books_df


# In[6]:


books_df.drop_duplicates(inplace=True)


# In[7]:


books_df


# In[47]:


books_df.dropna(axis=1,inplace=True)


# In[48]:


books_df


# # most popular books
# 

# In[81]:


books_df['average_rating']=pd.to_numeric(books_df['average_rating'])
books_df[(books_df['average_rating']>4) &(books_df['ratings_count']>10000)]



# # pages with lower count 

# In[82]:


books_df[(books_df['average_rating']>4) &(books_df['  num_pages']<200)]


# # pages with more number
# 

# In[83]:


books_df[(books_df['  num_pages']>800)]


# # yes pages with less number having higher ratings are more than books having large number of pages
# 

# # most popular book of 60s

# In[124]:


books_df['publication_date']=pd.to_datetime(books_df['publication_date'],format='%m-%d-%Y',errors='coerce')
books_df[((books_df['publication_date'] >= '01-01-1960') & (books_df['publication_date'] <= '12-31-1969')) & (books_df['average_rating']>4)&(books_df['ratings_count']>5000)]



# # most pages
# 

# In[96]:


books_df['  num_pages'].max()


# # the average or the mean count of page of author books is 336
# 

# In[98]:


books_df['  num_pages'].mean()


# # books with lesss than 200  pages

# In[99]:


books_df[(books_df['  num_pages']<200)]


#  # Houghton Mifflin Harcourt's most popular book

# In[103]:


books_df[(books_df['publisher']=='Houghton Mifflin Harcourt') & (books_df['average_rating']>4) & (books_df['ratings_count']>20000)]


# In[118]:


book_author=books_df[['title','authors','average_rating','ratings_count']].copy()


# In[119]:


book_author


# In[120]:


book_author[((book_author['average_rating'])>(book_author['average_rating'].mean())) &((book_author['ratings_count'])>(book_author['ratings_count'].mean()))]


# # least popular of 90s

# In[129]:


books_df[ (books_df['average_rating']<2.5)&(books_df['ratings_count']<1000)]


# # highest rated book with more than 500 pages

# In[138]:


books_df[ (books_df['average_rating']>4.5)&(books_df['ratings_count']>100000) &(books_df['  num_pages']>500) & (books_df['text_reviews_count']>books_df['text_reviews_count'].mean())]


# # graph plotting

# In[8]:


books_df.info()


# In[11]:


books_df.rename(columns={'  num_pages':'num_pages'},inplace=True)


# In[16]:


books_df


# In[54]:


bins=800
f=plt.figure()
f.set_figwidth(15)
f.set_figheight(10)
range=(0,5)
plt.hist(books_df['average_rating'],bins,range,histtype='bar',label='popular',color='g')
plt.grid(True,color='k',linewidth=0.1)
plt.xlabel('Average Rating')
plt.ylabel('No. of Ratings')
plt.title('most popular books by average rating')


# In[55]:


books_df['language_code'].unique()


# In[64]:


bins=10
f=plt.figure()
f.set_figwidth(15)
f.set_figheight(10)
range=(0,5)
plt.hist(books_df['language_code'],bins,range,histtype='bar',label='variety of book with different language',color='g')
       


# # DESCRIPTIVE STATISTICS

# In[67]:


books_df.info()


# In[71]:


books_df.describe()


# # as you can see standard deviation for all the numeric values is described as shown above in the table
# # its not close to mean that is its a low standard deviation but for special case like text review count the std is high as compared to mean that is there is  alot of change in value in the column text review count
# 

# In[75]:


print(books_df['text_reviews_count'].max())
books_df.describe()


# # the max text review count  is   94265 and the mean of text review count is 542 thats a lot of difference in the values so text review count has outliers or error value that is causing the diff so much
# 

# In[76]:


books_df


# In[ ]:




