// JavaScript source code
/*  21-01-13 HTML       (c)cherryuki(ji) */

name = prompt("이름을 입력하세요", "공유");
document.write(name + "~Welcome <br>");
function chk() {
    if (frm.tel.value.length < 4) {
        alert("전화번호 뒷 4자리 이상 입력해주세요");
        return false;
    }
}