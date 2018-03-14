# node.js - SQLITE 예제


## 예제 - SELECT

```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database
let db = new sqlite3.Database('./db/chinook.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the chinook database.');
});
 
db.serialize(() => {
  db.each(`SELECT PlaylistId as id,
                  Name as name
           FROM playlists`, (err, row) => {
    if (err) {
      console.error(err.message);
    }
    console.log(row.id + "\t" + row.name);
  });
});
 
db.close((err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Close the database connection.');
});
```



## all() 메서드로 모든 행 가져오기

```javascript
db.all(sql,params,(err, rows ) => {
    // process rows here    
});
```

```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database
let db = new sqlite3.Database('./db/chinook.db');
 
let sql = `SELECT DISTINCT Name name FROM playlists
           ORDER BY name`;
 
db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  rows.forEach((row) => {
    console.log(row.name);
  });
});
 
// close the database connection
db.close();
```

```
>node all.js
90's Music
Audiobooks
Brazilian Music
Classical
Classical 101 - Deep Cuts
Classical 101 - Next Steps
Classical 101 - The Basics
Grunge
Heavy Metal Classic
Movies
Music
Music Videos
On-The-Go 1
TV Shows
```


## Resultset에서 첫번째 행 가져오기

```javascript
db.get(sql, params, (err, row) => {
    // process the row here 
});
```



```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database
let db = new sqlite3.Database('./db/chinook.db');
 
let sql = `SELECT PlaylistId id,
                  Name name
           FROM playlists
           WHERE PlaylistId  = ?`;
let playlistId = 1;
 
// first row only
db.get(sql, [playlistId], (err, row) => {
  if (err) {
    return console.error(err.message);
  }
  return row
    ? console.log(row.id, row.name)
    : console.log(`No playlist found with the id ${playlistId}`);
 
});
 
// close the database connection
db.close();
```


## each() 메소드로 질의하기

```javascript
db.each(sql,params, (err, result) => {
   // process each row here
});
```

```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database
let db = new sqlite3.Database('../db/chinook.db');
 
let sql = `SELECT FirstName firstName,
                  LastName lastName,
                  Email email
            FROM customers
            WHERE Country = ?
            ORDER BY FirstName`;
 
db.each(sql, ['USA'], (err, row) => {
  if (err) {
    throw err;
  }
  console.log(`${row.firstName} ${row.lastName} - ${row.email}`);
});
 
// close the database connection
db.close();
```

```text
>node each.js
Dan Miller - dmiller@comcast.com
Frank Harris - fharris@google.com
Frank Ralston - fralston@gmail.com
Heather Leacock - hleacock@gmail.com
Jack Smith - jacksmith@microsoft.com
John Gordon - johngordon22@yahoo.com
Julia Barnett - jubarnett@gmail.com
Kathy Chase - kachase@hotmail.com
Michelle Brooks - michelleb@aol.com
Patrick Gray - patrick.gray@aol.com
Richard Cunningham - ricunningham@hotmail.com
Tim Goyer - tgoyer@apple.com
Victor Stevens - vstevens@yahoo.com
```