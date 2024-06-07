import sys
from openai import OpenAI
client = OpenAI()

from rich.console import Console
from rich.markdown import Markdown


def run():
  if len(sys.argv) < 2:
    print("Please enter a prompt.")
    return

  prompt = sys.argv[1]
  if prompt.strip() == "":
    print("Please enter a prompt.")
    return

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