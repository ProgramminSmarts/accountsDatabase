import database as db
from passlib import ldap_md5 as md5

test = db.database("Accounts")
test.addField("Usernames")
test.addField("Passwords")
test.load()
#make directory - creates a directory at path you define


q = int(raw_input("Make an account or log in or delete your account? 1 or 2 or 3: "))

def createAcc():
    global test
    newUsername = raw_input("Pick a username: ")
    newPassword = raw_input("Pick a password: ")
    test.addEntry({"Usernames": newUsername, "Passwords": md5.hash(newPassword)})

def logIn():
    tryUser = raw_input("Enter your username: ")
    tryPass = raw_input("Enter your password: ")
    for entry in test.data:
        if tryUser == entry[0]:
            if tryPass == entry[1]:
                print("You are logged in as " + tryUser)

def deleteAcc():
    tryUsername = raw_input("Enter your username: ")
    tryPassword = raw_input("Enter your password: ")
    for entry in test.data:
        if tryUser == entry[0]:
            if tryPass == entry[1]:
                askDelete = input("You are logged in as " + tryUser + ", are you sure you want to delete this account? Type yes if you agree, type no if you want to cancel")
                if askDelete == "yes":
                    del test.data[tryUser]
                else:
                    logIn()
if q == 1:
    createAcc()
elif q == 2:
    logIn()
elif q == 3:
    deleteAcc()
else:
    print("Please enter either 1 or 2")
test.save()
print(test.data)

'''
workingDir = os.getcwd()
dataDir = os.path.join(workingDir, "data")
print(dataDir)
#make directory - creates a directory at path you define
try:
    os.mkdir(dataDir)
except:
    print("Data Directory already exists")
#how to list files that are in a directory
for file in os.listdir(dataDir):
    print(file)
#to save a numpy array into a file
asdfghjkl = np.ones((9, 9, 9, 9))
np.save(os.path.join(dataDir, "asdfghjkl"), asdfghjkl)
# loading a file
for file in os.listdir(dataDir):
    print(file)
    if file.endswith("asdfghjkl.npy"):
        asdfghjkl = np.load(os.path.join(dataDir,file))
        break
print asdfghjkl
'''
