def show_menu()->dict[int,str]:
    menu={
        1:"Scrape books",
        2:"List all books",
        3:"Filter books",
        4:"Create User",
        5:"Assign book to user",
        6:"View user's books"
    }

    for k,v in menu.items():
        print(f"{k}. {v}")

    return menu