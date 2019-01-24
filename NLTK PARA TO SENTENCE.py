
# coding: utf-8

# In[33]:


from nltk import tokenize
tk=tokenize


# In[34]:


p = "Good morning Dr. Adams. The patient is waiting for you in room number 3.This chapter is divided into sections that skip between two quite different styles. In the \"computing with language\" sections we will take on some linguistically motivated programming tasks without necessarily explaining how they work. In the closer look at Python sections we will systematically review key programming concepts. We'll flag the two styles in the section titles, but later chapters will mix both styles without being so up-front about it. We hope this style of introduction gives you an authentic taste of what will come later, while covering a range of elementary concepts in linguistics and computer science. If you have basic familiarity with both areas, you can skip to 5; we will repeat any important points in later chapters, and if you miss anything you can easily consult the online reference material at  http://nltk.org/. If the material is completely new to you, this chapter will raise more questions than it answers, questions that are addressed in the rest of this book."


# In[36]:


tk.sent_tokenize(p)


# In[31]:


import nltk
nltk.download('punkt')


# In[6]:


help('nltk')


# In[37]:


a="India, as the world’s fastest-growing major economy, may well be catching up with the richer economies in terms of absolute size. But economic convergence within the country remains a distant dream as poorer States continue to lag behind the richer ones in economic growth. A report from the rating agency Crisil found that the inter-State disparities have widened in recent years even as the larger economy grows in size and influence on the global stage. Many low-income States have experienced isolated years of strong economic growth above the national average. Bihar, in fact, was the fastest-growing State this year among the 17 non-special category States evaluated by the report. But they have still failed to bridge their widening gap with the richer States since they have simply not been able to maintain a healthy growth rate over a sustained period of time. Richer States like Gujarat, for instance, have been able to achieve sustained economic growth and increase their gap over other States. The report found that there was a slight, albeit weak, convergence in the per capita income levels of the poorer and richer States between fiscal years 2008 and 2013, but the trend was reversed in the subsequent years. Between fiscal years 2013 and 2018, there has been a significant divergence rather than convergence in the economic fortunes of the poorer and richer States. This was the result of richer States continuing to show strong growth while the poorer States fell behind. In fact, only two of the eight low-income States in 2013 had growth rates above the national average over the next five years. On the other hand, six out of the nine high-income States recorded rates higher than the national average during 2013-18.The gap between rich and poor States.What explains the divergence in the economic fortunes of States? The report suggests that, at least during fiscal year 2018, government spending may be what boosted gross domestic product growth in the top-performing States, particularly in Bihar and Andhra Pradesh whose double-digit growth rates have come along with a burgeoning fiscal deficit. The impact of greater spending was that 10 of the 17 States breached the 3% fiscal deficit limit set by the Fiscal Responsibility and Budget Management Act. Many other big-spending States, however, have not managed to achieve growth above the national average. Punjab and Kerala, which are at the bottom of the growth table, are ranked as profligates by the report. This suggests that the size of public spending is probably not what differentiates the richer States from the poorer ones. Other variables like the strength of State-level institutions, as gauged by their ability to uphold the rule of law and create a free, competitive marketplace for businesses to thrive, and the quality of public spending could be crucial determinants of the long-run growth prospects of States."


# In[38]:


tk.sent_tokenize(a)

