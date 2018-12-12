var express = require('express')
var app = express()
var path = require('path')
var bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

var userDAO = require('./models/dao/userDAO')


  app.set('views', path.join(__dirname, 'views'))
  app.set('view engine', 'ejs')

  app.get('/', function (req, res){
      res.render('index')
  })

  var user = require('./routers/user')
  app.use('/user', user)

  app.use(function (err, req, res, next){
      console.log(err);
      res.end("<h1>ERROR!</h1>")
  })

  app.listen(3000, function(){
      console.log('3000번 포트 구동중')
  })
  