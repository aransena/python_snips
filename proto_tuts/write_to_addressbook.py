#! /usr/bin/python
import sys
sys.path.append('/home/aransena/Python_Code_Snippets/proto_tuts/proto_out')
import addressbook_pb2



#This function fills out a Person message based on user input
def PromptForAddress(person):
    person.id=int(raw_input("Enter persons ID: "))
    person.name=raw_input("Enter persons name: ")

    email = raw_input("Enter email (blank or none): ")
    if email != "":
        person.email=email
    number=""
    while True:
        number1 = raw_input("Enter a phone number (blank to finish): ")
        if number1 =="":
            break
        else:
            number=number1

    phone_number=person.phone.add()
    phone_number.number=number

    type = raw_input("Is this a mobile, home, or work number? ")
    if type == "mobile":
        phone_number.type=addressbook_pb2.Person.MOBILE
    elif type == "home":
        phone_number.type=addressbook_pb2.Person.HOME
    elif type=="work":
        phone_number.type=addressbook_pb2.Person.WORK

    else:
        print "Unknown phone type; leaving as default value."

# Main procedure: Reads the entire address book from a file,
# adds one person based on user input, then writes it back out to
# the same file

if len(sys.argv) != 2:
    print "Usage: ", sys.argv[0] , "ADDRESS_BOOK_FILE"
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.

try:
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()
except IOError:
    print sys.argv[1] + ": Could not open file. Creating a new one."

# Add an address.
PromptForAddress(address_book.person.add())

# Write the new address book back to disk.

f = open(sys.argv[1],"wb")
f.write(address_book.SerializeToString())
f.close()
