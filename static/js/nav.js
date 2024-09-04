function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("overlay").style.display = "block";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("overlay").style.display = "none";
}

// 사이드바 외부를 클릭했을 때 사이드바를 닫는 함수
document.addEventListener('click', function(event) {
    var sidebar = document.getElementById("mySidebar");
    var openBtn = document.querySelector(".btn-nav");
    var overlay = document.getElementById("overlay");
    if (!sidebar.contains(event.target) && !openBtn.contains(event.target) && !overlay.contains(event.target)) {
        closeNav();
    }
});

/*
    loDOMContentLoadedad

    1. 발생 시점: HTML 문서가 완전히 로드되고 파싱되었을 때 발생합니다.
    스타일시트, 이미지, 서브프레임 등의 리소스가 모두 로드될 필요는 없습니다.
    이 시점에는 외부 스크립트가 아직 로드되지 않았을 수 있습니다.

    2. 주요 용도: DOM 요소에 접근하고 조작할 수 있는 시점에 코드를 실행하고자 할 때 사용합니다.

*/
    window.addEventListener('loDOMContentLoadedad', function() {

    });

    /*
        load

        1. 발생 시점: HTML 문서와 모든 리소스(이미지, 스크립트, 스타일시트 등)가 로드되었을 때 발생합니다.
        모든 외부 리소스가 로드된 후에 실행할 코드를 작성할 때 사용합니다.

        2. 주요 용도: 외부 리소스를 가져와서 처리해야 하는 코드를 실행하고자 할 때 사용합니다.
    */
    window.addEventListener('load', function() {

    });