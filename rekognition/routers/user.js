var express = require('express')
var router = express.Router()
var userDAO = require('../models/dao/userDAO')
var path = require('path')

router.get('/userList', function(req, res, next){
    userDAO.userCheck(function(err, result){
        if(err) return next(err)
        res.render('userList', {stud_info : result})
    })
})


module.exports = router