# find average and total amount spent
# find average and total items
# skip all rows for 0's, empty, or negatives in cells
# count the skips
# find a and b per customer

import pandas as pd
pd.set_option('display.max_rows', None)

# checking / skipping everything less than or equal to 0 or empty
def logic(i): 
    if i in rows <= 0 or " ": 
        return True
    return False
# Skipping rows based on a condition 
df = pd.read_csv("sales.csv", "rt", skiprows = logic) 

#finding averages and sums
amount_average = df["amount"].mean()
amount_sum = df["amount"].sum()
item_average = df["items"].mean()
item_sum = df["items"].sum()

print("Amount spent average: ", amount_average)
print("Amount spent sum: ", amount_sum)
print("Items bought average: ", item_average)
print("Items bought sum: ", item_sum)









