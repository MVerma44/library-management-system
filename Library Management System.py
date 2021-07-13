class Library:

    # TO CREATE THEIR OWN LIBRARY
    def __init__(self, list_of_books, name):
        self.list_of_books = list_of_books
        self.name = name
        self.list_dict = {}

    # TO DISPLAY THE LIST OF BOOKS
    def display(self):
        print(f"The books present in the {self.name}'s library\t{self.list_of_books}")

    # TO LEND THE BOOK
    def issue_book(self, book_name, lender_name):
        if book_name in self.list_of_books:
            self.list_dict.update({book_name:lender_name})
            print(f"The book '{book_name}' is successfully issued to '{lender_name}'")
            self.list_of_books.remove(book_name)

        else:
            print("The book you want to issue is not available in the library")

    # TO ADD A BOOK IN A LIBRARY
    def add_book(self, book_name, user_name):
        self.list_of_books.append(book_name)
        print(f"The book '{book_name}' given by '{user_name}' has been added to the list of books")

    # TO RETURN A BOOK TO THE LIBRARY
    def return_book(self, book_name):
        if lender_name in self.list_dict.values():
            self.list_dict.pop(book_name)
            print(f"The book '{book_name}' is successfully returned to the library")
            self.list_of_books.append(book_name)   # THIS ONE IS EDITED

        else:
            print(f"Sir you haven't issued the book '{book_name}', so how can you return it")

    # TO REMOVE A BOOK FROM THE LIBRARY IF PRESENT
    def remove_book(self, book_name):
        if book_name in self.list_of_books:
            self.list_of_books.remove(book_name)
            print(f"The book '{book_name}' is successfully removed from the list of books")

        else:
            print(f"The book '{book_name}' you wish to remove, is not available in the library")

if __name__ == '__main__':

    instance_name = input("What name you want to give to your Library\n")
    instance_list = list()
    no_of_book = int(input("Enter the number of books you want to add in your library: "))

    for items in range(no_of_book):
        items = input(f"Name the book {items + 1} : ")
        instance_list.append(items)

    instance_name = Library(instance_list, instance_name)

    while(True):
        print(f"\t\t\tWelcome to the {instance_name.name}'s Library")
        print("1. Display the books")
        print("2. Issue a book")
        print("3. Add a book")
        print("4. Return a book")
        print("5. Remove a book")

        choice = input()

        if choice not in ['1', '2', '3', '4', '5']:
            print("Please select the valid option")
            continue

        else:
            choice = int(choice)

        if choice == 1: # TO DISPLAY THE LIST OF BOOKS IN THE LIBRARY
            instance_name.display()

        elif choice == 2: # TO LEND ANY BOOK IF PRESENT IN THE LIBRARY
            book_name = input("Enter the name of the book you want to issue: ")
            lender_name = input("Enter your good name: ")
            instance_name.issue_book(book_name, lender_name)

        elif choice == 3: # TO ADD A BOOK TO THE LIST OF BOOKS
            book_name = input("Enter the name of the book you want to add: ")
            user_name = input("Enter your good name: ")
            instance_name.add_book(book_name, user_name)

        elif choice == 4: # TO RETURN A BOOK IF YOU HAVE ISSUED ANY
            book_name = input("Enter the name of the book you want to return: ")
            user_name = input("Enter your good name: ")
            instance_name.return_book(book_name, user_name)

        elif choice == 5: # TO REMOVE THE BOOK IS PRESENT IN THE LIBRARY
            book_name = input("Which book you want to remove from the library: ")
            instance_name.remove_book(book_name)

        else:
            print("Please select the valid option only")

        print("Press 1 to continue and 0 to quit")
        choice2 = ""
        while(choice2 != "0" and choice2 != "1"):
            choice2 = input()
            if (choice2) == "0":
                exit()

            elif choice2 == "1":
                continue

            else:
                print("Select the valid option only")
