// $(document).ready( function() {
//
//  $("div").each( function(i) {
//   $(this).append("<img src='images/"+(++i)+".jpg' width='100' height='' />");
//  });
//
// // });

$(function(){

  //showimages();
  setInterval("refreshpage()",5000);
  //  setInterval("showimages()",5500);

})

function showimages(){

 // ----------------SHOW IMAGE ----------------------------------

  var folder  = "images/";
  $.ajax({
      url : folder,
      success: function (data) {
          $(data).find("a").attr("href", function (i, val) {


              if( val.match(/\.(jpg|png|gif)$/) ) {

                  $(".images").append( "<img src='"+ folder + val +"' width='100' height='100' ><br>" );

              }
          });
            // $(".images").append( "<br>" );
      }
  });

  // ----------------SHOW IMAGE ----------------------------------
  // ----------------SHOW  WORD ----------------------------------

  $(document).ready(function() {
      $.ajax({
          url : "./NAME.txt",
          success : function (data) {

            $.each(data.split(/\n/) , function (index, value){
              // alert(value);
                $(".names").append("<br><br><br>"+ value + "<br><br><br>")
            });

            // $(".names").html(data);
          }
      });

       $("body").append( "<br>" );

      $.ajax({
          url : "./SCORE.txt",
          success : function (data) {

            $.each(data.split(/\n/) , function (index, value){
              // alert(value);
              $(".scores").append("<br><br><br>" +value + "<br><br><br>");

            });
            //
              // $(".scores").html(data);
          }
      });
  });

  // ----------------SHOW  WORD ----------------------------------
}


function refreshpage()
{
  window.location.reload();
  showimages();
}
