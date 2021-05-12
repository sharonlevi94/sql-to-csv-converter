#                         README section
# -------------------------------------------------------------------------
# Names: Sharon Levi | Bar Ifrah
# ID: 311593313 |
# General:
# This program open, read and operate a sql file of medical data base.
# The program convert this file to a csv file to every table that exist
# in the sql file.
# Input:
# SQL file. Make sure that this file exist in the same directory.
# Output:
# CSV files - one to every table.
# -------------------------------------------------------------------------
#                         Import section
import csv

# -------------------------------------------------------------------------
#                         Functions section


def insert_into_exists(block):
    return block.find("INSERT INTO") != -1

# -------------------------------------------------------------------------


def get_values_for_table(table_block):
    values = table_block.replace(" ", "").split("VALUES")[1:]
    # to remove unnecessary parenthesis from data
    values = values[0].split("),(")
    values[0] = values[0].replace("(", "")
    values[-1] = values[0].replace(")", "")
    values_for_csv = []
    for input_list in values:
        values_for_csv.append(input_list.split(','))
    return values_for_csv

# -------------------------------------------------------------------------


def get_titles_for_table(table_list):
    titles = []
    for item in table_list:
        if item.find("PRIMARY") != -1:
            break
        titles.append(item)
    titles = list(map(lambda x: x[1:(x[1:]).find('`') + 1], titles))
    return titles

# -------------------------------------------------------------------------
#                         Main section


sql_file = open('demo.sql', 'r')
sql_content = sql_file.read()

# now we split, to have a list of tables to create later.
tables_to_create = sql_content.split("CREATE TABLE")

# filter list to hold only tables that has content.
non_empty_tables = list(filter(insert_into_exists, tables_to_create))

# run on nonempty tables:
for table in non_empty_tables:
    my_table_list = table.replace(" ", "").split('\n')   # to set as a list

    # Search the values for each table:
    output_to_csv = get_values_for_table(table)

    # Search the titles for each table:
    table_titles = get_titles_for_table(my_table_list)

    # create csv:
    file_name = table_titles[0]   # first argument in 'titles'
    with open('csvFiles\\' + file_name + ".csv", "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(table_titles[1:])

        # writing the data rows
        csvwriter.writerows(output_to_csv)
