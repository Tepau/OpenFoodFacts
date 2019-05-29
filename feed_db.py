import requests
from functions_db import no_doublons_good_format, insert_category, insert_store, insert_product, insert_category_and_store_product, mydb
from service import final_format


all_category = []
all_category = no_doublons_good_format(all_category, final_format, 5)

all_store = []
all_store = no_doublons_good_format(all_store, final_format, 1)

insert_category(all_category)
insert_store(all_store)
insert_product(final_format)
insert_category_and_store_product(final_format, 5, 1)

mydb.commit()
