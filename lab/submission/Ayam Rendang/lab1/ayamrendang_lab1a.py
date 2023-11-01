# -*- coding: utf-8 -*-
"""AyamRendang lab1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mzfg2oxfIIioyQQJlfe9ZR-fqRCfeMSf

# Lab 1a - Understanding Your Data

Please use the [**Chipotle Sales dataset**](https://raw.githubusercontent.com/drshahizan/dataset/main/pandas/chipotle.tsv) for this exercise.

### Step 1. Import the necessary libraries
"""

import pandas

"""### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/drshahizan/dataset/main/pandas/chipotle.tsv)."""

path = "https://raw.githubusercontent.com/drshahizan/dataset/main/pandas/chipotle.tsv"

"""### Step 3. Assign it to a variable called chipo."""

chipo = pandas.read_csv(path,sep="\t")

"""### Step 4. See the first 10 entries"""

chipo.head(10)

"""### Step 5. What is the number of observations in the dataset?"""

# Solution 1
chipo.count

# Solution 2

chipo.shape[0]

"""### Step 6. What is the number of columns in the dataset?"""

chipo.shape[1]

"""### Step 7. Print the name of all the columns."""

print(chipo.columns.values)

"""### Step 8. How is the dataset indexed?"""

index_range = chipo.index
print("Index Range:", index_range)

"""### Step 9. Which was the most-ordered item?"""

# Group the dataframe by item_name and sum the quantity for each item
item_counts = chipo.groupby('item_name')['quantity'].sum()

# Find the item with the highest total quantity
most_ordered_item = item_counts.idxmax()
total_quantity = item_counts.max()

# Print the most-ordered item and its total quantity
print(f"The most-ordered item is '{most_ordered_item}' with a total quantity of {total_quantity}.")

"""### Step 10. For the most-ordered item, how many items were ordered?"""

print(total_quantity)

"""### Step 11. What was the most ordered item in the choice_description column?"""

# Group the dataframe by choice_description and sum the quantity for each choice_description
choice_counts = chipo.groupby('choice_description')['quantity'].sum()

# Find the choice_description with the highest total quantity
most_ordered_choice = choice_counts.idxmax()
total_quantity = choice_counts.max()

# Print the most-ordered choice_description and its total quantity
print(f"The most-ordered choice_description is '{most_ordered_choice}' with a total quantity of {total_quantity}.")

"""### Step 12. How many items were orderd in total?"""

# Calculate the total number of items ordered by summing the 'quantity' column
total_items_ordered = chipo['quantity'].sum()

# Print the total number of items ordered
print(f"Total number of items ordered: {total_items_ordered}")

"""### Step 13. Turn the item price into a float"""

# Remove the dollar sign ($) from the 'item_price' column and convert it to a float
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)

# Now, the 'item_price' column contains float values

# Print the first few rows of the dataset to verify the changes
print(chipo.head())

"""#### Step 13.a. Check the item price type"""

# Check the data type of the 'item_price' column
item_price_type = chipo['item_price'].dtype

# Print the data type of the 'item_price' column
print(f"Data type of 'item_price' column: {item_price_type}")

"""#### Step 13.b. Create a lambda function and change the type of item price"""

# Convert 'item_price' to another data type (e.g., int) and then back to float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(int(x)))

# Now, the 'item_price' column contains float values

# Print the first few rows of the dataset to verify the changes
print(chipo.head())

"""#### Step 13.c. Check the item price type"""

# Check the data type of the 'item_price' column
item_price_type = chipo['item_price'].dtype

# Print the data type of the 'item_price' column
print(f"Data type of 'item_price' column: {item_price_type}")

"""### Step 14. How much was the revenue for the period in the dataset?"""

#due toconverting type of item price its truevalue is altered so deriving it again from source
chipo = pandas.read_csv(path,sep="\t")
# Remove the dollar sign ($) from the 'item_price' column and convert it to a float
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)

chipo['revenue'] = chipo['quantity'] * chipo['item_price']
total_revenue = chipo['revenue'].sum()

# Print the total revenue
print(f"The total revenue for the period is ${total_revenue:.2f}")

"""### Step 15. How many orders were made in the period?"""

# Count the unique order IDs to find the number of orders made
total_orders = chipo['order_id'].nunique()

# Print the total number of orders
print(f"The total number of orders made in the period is {total_orders}.")

"""### Step 16. What is the average revenue amount per order?"""

# Solution 1

# Group the dataframe by 'order_id' and calculate the mean revenue for each order
average_revenue_per_order = chipo.groupby('order_id')['revenue'].sum().mean()

# Print the average revenue amount per order
print(f"The average revenue amount per order is ${average_revenue_per_order:.2f}")

"""### Step 17. How many different items are sold?"""

# Count the number of unique item names
unique_items_sold = chipo['item_name'].nunique()

# Print the number of different items sold
print(f"The number of different items sold is {unique_items_sold}.")