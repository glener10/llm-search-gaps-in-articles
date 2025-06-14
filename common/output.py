import pathlib

def persist_output(path, input, model, response):
  gaps_path = pathlib.Path(path)
  gaps_path.touch(exist_ok=True)
  separator = "-" * 100
  with gaps_path.open("a", encoding="utf-8") as f:
    f.write("file " + input + " | " + model + "\n\n" + response + "\n" + separator + "\n\n\n")
  print(f"✅ gaps saved to {gaps_path}")