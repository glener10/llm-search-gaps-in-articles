import datetime
import pathlib
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from src.utils.args import get_args
from src.utils.prompt import read_prompt
from src.utils.output import persist_output

DEFAULT_MODEL = "gemini-2.5-flash-preview-05-20"


def get_api_key():
  load_dotenv()
  api_key = os.getenv("API_KEY")
  if not api_key:
    raise Exception("❌ missing API_KEY in .env")
  return api_key


def main():
  args = get_args()
  api_key = get_api_key()

  filepath = pathlib.Path(args.input)
  model = args.model or DEFAULT_MODEL

  print(
    f"📄 processing file: {filepath} with model: {model} output path: {args.output}"
  )

  prompt = read_prompt()

  client = genai.Client(api_key=api_key)
  response = client.models.generate_content(
    model=model,
    contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type="application/pdf",
      ),
      prompt,
    ],
  )

  output_text = (
    response.text.strip() if hasattr(response, "text") and response.text else ""
  )
  persist_output(args.output, args.input, model, output_text)


if __name__ == "__main__":
  start_time = datetime.datetime.now()
  print(f"🚀 starting process at {start_time}")

  main()

  end_time = datetime.datetime.now()
  total_time = end_time - start_time
  print(f"⏱️ execution finished. Total time: {total_time}")
