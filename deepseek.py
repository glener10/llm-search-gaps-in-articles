import datetime
from openai import OpenAI
import pathlib

from common.args import get_args

def main():
  args = get_args()

  filepath = pathlib.Path(args.input)

  client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
  )

  response = client.chat.completions.create(
      model="deepseek-r1:8b",
      messages=[
          {"role": "system", "content": "You are a helpful assistant"},
          {"role": "user", "content": "Hello"},
      ],
      stream=False
  )
  print(response.choices[0].message.content)

if __name__ == "__main__":
  start_time = datetime.datetime.now()
  print(f"🚀 starting process at {start_time}")

  main()

  end_time = datetime.datetime.now()
  total_time = end_time - start_time
  print(f"⏱️ execution finished. Total time: {total_time}")