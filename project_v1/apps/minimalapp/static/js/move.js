//緩慢滑動
$(document).on('click', 'a', function(event){
    event.preventDefault();
    var target = $(this).attr("href");
    $('html, body').animate({
      scrollTop: $(target).offset().top
    }, 500);
  });
  
  //滑鼠移動時觸發的事件
  $(window).mousemove(function(evt){
    var pagex = evt.pageX;
    var pagey = evt.pageY;
    
    //計算相對區域的位置
    var x = pagex-$("section#section_about").offset().left;
    var y = pagey-$("section#section_about").offset().top;
    
    //計算現在的y位置超過區域則隱藏
    if (y<0 ||　y>$("section#section_about").outerHeight())
      $("#cross").css("opacity",0);
    else
      $("#cross").css("opacity",1);
  
    //更新一些移動景物的位置
    $(".mountain").css("transform","translateX("+(x/-20+0)+"px)")
    
    //更新簡介中文字的飄浮位置
    $(".r1text").css("transform","translateX("+y/+7+"px)");
    $(".r2text").css("transform","translateX("+y/-10+"px)");
    $(".r3text").css("transform","translateX("+y/+4+"px)");
    $(".r4text").css("transform","translateX("+y/-5+"px)");
  });