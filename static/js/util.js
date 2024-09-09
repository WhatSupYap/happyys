/**
 * JavaScript Utility Class
 */
export class Util {

    /**
     * @returns {boolean} 입력 모드 여부
     */
    get isWriteModeOn() {
        const element = document.activeElement
        if (element.tagName === 'TEXTAREA' || (element.tagName === 'INPUT' && element.type === 'text')) {
            return true;
        }
        else return false;
    }

    /**
     * @param {string} selector - CSS 선택자
     * @return {Element | NodeList} HTML 요소 또는 HTML 요소 리스트
     * @description
     * CSS 선택자를 사용하여 HTML 요소 또는 HTML 요소 리스트를 반환하는 함수
     * HTML 요소가 하나인 경우에는 HTML 요소를 반환하고, 여러 개인 경우에는 HTML 요소 리스트를 반환합니다.
     * 사용 예:
     * - q(".layer-curtain") => <div class="layer-curtain"></div>
     * - q(".btn") => [<button class="btn">버튼1</button>, <button class="btn">버튼2</button>]
     * - q("div") => [<div>요소1</div>, <div>요소2</div>, <div>요소3</div>]
     * - q("#app") => <div id="app">앱</div>
     * - q("#app .btn") => <button class="btn">버튼</button>
     * - q(".layer-curtain, .btn") => [<div class="layer-curtain"></div>, <button class="btn">버튼</button>]
     */
    q(selector) {
        const elements = document.querySelectorAll(selector);
        if (elements.length === 1) return elements[0];
        else return elements;
    }

    /**
     * @param {Element} element - HTML 요소
     * @return {boolean} 포커스 여부
     */
    getIsInputFocused(inputElement) {
        return document.activeElement === inputElement;
    }

    /**
     * 입력 값이 공백, null, undefined인 경우 기본값을 반환하는 함수
     * @param {any} value - 입력 값
     * @param {any} defaultValue - 기본값
     * @returns {any} - 유효한 입력 값 또는 기본값
     */
    getValidValue(value, defaultValue) {
        if (value === null || value === undefined || value === '') {
            return defaultValue;
        }
        return value;
    }

    /**
     * 문자열의 왼쪽에서부터 지정한 길이만큼 잘라내는 함수
     * @param {str} String 예) "Hello, World!"
     * @param {number} Number 예) 5
     * @returns {str} String 예) "Hello"
     */
    left(s, i) {
        return s.substr(0, i);
    }

    /**
     * 문자열의 오른쪽에서부터 지정한 길이만큼 잘라내는 함수
     * @param {str} 문자열 예) "Hello, World!"
     * @param {number} i 숫자 예) 5
     * @returns 문자열 예) "orld!"
     */
    right(s, i) {
        return s.substr(-i);
    }

