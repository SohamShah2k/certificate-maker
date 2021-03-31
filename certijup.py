#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install Pillow')


# In[4]:


import pandas as pd


# In[10]:


dfn = pd.read_csv("names.txt")
dfd = pd.read_csv("desig.txt")
print(dfn)
NAMES = list(dfn.Name)
DESIG = list(dfd.Desig)
print(NAMES,DESIG)


# In[11]:


import re
CERTIFICATE = []
for d in DESIG:
    h = re.search('Head$',d)
    x = re.search('Executive',d)
    if (h==None and x == None):
        CERTIFICATE.append('core.png')
    elif (h != None):
        CERTIFICATE.append('head.png')
    elif (x!=None):
        CERTIFICATE.append('exec.png')
print(CERTIFICATE)


# In[12]:


from PIL import Image, ImageDraw, ImageFont 
  
   
def coupons(names: list,desigs:list, certificates: list): 
   
    for (name,desig,certificate) in zip(names,desigs,certificates): 
          
        # adjust the position according to  
        # your image 
        text_y_name = 450
        text_y_desig = 580

        # opens the image 
        img = Image.open(certificate, mode ='r') 
          
        # gets the image width 
        image_width = img.width 
          
        # gets the image height 
        image_height = img.height  
   
        # creates a drawing canvas overlay  
        # on top of the image 
        draw = ImageDraw.Draw(img) 
   
        ##################### name ##########################
        fontname = ImageFont.truetype( 
            "Lora-Italic-VariableFont_wght.ttf", 
            size = 90
             # change this according to your needs 
        ) 
   
        # fetches the text width for  
        # calculations later on 
        text_width, _ = draw.textsize(name, font = fontname) 
   
        draw.text( 
            ( 
                # this calculation is done  
                # to centre the image 
                (image_width - text_width) / 2, 
                text_y_name 
            ), 
            name, 
            font = fontname,
            fill=(83, 144, 217,255)
               ) 
    
         ##################### Desig #########################
        fontdesig = ImageFont.truetype( 
            "PlayfairDisplay-VariableFont_wght.ttf", 
            size = 45
             # change this according to your needs 
        ) 
   
        # fetches the text width for  
        # calculations later on 
        text_width, _ = draw.textsize(desig, font = fontdesig) 
   
        draw.text( 
            ( 
                # this calculation is done  
                # to centre the image 
                (image_width - text_width) / 2, 
                text_y_desig 
            ), 
            desig, 
            font = fontdesig,
            fill=(83, 144, 217,255)
               )
        #############################################################
        
        # saves the image in png format 
        #img.save("certs\{}.png".format(name))  
        #saves in pdf format
        img1 = img.convert('RGB')
        img1.save("certspdf\{}.pdf".format(name))
  
# Driver Code 
if __name__ == "__main__": 
   
    # List of names 
    #NAMES = df.to_list()
      
    # path to font 
    #over written in coupon function, kept here to pass to function so dont have to change the 
    FONT = "times-new-roman.ttf"
      
    # path to sample certificate 
    
    name = ["Naman Agarwal"]
    desig = ['Public Relations Executive']
    coupons(NAMES,DESIG, CERTIFICATE) 


# In[ ]:





# In[ ]:




