import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn
from PIL import Image

st.markdown("<h1 style='text-align: center; color: yellow;'>WELCOME ALL</h1></br>", unsafe_allow_html=True)  
image = Image.open('Quote.png')
st.image(image)

st.markdown("<h3 style='text-align: center; color: yellow;'>\"This model classifies certain quotes into their most suitable genre\"</h3></br></br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>About this Model</h2></br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify; color: white;'>Genre is any form or type of communication in any mode with socially-agreed-upon conventions developed over time. In popular usage, it normally describes a category of literature, music, or other forms of art or entertainment, whether written or spoken, audio or visual, based on some set of stylistic criteria, yet genres can be aesthetic, rhetorical, communicative, or functional.</p></br></br>", unsafe_allow_html=True)

spam_model = joblib.load('naive_model2.joblib')
vectorizer = joblib.load('CountVectorizer2.joblib')

inp_text = st.text_area('Enter the Quote here ',height=200)

motivational = pd.read_csv('motivational.csv',header=None,names=['Quotes','Tags'])
work  = pd.read_csv('work.csv',header=None,names=['Quotes','Tags'])
freedom  = pd.read_csv('ffreedom.csv',header=None,names=['Quotes','Tags'])
inspirational = pd.read_csv('inspirational.csv',header=None,names=['Quotes','Tags'])
chance  = pd.read_csv('chance.csv',header=None,names=['Quotes','Tags'])
failure  = pd.read_csv('failure.csv',header=None,names=['Quotes','Tags'])
life  = pd.read_csv('life.csv',header=None,names=['Quotes','Tags'])
knowledge  = pd.read_csv('knowledge.csv',header=None,names=['Quotes','Tags'])
sympathy  = pd.read_csv('sympathy.csv',header=None,names=['Quotes','Tags'])
strength  = pd.read_csv('strength.csv',header=None,names=['Quotes','Tags'])

vectorised_text = vectorizer.transform([inp_text])


pred = ''
def genre(inp_text):
    prediction = int(spam_model.predict(inp_text))
    if prediction == 0:
        pred = 'Motivational'
    elif(prediction == 1):
        pred = 'Inspirational'
    elif (prediction ==2):
        pred = 'Freedom'
    elif (prediction ==3):
        pred = 'Work'
    elif (prediction ==4):
        pred = 'Chance'
    elif (prediction ==5):
        pred = 'Failure'
    elif (prediction ==6):
        pred = 'Life'
    elif (prediction ==7):
        pred = 'Knowledge'
    elif (prediction ==8):
        pred = 'Sympathy'
    elif (prediction ==9):
        pred = 'Strength'
    return pred

def printd(dataframe):
    b = dataframe.Quotes
    b = b.head(8)
    for i in b:
        st.write(i)

s = []
pre = genre(vectorised_text)
if st.button('Submit'):
    st.write('Tag :',genre(vectorised_text))
    st.markdown("<h4 style='text-align: left; color: yellow;'>Related Quotes:</h4></br>", unsafe_allow_html=True)
    
    if(pre == 'Motivational'):
        printd(motivational)
    elif(pre == 'Work'):
        printd(work)  
    elif(pre == 'Freedom'):
        printd(freedom)
    elif(pre == 'Chance'):
        printd(chance)
    elif(pre == 'Failure'):
        printd(failure)
    elif(pre == 'Life'):
        printd(life)
    elif(pre == 'Knowledge'):
        printd(knowledge)
    elif(pre == 'Sympathy'):
        printd(sympathy)
    elif(pre == 'Inspirational'):
        printd(inspirational)
    else:
        printd(strength)
        
    st.markdown("<h6 style='text-align: right; color: white;'>Courtesy: brainlyquotes.com</h6></br></br></br></br>", unsafe_allow_html=True)
    
st.markdown("<h2 style='text-align: center; color: white;'>About the author</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify; color: white;'>  I, Anirudh S Rajeev is a third-year B.Tech student pursuing my degree in Computer Science and Engineering stream at Sreepathy Institute of Management and Technology. I have my interest stick with the Python language and have done many projects in it already. I am a cloud enthusiast and have hand on experience in AWS Cloud Services and Azure. On April 2021, I was selected for the Microsoft Learn Student Partner programme. </p>", unsafe_allow_html=True)
st.markdown("<a href = 'https://www.linkedin.com/in/anirudhsrajeev316/'>Check my LinkedIn</a>", unsafe_allow_html=True)    
st.markdown("<a href = 'https://github.com/ANIRUDHSRAJEEV/Python-Apps'>Check my GitHub </a>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: yellow;'>Thank You</h1>", unsafe_allow_html=True)
