

def main():
    todo = "nothing"

    requestManager(todo)
    
def requestManager(todo):
    
    todo = todo.upper();
    
    if todo == "JOIN":
        addUser()
    elif todo == "QUIT":
        removeUser()
    elif todo == "DEPOSIT":
        deposit()
    elif todo == "WITHDRAW":
        withdraw()
    elif todo == "PAYLOAN":
        payLoan()
    else:
        return


if __name__ == "__main__":
    main()
