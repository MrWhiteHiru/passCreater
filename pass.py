import random
# colors
r ='\033[91m' # red
g ='\033[92m' # green
b = '\033[94m' # blue
y = '\033[93m' # yellow
s_b ='\033[96m' # sky_blue
pi = '\033[35m' # pink
reset = '\033[0m' # reset
blink = "\033[5;92m" # blink

print(g+"""
██████╗  █████╗  ██████╗ ██████╗     █████╗ ██████╗ ███████╗ █████╗ ████████╗███████╗██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║╚█████╗ ╚█████╗     ██║  ╚═╝██████╔╝█████╗  ███████║   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██║ ╚═══██╗ ╚═══██╗    ██║  ██╗██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║██████╔╝██████╔╝    ╚█████╔╝██║  ██║███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═════╝      ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")


print(g+"                                                         [#] PASS CREATER BY WHITE HIRU"+reset)
print(g+"                                                         [#] CAPTION OF HISL           "+reset)

def create_password(firstname, lastname, age):
    
    username = (firstname.lower() + lastname.lower()).replace(" ", "")
    
    rand_letters = "".join(random.sample(username, len(username)))
    rand_numbers = str(random.randint(age, age+10))
    rand_specials = "!@#*"
    rand_password = rand_letters + rand_numbers + rand_specials
    
    shuffled_password = "".join(random.sample(rand_password, len(rand_password)))
    return shuffled_password


firstname = input(y+"Enter your first name: ")
lastname = input(y+"Enter your last name: ")
age = int(input(y+"Enter your age: "))

password = create_password(firstname, lastname, age)


print(pi+"\n[#] Password Creator by White Hiru [#]\n"+reset)
print(g+f"Your password is:  {password}")


  
