

from tools import build_request
from model import ask_ai


def display_menu():
    print("\n" + "=" * 45)
    print("             STUDYMATE AI")
    print("       Your Local AI Study Tutor")
    print("=" * 45)
    print("1. Explain a topic")
    print("2. Summarize study notes")
    print("3. Generate a quiz")
    print("4. Create a study plan")
    print("5. Exit")
    print("-" * 45)


def main():
    print("Welcome to StudyMate AI!")
    print("Powered by a local AI model using Ollama.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Good luck with your studies. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
            continue

        try:
            if choice == "2":
                print("\nPaste your study notes in one line.")
                topic = input("Notes: ").strip()
            else:
                topic = input("\nEnter your topic: ").strip()

            days = 7

            if choice == "4":
                raw_days = input(
                    "How many days do you have? (1-30): "
                ).strip()

                if not raw_days.isdigit():
                    print("Please enter a whole number.")
                    continue

                days = int(raw_days)

            prompt = build_request(choice, topic, days)

            print("\nStudyMate AI is thinking...")
            answer = ask_ai(prompt)

            print("\n" + "=" * 45)
            print("                 RESULT")
            print("=" * 45)
            print(answer)
            print("=" * 45)

        except (ValueError, RuntimeError, FileNotFoundError) as error:
            print(f"\nError: {error}")

        except KeyboardInterrupt:
            print("\nOperation cancelled.")

        except Exception as error:
            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
