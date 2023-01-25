#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install win10toast


# In[2]:


from win10toast import ToastNotifier

notifier = ToastNotifier()
notifier.show_toast("Title", "This is the message for the notification.", duration=10)


# In[ ]:




