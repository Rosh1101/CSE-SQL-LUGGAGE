import mysql.connector as sqlconnector


connection = sqlconnector.connect(host="localhost",user="root",passwd="mishraroshan@1101",database="airlines")

if connection.is_connected()==True:
    print(f"Connected with {connection.database}")

id=int(input("ID DAALD DO: "))
weight = int(input("WEIGHT DAAL DO BHAII: "))
price = int(input("Daam btao bhaii: "))



insert_data = f"INSERT INTO luggage (id,weight,price) VALUES({id},{weight},{price})"

cursor = connection.cursor()
cursor.execute(insert_data)
connection.commit()


#UPDATING WITH ID
'''id=int(input("ID DAALD DO: "))'''
'''copy_weight = weight
copy_pice = price'''



ask = input("UPDATE KRNA HAIN>? Y or N: ")

if ask == 'N':
    pass
elif ask == 'Y':

    id_update = int(input("Update id: "))

    new_weight = int(input())
    weight+=new_weight
    price+=new_weight*250

    updated_data = f"UPDATE luggage SET weight = {weight} where id = {id_update}"

    cursor = connection.cursor()
    cursor.execute(updated_data)
   # cursor.execute(updated_price)
    connection.commit()
   

    print(f"Changes committed to {connection.database}")
else:
    pass

cursor.close()