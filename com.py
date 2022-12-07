#a =[]
#for i in range(2, 20, 2):
    #a.append(i)
#print(a)


#a= [i for i in range(2, 20, 2)]
#print(a)

email= ["1@gmail.com", "2@gmail.com", "3@yahoo.com"] 
gmail= [i for i in email if i.endswith("gmail.com")]
print(gmail)