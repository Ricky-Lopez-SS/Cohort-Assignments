
order_number = [34587, 98762, 77226, 88112]
book_title_and_author = ['Learning Python, Mark Lutz', 'Programming Python, Mark Lutz', 'Head First Python, Paul Barry', 'Einfuhrung in Python3, Bernd Klein']
quantity = [4, 5, 3, 3]
price_per_item = [40.95, 56.80, 323.95, 24.99]



def question_1():

    book_shop = [order_number, book_title_and_author, quantity, price_per_item]
    combined_list = []

    print("Book Shop: {}\n\n".format(book_shop))

    for i in range(len(quantity)):
        combined_list.append((quantity[i], price_per_item[i]))
    
    combined_list = list(map(lambda x : x[0] * x[1], combined_list))


    ret_list = []

    
    for i in range(len(book_shop)) :
        ret_list.append((order_number[i], list(combined_list)[i]) )
    
    print("two-tuple list: {}".format(ret_list))


def question_2() :


    new_list = []

    for i in range(len(order_number)):
        new_list.append((book_title_and_author[i], quantity[i], price_per_item[i])) 


    new_book_shop = [order_number, new_list]
    print("New Book Shop: {}\n\n".format(new_book_shop))

    new_list = list(map(lambda x : x[1] * x[2] , new_list))

    ret_list = []

    for i in range(len(new_book_shop[0])):
        ret_list.append((order_number[i], new_list[i]))

    print("two-tuple list: {}".format(ret_list))

if __name__ == '__main__' :
    
    print("Question 1:\n\n")
    print(question_1())
    print("\nQuestion 2:\n\n")
    print(question_2())
