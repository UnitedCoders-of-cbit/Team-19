import random
generatorotp=random.randint(000000,100000)
print("OTP for verification",generatorotp)
if password==str(generatorotp):
    print("Verfication successful")
else:
    password!=str(generatorotp)
    print("Check the otp entered ")