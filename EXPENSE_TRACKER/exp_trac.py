import csv
import os
from operator import index

from numpy.ma.extras import row_stack

file_name = "expenses.csv"


def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = input("Enter date : ")
    Category = input("Enter category : ")
    Amount = input("Enter amount : ")
    Description = input("Enter description  : ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

    print("Expenses added Successfully \n")


def view_expense():
    with open(file_name, "r") as file:
        reader = csv.reader(file)

        print("\n ---- Expenses List ----")

        for row in reader:
            print(row)
        print()


def delete_expense():
    view_expense()
    index = input("Enter row number to delete (Starts from 1) : ")

    row = []

    with open(file_name, "r") as file:
        reader=csv.reader(file)
        row=list(reader)

        if index < len(row)