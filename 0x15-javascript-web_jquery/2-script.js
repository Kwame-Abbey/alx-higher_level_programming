// Change header text color when a div is clicked
$(function () {
  $("div#red_header").bind("click", function () {
    $("header").css("color", "#FF0000");
  });
});
