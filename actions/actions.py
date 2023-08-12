import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

book_database = [
    {"title": "Python for Beginners", "author": "John Smith", "publication_year": 2018},
    {"title": "Introduction to Algorithms", "author": "Thomas Cormen", "publication_year": 2009},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": 1925},
    {"title": "Python Crash Course", "author": "Eric Matthes", "publication_year": 2015},
    {"title": "Clean Code: A Handbook of Agile Software Craftsmanship", "author": "Robert C. Martin", "publication_year": 2008},
    {"title": "Introduction to the Theory of Computation", "author": "Michael Sipser", "publication_year": 2012},
    {"title": "The Pragmatic Programmer: Your Journey to Mastery", "author": "Andrew Hunt, David Thomas", "publication_year": 1999},
    {"title": "Cracking the Coding Interview: 189 Programming Questions and Solutions", "author": "Gayle Laakmann McDowell", "publication_year": 2015},
    {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "publication_year": 2008},
    {"title": "Algorithms, Part I", "author": "Robert Sedgewick, Kevin Wayne", "publication_year": 2011},
    {"title": "Programming Language Pragmatics", "author": "Michael L. Scott", "publication_year": 2015},
    {"title": "Design Patterns: Elements of Reusable Object-Oriented Software", "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "publication_year": 1994},
    {"title": "The C Programming Language", "author": "Brian W. Kernighan, Dennis M. Ritchie", "publication_year": 1988},
    {"title": "Operating System Concepts", "author": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne", "publication_year": 2018},
    {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell, Peter Norvig", "publication_year": 2016},
    {"title": "Database System Concepts", "author": "Abraham Silberschatz, Henry F. Korth, S. Sudarshan", "publication_year": 2019},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein", "publication_year": 2009},
    {"title": "Head First Design Patterns", "author": "Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra", "publication_year": 2004},
    {"title": "Deep Learning", "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "publication_year": 2016},
    {"title": "The Mythical Man-Month: Essays on Software Engineering", "author": "Frederick P. Brooks Jr.", "publication_year": 1995},
    {"title": "Introduction to the Design and Analysis of Algorithms", "author": "Anany Levitin", "publication_year": 2011},
    {"title": "The Algorithm Design Manual", "author": "Steven S. Skiena", "publication_year": 2008},
    {"title": "Structure and Interpretation of Computer Programs", "author": "Harold Abelson, Gerald Jay Sussman, Julie Sussman", "publication_year": 1996},


]


class SearchBook(Action):

    def name(self) -> Text:
        return "action_search_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        book_title = tracker.latest_message.get("text")

        matching_books = [book for book in book_database if book_title.lower() in book["title"].lower()]

        if matching_books:

            book_details = random.choice(matching_books)
            message = f"Book found:\nTitle: {book_details['title']}\nAuthor: {book_details['author']}" \
                      f"\nPublication Year: {book_details['publication_year']}"
        else:
            message = "Book not found."

        dispatcher.utter_message(text=message)

        return []
