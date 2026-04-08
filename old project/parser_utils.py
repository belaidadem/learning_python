# TODO: Add imports if needed
# TODO: Define extract_errors with type hints
# TODO: Define save_report with type hints and try/except

def extract_errors(log_file_path: str) -> list[str]:
  content: list[str] = []
  try:
    with open(log_file_path, "r") as f:
      for line in f:
        if "ERROR" in line:
          content.append(line.strip())
  except FileNotFoundError:
    print(f"Error: File '{log_file_path}' not found.")
  return content

def save_report(filename: str, errors: list[str]) -> None:
  with open(filename, "w") as f:
    for error in errors:
      print(error, file=f)

if __name__ == "__main__":
  save_report("", [])