# node.js - SQLITE 예제

## Executing statement in serialized mode with Database.serialize

```javascript
db.serialize(() => {
  // queries will execute in serialized mode
  db.serialize(() => {
    // queries will execute in serialized mode
  });
  // queries will execute in serialized mode
});
```

```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open the database connection
let db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    console.error(err.message);
  }
});
 
db.serialize(() => {
  // Queries scheduled here will be serialized.
  db.run('CREATE TABLE greetings(message text)')
    .run(`INSERT INTO greetings(message)
          VALUES('Hi'),
                ('Hello'),
                ('Welcome')`)
    .each(`SELECT message FROM greetings`, (err, row) => {
      if (err){
        throw err;
      }
      console.log(row.message);
    });
});
 
// close the database connection
db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
});
```

```
> node serialize.js
Hi
Hello
Welcome
```




## Executing statements in parallel with Database.parallelize

```javascript
db.parallelize(() => {
  // queries will execute in parallel mode
  db.parallelize(() => {
    // queries will execute in parallel mode
  });
  // queries will execute in parallel mode
});
```


```javascript
const sqlite3 = require('sqlite3').verbose();
 
// open a database connection
let db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    console.error(err.message);
  }
});
 
db.parallelize(() => {
  dbSum(1, 1, db);
  dbSum(2, 2, db);
  dbSum(3, 3, db);
  dbSum(4, 4, db);
  dbSum(5, 5, db);
});
 
// close the database connection
db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
});
 
function dbSum(a, b, db) {
  db.get('SELECT (? + ?) sum', [a, b], (err, row) => {
    if (err) {
      console.error(err.message);
    }
    console.log(`The sum of ${a} and ${b} is ${row.sum}`);
  });
}
```

```
>node parallelize.js
The sum of 5 and 5 is 10
The sum of 1 and 1 is 2
The sum of 4 and 4 is 8
The sum of 3 and 3 is 6
The sum of 2 and 2 is 4
```