#!/usr/bin/env python
# coding: utf-8

# In[20]:


from tkinter import *
import random
    
import random

class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Random Chores")

        self.pack(fill=BOTH, expand=1)

        choreButton = Button(self, text="GENERATE",command="run_Chores")

        choreButton.place(x=400, y=250)  


    def run_Chores(self):
        
        run_Chores = ['Walk the Dog', 'Feed the Cat', 'Eat the Iguana']
        
        print(random.choice(run_Chores))
        

root = Tk()

root.geometry("800x500")

app = Window(root)

root.mainloop()  


# In[ ]:





# In[ ]:





# In[ ]:




