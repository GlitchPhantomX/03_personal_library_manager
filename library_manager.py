import json

filename = "library.json"
library = []

def load_library():
    global library
    try:
        with open(filename, "r") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        library = []

def save_library():
    with open(filename, "w") as file:
        json.dump(library, file, indent=4)

def add_book():
    title = input("📖 Enter book title: ")
    author = input("✍️ Enter author: ")
    try:
        year = int(input("📅 Enter publication year: "))
    except ValueError:
        print("❌ Invalid year format. Please enter a number.")
        return
    genre = input("🎭 Enter genre: ")
    read_status = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library()
    print(f"\n📚 Book '{title}' added successfully! 🎉\n")

def remove_book():
    title = input("🗑️ Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print(f"\n✅ Book '{title}' removed successfully!\n")
            return
    print("❌ Book not found.\n")

def search_book():
    query = input("🔍 Enter book title or author to search: ").lower()
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    
    if results:
        print("\n🔎 Search Results:")
        for book in results:
            display_book(book)
    else:
        print("❌ No matching books found.\n")

def display_books():
    if not library:
        print("\n📭 No books in the library.\n")
        return
    print("\n📚 Library Collection:")
    for book in library:
        display_book(book)

def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("\n📭 No books in the library.\n")
        return
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    print(f"\n📊 Total books: {total_books}")
    print(f"📖 Books read: {read_books} ({read_percentage:.2f}% completed)\n")

def display_book(book):
    read_status = "✅ Read" if book["read"] else "❌ Unread"
    print(f"- 📖 {book['title']} by {book['author']} ({book['year']}) - 🎭 {book['genre']} [{read_status}]")

def run():
    load_library()
    while True:
        print("\n📚 Personal Library Manager")
        print("1️⃣  Add a book")
        print("2️⃣  Remove a book")
        print("3️⃣  Search for a book")
        print("4️⃣  Display all books")
        print("5️⃣  Display statistics")
        print("6️⃣  Exit")
        
        choice = input("👉 Enter your choice (1-6): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    run()