import os
from PyPDF2 import PdfReader

def get_api_key():
  api_key = os.getenv('API_KEY')
  if not api_key:
    raise Exception("❌ missing API_KEY in .env")
  return api_key