from pymongo import MongoClient

# Create a MongoClient to the running mongod instance
client = MongoClient('localhost', 27017)

# Get a reference to a particular database
db = client['library']

# Reference a particular collection in the database
books = db['books']
book_data = []

# Now you can use the 'books' collection to perform queries
book_data.extend([
    {"SerialNo": "LIB-013", "Book_Name": "Discrete Mathematics and Its Applications", "Shelf_No": "B3", "Row_No": "4", "Author": "Kenneth H. Rosen", "Genre": ["textbook", "mathematics"], "Contents": ["Logic and Propositional Calculus", "Sets and Functions", "Algorithms and the Growth of Functions", "Integers and Matrices"]},
    {"SerialNo": "LIB-014", "Book_Name": "Operating System Concepts", "Shelf_No": "B4", "Row_No": "1", "Author": "Abraham Silberschatz", "Genre": ["textbook", "computer science"], "Contents": ["Introduction", "Process Management", "Memory Management", "File System"]},
    {"SerialNo": "LIB-015", "Book_Name": "Artificial Intelligence: A Modern Approach", "Shelf_No": "B4", "Row_No": "2", "Author": "Stuart Russell", "Genre": ["textbook", "computer science"], "Contents": ["Intelligent Agents", "Problem Solving", "Knowledge and Reasoning", "Uncertain Knowledge and Reasoning"]},
    {"SerialNo": "LIB-016", "Book_Name": "Digital Design and Computer Architecture", "Shelf_No": "B4", "Row_No": "3", "Author": "Sarah Harris", "Genre": ["textbook", "computer science"], "Contents": ["Digital Design", "Computer Architecture", "Assembly Language", "Processor Design"]},
    {"SerialNo": "LIB-017", "Book_Name": "Database System Concepts", "Shelf_No": "B4", "Row_No": "4", "Author": "Abraham Silberschatz", "Genre": ["textbook", "computer science"], "Contents": ["Introduction", "Relational Model", "SQL", "Data Storage and Querying"]},
    {"SerialNo": "LIB-018", "Book_Name": "Computer Networks", "Shelf_No": "B5", "Row_No": "1", "Author": "Andrew S. Tanenbaum", "Genre": ["textbook", "computer science"], "Contents": ["Introduction", "The Physical Layer", "The Data Link Layer", "The Network Layer"]},
    {"SerialNo": "LIB-019", "Book_Name": "Modern Control Systems", "Shelf_No": "B5", "Row_No": "2", "Author": "Richard C. Dorf", "Genre": ["textbook", "engineering"], "Contents": ["Introduction", "Mathematical Models of Systems", "State Variable Models", "Feedback Control System Characteristics"]},
    {"SerialNo": "LIB-020", "Book_Name": "Fundamentals of Electric Circuits", "Shelf_No": "B5", "Row_No": "3", "Author": "Charles K. Alexander", "Genre": ["textbook", "engineering"], "Contents": ["Introduction", "Basic Laws", "Circuit Theorems", "Operational Amplifiers"]},
    {"SerialNo": "LIB-021", "Book_Name": "Thermodynamics: An Engineering Approach", "Shelf_No": "B5", "Row_No": "4", "Author": "Yunus A. Cengel", "Genre": ["textbook", "engineering"], "Contents": ["Introduction and Basic Concepts", "Energy, Energy Transfer, and General Energy Analysis", "Properties of Pure Substances", "Energy Analysis of Closed Systems"]},
    {"SerialNo": "LIB-022", "Book_Name": "Mechanics of Materials", "Shelf_No": "B6", "Row_No": "1", "Author": "Russell C. Hibbeler", "Genre": ["textbook", "engineering"], "Contents": ["Stress", "Strain", "Mechanical Properties of Materials", "Axial Load"]}
])


# Insert a document into the 'books' collection
for book in book_data:
    result = books.insert_one(book)
   # print('One book: {0}'.format(result.inserted_id))

# Print all books in the 'books' collection
for book in books.find():
    print(book)
