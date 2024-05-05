import mysql.connector

# Function to fetch and display heritage sites in a given state
def display_heritage_sites_by_state(state_name):
    storage=[]
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="your_database"
        )
        if connection.is_connected():
            cursor = connection.cursor()

            # Query to fetch heritage sites in the given state
            query = """
                SELECT
                    SiteName,
                    Location,
                    Transit,
                    OpeningTime,
                    TicketPrice
                FROM
                    HeritageSites
                INNER JOIN
                    StatesAndUTs
                ON
                    HeritageSites.StateID = StatesAndUTs.StateID
                WHERE
                    StatesAndUTs.StateName = %s
            """
            
            cursor.execute(query, (state_name,))
            sites = cursor.fetchall()

            if sites:
                print(f"Heritage Sites in {state_name}:\n")
                for site in sites:
                    site_name, location, transit, opening_time, ticket_price = site
                    storage.append(
                        f"PLACE NAME: {site_name}\n"
                        f"LOCATION: {location}\n"
                        f"NEAREST TRANSPORTATION DEPO: {transit}\n"
                        f"OPENING TIME: {opening_time}\n"
                        f"TICKET PRICE: {ticket_price}\n"
                    )
                # Concatenate the list elements into a single string
                result = "\n".join(storage)
                return result
            else:
                print(f"No heritage sites found in {state_name}.")

    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            storage.clear()
            print("MySQL connection is closed.")


