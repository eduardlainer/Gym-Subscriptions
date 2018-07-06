import mysql.connector
from flask import render_template


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

    def subscriber_exist(self, fn, ln):
        """
        See if a subscriber already exist
        """
        query = ("SELECT COUNT(*) FROM subscribers "
                 "WHERE firstname=%s "
                 "AND lastname=%s")
        self.cursor.execute(query, (fn, ln))
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

    def totalactivesubscription(self):
        """
        Check for active subscription
        :return:
        """
        query = ("SELECT COUNT(*) FROM subscription "
                 "WHERE expiration_date > currents_date")
        self.cursor.execute(query)
        activeSubs = self.cursor.fetchone()[0]
        return activeSubs

    def totalexpiredsubscription(self):
        """
        Check for expired subscriptions
        """
        query = ("SELECT COUNT(*) FROM subscription "
                 "WHERE expiration_date < currents_date")
        self.cursor.execute(query)
        expiredSubs = self.cursor.fetchone()[0]
        return expiredSubs

    def getsubscribers(self):
        """
        Get all subscribers
        """
        query = ("SELECT id,firstname,lastname FROM subscribers")
        self.cursor.execute(query)
        subs = self.cursor.fetchall()
        lista = []
        for sub in subs:
            lista.append(sub)
        return lista

    def renewsubscription(self, id, cd, ed):
        """
        Renew subscription of an old subscriber
        """
        query = ("UPDATE subscription "
                 "SET creation_date=%s, expiration_date=%s "
                 "WHERE subscribers_id=%s")
        self.cursor.execute(query, (cd, ed, id))
        self.connection.commit()

    def checksubscription(self, fn, ln):
        """
        Check a subscription
        """
        query = ("SELECT creation_date, expiration_date "
                 "FROM subscription INNER JOIN subscribers "
                 "ON subscribers_id = subscribers.id "
                 "WHERE (subscribers.firstname=%s "
                 "AND subscribers.lastname=%s);")
        self.cursor.execute(query, (fn, ln))
        sub = self.cursor.fetchall()
        return sub

    def checksubscriptionalert(self, fn, ln):
        """
        Check a subscription
        """
        query2 = ("SELECT COUNT(*) FROM subscription "
                  "INNER JOIN subscribers ON subscribers_id=subscribers.id "
                  "WHERE (expiration_date < currents_date) AND (subscribers.firstname=%s AND subscribers.lastname=%s)")
        self.cursor.execute(query2, (fn, ln))
        sub = self.cursor.fetchone()[0]
        return sub
