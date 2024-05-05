import mysql.connector

def get_item_info_text(item_info):
    state_name, museum_name, gallery_name, item_name = item_info.split(' - ')
    
    try:
        # Connect MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="your_database"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query 
            query = """
                SELECT
                    ItemsInGalleries.TextInfo
                    
                FROM
                    Museums
                INNER JOIN
                    Galleries
                ON
                    Museums.MuseumID = Galleries.MuseumID
                INNER JOIN
                    ItemsInGalleries
                ON
                    Galleries.GalleryID = ItemsInGalleries.GalleryID
                INNER JOIN
                    StatesAndUTs
                ON
                    Museums.StateID = StatesAndUTs.StateID
                WHERE
                    StatesAndUTs.StateName = %s
                    AND Museums.MuseumName = %s
                    AND Galleries.GalleryName = %s
                    AND ItemsInGalleries.ItemName = %s
            """
            
            cursor.execute(query, (state_name, museum_name, gallery_name, item_name))
            result = cursor.fetchone()
            if result:
                text_info = result[0]  # Access the first (and presumably only) element of the tuple
                text_info_str = str(text_info)  # Convert it to a string
                return text_info_str
            else:
                print("Item not found in the database.")

    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


def get_item_info_voice(item_info):
    state_name, museum_name, gallery_name, item_name = item_info.split(' - ')

    try:
        # Connect MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rupamdas",
            database="indian_tourism"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Query 
            query = """
                SELECT
                    ItemsInGalleries.VoiceInfo
                    
                FROM
                    Museums
                INNER JOIN
                    Galleries
                ON
                    Museums.MuseumID = Galleries.MuseumID
                INNER JOIN
                    ItemsInGalleries
                ON
                    Galleries.GalleryID = ItemsInGalleries.GalleryID
                INNER JOIN
                    StatesAndUTs
                ON
                    Museums.StateID = StatesAndUTs.StateID
                WHERE
                    StatesAndUTs.StateName = %s
                    AND Museums.MuseumName = %s
                    AND Galleries.GalleryName = %s
                    AND ItemsInGalleries.ItemName = %s
            """
            
            cursor.execute(query, (state_name, museum_name, gallery_name, item_name))
            result = cursor.fetchone()

            if result:
                voice_info = result[0]  # Access the first (and presumably only) element of the tuple
                voice_info_str = str(voice_info)  # Convert it to a string
                print(voice_info_str)  # Print the plain string
                return voice_info_str  # Return the plain string
            else:
                print("Item not found in the database.")

    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def get_item_info_video(item_info):
    state_name, museum_name, gallery_name, item_name = item_info.split(' - ')

    try:
        # Connect MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rupamdas",
            database="indian_tourism"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query 
            query = """
                SELECT
                    ItemsInGalleries.VideoLink
                    
                FROM
                    Museums
                INNER JOIN
                    Galleries
                ON
                    Museums.MuseumID = Galleries.MuseumID
                INNER JOIN
                    ItemsInGalleries
                ON
                    Galleries.GalleryID = ItemsInGalleries.GalleryID
                INNER JOIN
                    StatesAndUTs
                ON
                    Museums.StateID = StatesAndUTs.StateID
                WHERE
                    StatesAndUTs.StateName = %s
                    AND Museums.MuseumName = %s
                    AND Galleries.GalleryName = %s
                    AND ItemsInGalleries.ItemName = %s
            """
            
            cursor.execute(query, (state_name, museum_name, gallery_name, item_name))
            result = cursor.fetchone()

            if result:
                vedio_info = result[0]  # Access the first (and presumably only) element of the tuple
                vedio_info_str = str(vedio_info)  # Convert it to a string
                print(vedio_info_str)  # Print the plain string
                return vedio_info_str  # Return the plain string
            else:
                print("Item not found in the database.")

    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")



            
