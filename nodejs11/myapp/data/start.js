var express = require('express');
const { fstat } = require('fs');
var router = express.Router();
var path = require('path');
var Id = require('../html/topic');

//var title = require('./option.js');
console.log(title);
var title = 'sample7';
console.log(title);
router.use(express.static(__dirname + `/${title}`));


module.exports = router;