# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:38:28 2020

@author: asus
"""


import streamlit as st

#text.title
st.title('My first webapp on streamlit')

st.header('Header')
st.subheader('SubHeader')

#text
st.text('Hii there!!!')

#markdown
st.markdown("##T his is a markdown")

#success
st.success("Woohoo")
st.warning('Dont')
st.error('Danger')
st.info('info')

#write
st.write('I am writing')
st.write(range(1,11))
st.text(range(1,11))

#image
#img = Image.open("819837.png")
#st.image(img, width=200)

#checkbox
if(st.checkbox('Show/Hide')):
    st.text('You did it')
# radio
status = st.radio("Select Gender: ", ('Male', 'Female'))

if(status == 'Male'):
    st.text('You are male')
elif(status=='Female'):
    st.text('You are female')
else:
    st.text('No input')
    
    
#selection box
#hobbies = st.selection('Hobbies:' ,['Dancing','Reading','writing'])

#button
st.button('Submit')

name = st.text_input('Enter your name')
st.write('Your name is',name)

#numberinput
age = st.number_input('Your age')
st.write('Your age is', age)

import datetime as dt
today = st.date_input('Todays date is ',dt.datetime.now())
st.text(today)


if(st.button('Click if streamlit is FUN')):
    st.balloons()