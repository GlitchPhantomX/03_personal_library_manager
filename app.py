import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        """Load library data from a file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        """Save library data to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        """Add a new book to the library."""
        title = input("Enter book title: ")
        author = input("Enter author: ")
        try:
            year = int(input("Enter publication year: "))
        except ValueError:
            print("Invalid year format. Please enter a number.")
            return
        genre = input("Enter genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }
        self.library.append(book)
        self.save_library()
        print(f"\nBook '{title}' added successfully!\n")

    def remove_book(self):
        """Remove a book from the library by title."""
        title = input("Enter the title of the book to remove: ")
        for book in self.library:
            if book["title"].lower() == title.lower():
                self.library.remove(book)
                self.save_library()
                print(f"\nBook '{title}' removed successfully!\n")
                return
        print("Book not found.\n")

    def search_book(self):
        """Search for books by title or author."""
        query = input("Enter book title or author to search: ").lower()
        results = [book for book in self.library if query in book["title"].lower() or query in book["author"].lower()]
        
        if results:
            print("\nSearch Results:")
            for book in results:
                self.display_book(book)
        else:
            print("No matching books found.\n")

    def display_books(self):
        """Display all books in the library."""
        if not self.library:
            print("\nNo books in the library.\n")
            return
        print("\nLibrary Collection:")
        for book in self.library:
            self.display_book(book)

    def display_statistics(self):
        """Display statistics about the library."""
        total_books = len(self.library)
        if total_books == 0:
            print("\nNo books in the library.\n")
            return
        read_books = sum(1 for book in self.library if book["read"])
        read_percentage = (read_books / total_books) * 100
        print(f"\nTotal books: {total_books}")
        print(f"Books read: {read_books} ({read_percentage:.2f}% completed)\n")

    @staticmethod
    def display_book(book):
        """Helper function to display book details."""
        read_status = "Read" if book["read"] else "Unread"
        print(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} [{read_status}]")

    def run(self):
        """Main menu loop for the Personal Library Manager."""
        while True:
            print("\nPersonal Library Manager")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.run()
