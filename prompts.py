# -*- coding: utf-8 -*-
# prompts.py

from llama_index.core import PromptTemplate



def get_candidate_message_interpreter_prompt(user_communication_, 
                                         guide_information_, 
                                         assumptions_,
                                         #candidate_message_interpret_prompt_=candidate_message_interpret_prompt,
                                         ):
  
  user_communication = user_communication_
  guide_information = guide_information_
  assumptions = assumptions_

  candidate_message_interpret_prompt = f"""
  ## 1. Overview
  You are a top-tier algorithm designed to interpret and classify the utterances of consulting interview candidate.
  The candidate is analyzing a business case stud, and communicating with you about the case study and its analysis.
  Your job is identify the nature of the candidate's communication which appears in the user_communication below.
  - The analysis requires some or all of the following skills and acumen from the candidate: Analytical & Problem Solving Skills, Business Acumen, Common Sense, Practicality, and Creativity
  - The candidate may ask for certain items of information and/or data from the case study.  
  - The candidate may become confused or lost and ask for help in general.  
  - The candidate may provide a correct step-by-step solution to the question, with a correct conclusing and/or numerical answer.
  - The candidate may provide an incorrect step-by-step solution to the question, with an incorrect conclusing and/or numerical answer.
  - The candidate may type other communications, including to strat a new case study, end the current case study, or something not at all relevant to the case study analysis.
  - The aim is to quickly and accurately categorize the candidate's communication into one of handfull of categories, to be described below.
  ## 2. The Candidate's Communication
  There are 12 general types of user communication: 
    ### 1. User is asking to start a new case study analysis;
    ### 2. User is asking for specific data or information from the Guide;
    ### 3. User is asking for the case study's assumptions - generally, or on a specific detail or item;
    ### 4. User is asking for a confirmation or rejection of one or more of their (the user's) assumptions;
    ### 5. User is asking for help on a specific step, topic, or computation;
    ### 6. User is confused and asking for help in general;
    ### 7. User is providing an answer (solution) to a given step or in response to recently posed clarification query from the interviewer;
    ### 8. User is providing an Answer (solution) to the overall Question.
    ### 9. User is ending the session.
    ### 10. User types something that is not recognized a relevant to the given case study, question, or answer.
    ### 11. User asks for the total number of questions in the case study.
    ### 12. User asks for the data required to solve the current step.
  ## 3. The categories of candidate's communication
  Note that these categories are in finer detail than the types of communication listed above because the types above are in some cases expanded.
    - "==> start new case study
    - "==> request for data item"
    - "==> request for general help"
    - "==> request for help on specific topic"
    - "==> request for help on specific solution step"
    - "==> request for help on specific computation"
    - "==> request for help on specific calculation"
    - "==> request for all case study assumptions"
    - "==> request for confirmation of user assumptions"
    - "==> request for required data for current step"
    - "==> user provides Answer to Question"
    - "==> user provides solution step answer (solution) description"
    - "==> user provides solution step answer (solution) data items"
    - "==> user provides solution step answer (solution) computation"
    - "==> user provides solution step answer (solution) calculation"
    - "==> user provides solution step answer (solution) as numerical"
    - "==> user ends session"
    - "==> user communication not understood"
  ## 4. Categorizing the candidate's (user's) communication
  Determine the nature of the user communication, and provide a response categorizing the user communication into one 
  of the categories in section 3 above using the following guidelines:
  * If the User is asking to start a new case study, respond: "==> start new case study";
  * If the User is confused and asking for help in general (if they write, for example, "help" or "I need help" or "I am confused" or "I don't know 
  how to proceed" or "I don't know what to do next" or "I don't know how to do that" or something similar), respond: "==> request for general help";
  * If the User is asking for help on a specific topic (for example, "How do I define 'utilization?' or "I am confused about how to use utilization" or "What is 'market penetration?'" 
  or "how do I use the growth rate variable?" or "I'm not sure how to compute the annual revenue"), respond: "==> request for help on specific topic: ", 
  followed by your best guess of the topic;
  * If the User is asking for help on a specific solution step (for example, "what is the goal of this step?" or "what is happening in this step conceptually?"
  or "what data do I need for this step?" or "what is the computation in this step?" or "what is the calculation in this step?");
  respond: "==> request for help on solution step: ", followed by your best guess of what kind of help the user wants on the current solution step;
  * If the User is asking for help on a specific computation (for example, "what data do I need for this computation?" or "how do I compute X?" - where X is some 
  intermediate or final result in the solution - or "what computation will get me Y?" - where Y is some intermediate or final result in the solution), 
  respond: "==> request for help on specific computation: ", followed by the computation to help with;
  * If the User is asking for help on a specific calculation (for example, "given the computation, how do I calculate the answer?" or 
  "how do I calculate Z" - where Z is an intermediate or finale result in the solution - or "what is the calculation to use next?"), 
  respond: "==> request for help on specific calculation: ", followed by the calculation to help with;
  * If the user is asking for the case study's assumptions generally, respond: "==> request for all case study assumptions"  - example: "what assumptions am I permitted to make?";
  * If the user is asking for the case study's assumptions on a specific detail or topic, respond: "==> request for case study assumptions on: ", 
  followed by your best gues of one or more topics/details pursuent to which assumtions are being requested;
  * If the user is asking for one or more specific data items from the case study (for example, "what per centage of the population in the target city drinks coffee?"), 
  respond: "request for data item: ", followed by your best guess as to what specific item of data or information the user is requesting;
  * If User is asking for confirmation or rejection of one or more of their (the user's) assumptions, respond: "==> request for confirmation of user 
  assumption: ", followed by what assumptions(s) you believe the User is askinng to have confirmed;
  * If the User is providing an Answer (solution) to the overall Question, respond: "==> Answer to Question: ", followed by the text of the User's answer;
  * If the User is providing a description of the solution (answer) for the current step, respond: "==> user provides solution step answer (solution) description", 
  followed by the text of the User's description;
  * If the User is providing the data items used or to be used in the solution (answer) for the current step, respond: "==> user provides solution step answer (solution) data items", 
  followed by the names (and values, if supplied by the User) of the data items provided by the User;
  * If the User is providing a computation for the solution (answer) for the current step, respond: "==> user provides solution step answer (solution) computation", 
  followed by the text of the User-provided computation;
  * If the User is providing a calculation for the solution (answer) for the current step, respond: "==> user provides solution step answer (solution) calculation", 
  followed by the text of the User-provided calculation (should have numerical values for the variables);
  * If the User is providing a numerical value as the answer (solution) for the current step,spond "==> user provides solution step answer (solution) numerical",
  followed by the numerical value supplied by the user;
  * If the user types one of "quit", "Quit", "end", "End", "end session", "End session", or something similar, respond: "User ends session";
  * If you cannot determine the nature of the User's communication, respond: "==> user communication not understood".
  ## 5. Strict Compliance
  Adhere to the rules strictly. Non-compliance will result in termination.
  - Do not use any other context besides what exists in this prompt!
  - Do not add anything from yourxself!  
  - Do not answer any of the User questions or requests directly! Only categorize the User communication in accordance with above instructions!
  - DO NOT ADD ANYTHING EXTERNAL!!!! Only use information and data from the materials provided below!!!!
  
 ------
 User Communication:
 {user_communication}
 ------
 Guide Information and Data:
 {guide_information}
 ------
 Assumptions:
 {assumptions}
 ------  
 """
 
 print(candidate_message_interpret_prompt)
 
 return candidate_message_interpret_prompt