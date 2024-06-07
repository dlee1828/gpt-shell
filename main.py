#!/usr/bin/env python3
import sys
from openai import OpenAI
client = OpenAI()

from rich.console import Console
from rich.markdown import Markdown

MESSAGE_HISTORY_LIMIT = 10

def get_question(instruct = False):
  prompt = ""

  while prompt.strip() == "":
    if instruct: 
      print("-----")
      print("Enter text, then press Enter and Ctrl-D to send. Send \"exit\" to end the conversation.") 
      print("-----")
    prompt = sys.stdin.read()

  print("-----")
  return prompt

def get_system_message():
  return {"role": "system", "content": "If you ever write code, make sure it is enclosed in triple backticks."}

# Gets answer, also updates messages 
def get_answer(messages: list[str]) -> str:
  if len(messages) > MESSAGE_HISTORY_LIMIT:
    messages = messages[-MESSAGE_HISTORY_LIMIT:]

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[get_system_message()] + messages
  )
  answer_message = completion.choices[0].message
  messages.append(answer_message)
  return answer_message.content

def create_question_message(question: str):
  return {"role": "user", "content": question}

def conversation():
    console = Console() 

    question = ' '.join(sys.argv[1:])
    if question.strip() == "":
      question = get_question(instruct=True)
    
    messages = [
      create_question_message(question)
    ]

    while question.strip() != "exit":
      answer = get_answer(messages)
      console.print(Markdown(answer))
      print("-----")
      question = get_question()
      messages.append(create_question_message(question))

conversation()
