import mysql.connector


class Database:

    # Database connection and cursor

    connection = mysql.connector.connect(user='root', host='127.0.0.1', database='gymsubs_flask')
    cursor = connection.cursor()

    # Methods for extracting data

    def total_subscribers(self):
        """
        Get the number of subscribers
        """
        self.cursor.execute("SELECT COUNT(*) FROM subscribers")
        totalsubscribers = self.cursor.fetchone()[0]
        return totalsubscribers

    def subscriber_exist(self, fn):
        """
        See if a subscriber already exist
        """
        query = ("SELECT COUNT(*) FROM subscribers "
                 "WHERE firstname=%s")
        self.cursor.execute(query, (fn,))
        result = self.cursor.fetchone()[0]
        if result > 0:
            return True
        else:
            return False

    def get_subscriber_id(self, fn, ln):
        """
        Get subscriber id
        """
        query = ("SELECT id FROM subscribers "
                 "WHERE firstname=%s "
                 "AND lastname=%s")
        self.cursor.execute(query, (fn, ln))
        subscriberid = self.cursor.fetchone()[0]
        return subscriberid

    def addsubscriber(self, fn, ln, phone, email, cd, ed):
        """
         Add subscriber
        """
        query1 = ("INSERT INTO subscribers(firstname,lastname,phoneNumber,email) "
                  "VALUES (%s,%s,%s,%s)")
        self.cursor.execute(query1, (fn, ln, phone, email))
        subid = self.get_subscriber_id(fn, ln)
        query2 = ("INSERT INTO subscription(subscribers_id,creation_date,expiration_date) "
                  "VALUES (%s,%s,%s)")
        self.cursor.execute(query2, (subid, cd, ed))
        self.connection.commit()
