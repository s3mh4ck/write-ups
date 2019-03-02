var express = require("express");
var app = express();
var expressWs = require('express-ws')(app);
var fs = require("fs");

var flag = fs.readFileSync("../flag").toString();

app.use(express.static('.'));

app.ws('/', function(ws, req) {
	var seed = new Date().valueOf() & 0xFFFFFFFF;
	var rnd = betterRand(seed)
    var userId = new Buffer(seed.toString()+","+rnd.next().value).toString("base64")
    
    var numbers = Array.from(Array(6)).map(() => Math.floor(rnd.next().value * 89 + 10))

    ws.on('message', function(msg) {
        try {
            var m = JSON.parse(msg.replace("'", '').replace("'", ''));
            var resp = {"numbers": numbers}
            
            if(JSON.stringify(resp.numbers) === JSON.stringify(m.numbers))
                resp.flag = flag;

            console.log(resp);
            ws.send(JSON.stringify(resp));
        } catch(err) { }

        ws.close()
    });

    console.log("[*] Peer connected!");
    ws.send(JSON.stringify({"userId": userId}))
});

console.log("[*] Listening on port 5555...")
app.listen(5555);

function* betterRand(seed) {
  var m = 25, a = 11, c = 17, z = seed || 3;
  for(;;) yield (z=(a*z+c)%m)/m;
}
