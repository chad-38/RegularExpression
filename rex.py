import re
data1 = 'My phone number is: 800‐555‐1212.'
data2 = '800‐555‐1234 is my phone number.'
#finding the phone number from a text above.
pattern = re.compile(r'(\d{3})‐(\d{3})‐(\d{4})')
dmatch1 = pattern.search(data1).groups()
dmatch2 = pattern.search(data2).groups()
print (dmatch1)
print (dmatch2)



##Now lets look into email address validation:
import re
def emailvalidator(email):
    emailchecker = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if (re.fullmatch(emailchecker, email)):
        print("The email is valid")
    else:
        print("Check again, the email is invalid")

##Validating Password as per the company/domain policy##

def emailvalidator(email):
    emailchecker = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(emailchecker, email)):
        print("The email is valid")
    else:
        print("Check again, the email is invalid")
@emailvalidator(email):
    print("Type your email")
