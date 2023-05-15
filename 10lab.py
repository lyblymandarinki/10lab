def z1_2():
    with open("products.json", "r", encoding='utf-8') as file:
        data = json.load(file)

    new_product = {
        "name": input("Введите название продукта: "),
        "price": int(input("Введите цену продукта: ")),
        "available": input("Есть ли продукт в наличии (да/нет)? ") == "да",
        "weight": int(input("Введите вес продукта: "))
    }

    data["products"].append(new_product)

    with open("products.json", "w",  encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

    print("Содержимое файла:")
    for product in data["products"]:
        print("Название:", product["name"])
        print("Цена:", product["price"])
        print("Вес:", product["weight"])
        if product["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z3():
    with open("en-ru.txt", "r") as file:
        lines = file.readlines()

    dictionary = {}

    for line in lines:
        words = line.strip().split(" - ")
        english = words[0]
        russian = words[1].split(", ")
        for word in russian:
            if word not in dictionary:
                dictionary[word] = [english]
            else:
                dictionary[word].append(english)

    with open("ru-en.txt", "w") as file:
        for russian, english in sorted(dictionary.items()):
            file.write(f"{russian} - {', '.join(english)}\n")

z1_2()
z3()
