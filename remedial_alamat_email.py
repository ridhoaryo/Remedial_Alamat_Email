def username_valid(username):
    if (username.isalpha() == True) or (username.isdigit() == True) or (username.isalnum() == True) or ('-' in username) or ('_' in username):
        return 1
    else:
        return 0

def hosting_valid(hosting):
    if (hosting.isalpha() == True) or (hosting.isdigit() == True) or (username.isalnum() == True):
        return 1
    else:
        return 0

def ekstensi_valid(ekstensi):
    if (ekstensi.isdigit() == True) or (len(ekstensi)>5) or ekstensi == '':
        return 0
    else:
        return 1

email = input('Input email: ')
split_list = email.split('@')
username = split_list[0]
rest = split_list[1]
if '.' not in rest:
    print('HASIL: EMAIL TIDAK VALID')
else:
    split_list2 = rest.split('.')
    hosting = split_list2[0]
    ekstensi = split_list2[1]

    valid_list = []
    valid_list.append(username_valid(username))
    valid_list.append(hosting_valid(hosting))
    valid_list.append(ekstensi_valid(ekstensi))
    if 0 in valid_list:
        print('HASIL: EMAIL TIDAK VALID')
    else:
        print('HASIL: EMAIL VALID')
