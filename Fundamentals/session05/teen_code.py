code_dict = {
    "any": "Anh người yêu",
    "eny": "Em người yêu",
    "hc": "học",
    "pt": "Phát triển"
}
while True:
    print(*code_dict)
    print()

    code = input("Enter a code:")

    if code in code_dict:
        print(code_dict[code])
    else:
        print("Not found")
        contribute = input("Add this code (Y/N)?")
        if contribute.lower() == "y":
            translation = input("Enter translation: ")
            code_dict[code] = translation

            print(code_dict)
