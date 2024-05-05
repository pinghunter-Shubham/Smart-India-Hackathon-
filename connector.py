import mysql.connector;
def get_cultural_details(Statename):
    try:
        server = mysql.connector.connect(
            host = "localhost",
            database="database_name",
            user = "root",
            password = "your_password"
        )
    except:
        print("There was an error connecting to the server.\n")
    sqlquery="SELECT heritage,details FROM cultural_heritage JOIN `StatesAndUTs` ON StatesAndUTs.`StateID`=cultural_heritage.stateid WHERE `StateName`=%s;";
    reader=server.cursor()
    data=reader.execute(sqlquery,(Statename,))
    data=reader.fetchall()
    str=""
    count=1
    for i in data:
        str+=(count.__str__()+". "+i[0]+":\n \t-"+i[1]+"\n")
        count+=1
    return str
