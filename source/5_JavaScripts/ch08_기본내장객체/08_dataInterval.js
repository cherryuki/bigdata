//2021 - 01 - 27 JavaScripts_�⺻ ���尴ü      ��cherryuki(ji)
//this.getInterval(that); this���� that�� ������ ��¥ ������ִ� �޼ҵ�
Date.prototype.getInterval = function (that) {
    if (this > that) {
        var intervalMili = this.getTime() - that.getTime(); //�����
    } else {
        var intervalMili = that.getTime() - this.getTime(); //D-day
    }
    var intervalDay = intervalMili / (1000 * 60 * 60 * 24);
    return Math.trunc(intervalDay);
};