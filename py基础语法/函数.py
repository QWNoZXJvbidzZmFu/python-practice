def greet_users(names):
    for name in names:
        msg = f"hello {name.title()}"
        print(msg)
usernames=['haievh','sjv','jueq']
greet_users(usernames)

def name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease enter your name:")
    print("(enter q at any time to quit)")
    f_name=input("First name:")
    if f_name == "q":
        break
    l_name=input("Last name:")
    formatted_name=name(f_name,l_name)
    print(f"Hello {formatted_name}")

def build_profile(first,last,**user_info):
    user_info['first_name']=first
    return user_info
user_profile=build_profile('jdqkej','wjve',location='qjoeoqe',field='bvqe')
print(user_profile)