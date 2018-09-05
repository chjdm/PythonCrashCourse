sandwich_orders = ['tuna sandwich', 'pastrami', 'beef sandwich', 'pastrami', 'pastrami', 'plain sandwich']
finished_sandwiches = []

print("Pastrami is sold out.")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        # sandwich_orders.remove('pastrami')  数据已经弹出
        continue
    else:
        print(sandwich.title() + "is done.")
        finished_sandwiches.append(sandwich)

print("\nAll sandwich is done, list is below:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())
