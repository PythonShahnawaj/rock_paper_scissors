#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'


# In[9]:


def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or        (player == 'p' and opponent == 'r'):
    
        return True


# In[12]:


play()


# In[ ]:




