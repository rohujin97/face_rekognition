const mysql = require('mysql');

var connection = mysql.createConnection({
    host : "localhost",
    port : 3306,
    user : "root",
    password : "1111",
    database : "sys"
})

connection.connect(function(err) {
  if (err) {
    return console.error('error: ' + err.message);
  }
 
  console.log('Connected to the MySQL server.');
});

module.exports = connection;