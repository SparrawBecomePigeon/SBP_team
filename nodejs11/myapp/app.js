var express = require('express');
var app = express();
var fs = require('fs');

const bodyParser = require('body-parser'); 
app.use(bodyParser.urlencoded({extended:true})); 
app.use(bodyParser.json());

app.get('*', function(request, response, next){
    fs.readdir('./data', function(error, filelist){
      request.list = filelist;
      next();
    });
  });

app.use('/', require('./html/option'));
// console.log(__dirname);
// app.use(express.static(__dirname + '/html/sample5'));

var server = app.listen(3000, () => {
    console.log('app listening on port : 8000');
});