    /**
     * 포함여부 확인 true / false를 반환
     * @param {*} arr 
     * @param {*} s 
     * @returns 
     */
    contains(arr, s) {
        let bResult = false;
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] == s) {
                bResult = true;
                break;
            }
        }
        return bResult;
    }

    /**
     * 포함여부 확인 include, 없으면 -1, 있으면 인덱스 반환
     * @param {*} arr 
     * @param {*} s 
     * @returns 
     */
    contains2(arr, s) {
        let iResult = -1;
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] == s) {
                iResult = i;
                break;
            }
        }
        return iResult;
    }

    // 연구주제
    setCookie(name, value, expiredays) {
        var todayDate = new Date();
        todayDate.setDate(todayDate.getDate() + expiredays);
        document.cookie = name + "=" + escape(value) + "; path=/; expires=" + todayDate.toGMTString() + ";"
    }

    setCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/";
    }

    /**
 * @returns {string} 짧은 랜덤 텍스트
 */
    get randomTextShort() {
        const adjectives = ['매운', '작은', '큰', '행운의', '밝은', '화려한', '빛나는', '어두운', '무서운', '착한', '사랑스러운', '귀여운', '멋진', '아름다운', '행복한', '슬픈', '우울한', '무료한'];
        const nouns = ['사슴', '고양이', '강아지', '사자', '호랑이', '돌고래', '고래', '펭귄', '팬더', '코끼리', '코알라', '용', '망아지', '토끼', '거북이', '거미', '나비', '벌', '꿀벌', '악어', '앵무새', '참새', '독수리', '매', '매미', '개미'];
        const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
        const noun = nouns[Math.floor(Math.random() * nouns.length)];
        return `${adjective} ${noun}`;
    }

    /**
     * @returns {string} 긴 랜덤 텍스트
     */
    get randomTextLong() {
        // 긴 노래 가사 배열
        const lyrics = [
            `몸 속 세포에 불을 지피듯이
            힘껏 공기를 들이마신다
            피와 땀을 제물로 동경을 성화로
            최고 음량으로 외쳐 봐
            빛이 있으리
            미래에 대한 염원을 신호로 삼고 스타트를 끊어
            가라 어둠을 활주로 삼아
            자신의 길을 경건히 나아가
            한 뼘 앞 절망에
            두 뼘 앞 희망을 믿고서
            대지를 박차는 이유는 단 하나
            더욱 빛나는 나는 날 수 있어
            오늘의 네 빛이
            망설이는 동료의 내일을 비출테니
            꿈을 십자가처럼 짊어지고
            에덴을 향하는 전사들에게
            높이 솟은 벽과 불안을 먹고 자라는 괴물에게
            희망이라는 바람 구멍을 뚫은 것은
            자그마한 가능성을 믿고 꿰뚫은 용기야 ​최고 음량으로 외쳐 봐
            빛이 있으리 가라 그림자와 보폭 맞춰서
            ​자신과 싸우는 나날에 행복 있으리
            ​구부러지지 않고 굴하지 않은 채 이상을 계속 쫓는
            ​가라 어둠을 활주로 삼아​그 각오를 ‘빛’이라 부르자
            ​빛이 있으리
            ​자신의 길을 경건히 나아가
            ​한 뼘 앞 절망에
            ​두 뼘 앞 희망을 믿고서
            ​천공을 높이 나는 유성은 오늘 밤
            목숨을 촉매로 태우네 ​오늘의 네 빛이
            ​무한대의 꿈을 십자가처럼 짊어지고
            에덴을 향하는 전사들에게 빛이 있으라`,
            `Tonight
            I'm gonna have myself a real good time
            I feel alive
            And the world, I'll turn it inside out, yeah
            I'm floating around in ecstasy, so
            Don't stop me now
            Don't stop me
            'Cause I'm having a good time, having a good time
            I'm a shooting star leaping through the sky like a tiger
            Defying the laws of gravity
            I'm a racing car, passing by like Lady Godiva
            I'm gonna go, go, go, there's no stopping me
            I'm burnin' through the sky, yeah
            200 degrees, that's why they call me Mister Fahrenheit
            I'm travelling at the speed of light
            I wanna make a supersonic man out of you
            I'm having such a good time
            I'm having a ball
            (Don't stop me now) if you wanna have a good time
            Just give me a call
            'cause I'm having a good time
            (Don't stop me now) yes, I'm havin' a good time
            I don't wanna stop at all, yeah
            I'm a rocket ship on my way to Mars on a collision course
            I am a satellite, I'm out of control
            I'm a sex machine ready to reload like an atom bomb
            About to whoa-oh, whoa-oh, oh, explode
            I'm burnin' through the sky, yeah
            200 degrees, that's why they call me Mister Fahrenheit
            I'm travelling at the speed of light
            I wanna make a supersonic woman of you
            hey-hey-hey
            (Don't stop me, don't stop me, ooh-ooh-ooh) I like it
            (Don't stop me, don't stop me) have a good time, good time
            (Don't stop me, don't stop me) oh
            Let loose, honey, alright
            Oh, I'm burnin' through the sky, yeah
            200 degrees, that's why they call me Mister Fahrenheit, hey
            I'm travelling at the speed of light
            I wanna make a supersonic man out of you (hey, hey)
            I'm having such a good time
            I'm having a ball
            (Don't stop me now) if you wanna have a good time (ooh, alright)
            Just give me a call
            yes, I'm havin' a good time
            I don't wanna stop at all
            Ah, da-da-da-da- da-da-ah-ah
            Ah-da-da, ah-ah-ah
            Ah, da-da, da-da-da-da-ah-ah
            Ooh, ooh-ooh, ooh-ooh`,
            `후회하고 있다면 깨끗이 잊어버려
            가위로 오려낸것 처럼
            다 지난 일이야
            후회하지 않는다면
            소중하게 간직해 언젠가 웃으면
            말할 수 있을 때까지
            너를 둘러싼 그 모든 이유가
            견딜수 없이 너무 힘들다 해도
            너라면 할수 있을꺼야
            할수가 있어 그게 바로 너야
            후하지 않는 보석같은 마음있으니
            어려워 마 두려워마
            아무것도 아니야
            천천히 눈을 감고 다시 생각해
            보는거야 세상이 너를
            무릅꿇게하여도
            당당히 니 꿈을 펼쳐 보여줘
            너라면 할수 있으꺼야
            할수가 있어
            그게 바로 너야 후하지 않는
            보석같은 마음있으니
            너라면 할수 있을거야
            할수가 있어 그게 바로 너야
            후하지 않는 보석같은 마음
            있잖니 후하지 않는 보석같은
            마음있...잖니`,
            `누구나 한 번쯤은 자기만의 세계로
            빠져들게 되는 순간이 있지
            그렇지만 나는 제자리로 오지 못했어
            되돌아 나오는 길을 모르니
            너무 많은 생각과 너무 많은 걱정에
            온통 내 자신을 가둬두었지
            이젠 이런 내 모습 나조차 불안해 보여
            어디부터 시작할지 몰라서
            나도 세상에 나가고 싶어
            당당히 내 꿈들을 보여줘야 해
            그토록 오랫동안 움츠렸던 날개
            하늘로 더 넓게 펼쳐 보이며
            날고 싶어
            감당할 수 없어서 버려둔 그 모든 건
            나를 기다리지 않고 떠났지
            그렇게 많은 걸 잃었지만 후회는 없어
            그래서 더 멀리 갈 수 있다면
            상처받는 것보다 혼자를 택한 거지
            고독이 꼭 나쁜 것은 아니야
            외로움은 나에게 누구도 말하지 않은
            소중한 걸 깨닫게 했으니까
            이젠 세상에 나갈 수 있어
            당당히 내 꿈들을 보여줄 거야
            그토록 오랫동안 움츠렸던 날개
            하늘로 더 넓게 펼쳐 보이며
            다시 새롭게 시작할 거야
            더 이상 아무것도 피하지 않아
            이 세상 견뎌낼 그 힘이 돼줄 거야
            힘겨웠던 방황을`,
            `사노라면 언젠가는
            밝은 날도 오겠지
            흐린 날도 날이 새면
            해가 뜨지 않더냐
            새파랗게 젊다는 게 한밑천인데
            째째하게 굴지말고 가슴을 쫙펴라
            내일은 해가 뜬다
            내일은 해가 뜬다
            비가 새는 작은 방에
            새우잠을 잔데도
            고운 님 함께라면 즐거웁지 않더냐
            오손도손 속삭이는 밤이 있는 한
            째째하게 굴지 말고 가슴을 쫙펴라
            내일은 해가 뜬다
            내일은 해가 뜬다
            사노라면 언젠가는
            밝은 날도 오겠지
            흐린날도 날이 새면
            해가 뜨지 않더냐
            새파랗게 젊다는 게 한밑천인데
            한숨일랑 쉬지말고 가슴을 쫙펴라
            내일은 해가 뜬다
            내일은 해가 뜬다
            내일은 해가 뜬다
            내일은 해가 뜬다`
        ];

        // 랜덤으로 가사를 선택하는 함수
        const randomIndex = Math.floor(Math.random() * lyrics.length);
        return lyrics[randomIndex];
    }
}