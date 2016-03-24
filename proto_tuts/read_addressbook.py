#! /usr/bin/python
import sys
sys.path.append('/home/aransena/Python_Code_Snippets/proto_tuts/proto_out')
import addressbook_pb2



# iterates through all people in the addressbook and prints info about them.

def ListPeople(address_book):
    for person in address_book.person:
        print "Person ID: ", person.id
        print "Name: ", person.name
        if person.HasField('email'):
            print " Email Addr: ", person.email

        for phone_number in person.phone:
            if phone_number.type == addressbook_pb2.Person.MOBILE:
                print " Mobile phone #: ",
            elif phone_number.type == addressbook_pb2.Person.HOME:
                print " Home phone #: ",
            elif phone_number.type == addressbook_pb2.Person.WORK:
                print " Work phone #: ",

            print phone_number.number


# Main procedure: Reads the entire address book from a file and prints all
# the info inside

if len(sys.argv)!=2:
    print "Usage: ", sys.argv[0], "ADDRESS_BOOK_FILE"
    sys.exit(-1)
print "Running"
address_book=addressbook_pb2.AddressBook()
    
# Read the existing address book
f=open(sys.argv[1],"rb")
address_book.ParseFromString(f.read())
f.close()
    
ListPeople(address_book)
