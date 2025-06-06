import argparse

def get_input_from_args():
  parser = argparse.ArgumentParser(description="article in pdf to search gaps")
  parser.add_argument('-i', '--input', required=True, help='path to the input PDF file')
  args = parser.parse_args()
  return args.input