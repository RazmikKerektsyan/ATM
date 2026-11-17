def load_accounts(filename="accounts.txt"):
    accounts = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 3:
                    continue
                accounts[parts[0]] = {
                    "pin": parts[1],
                    "balance": float(parts[2])
                }
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as file:
            pass
    return accounts

def save_accounts(accounts, filename="accounts.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for login, data in accounts.items():
            file.write(f"{login}:{data['pin']}:{data['balance']}\n")

def login_user(accounts):
    login = input("Enter your login: ").strip()
    if login not in accounts:
        print("ესეთი login-ი არ არსებობს")
        return None
    else:
        for attempt in range(3):
            pin = input("შეიყვანეტ PIN-კოდი ...").strip()
            if pin == accounts[login]["pin"]:
                print(f"მოგესალმებით {login}!")
                return login
            else:
                print(f"PIN-ი არასწორია! დარჩენილი მცდელობები: {2 - attempt}")
        print("ზედმეტად ბევრი არასწორი მცდელობა. წვდომა დაბლოკილია!")
        return None

def deposit(accounts, login):
    try:
        amount = float(input("შეიყვანეთ შესატანი თანხა: "))
    except ValueError:
        print("შეცდომა: გთხოვთ შეიყვანოთ რიცხვი!")
        return None

    if amount <= 0:
        print("თანხა უნდა იყოს ნულზე მეტი!")
        return None
    else:
        accounts[login]["balance"] += amount
        save_accounts(accounts)
        print(f"ბალანსი წარმატებით შეივსო! მიმდინარე ბალანსი: {accounts[login]['balance']:.2f} ლარი")

def withdraw(accounts, login):
    try:
        amount = float(input("შეიყვანეთ გასატანი თანხა: "))
    except ValueError:
        print("შეცდომა: გთხოვთ შეიყვანოთ რიცხვი!")
        return None
    if amount <= 0:
        print("თანხა უნდა იყოს ნულზე მეტი!")
        return None
    elif amount > accounts[login]["balance"]:
        print("ანგარიშზე არასაკმარისი თანხაა!")
        return None
    else:
        accounts[login]["balance"] -= amount
        save_accounts(accounts)
        print(f"ოპერაცია შესრულდა! ანგარიშზე დარჩენილი თანხა: {accounts[login]['balance']:.2f} ლარი")

