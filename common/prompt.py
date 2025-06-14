import pathlib

def read_prompt():
  prompt_path = pathlib.Path("prompt.txt")
  if not prompt_path.exists():
    raise FileNotFoundError("❌ prompt.txt not found")
  return prompt_path.read_text(encoding="utf-8").strip()