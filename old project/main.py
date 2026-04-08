# TODO: Import your utils
from parser_utils import extract_errors, save_report
# TODO: Define main()
# TODO: Add the Main Gate

def main() -> None:
  list_of_errors: str[str] = extract_errors("errors.txt")
  save_report("report.txt", list_of_errors)

if __name__ == "__main__":
  main()
  print("Process completed successfully.")