import psycopg2

id=input("enter userid: ")
pas=input("enter the password: ")
try:
    connection = psycopg2.connect(user = "",password = "",host = "",port = "",database = "")

    cursor = connection.cursor()
    cursor.execute("SELECT * from public.users where id=" + id +" and name='"+pas+"'" )
    record = cursor.fetchall()
    for row in record:
        print("userid=",row[0],"password=",row[1],"gender",row[2])
    if row[1]==pas:
        print("You are connected to Table")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")