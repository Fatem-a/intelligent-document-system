import sys
from src.preprocessing.text_cleaner import clean_text

def main():
    print("Intelligent Document Retrieval & Analysis System")
    print("-----------------------------------------------")
    print(f"Python version: {sys.version}")
    print("Project environment is ready!")

    sample_text = "  Intelligent    Document   Processing  "
    cleaned_text = clean_text(sample_text)

    print(f"Original text: {sample_text}")
    print(f"Cleaned text: {cleaned_text}")


if __name__ == "__main__":
    main()
