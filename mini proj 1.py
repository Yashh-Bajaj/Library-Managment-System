class Library:
    def __init__(self,lbooks,lname):
        self.lbooks=lbooks
        self.lname=lname
        self.lendrecord={}

    def Booksdisplay(self):
        print(self.lbooks)

    def Lendbooks(self):
        book=input("Enter book name")
        if book not in self.lbooks :
            print("Please Enter valid Input")
        elif book in self.lbooks :
            name=input("Enter your Name")
            self.lbooks.remove(book)
            self.lendrecord[book]=name
            print("Your Book is ready Take it away from counter")
        else:
            if self.lendrecord.get(book):
                print(f"Book does not exist in library this book taken by {self.lendrecord[book]}")

    def Donatebook(self):
        book=input("Enter book name")
        self.lbooks.append(book)
    def Returnbook(self):
        book=input("Which book you have to return")
        name=input("What is your name")
        if book in self.lendrecord:
            self.lbooks.append(book)
            del self.lendrecord[book]
        else:
            print("Invalid Input")


if __name__=='__main__':
    bookname=["Python","Cpp","Java","C"]
    yash=Library(bookname,"Yash Bajaj")
    while True:
        user=input("1. If you want to Display list of book press display\n"
                   "2. If you want to Lend Books press lend\n"
                   "3. If you want to Donate books press donate\n"
                   "4. If you wamt to Return book press return\n"
                   "5. Want to quit press q\n")

        if user=="Display" or user=="display":
            yash.Booksdisplay()
        elif user=="Lend" or user=="lend":
            yash.Lendbooks()
        elif user=="donate" or user=="Donate":
            yash.Donatebook()
        elif user=="return" or user=="Return":
            yash.Returnbook()
        elif user=="q" or user=="Q":
            quit()
        else:
            print("Wrong Input Please Try Again")

