var con = require('../connection')

var userDAO = {
    userCheck : function(callback){
        var sql = 'select * from stud_info'
        con.query(sql, function(err, result){
            if(err) return callback(err)
            callback(null, result)
        })
    },
}

module.exports = userDAO;