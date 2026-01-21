def calculate_love_score(name1,name2):
    name=(name1+name2).lower()
    first_digit=0
    second_digit=0
    for letter in name:
        for alphabet in "true":
            if letter==alphabet:
                first_digit+=1
            else:
                first_digit+=0
    for letter in name:
        for alphabet in "love":
            if letter==alphabet:
                second_digit+=1
            else:
                second_digit+=0
    love_score=str(first_digit)+str(second_digit)
    print(f"Your love score is {love_score}")

calculate_love_score('Kanye West','Kim Kardashian')