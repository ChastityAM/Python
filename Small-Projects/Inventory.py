in_stock = 600
jeans_sold = 500
target_sales = 500

target_hit = jeans_sold == target_sales
print("Hit jeans sales target:")
print(target_hit)

on_hand = in_stock - jeans_sold
in_stock = on_hand != 0
print("Amount of jeans on hand:")
print(on_hand)