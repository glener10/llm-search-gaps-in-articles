import datetime
import pathlib
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from common.args import get_input_from_args

DEFAULT_MODEL = "gemini-2.0-flash"

def get_api_key():
  load_dotenv()
  api_key = os.getenv('API_KEY')
  if not api_key:
    raise Exception("❌ missing API_KEY in .env")
  return api_key

def main():
  args = get_input_from_args()
  api_key = get_api_key()

  filepath = pathlib.Path(args.input)
  model = args.model or DEFAULT_MODEL
  
  print(f"📄 processing file: {filepath} with model: {model} output path: {args.output}")
  
  prompt_path = pathlib.Path("prompt.txt")
  if not prompt_path.exists():
    raise FileNotFoundError("❌ prompt.txt not found")
  prompt = prompt_path.read_text(encoding="utf-8").strip()

  client = genai.Client(api_key=api_key)
  response = client.models.generate_content(
    model=model,
    contents=[
        types.Part.from_bytes(
          data=filepath.read_bytes(),
          mime_type='application/pdf',
        ),
        prompt])
  
  gaps_path = pathlib.Path(args.output)
  gaps_path.touch(exist_ok=True)
  with gaps_path.open("a", encoding="utf-8") as f:
    f.write(f"file {args.input} | {model}\n\n{response.text.strip()}\n--------------------------------------------------------------------------\n\n\n")
  print(f"✅ gaps saved to {gaps_path}")

if __name__ == "__main__":
  start_time = datetime.datetime.now()
  print(f"🚀 starting process at {start_time}")

  main()

  end_time = datetime.datetime.now()
  total_time = end_time - start_time
  print(f"⏱️ execution finished. Total time: {total_time}")