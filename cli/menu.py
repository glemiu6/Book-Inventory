def show_menu():
    options = {
        1:"Scrape books",
        2:"List all books",
        3:"Filter books",
        4:"Create User",
        5:"Assign book to user",
        6:"View user's books",
        0:"Exit"
    }

    for k,v in options.items():
        print(f"{k}. {v}")



if __name__=="__main__":
    menu=show_menu()
