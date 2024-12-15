

def total_salary(path):
      try:
        with open(path, "r", encoding='utf-8') as file:
            line = file.read().split(',')
            print(type(line))
            print(line)
            numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
            new_l = [int(item) for item in numbers]
            total = sum(new_l)
            avrage = total / 3
            print(type(total))
            print(total, avrage)
            return total, avrage
      except UnicodeError:
           print("Must be file")
           

            
total, average = total_salary("C:\\Users\\Admin\\Desktop\\repos\\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




def get_cats_info(path):
        try:
            with open(path, "r", encoding='utf-8') as file:
              l = file.readlines()
              cat_list = []
              for rows in l:
                rows = rows.split(',')
                cat_dict = {}
                cat_dict["id"] = rows[0]
                cat_dict["name"] = rows[1]
                cat_dict['age'] = rows[2]
                cat_list.append(cat_dict)
            return cat_list
        except UnicodeError:
            print('Must be file')


cats_info = get_cats_info("C:\\Users\\Admin\\Desktop\\repos\\cat_info.txt")
print(cats_info)


def parse_input(input_user):
    cmd, *args = input_user.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contact):
    name , phone= args
    contact[name] = phone
    return 'Contact added'

def phone_username(args, contact):
    name = args[0]
    f = contact[name]
    return f
    
  
def change_username_phone(args, contact ):
    name, new = args
    contact[name] =new
    return "contact change" 

def all(contacts):
    cont= [key + " => " + value for key, value in contacts.items()]
    return cont



def main():
    contact = {}
    print(contact)
    print("Welcome to assistance bot")
    while True:
        user_input = input("Enter a command ")
        command, *args = parse_input(user_input)

        if command in ["close", 'exit']:
            print("see you next time")
            break

        elif command == 'hey':
            print("How i can help you?")
        elif command == 'add':
            print(add_contact(args, contact))
        elif command == "change":
            print(change_username_phone(args, contact))
        elif command == 'phone':
            print(phone_username(args, contact))
        elif command == 'all':
            print(all(contact))
        else:
            print("Say this to your mother")

if __name__=="__main__":
    main() 



