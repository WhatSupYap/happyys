import { Util } from '/static/js/util.js';
const u = new Util();


const layer_curtain = u.q(".layer-curtain");
const sidebar = u.q(".sidebar");
const btn_open_lp_list = u.q(".btn-open-lp");
const btn_close_list = u.q(".btn-close-lp");
const searchbar = u.q(".searchbar");


const openSearchBar = function() {
    searchbar.style.display = "block";
    searchbar.querySelector("input[type='text']").focus();
    layer_curtain.style.display = "block";
}

const openSidebar = function() {
    sidebar.style.width = "250px";
    layer_curtain.style.display = "block";
}

const closeAllLP = function() {
    if (sidebar.style.width !== "0") sidebar.style.width = "0";
    if (searchbar.style.display !== "none") searchbar.style.display = "none";
    const inputText = searchbar.querySelector("input[type='text']");
    if (inputText.value !== "") inputText.value = "";
    layer_curtain.style.display = "none";
}

/**
 * @returns {boolean} true: layer popup is open, false: layer popup is closed
 */
const isLayerPopupOpen = function() {
    return !u.contains(["0","0px"], u.getValidValue(sidebar.style.width,"0")) || u.getValidValue(searchbar.style.display,"none") !== "none";
}

const init = function() {

    document.addEventListener('keydown', function(event) {

        if (event.key === 'Escape') {
            closeAllLP();
        }
        else if (!u.isWriteModeOn && !isLayerPopupOpen())
        {
            const input = document.querySelector('.searchbar input[type="text"]');
            if (u.getIsInputFocused(input)) return;
            else if (event.key === '/') {
                event.preventDefault(); // 기본 동작 방지 (예: 검색창 포커스)
                    if (!isLayerPopupOpen()) openSearchBar();
            }
            else if (event.key === '`') {
                event.preventDefault(); // 기본 동작 방지 (예: 검색창 포커스)
                if (!isLayerPopupOpen()) openSidebar();
            }
        }
    });

    // 사이드바 외부를 클릭했을 때 사이드바를 닫는 함수
    document.addEventListener('click', function(event) {

        if (event.target.closest('.btn-open-lp'))
        {
            const attrName = "data-target";
            let className = "";
            if (event.target.parentElement.hasAttribute(attrName))
                className = event.target.parentElement.getAttribute(attrName);
            else className = event.target.getAttribute(attrName);
            const target_layer = u.q('.' + className);
            if (target_layer === sidebar) openSidebar();
            else if (target_layer === searchbar) openSearchBar();
        }
        else if (!sidebar.contains(event.target) && !searchbar.contains(event.target) && !u.contains(btn_open_lp_list, event.target)) closeAllLP();
    });

    // 닫기 버튼을 눌렀을 때 레이어팝업 닫는 이벤트
    for (let btn of btn_close_list) btn.addEventListener('click', closeAllLP);

    // 검색창에서 엔터키를 눌렀을 때 이벤트
    document.getElementById('searchText').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            var query = event.target.value;
            var url = '/search?kw=' + encodeURIComponent(query) + '&page=1';
            window.location.href = url;
        }
    });



}

const page_load = function() {
}


/*
    DOMContentLoadedad

    1. 발생 시점: HTML 문서가 완전히 로드되고 파싱되었을 때 발생합니다.
    스타일시트, 이미지, 서브프레임 등의 리소스가 모두 로드될 필요는 없습니다.
    이 시점에는 외부 스크립트가 아직 로드되지 않았을 수 있습니다.

    2. 주요 용도: DOM 요소에 접근하고 조작할 수 있는 시점에 코드를 실행하고자 할 때 사용합니다.

*/
window.addEventListener('DOMContentLoaded', init);

/*
    load

    1. 발생 시점: HTML 문서와 모든 리소스(이미지, 스크립트, 스타일시트 등)가 로드되었을 때 발생합니다.
    모든 외부 리소스가 로드된 후에 실행할 코드를 작성할 때 사용합니다.

    2. 주요 용도: 외부 리소스를 가져와서 처리해야 하는 코드를 실행하고자 할 때 사용합니다.
*/
window.addEventListener('load', page_load);