// var wordslist = {};

// wordslist.list = [
//   {name: "爛", score: 1, times: 1},
//   {name: "糟糕", score: 1, times: 5},
//   {name: "服務差", score: 2, times: 5},
//   {name: "不好", score: 1, times: 2},
//   {name: "廢", score: 1, times: 3}
// ];

var  no_item_html = "<p class='no_item'>沒有資料歐</p>";

if (Object.keys(dataset_p['source']).length==1) {
  $("#no_item_p").append(no_item_html);
}

if (Object.keys(dataset_n['source']).length==1) {
  $("#no_item_n").append(no_item_html);
}

if (Object.keys(dataset_b['source']).length==1) {
  $("#no_item_b").append(no_item_html);
}

// var item_html = "<li class='words'>{{item}}<div class='score'>{{score}}</div><div class='times'>{{times}}</div></li>";


// for(var i=0; i<wordslist.list.length; i++) {
//   var item = wordslist.list[i];
  
//   var current_item_html =
//       item_html.replace("{{item}}", item.name)
//                .replace("{{score}}", item.score)
//                .replace("{{times}}", item.times)
//   ;
  
//   $("#items_list").append(current_item_html);
  
// }