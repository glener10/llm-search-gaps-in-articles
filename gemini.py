import datetime
import pathlib
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from common.args import get_args
from common.prompt import read_prompt
from common.output import persist_output

DEFAULT_MODEL = "gemini-2.0-flash"

def get_api_key():
  load_dotenv()
  api_key = os.getenv('API_KEY')
  if not api_key:
    raise Exception("❌ missing API_KEY in .env")
  return api_key

def main():
  args = get_args()
  api_key = get_api_key()

  filepath = pathlib.Path(args.input)
  model = args.model or DEFAULT_MODEL
  
  print(f"📄 processing file: {filepath} with model: {model} output path: {args.output}")
  
  prompt = read_prompt()

  client = genai.Client(api_key=api_key)
  response = client.models.generate_content(
    model=model,
    contents=[
        types.Part.from_bytes(
          data=filepath.read_bytes(),
          mime_type='application/pdf',
        ),
        prompt])
  
  persist_output(args.output, args.input, model, response.text.strip())

if __name__ == "__main__":
  start_time = datetime.datetime.now()
  print(f"🚀 starting process at {start_time}")

  main()

  end_time = datetime.datetime.now()
  total_time = end_time - start_time
  print(f"⏱️ execution finished. Total time: {total_time}")