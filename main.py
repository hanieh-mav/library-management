import ast , os


def check_file_exist(filename):
    check = os.path.getsize(filename) > 0
    return check



class User:

    if check_file_exist('user.txt'):
        with open('user.txt','r') as read_obj:
            lastline = read_obj.readlines()[-1]
            lastline_dict = ast.literal_eval(lastline)
            __id = lastline_dict['Id']
    else:
        __id = 0


    def __init__(self):
        self.__firstname = None
        self.__lastname = None
        self.__email = None
        self.__username = None
        self.__password = None


    @property
    def getter(self):
        return self.__username


    def __searchUserinfo(self,str1,varible):
        try:
            with open('user.txt', 'r') as read_obj:
                for line in read_obj:
                    dict_line = ast.literal_eval(line)
                    if (dict_line[str1] == varible):
                        return True
                    else:
                        continue
                            
        except FileNotFoundError as error:
            print(error)


    def register(self):
        self.__firstname = input("Enter Firstname: ")
        self.__lastname = input("Enter lastname: ") 
        self.__email = input("Enter email: ")
        self.__username = input("Enter username: ")
        self.__password = input("Enter password: ")
        self.__pass_check = input("Enter password again: ")
        User.__id += 1
        register = False
        
        if self.__searchUserinfo('username',self.__username):
            print('This Username is taken . try again ;)')
        elif self.__password != self.__pass_check:
            print('Passwords must be match , try again ;)')
        else:
            user = {
            'Id':User.__id,
            'firstname':self.__firstname,
            'lastname':self.__lastname,
            'email':self.__email,
            'username':self.__username,
            'password':self.__password,
            }

            with open('user.txt','a') as write_obj:
                write_obj.write(str(user)+'\n')
                print("""
                 You register successfully!
                 you can login 
                """)
                register = True
        return register


    def login(self):
        self.__username = input("Enter username: ")
        self.__password = input("Enter password: ")

        username = self.__searchUserinfo('username',self.__username)
        password = self.__searchUserinfo('password',self.__password)

        if username and password:
            return True
        else:
            return False


    @staticmethod
    def __deleteLine(str1,varible):
        with open("user.txt", "r") as f:
            lines = f.readlines()
        with open("user.txt", "w") as f:
            for line in lines:
                line_dict = ast.literal_eval(line)
                if line_dict[str1] != varible:
                    f.write(str(line_dict)+'\n')


    def deleteUser(self):
        self.__id = input('Please enter Id  for security: ')
        id = int(self.__id)
        check_exist = self.__searchUserinfo('Id',id)
        if check_exist:
            self.__deleteLine('Id',id)
        else:
            print('This Id not exist! find your id from information')
       

    def __str__(self):
        try:
            with open('user.txt', 'r') as read_obj:
                for line in read_obj:
                    dict_line = ast.literal_eval(line)
                    if (dict_line['username'] == self.__username):
                        return f"""
                        Id:{dict_line['Id']},
                        firstname:{dict_line['firstname']},
                        lastname:{dict_line['lastname']},
                        email:{dict_line['email']},
                        username:{dict_line['username']},
                        password:{dict_line['password']},
                        """
                    else:
                        continue
                            
        except FileNotFoundError as error:
            print(error)
        

