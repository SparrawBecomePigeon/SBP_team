const { json } = require('express');
var express = require('express');
var fs = require('fs');
var router = express.Router();
var path = require('path');
var request = require('request');
var template = require('../template/template.js');
var qs = require('querystring');

router.get('/', (req, res, next) => res.sendFile(__dirname + '/main.html'));
router.post('/', (req, res, next) => {

  var post = req.body;
  var title = post.title;
  global.title = title;
  console.log(title);
  res.redirect('/');
  
})

router.get('/send', function (req, res) {
  
  var jsonDataObj = { name : 'model_1'};
  request.post({
    url: 'http://54.180.142.70:3000/modeling',
    body: jsonDataObj,
    json: true
  }, function(error, response, body){
    res.json(body);
    console.log("success to send!");
  })

  //192.168.0.6 
  //54.180.142.70:3000/modeling
  //console.log("success to send!");
  
  

  res.sendFile(__dirname + '/send.html')

});
router.post('/send', (req, res, next) => { 
    /* 
    
    url + /list 에 post시 json파일을 body에 담아 온다 
    본 web서버 post에서는 받아온 json파일을 저장(즉, POST요청을 받았을시)
    + 작업이 끝난 아두이노는 unity에게 파일 제목과 함께 신호를 보냄

    신호를 받은 unity는 자동으로 서버에 post요청
    그러면 unity에서 url+/get 으로 post요청을 보내면 
    request에서 받을 json에대한 정보를 꺼내고
    해당 json파일을 리턴

    모델링이 완료된 unity에서는 post요청을 보냄
    url+/upload 라 할시 data 저장하고 목록을 갱신

    or s3에서 가져옴
    
    */
   var title = "lab_modeling";
    var description = JSON.stringify(req.body);
    fs.writeFile(`html/index/${title}.json`, description, 'utf8', function(err){
        if(err) throw err;
        res.send('성공!');
        //res.send("<script>alert('your alert message'); window.location.href = \"/\"; </script>");
    })
    
    
    console.log(req.body);
    
})
router.use('/data', require('./topic'));
router.get('/modeling', function(req, res) { 
    var title = 'Modeling List';

    var list = template.list(req.list);
    var html = template.HTML(title, list); 
    res.send(html);

  });

router.post('/modeling', (req, res, next) => {
    router.use('/modeling', require('../data/start'));
    next();
    //console.log(req.body);
})


//router.use('/index', require('./start'));
//app.use(express.static(__dirname + '/data/sample'));
router.get('/index', (req, res, next) => {
    //router.use(express.static(__dirname + '/temp'));
    
    // console.log('index get');
    router.use('/index', require('../data/start'));
    next();
})
// router.post('/index', (req, res, next) => {
//     console.log(__dirname);
//     router.use(express.static(__dirname + '/sample5'));
// })


module.exports = router;
