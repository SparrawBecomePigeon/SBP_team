var express = require('express');
var router = express.Router();

router.get('/', (req, res, next) => res.sendFile(__dirname + '/main.html'));
router.post('/', (req, res, next) => {
    
})

router.get('/list', (req, res, next) => res.sendFile(__dirname + '/list.html'));
router.post('/list', (req, res, next) => {
    console.log(req);
    const response = {
        result:1
    }
    
    res.send(response);
})

router.get('/modeling', (req, res, next) => res.sendFile(__dirname + '/modeling.html'));
router.post('/modeling', (req, res, next) => {
    
})

router.get('/index', (req, res, next) => res.sendFile(__dirname + '/sample5/index.html'));
router.post('/index', (req, res, next) => {
    
})

module.exports = router;