class Book:

    if check_file_exist('book.txt'):
        with open('book.txt','r') as read_obj:
            lastline = read_obj.readlines()[-1]
            lastline_dict = ast.literal_eval(lastline)
            __id = lastline_dict['Id']
    else:
        __id = 0


    def __init__(self):
        self.__bookname = None
        self.__author = None
        self.__year = None
        self.__language = None
    

    def donateBook(self):
        self.__bookname = input('Enter name of book: ')
        self.__author = input('Enter name of author: ')
        self.__year = input('Enter year that book published: ')
        self.__language = input('Enter language of book: ')
        Book.__id += 1
        
        book = {
            'Id':Book.__id,
            'bookname':self.__bookname,
            'author':self.__author,
            'year':self.__year,
            'language':self.__language,
            }

        with open('book.txt','a') as write_obj:
                write_obj.write(str(book)+'\n')
                print("""
                 You Donate successfully!
                 Thank you
                """)

    
    def searchByBookName(self):
        self.__bookname = input('Enter name of book: ')
        with open('book.txt','r') as read_obj:
            for line in read_obj:
                book_dict = ast.literal_eval(line)
                if book_dict['bookname'] == self.__bookname:
                    print(f"""
                        Id:{book_dict['Id']}
                        bookname:{book_dict['bookname']},
                        author:{book_dict['author']},
                        year:{book_dict['year']},
                        language:{book_dict['language']},
                        """)
                else:
                    continue


    def searchByAuthor(self):
        self.__author = input('Enter name of author: ')
        with open('book.txt','r') as read_obj:
            for line in read_obj:
                book_dict = ast.literal_eval(line)
                if book_dict['author'] == self.__author:
                    print(f"""
                        Id:{book_dict['Id']},
                        bookname:{book_dict['bookname']},
                        author:{book_dict['author']},
                        year:{book_dict['year']},
                        language:{book_dict['language']},
                        """)
                else:
                    continue


    def __seachBookId(self,id):
        with open('book.txt','r') as read_obj:
            for line in read_obj:
                book_dict = ast.literal_eval(line)
                if book_dict['Id'] == id:
                    return True
                else:
                    continue


    @staticmethod
    def __deleteLine(str1,varible):
        with open("book.txt", "r") as f:
            lines = f.readlines()
        with open("book.txt", "w") as f:
            for line in lines:
                book_dict = ast.literal_eval(line)
                if book_dict[str1] != varible:
                    f.write(str(book_dict)+'\n')
       

    def borrow(self,user):
        self__id = input('Enter ID of book: ')
        id = int(self__id)
        if self.__seachBookId(id):
            with open('borrow.txt', 'a') as write_obj:
                borrow = {
                    'BookId':id,
                    'user':user,
                }
                write_obj.write(str(borrow)+"\n") 
                self.__deleteLine('Id',id)
                print("""
                 You borrowed successfully!
                """)  
    
        else:
            print('This book not availble')


    @staticmethod
    def showAvailbleBook():
        with open('book.txt','r') as read_obj:
            for line in read_obj:
                book_dict = ast.literal_eval(line)
                print(book_dict)

    

def search_book_menu():
    print("""
    1 - Search by BookName
    2 - Search by Author
    """)


def search_book():
    choice = True
    search_book_menu()
    book = Book()
    choice = int(input("welcome ! choice from menu : ")) 
    while True:
        if choice == 1:
            book.searchByBookName()
            break

        elif choice == 2:
            book.searchByAuthor()
            break   
        else:
            print("Invalid choice Try again")
            sign_in()


def sign_in_menu():

    print("""
    1 - show account information
    2 - Donate book
    3 - show avaible books
    4 - borrow book
    5 - search book
    6 - delete my account
    """)      


def sign_in():
    sign_in_menu()
    choice = int(input("welcome ! choice from menu : ")) 
    book = Book()
    while True:
        if choice == 1:
            print(user)
            sign_in()
        elif choice == 2:
            book.donateBook()
            sign_in()
        elif choice == 3:
            Book.showAvailbleBook()
            sign_in()
        elif choice == 4:
            book.borrow(user.getter)
            sign_in()
        elif choice == 5:
            search_book()
            sign_in()
        elif choice == 6:
            user.deleteUser()
            continue
        else:
             print("Invalid choice ! Try again :)")


def mainMenu():

    print("""
        Welcome To our Library 
        1 - login
        2- Register
    """)







def menu():
    while True:
        mainMenu()
        choice = input('Please,Choose from menu \n')
        choice = int(choice)
        if choice == 1:
            login = user.login()
            if login:
                sign_in()
            else:
                print('username or password is wrong try again')
                menu()
            break
        elif choice == 2:
            register = user.register()
            if register:
                menu()
            else:
                print('Try again :)')
                menu()
            break
        else:
            print("Invalid choice ! Try again :)")

    
user = User()      
menu()

         