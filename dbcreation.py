#!/usr/bin/env python
# coding: utf-8

# # Create the database

# In[17]:


import yfinance as yf
import sqlite3


# In[15]:




# Connect to the database
conn = sqlite3.connect('dow_jones_companies.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the CREATE TABLE statement
cursor.execute('''
    CREATE TABLE daily_movement (
        company text,
        date date,
        movement real
    )
''')

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# In[16]:




# Connect to the database
conn = sqlite3.connect('dow_jones_companies.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the INSERT statement
cursor.execute('''
    INSERT INTO daily_movement (company, date, movement)
    VALUES (?, ?, ?)
''', ("Company A", "2020-01-01", 10.5))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


# In[21]:


import yfinance as yf
import sqlite3

# Connect to the database
conn = sqlite3.connect('dow_jones_companies.db')

# Create a cursor object
cursor = conn.cursor()

# Get the top 20 performing symbols for 2019
symbols = ['AAPL', 'MSFT', 'JPM', 'XOM', 'BRK.A', 'BA', 'GS', 'V', 'JNJ', 'WFC',
           'MCD', 'PFE', 'CVX', 'UNH', 'INTC', 'HD', 'CSCO', 'CAT', 'DIS', 'MRK']

# Iterate over the symbols and insert the daily movements into the database
for symbol in symbols:
    # Get the stock data for the symbol
    stock_data = yf.Ticker(symbol).history(period='1d', start='2019-01-01', end='2019-12-31')

    # Insert the data into the database
    for index, row in stock_data.iterrows():
        # Convert the date to a string
        date_str = index.strftime('%Y-%m-%d')
        cursor.execute('''
            INSERT INTO daily_movement (company, date, movement)
            VALUES (?, ?, ?)
        ''', (symbol, date_str, row['Close']))


conn.commit()

cursor.close()
conn.close()


# # Check the data

# In[22]:





conn = sqlite3.connect('dow_jones_companies.db')


cursor = conn.cursor()


cursor.execute('''
    SELECT * FROM daily_movement
''')


rows = cursor.fetchall()


for row in rows:
    print(row)

cursor.close()
conn.close()


# In[ ]:




