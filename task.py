import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create tables
def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        seasonal TEXT,
        allergens TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        flavor_suggestion TEXT,
        allergy_concerns TEXT
    )
    ''')
    conn.commit()

# Function to add a seasonal flavor
def add_flavor(name, seasonal, allergens):
    cursor.execute('INSERT INTO flavors (name, seasonal, allergens) VALUES (?, ?, ?)', (name, seasonal, allergens))
    conn.commit()
    print(f'Flavor "{name}" added successfully!')

# Function to add an ingredient
def add_ingredient(name, quantity):
    cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    print(f'Ingredient "{name}" added successfully!')

# Function to record customer suggestions
def add_suggestion(customer_name, flavor_suggestion, allergy_concerns):
    cursor.execute('INSERT INTO suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)',
                   (customer_name, flavor_suggestion, allergy_concerns))
    conn.commit()
    print('Suggestion recorded successfully!')

# Function to view all flavors
def view_flavors():
    cursor.execute('SELECT * FROM flavors')
    for row in cursor.fetchall():
        print(row)

# Function to view ingredient inventory
def view_ingredients():
    cursor.execute('SELECT * FROM ingredients')
    for row in cursor.fetchall():
        print(row)

# Function to view customer suggestions
def view_suggestions():
    cursor.execute('SELECT * FROM suggestions')
    for row in cursor.fetchall():
        print(row)

# Create tables
create_tables()

# Example usage
add_flavor('Mint Chocolate', 'Winter', 'None')
add_flavor('Pumpkin Spice', 'Fall', 'None')
add_ingredient('Cocoa Powder', 50)
add_ingredient('Sugar', 100)
add_suggestion('Alice', 'Dark Chocolate with Sea Salt', 'None')

print("\nAvailable Flavors:")
view_flavors()

print("\nIngredient Inventory:")
view_ingredients()

print("\nCustomer Suggestions:")
view_suggestions()

# Close the database connection
conn.close()
