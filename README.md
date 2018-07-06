## Titlu proiect
**Gym Subscription System**

## Structura baza de date

**tabel: subscribers -> rows: id(auto increment int, primary key), firstname(varchar), lastname(varchar), phoneNumber(varchar), email(varchar)**
**tabel: subscriptions -> rows: id(auto increment int), subscribers_id(int), creation_date(datetime), expiration_date(datetime), current_date(datetime/currents_timestamp)**

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


## Realizat in
* Python 3.7 + Flask + MySQL + HTML + CSS + Bootstrap

## Realizat de
**Eduard Lainer**
