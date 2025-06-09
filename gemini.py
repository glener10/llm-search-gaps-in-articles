import datetime
from google import genai
from google.genai import types
import pathlib

from common.args import get_input_from_args
from common.env import get_api_key

input_file = get_input_from_args()
api_key = get_api_key()

start_time = datetime.datetime.now()
print(f"🚀 Starting process at {start_time}")

filepath = pathlib.Path(input_file)

client = genai.Client(api_key=api_key)

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)

end_time = datetime.datetime.now()
total_time = end_time - start_time
print(f"⏱️ execution finished. Total time: {total_time}")
