// write "["
// loop through the json object
// for each {
// 	write "{"language":"key","
// 		for the object
// 		write ""location":"Location","
// 		create "speakers" array
// 		create "articles" array
// 		create "users" array
// 		create "depth" array
// 		parse string until the space
// 			if it matches "Speakers" {
// 				continue parsing and add the next four chars +","+"data" to the "speakers" array
// 			}
// 			if it matches "Articles"{
// 				continue parsing and add the next four chars +","+"data" to the "articles" array
// 			}
// 			if it matches "Users"{
// 				continue parsing and add the next four chars +","+"data" to the "users" array
// 			}
// 			if it maches "Depth"{
// 				continue parsing and add the next four chars +","+"data" to the "depth" array
// 			}
// 	write "},"
// }
// write "]"

var ourdata.json;

console.log("[")
$.each(json, function(key, data){
	console.log('{"language":"', key, '",')
	$.each(index, data)
	console.log()


})