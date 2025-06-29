import argparse


def get_args():
  parser = argparse.ArgumentParser(description="article in pdf to search gaps")
  parser.add_argument("-i", "--input", required=True, help="path to the input PDF file")
  parser.add_argument("-m", "--model", required=False, help="model for llm")
  parser.add_argument(
    "-o",
    "--output",
    required=False,
    default="gaps.txt",
    help="path to the output file (default: gaps.txt)",
  )
  args = parser.parse_args()
  return args
