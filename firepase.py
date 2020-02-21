#pip install python-firebase

#SET THE DATABASE RULES FOR AUTHENTICATION, WE CAN ALSO REMOVE AUTHENTICATION
'''
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
'''



from firebase.firebase import FirebaseApplication, FirebaseAuthentication

################# firebase  authentication
DSN = 'https://project-db-xxx7.firebaseio.com/' #DSN - 'Data Source Name'
EMAIL = 'mahesh4075@gmail.com'
SECRET = 'xxxxxxxxxxxxxxxxxxxxxLuGWdH07EW4Ul4' # 'secretkey'


authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

################## firebase  authentication

'''
result = firebase.post('/data', {"dob" : "96"}) # create a parent-dir automatically - can pass only 1 value
print(result)

result = firebase.put( '/MARKS-DB/new','marks',{"no1" : "96", "no2" : "87", "no3" : "97" }) # create a parent-dir named 'marks' with values 'no1',no2, no3
print(result)

getresult = firebase.get('/data', None) #get all data from db
print(getresult)

getresult = firebase.get('/data', 'marks')   #get all data from db with dict named 'marks'
print(getresult['no1'])


result = firebase.delete('/data/-LekgimUW7hQf0T8Qtqc','dob') # delete the particular elememnt in a directory
print(result)


result = firebase.delete('/MARKS-DB/new/marks','dob') # delete the particular elememnt in a directory
print(result)


result = firebase.put( '/MARKS-DB/new','marks',{"dob" : "22"}) # updating the values in specified path
print(result)
'''


dic = {
    "ipClassOfService": ["1","2"],
    "protocolIdentifier": "17"
  }

#sending json data to firebase
#result = firebase.put('/','data', dic) # create a parent-dir automatically - can pass only 1 value

#getting dictionary of list
getresult = firebase.get('/', 'data')   #get all data from db with dict named 'marks'
print(getresult)
print(getresult['ipClassOfService'][0])
print(getresult['protocolIdentifier'])


#print(result)



