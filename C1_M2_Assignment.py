# ==========================================
# Book Tracker Application
# ==========================================


class Book:
    def __init__(self, title, author, on_shelf, borrower, overdue, on_hold):
        self.title = title
        self.author = author
        self.on_shelf = on_shelf
        self.borrower = borrower
        self.overdue = overdue
        self.on_hold = on_hold

    def availability_status(self):
        if self.on_shelf and not self.on_hold:
            print("Book is available to be borrowed")
        else:
            print("Book is not available to be borrowed")

    def check_overdue(self):
        if self.overdue:
            print(f"Book is overdue - Contact {self.borrower} to return it")
        else:
            self.on_hold = True
            print("Book has been put on hold")

    def generate_prompt(self, due_date):
        prompt = (
            f"Please write a polite email to {self.borrower}, "
            f"reminding them to return the book '{self.title}' "
            f"by {self.author}. The book was due on {due_date}."
        )
        return prompt


def find_borrower_email(borrower_name, borrowers_list):
    for borrower in borrowers_list:
        if borrower["name"] == borrower_name:
            return borrower["email"]
    return None


def generate_email(person_name, book_name, book_author, due_date):
    return f"""Subject: Reminder to Return Library Book

Dear {person_name},

I hope this message finds you well. This is a friendly reminder that the book "{book_name}" by {book_author} was due back at the library on {due_date}.

Please return the book at your earliest convenience to avoid any late fees. If you have already returned it, kindly disregard this message.

Best regards,
Library Team
"""


# ==========================================
# Application Execution
# ==========================================

def main():

    # Create book instance
    book = Book(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        on_shelf=False,
        borrower="Arthur Dent",
        overdue=True,
        on_hold=False
    )

    # Borrower database
    borrowers_list = [
        {"name": "Alice Johnson", "email": "alice.johnson@dlailibrary.com", "phone": "+1111111111"},
        {"name": "Bob Smith", "email": "bob.smith@dlailibrary.com", "phone": "+2222222222"},
        {"name": "Arthur Dent", "email": "arthur.dent@dlailibrary.com", "phone": "+3333333333"},
        {"name": "Diana Prince", "email": "diana.prince@dlailibrary.com", "phone": "+4444444444"}
    ]

    print("\n--- BOOK STATUS CHECK ---")
    book.availability_status()

    print("\n--- OVERDUE CHECK ---")
    book.check_overdue()

    print("\n--- FINDING BORROWER EMAIL ---")
    borrower_email = find_borrower_email(book.borrower, borrowers_list)

    if borrower_email:
        print(f"{book.borrower}'s email is: {borrower_email}")
    else:
        print("Borrower email not found.")

    print("\n--- GENERATED EMAIL ---")
    due_date = "16 November 2024"
    email_text = generate_email(book.borrower, book.title, book.author, due_date)
    print(email_text)


if __name__ == "__main__":
    main()

