

def explain_topic(topic: str) -> str:
    if not topic.strip():
        raise ValueError("Please enter a topic.")

    return f"""
Explain this topic to a beginner: {topic}

Include:
1. Definition
2. Step-by-step explanation
3. Practical example
4. Short recap
"""


def summarize_notes(notes: str) -> str:
    if not notes.strip():
        raise ValueError("Please enter some study notes.")

    return f"""
Summarize the following study notes.

Include:
1. Main idea
2. Important points
3. Key terms
4. Short revision summary

STUDY NOTES:
{notes}
"""


def generate_quiz(topic: str) -> str:
    if not topic.strip():
        raise ValueError("Please enter a topic.")

    return f"""
Create 5 multiple-choice questions about: {topic}

Provide four options (A, B, C, D) for each question.
Include an answer key and a short explanation for each answer.
Use beginner-to-intermediate difficulty.
"""


def create_study_plan(topic: str, days: int) -> str:
    if not topic.strip():
        raise ValueError("Please enter a topic.")

    if not 1 <= days <= 30:
        raise ValueError("Days must be between 1 and 30.")

    return f"""
Create a realistic {days}-day study plan for {topic}.

For every day, include:
- Learning topics
- Practice activity
- Revision task

Include a final review and self-test when appropriate.
"""


def build_request(choice: str, topic: str, days: int = 7) -> str:
    if choice == "1":
        return explain_topic(topic)

    if choice == "2":
        return summarize_notes(topic)

    if choice == "3":
        return generate_quiz(topic)

    if choice == "4":
        return create_study_plan(topic, days)

    raise ValueError("Invalid choice. Choose 1, 2, 3, or 4.")
