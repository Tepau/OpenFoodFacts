from functions_db import no_duplicates_good_format, insert_category,\
                         insert_store, insert_product,\
                         insert_category_and_store_product, mydb
from service import final_format

# Create an empty list that will contain the categories in the desired format
all_category = []
all_category = no_duplicates_good_format(all_category, final_format, 5)


# Create an empty list that will contain the stores in the desired format
all_store = []
all_store = no_duplicates_good_format(all_store, final_format, 1)

# Insert categories in the Category table
insert_category(all_category)

# Insert stores in the Store table
insert_store(all_store)

# Insert products in the Product table
insert_product(final_format)

# Filling tables Category_product and Store_product
insert_category_and_store_product(final_format, 5, 1)

# Save insertions in database
mydb.commit()
