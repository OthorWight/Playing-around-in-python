# import the library
from appJar import gui
import hashlib
import uuid
import sqlite3

# vars
database_name = 'accounts.sqlite'
table_accounts = 'Accounts'
username_field = 'Usernames'
salt_field = 'Salts'
hash_field = 'PasswordHash'
field_type = "TEXT"

# connect to database
conn = sqlite3.connect(database_name)
c = conn.cursor()

# make sure the database is set up
colums = [i[1] for i in c.execute('PRAGMA table_info(' + table_accounts + ')')]
if username_field not in colums:
    try:
        c.execute('ALTER TABLE ' + table_accounts +
                  ' ADD COLUMN ' + username_field + ' TEXT')
    except:
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_accounts, nf=username_field, ft=field_type))
if salt_field not in colums:
    c.execute('ALTER TABLE ' + table_accounts +
              ' ADD COLUMN ' + salt_field + ' TEXT')
if hash_field not in colums:
    c.execute('ALTER TABLE ' + table_accounts +
              ' ADD COLUMN ' + hash_field + ' TEXT')
# ................................


def password_hasher(password, salt=""):
    if salt == "":
        salt = uuid.uuid4().hex
        print(salt)
    return hashlib.sha512(salt.encode('utf-8') + password.encode(
                          'utf-8')).hexdigest(), salt


def add_account(username, salt, hashed_password):
    c.execute("INSERT INTO %s VALUES('%s', '%s', '%s')" %
              (table_accounts, username, salt, hashed_password))
    conn.commit()


def get_account(username):
    c.execute("SELECT * FROM Accounts WHERE Usernames='%s'" % (username))
    return c.fetchall()


# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "Submit":
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        account_info = get_account(usr)
        account_info = account_info[0]
        salt = account_info[1]
        hashed_password = account_info[2]
        print(usr, salt, hashed_password)
        # hashed_password, salt = password_hasher(pwd, salt)
        # add_account(usr, salt, hashed_password)
        # print("User:", usr, "Pass:", pwd,
        #       "Hashed Password:", hashed_password)
    else:
        print("Button " + button + " is not configured")


# create a GUI variable called app
app = gui("Login Window", "400x265")
app.setBg("light gray")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "black")
app.setLabelFg("title", "white")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Submit", "New", "Cancel"], press)

app.setFocus("Username")

# start the GUI
app.go()
