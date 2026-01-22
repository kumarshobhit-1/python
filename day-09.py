with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    contents = file.read()
    print(contents)

with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    lines = file.readlines()
    number_of_students = len(lines)
    print(f"Number of students: {number_of_students}")
    print(lines)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    for line in file:
        print(line.strip())

with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    lines = file.readlines() 
    number_of_products = len(lines)
    print(f"Number of products: {number_of_products}")
    print(lines)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    for line in file:
        product_details = line.strip().split(",")
        product_name = product_details[1]
        print(product_name)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    for line in file:
        product_details = line.strip().split(",")
        price = float(product_details[2])
        if price > 10000:
            print(line.strip())


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'w') as file:
    file.write("P201, Headphones, 2000, Electronics\n")
    file.write("P202, Sofa, 28000, Furniture\n")
    file.write("P203, Printer, 12000, Electronics\n")


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    contents = file.read()
    print(contents)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'a') as file:
    file.write("P204, Smartwatch, 15000, Electronics\n")

with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    contents = file.read()
    print(contents)

with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r+') as file:
    contents = file.readlines()
    contents[0] = "P201, Wireless Headphones, 2000, Electronics\n"
    file.seek(0)
    file.writelines(contents)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r+') as file:
    contents = file.read()
    print(contents)
    file.write("P205, Bed, 45000, Furniture\n")
    file.seek(0)
    contents = file.read()
    print(contents)


with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    count = 0
    for line in file:
        product_details = line.strip().split(",")
        category = product_details[3].strip()
        if category == "Electronics":
            count += 1
    print(f"Number of products in Electronics category: {count}")


#create a new file expensive_products.txt and write only those produces whose price > 20000
with open (r"C:\Users\Hp\OneDrive\Desktop\data.txt", 'r') as file:
    with open (r"C:\Users\Hp\OneDrive\Desktop\expensive_products.txt", 'w') as expensive_file:
        for line in file:
            product_details = line.strip().split(",")
            price = float(product_details[2])
            if price > 20000:
                expensive_file.write(line)
file.close()
expensive_file.close()