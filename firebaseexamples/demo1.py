from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://fir-python-f1e1e.firebaseio.com/",None)
fire.put("Merchant","admin",{"username":"admin","password":"admin"})
print("admin account is created")