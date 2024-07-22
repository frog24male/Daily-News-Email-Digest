import streamlit as st
import requests
from email_send import email_sender
import datetime



#Dont forget to add user in st


st.title(" News ")
st.subheader("Function")

st.write("This web app allows you to receive news in yypur email with just the click of a button. Even you want to automate further such that you would ereceive news automatically at certain time everyday at a specific time.")
with st.form(key="My form"):
    
    user=st.text_input("Please enter your email address")
    topic=st.text_input("What topics would you like to receive news about?")
    current_date = datetime.date.today()
    topic=st.text_input("What topic are you interested in?")
    submit=st.form_submit_button("Submit")
    
if submit:
    
    api="f3eb410c821e43c6a632c6a7383c1bbc"
    url=f"https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=publishedAt&apiKey={api}"
    
    req=requests.get(url)
    content=req.json()
    content["articles"]
    
    for article in content["articles"]:
        if article['title'] is not None:
            title=article['title']
            description=article['description']
            message=""
            message=message+'\n'+'\n'+title+'\n'+description
        
    message=message.encode('utf-8')
    email_sender(message)
    st.info("Email Succesfully Sent !")
    a=1
    
