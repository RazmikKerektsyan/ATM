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

def register_user(accounts):
    new_login = input("შეიყვანეთ მომხმარებელის სახელი (Login): ").strip()
    if not new_login or ":" in new_login or new_login in accounts:
        print("მომხმარებელის სახელი დაკავებულია ან შეიცავს დაუშვებელ სიმბოლოწვს!")
        return None
    new_pin = input("მოიფიქრეთ 4-ნიშნა PIN-კოდი: ").strip()
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN-კოდი უნდა შედგებოდეს ზუსტად 4 ციფრისაგან!")
        return None
    else:
        accounts[new_login] = {
            "pin": new_pin,
            "balance": 0.0
        }
        save_accounts(accounts)
        print(f"ანგარიში {new_login} წარმატებით შეიქმნა!")

def delete_account(accounts, login):
    confirm = input("დარწმუნებული ხართ, რომ გსურთ ანგარიშის წაშლა? (დიახ/არა): ").strip().lower()
    if confirm == "დიახ":
       del accounts[login]
       save_accounts(accounts)
       print("ანგარიში წარმატებით წაიშალა.")
       return True
    else:
        print("წაშლა გაუქმებულია!")
        return False

