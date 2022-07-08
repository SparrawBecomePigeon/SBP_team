var express = require('express');
var router = express.Router();
var path = require('path');

/* GET home page. */
router.get('/', function(req, res, next) {
  var publicPath = path.join(__dirname, '/sample1/1.html');
  router.use(express.static(publicPath));
  res.render('index', { title: 'Express' }); 
});

// router.get('/', function(req, res, next) {
//   var publicPath = path.join(__dirname, '/sample1/1.html');
//   console.log(__dirname);
//   router.use(express.static(publicPath));
// });

module.exports = router;
