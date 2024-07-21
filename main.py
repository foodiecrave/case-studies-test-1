# -*- coding: utf-8 -*-

import streamlit as st
from streamlit_chat import message

from virtual_interviewer import VirtualInterviewer


from langchain.schema import (
  SystemMessage,
  HumanMessage,
  AIMessage
  )


def init():
  st.set_page_config(
    page_title="Case Study Interactive Analysis",
    page_icon=":smiling_imp:"
    )

def main():
  init()
  
  #chat = ChatOpenAI()
  vi = VirtualInterviewer()
  
  
  if "messages" not in st.session_state:
    st.session_state.messages = [
      SystemMessage(content="You are an interviewer and a helpful teacher.")
      
      ]

  st.header("Case Study Interactive Analysis :smiling_imp:")
  
  with st.sidebar:
    user_input = st.text_input("Your input... ", key="user_input")
    
  #user_input = st.text_input("Your input... ", key="user_input")

  #message("hellow how are you?")
  #message("I'm fine", is_user=True)
  
  
  if user_input:
    print("This is user_input: ", user_input)
    ###message(user_input, is_user=True)
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Considering..."):
      #response = chat(st.session_state.messages)  # <====== this is where the VirtualInterviewer is called
      temp_response = "Thank you!"
      #x = message(user_input, is_user=True)
      #y = x  #vi.candidate_message(x)
      #message(user_input, is_user=True)
      temp_response = vi.candidate_message(user_input)
      
    #message(response.content, is_user=False)
    ####message(temp_response, is_user=False)
    #st.session_state.messages = st.session_state.messages[:-1]
    st.session_state.messages.append(AIMessage(content=temp_response))  # note: when doing this with real AIMessage, must use response.content
    with st.sidebar:
      st.user_input = ""
  messages = st.session_state.get('messages', [])
  
  for i, msg in enumerate(messages[1:]):
    if i % 2 == 0:
      message(msg.content, is_user=True, key=str(i) + '_user')
    else:
      message(msg.content, is_user=False, key=str(i) + '_ai')
      




if __name__ == "__main__":
    main()
