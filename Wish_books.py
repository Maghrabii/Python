#book list
book_list=[]

add = input("please enter your Favorite book name\n")

book_list.append(add)

new_add = input("please enter another Favorite book you own (or press 'Enter' to Skip)\n")

if new_add:
    
    book_list.append(new_add)
    print(f"Your library: {book_list}")
else:
    print(f"Your library: {book_list}")

#Wish list

wish_list =[]
wish_add = input("please enter your wish book name\n")

wish_list.append(wish_add)

new_wish_add = input("please enter another Favorite book you own (or press 'Enter' to Skip)\n")

if new_wish_add:
    
    wish_list.append(new_wish_add)
    print(f"Your library: {wish_list}")
else:
    print(f"Your library: {wish_list}")

gain_book = input("Enter name of wish book you gained or press enter to skip \n ")

if gain_book in wish_list:
    book_list.append(gain_book)
    wish_list.remove(gain_book)
    print(f"Your Updated library: {book_list},\n and your wish list {wish_list}")
else:
    print(f"Your library: {book_list},\n and your wish list {wish_list}")

