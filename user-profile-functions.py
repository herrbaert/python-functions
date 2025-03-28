def create_user_profile(*, name, email,**kwargs):
    
    if not name or not email:
        print("name und mail sind nicht vorhanden")
    
    profile = {
        "name": name,
        "email": email
    }

    for key, value in kwargs.items():
        profile[key] = value

    return profile

alice = create_user_profile(name="Alice",email="bla@bla.de", age=33, city= "New York")
bob = create_user_profile(name="Bob",email="horst@dieter.de", last_name="Smith",age=22, phone_number=123456789 ) 
charly = create_user_profile(name="klaus", email="horst@dieter.de", last_name="Smith",age=22, phone_number=123456789 ) 


print(alice)
print(bob)