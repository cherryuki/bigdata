//2021 - 01 - 27 JavaScripts_기본 내장객체      ⓒcherryuki(ji)
//this.getInterval(that); this날과 that날 사이의 날짜 계산해주는 메소드
Date.prototype.getInterval = function (that) {
    if (this > that) {
        var intervalMili = this.getTime() - that.getTime(); //경과일
    } else {
        var intervalMili = that.getTime() - this.getTime(); //D-day
    }
    var intervalDay = intervalMili / (1000 * 60 * 60 * 24);
    return Math.trunc(intervalDay);
};