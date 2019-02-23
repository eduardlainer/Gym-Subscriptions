## Project Title
**Gym subscription system**

## Database structure
```
table: subscribers -> rows: id(auto increment int, primary key), firstname(varchar), lastname(varchar), phoneNumber(varchar), email(varchar)
```
```
table: subscriptions -> rows: id(auto increment int), subscribers_id(int), creation_date(datetime), expiration_date(datetime), current_date(datetime/currents_timestamp)
```

## Structura folder

  **static**
 * addsub.css
 * index.css
 * layout.css
 * logo.png

  **templates**
 * layout.html
 * error.html
 * succes.html
 * index.html
 * newsubscription.html

 **app.py**
 
 **database.py**


## Coded in
Python 3.6, Flask, MySQL,HTML5, CSS3, Bootstrap

