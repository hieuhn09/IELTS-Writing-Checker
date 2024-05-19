
let options = {
  startAngle: -1.55,
  size: 150,
  fill: {gradient: ['#a445b2', '#fa4299']}
}
$(".circle .bar").circleProgress(options).on('circle-animation-progress',
function(event, progress, stepValue){
  $(this).parent().find("span").text(7.5);
});
$(".js .bar").circleProgress({
  value: 7.5 / 9.0
});
