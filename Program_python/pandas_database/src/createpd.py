# @Author: Naphat Nithisopa <pection>
# @Date:   2020-12-26T10:52:02+07:00
# @Email:  pection.naphat@gmail.com
# @Last modified by:   pection
# @Last modified time: 2020-12-30T03:46:49+07:00


import string
import os
from managedproduct import ManageProductCode
#import logging
#import numpy as np
os.chdir(os.getcwd()+"/static/dataset")
print(os.getcwd())
#pd.set_option('display.width', 175)
#pd.set_option('display.max_columns', 7)

file_path = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
# print(os.path)
# print(os.path.abspath(os.getcwd()))

# print(file_path)
columns_name=[
    "Product_Name",
    "Product_Size",
    "Prodcut_Prize",
    "Product_Image",
    "Product_Link",
]
# df = pd.read_csv(file_path[4],names=columns_name)
Working_dest = ManageProductCode(file_path[1])
Working_dest.get_product_details()
Working_dest.read_csv_file()
product_code_list= Working_dest.add_product_code()
print(product_code_list)

# print(product_code_list)
# print(df["Product_Image"])
#
# image_list = df['Product_Image'].values.tolist()
# # print (image_list[0])
# # i = image_list[0].index("https")
# # del image_list[0][i]
# chars_to_remove = ['[',"''",']']
# print (type(image_list[0]))
# a = image_list[0]
# a = a .strip("[]")
# # print (a.strip(""))
# a = Convert(a)
