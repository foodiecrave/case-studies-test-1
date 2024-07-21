# -*- coding: utf-8 -*-
# VirtualInterviewer class implementation

import os
import sys
import time
import os
from os import listdir
from os.path import isfile, join
import requests
import json
from enum import Enum
import math
from enum import Enum
import inflect

import numpy as np
import pandas as pd

#import cohere

from prompts import *



guide_information = ["Population of New York City", "Average household income", "Percentage of population consuming coffee daily", 
                     "Average expenditure on coffee per consumer per day", "Current number of Starbucks stores", 
                     "Foot traffic in key areas (average pedestrians per day) - Times Square", 
                     "Foot traffic in key areas (average pedestrians per day) - Central Park",
                     "Foot traffic in key areas (average pedestrians per day) - Wall Street"
                    ]

assumptions = ["Each store is assumed to serve an average of 500 customers per day.", 
               "Market capture rate by Starbucks in a new location is assumed to be 10% of the daily foot traffic."
              ]


case_studies_dir = r"C:/Users/Eugene Grois/working/streamlit_chat_case_studies/case_studies_json"

AZURE_OPENAI_API_KEY = "06b3100849a9415294a19c26b225c1b5"
AZURE_OPENAI_ENDPOINT = "https://eg-sandbox.openai.azure.com/"

deployment_name='gpt-35-turbo-16k-test1'  # THIS IS THE GPT 3.5 Turbo deployment in Azure set up previously

#from langchain_core.messages import HumanMessage
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI


llm_candidate_interpreter = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment=deployment_name,
    openai_api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    temperature=0
)


def enum(*sequential, **named):
  enums = dict(zip(sequential, range(len(sequential))), **named)
  return type('Enum', (), enums)
  
LastHelpProvided = enum('NO_HELP', 'HINT', 'DESCRIPTION', 'DATA_REQUIRED', 'COMPUTATION', 'CALCULATION')


class VirtualInterviewer:
  total_num_questions = 1
  question_number = 0
  total_num_solution_steps_for_cur_question = 1
  solution_step = 0
  co_candidate_interpreter = None
  co_info_qa = None
  
  p = inflect.engine()
  
  current_case_study_json_obj = None
  case_study_loaded = False
  name_current_case_study = ""
  
  # increment this variable each time new level of help provided
  # reset this variable each time new step is started
  last_help_provided = LastHelpProvided.NO_HELP  
  initial_solution_advice_given = False
  
  def __init__(self):
    self.p = inflect.engine()
    
    
  
  
  
  
  def interpret_candidate_message(self, message):
    """completion = llm_candidate_interpreter.completions.create(
    #completion = llm_candidate_interpreter.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
        ]
      )

    print(completion.choices[0].message)"""
    
    #k = llm_candidate_interpreter.invoke("tell me a joke")
  
    #k = llm_candidate_interpreter.invoke(message)
    
    #print(k)
    #return k.content
    
    #h=get_candidate_message_interpreter_prompt(user_communication_=message, 
    #                                                guide_information_=guide_information, 
    #                                                assumptions_=assumptions)
    #print(h)
  
    msg = [
      SystemMessage(
        content=get_candidate_message_interpreter_prompt(user_communication_=message, 
                                                        guide_information_=guide_information, 
                                                        assumptions_=assumptions),
                    ),
    #HumanMessage(content=message),
    ]
    

    response = llm_candidate_interpreter(msg)
    
    print(response)
    
    return response
    
  
  
  def process_candidate_message(self, message):
    response = self.interpret_candidate_message(message)
    
    return response


  def candidate_message(self, message):
    response = ""
    
    candidate_intent = self.process_candidate_message(message)
    #candidate_intent = "Thank you!"
    
    return candidate_intent
  
  
  def interviewer_message(self, message):
    pass
