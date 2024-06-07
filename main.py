#!/usr/bin/env python3
import sys
from openai import OpenAI
client = OpenAI()

from rich.console import Console
from rich.markdown import Markdown

def request_prompt():
  print("Enter your request, then press Enter and then Ctrl-D (EOF) to submit.") 
  prompt = sys.stdin.read()
  print("Processing...")
  return prompt

def run():
  prompt = ' '.join(sys.argv[1:])
  while prompt.strip() == "":
    prompt = request_prompt()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "If you ever write code, make sure it is enclosed in triple backticks."},
      {"role": "user", "content": prompt}
    ]
  )

  content = (completion.choices[0].message.content)
  console = Console() 
  console.print(Markdown(content))

run()
