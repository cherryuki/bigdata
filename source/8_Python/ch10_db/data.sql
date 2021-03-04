-- 21-03-03 Oracle ���� (c)cherryuki
CREATE TABLE MEMBER(
    NAME    VARCHAR2(20),
    PHONE   VARCHAR2(20),
    EMAIL   VARCHAR2(30),
    AGE     NUMBER(3),
    GRADE   NUMBER(1)   DEFAULT 1,
    ETC     VARCHAR2(30)
    );
COMMIT;
SELECT * FROM MEMBER;
INSERT INTO MEMBER VALUES('KONG', '010-0000-0000', 'KONG@GREEN.COM', 43, 5, 'KONGU');
INSERT INTO MEMBER VALUES('HAN', '010-0000-1111', 'HAN@GREEN.COM', 39, 5, 'JIMIN');
INSERT INTO MEMBER VALUES('YOON', '010-0000-2222', 'YOON@GREEN.COM', 73, 1, 'MINARI');
DELETE FROM MEMBER WHERE EMAIL='YOON@GREEN.COM';
COMMIT;
SELECT * FROM MEMBER;