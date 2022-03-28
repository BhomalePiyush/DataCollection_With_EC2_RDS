import boto3
import time
import mysql.connector
import Program

client = boto3.client('rds', region_name='us-east-1')
response = client.describe_db_instances()
dict1 = {}
for db_instance in response['DBInstances']:
    if db_instance['DBInstanceIdentifier'] == 'projectdatabase':
        dict1['DBInstanceIdentifier'] = db_instance['DBInstanceIdentifier']
        dict1['Endpoint'] = db_instance['Endpoint']["Address"]


print(dict1['Endpoint'])
mydb = mysql.connector.connect(
    host=dict1['Endpoint'],
    user="vitaproject",
    password="vitafinalproject",
    database="ProjectDatabase"
)

create_table = mydb.cursor()
create_table.execute("""CREATE TABLE IF NOT EXISTS amazon_products3(Product_name VARCHAR(255),Rating VARCHAR(255),
Total_rating_count int,Discounted_price int,Original_price VARCHAR(20),Product_url VARCHAR(500),Time VARCHAR(20))""")

# search_query = 'iphone'.replace(' ','+')
# base_url = 'https://www.amazon.in/s?k={0}'.format(search_query)

if __name__ == '__main__':

    lst = open('itemlist.txt', "r", encoding='utf-8').readlines()
    list1 = []
    for i in lst:
        list1.append(i.strip())

    print(type(list1), "Program Insialized")
    for i in range(1):
        Program.itemlist(list1) # calling amazon code
        print("Amazon Updated")
        print("Iteration Complete")
        for minute in range(1, 61):
            time.sleep(60)  # Delay for 1 minute (60 seconds)
            print(f"{minute}minute")



