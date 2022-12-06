/*!
* Start Bootstrap - Heroic Features v5.0.5 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

/*
function selectKW1(){
	var color = document.getElementById("맛");
	if (color.name === "맛"){
		color.style.backgroundColor = "#FF4A4A";
		color.name = "/맛"
	}
	else{
		color.style.backgroundColor = "white";
		color.name = "맛"
	}
}
function selectKW2(){
	var color = document.getElementById("가성비");
	if (color.name === "가성비"){
		color.style.backgroundColor = "#FF4A4A";
		color.name = "/가성비"
	}
	else{
		color.style.backgroundColor = "white";
		color.name = "가성비"
	}
}
function selectKW3(){
	var color = document.getElementById("서비스");
	if (color.name ==="서비스"){
		color.style.backgroundColor = "#FF4A4A";
		color.name = "/서비스"
	}
	else{
		color.style.backgroundColor = "white";
		color.name = "서비스"
	}
}
function selectKW4(){
	var color = document.getElementById("위생");
	if (color.name ==="위생"){
		color.style.backgroundColor = "#FF4A4A";
		color.name = "/위생"
	}
	else{
		color.style.backgroundColor = "white";
		color.name ="위생"
	}
}
function selectKW5(){
	var color = document.getElementById("분위기");
	if (color.name ==="분위기"){
		color.style.backgroundColor = "#FF4A4A";
		color.name = "/분위기"
	}
	else{
		color.style.backgroundColor = "white";
		color.name = "분위기"
	}
}*/

for (let e of document.querySelectorAll('input[type="range"].slider-progress')) {
  e.style.setProperty('--value', e.value);
  e.style.setProperty('--min', e.min == '' ? '0' : e.min);
  e.style.setProperty('--max', e.max == '' ? '100' : e.max);
  e.addEventListener('input', () => e.style.setProperty('--value', e.value));
}

var slider = document.getElementById("Range");
var output = document.getElementById("grade");
output.innerHTML = slider.value;
        
slider.oninput = function() {
	output.innerHTML = this.value;
}

function counter(text){	
	document.getElementById('lengthtext').innerHTML = text.value.length;
}

function reviewcancelBox(){
	var result= confirm("리뷰 작성을 취소하시겠습니까? 취소 시, 작성중인 리뷰는 삭제됩니다.")
	if(result == true) {
		alert("리뷰 작성이 취소되었습니다.")
		window.location.href = "detailInfo_review.html";
	}
}
function reviewsubmitBox(){
	alert("리뷰 작성이 완료되었습니다.");
	window.location.href = "detailInfo_review.html";
}

function addImg(){
  var fileName = document.getElementById("add-img").value;
  document.getElementById("img-btn").src = fileName;
}

function menucancelBox(){
	var result= confirm("대표메뉴 등록을 취소하시겠습니까?")
	if(result == true) {
		alert("대표메뉴 등록이 취소되었습니다.")
		window.location.href = "detailInfo_menu.html";
	}
}
function menusubmitBox(){
	alert("대표메뉴 등록이 완료되었습니다.");
	window.location.href = "detailInfo_menu.html";
}

function report(box) {
	let result=''
	if(box.checked == true){
	   var checkBox = document.getElementsByName("restaurant");
	   var msg = box.value + " 을(를) 내가 찜한 맛집에 추가했습니다.\n내가 찜한 맛집 페이지로 이동합니다.\n";
	   alert(msg);
	   location.href="/myRestaurantList"
	   }
	else{
	   result='';
	   var checkBox = document.getElementsByName("restaurant");
	   var msg = box.value + " 을(를) 내가 찜한 맛집에서 제거했습니다.\n";
	   alert(msg);
	}
 }

	


