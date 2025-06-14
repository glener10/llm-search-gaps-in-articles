import argparse

def get_input_from_args():
  parser = argparse.ArgumentParser(description="article in pdf to search gaps")
  parser.add_argument('-i', '--input', required=True, help='path to the input PDF file')
  parser.add_argument('-m', '--model', required=False, help='model for llm')
  args = parser.parse_args()
  return args