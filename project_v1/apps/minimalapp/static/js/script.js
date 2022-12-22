var s = skrollr.init();

//滑動離開頂部時就取消at_top的class
$(window).scroll(function(e){
  if($(window).scrollTop()<=0)
    $(".explore, .navbar").addClass("at_top");
  else
    $(".explore, .navbar").removeClass("at_top");
});

