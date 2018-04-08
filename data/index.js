var http = require('http');
var https = require('https');
var express = require('express');
fs = require('fs');

var app = express();
var bodyParser = require('body-parser');
var parseString = require('xml2js').parseString;

app.use(bodyParser.urlencoded());
app.use(bodyParser.json());


var server_port = process.env.PORT || 8000;
//var server_port = 8080;
var server_ip_address = '0.0.0.0';

var fileName = "CurrentCategoryIPDump.json";

app.get('/getFile/', function (req, result) {
	fs.readFile(fileName, "utf-8",function (err,data) {
	  if (err) {
		return console.log(err);
	  }
	data = JSON.parse(data)
	dataip = data["ip_category"]
	datamac = data["ip_mac"]
	body = {}
	for(var x in dataip){
		console.log(x);
		if(x.startsWith("192")){
			if(!body[dataip[x]]){
				body[dataip[x]] = []
			}
			body[dataip[x]].push([x,datamac[x]]);
		}
	}
	result.header("Access-Control-Allow-Origin", "*");
	result.header("Access-Control-Allow-Headers", "X-Requested-With");
	result.setHeader('content-type', 'application/json');
	result.send(body);
	});
});


app.post('/savefile/', function (req, result) {
	var file = req.body;
	fs.writeFile(fileName, JSON.stringify(file), function (err) {
		if (err) return console.log(err);
		result.header("Access-Control-Allow-Origin", "*");
		result.header("Access-Control-Allow-Headers", "X-Requested-With");
		result.setHeader('content-type', 'application/json');
		result.send("success");
	});
	
	
});


app.get('/getNewsData/:symbol', function (req, result) {
	
	var url= "https://seekingalpha.com/api/sa/combined/"+req.params.symbol+".xml";
	https.get(url, function(res) {
		res.setEncoding('utf8');
		var body = '';
		res.on('data', function(chunk) {
			body += chunk;
		});
	  
		res.on('end', function (chunk) {
			parseString(body, function (err, jsonObj) {
				var items = jsonObj['rss']["channel"][0]["item"];
				var count=1;
				var newsJson=[];
				for(var item in items){
					var item = items[item];
					var link = item["link"][0]; 
					if(link.indexOf("article")!==-1 && count<6){
						
						newsJson.push({
							"title": item["title"][0],
							"pubdate": item["pubDate"][0],
							"author": item["sa:author_name"][0],
							"link": link
							
						});
						count++;
					}
				}
				
				
				result.header("Access-Control-Allow-Origin", "*");
				result.header("Access-Control-Allow-Headers", "X-Requested-With");
				result.setHeader('content-type', 'application/json');
				result.send(newsJson);
			});	
		});
	}).end();
});


app.get('/getGraphData/:symbol/:functionName', function (req, response) {
	var functionName = req.params.functionName
	var url = "https://www.alphavantage.co/query?interval=daily&series_type=close&apikey=2JB5EK5YSRHM311D&function="+functionName+"&symbol="+req.params.symbol;
	
	if(functionName=="STOCH"){
		url+="&slowkmatype=1&slowdmatype=1&time_period=10";
	}
	else if(functionName=="BBANDS"){
		url+="&nbdevup=3&nbdevdn=3&time_period=5"
	}
	else{
		url+="&time_period=10";
	}
					
	
	https.get(url, function(res) {
		res.setEncoding('utf8');
		var body = '';
		res.on('data', function(chunk) {
			body += chunk;
		});
	  
	  res.on('end', function (chunk) {
		var data = JSON.parse(body);
		try{
			var sixMonths = new Date();
			sixMonths.setMonth(sixMonths.getMonth()-6);
			var lastDate = data["Meta Data"]["3: Last Refreshed"];
			var symbol = data["Meta Data"]["1: Symbol"].toUpperCase();
			var seriesData = data["Technical Analysis: "+functionName.toUpperCase()];
			var seriesNames = []
			var keys = Object.keys(seriesData[lastDate]);
			var result=[];
			
			if(keys.length>1){
				for(var x in keys){
					seriesNames.push(symbol+" "+keys[x]);
					result.push([]);
				}
			}
			else{
				seriesNames.push(symbol);
				result.push([]);
			}
			
			
			var dateArray=[];
			
			for(var x in seriesData){
				var date = x.split("-")
				date = Date.UTC(date[0],parseInt(date[1])-1,date[2]);
				if(date<sixMonths)
					break;
				dateArray.push(date);
				
				for(var i=0;i<keys.length;i++){
					result[i].push(parseFloat(seriesData[x][keys[i]]));	
				}
					
				
			}
			
			var series=[]
			for(var i=0;i<keys.length;i++){
					series.push({
						type: 'spline',
						name: seriesNames[i],
						data: result[i],
					});
					
			}
			
			response.setHeader("Access-Control-Allow-Origin", "*");
			response.setHeader("Access-Control-Allow-Headers", "X-Requested-With");
			response.setHeader('content-type', 'application/json');
			response.send({"series":series,"heading":data["Meta Data"]["2: Indicator"],"dateArray":dateArray,"functionName":functionName});
		}
		catch(err){
			console.log(err);
			response.setHeader("Access-Control-Allow-Origin", "*");
			response.setHeader("Access-Control-Allow-Headers", "X-Requested-With");
			response.setHeader('content-type', 'application/json');
			data["functionName"] = functionName;
			response.send(data);
		}
	  });
	}).end();
});

app.listen(server_port, server_ip_address, function () {
	console.log("Listening on " + server_ip_address + ", server_port " + server_port);
});

