-- 21-01-05 DBMS MySQL		ⓒcherryuki(ji)

-- 오라클과 MySQL 차이점( )
-- 계정생성, 권한부여, 권한박탈, 계정삭제(DCL)
-- DDL(제약조건, 시퀀스없음)
-- DML(OUTER JOIN, AND;&&, OR;||, 일부 단일행 함수) 
-- 기타(주석 '-- ' (SPACE까지 필요))

-- 계정생성, 권한부여, 권한박탈, 계정삭제(DCL)
-- JAVA에서 쓸 데이터 넣고 연습
show tables; -- select * from tab;
show databases; -- database들의 리스트 조회
-- DCL
create user user01 identified by 'password';
grant all on *.* to user01; -- DBA권한 부여
grant all privileges on *.* to user01; -- DBA권한
flush privileges; -- 권한 부여 확정(확실하게 권한 부여)
revoke all on *.* from user01; -- 권한 박탈
revoke all privileges on *.* from user01; -- 권한 박탈
drop user user01; -- 유저 삭제
-- 데이터베이스 공간으로 들어가기
create database kimdb; -- 새로운 kimdb 데이터베이스 공간 생성
show databases;
use world; -- wolrd 데이터베이스로 들어감
use kimdb; -- kimdb 데이터베이스로 들어감
select database(); -- 현재 들어와 있는 데이터베이스 확인
create table emp(
	empno		numeric(4)	 primary key,
    ename		varchar(20)	 not null,
    nickname	varchar(20)	 unique, -- null 포함 가능, 널 값 아닌 경우 유일한 값
    sal			numeric(7,2) check (sal>0),
    hiredate 	datetime	 default now(),
    comm		numeric(7,2) default 0
);
drop table if exists emp;
create table emp(
	empno		numeric(4),
    ename		varchar(20)	 not null, -- not null과 defalut는 아래로 내릴 수 없음. 반드시 옆에 기재
    nickname	varchar(20),
    sal			numeric(7,2),
    hiredate 	datetime	 default now(),
    comm		numeric(7,2) default 0,
    primary key(empno),
    unique(nickname),
    check(sal>0)
);
insert into emp (empno, ename, nickname, sal) values (1111, '공유', '도깨비', 5000);
select * from emp;
drop table if exists emp;
-- Major table(mCode; 자동 생성번호(like sequence) 이용, mName, mOffice)
-- Student table(sNo, sName, mCode)
drop table if exists student;
drop table if exists major;
create table major(
	mCode	int		primary key	auto_increment, -- auto_increment일 경우 데이터 타입 int여야 함
    mName	varchar(20),
    mOffice varchar(30)
);
desc major;
create table student(
	sNo		int,
    sName	varchar(20),
    mCode	int,
    primary key(sNo),
    foreign key(mCode) references major(mCode) -- foreign key 무조건 하단에 기재해야 함(데이터 타입 옆에 기재시 연동X)
);
desc student;
insert into major (mName, mOffice) values ('컴퓨터 공학', '704호'); -- auto_increment의 경우 언급x
insert into major (mName, mOffice) values ('지리학', '802호'); 
insert into major (mName, mOffice) values ('통번역학', '506호'); 
insert into major (mName, mOffice) values ('문화콘텐츠학', '401호'); 
select * from major;
insert into student values (1111, 'kong', 1);
insert into student values (1004, 'maehwa', 3);
insert into student values (1005, 'kim', 3);
insert into student values (2001, 'pooh', 4);
insert into student values (1000, 'tiger', 5); -- 삽입 불가능 (parent key; mCode 없음)
select * from student;
select sNo, sName, mName, m.mcode, mOffice from student s, major m
	where s.mcode=m.mcode;
select sNo 학번, sName 이름, mName 학과명, m.mcode 전공번호, mOffice 학과사무실 from student s, major m
	where s.mcode=m.mcode;
-- outer join은 오라클(+)과 다름
-- right outer join -- 원하는 정보가 있는 쪽의 방향(left, right) 입력
select sNo, sName, mName, m.mcode, mOffice
	from student s right outer join major m
    on s.mcode=m.mcode;

-- 자바(JDBC)에서 사용할 table 생성 및 데이터 입력
drop table if exists personal;
drop table if exists division;
create table division(
	dno			int, 		    -- 부서번호
    dname		varchar(20),	-- 부서명
    phone		varchar(20),	-- 부서전화
    position	varchar(20),	-- 부서 위치
    primary key(dno)
);
create table personal(
	pno		int,				  -- 사번
    pname	varchar(20)	not null, -- 사원명
    job		varchar(20) not null, -- 직책
    manager	int,				  -- 상사의 사번
    startdate	date, 			  -- 입사일
    pay		int,				  -- 급여
    bonus	int,				  -- 상여
    dno		int,				  -- 부서번호
    primary key(pno),
    foreign key(dno) references division(dno)
);
desc division;
desc personal;
insert into division values (10, 'finance', '02-700-1004', '신촌');
insert into division values (20, 'research', '02-777-7000', '신도림');
insert into division values (30, 'sales', '02-700-1000', '강남');
insert into division values (40, 'marketing', '02-700-2000', '종로');
commit;
insert into personal values (1111,'smith','manager', 1001, '1990-12-17', 1000, null, 10);
insert into personal values (1112,'ally','salesman',1116,'1991-02-20',1600,500,30);
insert into personal values (1113,'word','salesman',1116,'1992-02-24',1450,300,30);
insert into personal values (1114,'james','manager',1001,'1990-04-12',3975,null,20);
insert into personal values (1001,'bill','president',null,'1989-01-10',7000,null,10);
insert into personal values (1116,'johnson','manager',1001,'1991-05-01',3550,null,30);
insert into personal values (1118,'martin','analyst',1111,'1991-09-09',3450,null,10);
insert into personal values (1121,'kim','clerk',1114,'1990-12-08',4000,null,20);
insert into personal values (1123,'lee','salesman',1116,'1991-09-23',1200,0,30);
insert into personal values (1226,'park','analyst',1111,'1990-01-03',2500,null,10);
select * from personal;
commit;
-- DML (SELECT, UPDATE, DELETE, INSERT)
-- 연습문제
select * from personal;
select * from division;
-- 1. 사번, 이름, 급여를 출력
select pno, pname, pay from personal;
-- 2. 급여가 2000~5000 사이 모든 직원의 모든 필드
select * from personal where pay between 2000 and 5000;
-- 3. 부서번호가 10또는 20인 사원의 사번, 이름, 부서번호
select pno, pname, dno from personal where dno in (10, 20);
-- 4. 보너스가 null인 사원의 사번, 이름, 급여 급여 큰 순정렬
select pno, pname, pay from personal where bonus is null;
-- 5. 사번, 이름, 부서번호, 급여. 부서코드 순 정렬 같으면 PAY 큰순
select pno, pname, dno, pay from personal order by dno, pay desc;
-- 6. 사번, 이름, 부서명
select pno, pname, dname from personal p, division d
	where p.dno=d.dno;
-- 7. 사번, 이름, 상사이름
select w.pno, w.pname, m.pname mgrname from personal w, personal m
	where w.manager=m.pno;
-- 8. 사번, 이름, 상사이름(상사가 없는 사람도 출력)
select w.pno, w.pname, m.pname manager
	from personal w left outer join personal m 
	on w.manager=m.pno; -- outer join시 조건부분 where 아닌 on 써야함
-- 8-1. 사번, 이름, 상사이름(상사가 없을 경우 '없음' 출력)
select w.pno, w.pname, ifnull(m.pname, '없음') mgrname
	from personal w left outer join personal m
	on w.manager=m.pno;
select w.pno, w.pname, if(m.pname is null, '없음', m.pname) mgrname
	from personal w left outer join personal m
	on w.manager=m.pno;
-- 9. 이름이 s로 시작하는 사원 이름
select pname from personal where pname like 's%';
-- 10. 사번, 이름, 급여, 부서명, 상사이름
select w.pno, w.pname, w.pay, dname, m.pname
	from personal w, personal m, division d
    where w.manager=m.pno and w.dno=d.dno;
-- 11. 부서코드, 급여합계, 최대급여
select dno, sum(pay), max(pay) from personal group by dno;
-- 12. 부서명, 급여평균, 인원수
select dname, avg(pay), count(*) from personal p, division d
	where p.dno=d.dno group by dname;
-- 13. 부서코드, 급여합계, 인원수 인원수가 4명 이상인 부서만 출력
select dno, sum(pay), count(*) from personal
	group by dno having count(*)>=4;
-- 14. 사번, 이름, 급여 회사에서 제일 급여를 많이 받는 사람
select pno, pname, pay from personal
	where pay = (select max(pay) from personal);
-- 15. 회사 평균보다 급여를 많이 받는 사람 이름, 급여, 부서번호
select pname, pay, dno from personal 
	where pay > (select avg(pay) from personal);
-- 16. 15번에 부서명을 추가하고 부서명순 정열 같으면 급여 큰순
select pname, pay, p.dno, dname from personal p, division d 
	where p.dno=d.dno && pay > (select avg(pay) from personal)
    order by dname, pay desc;
-- 17. 자신이 속한 부서의 평균보다 많인 받는 사람의 이름, 급여, 부서번호, 반올림한 해당부서평균
select pname, pay, dno, round((select avg(pay) from personal where p.dno=dno)) avgpay from personal p
	where pay > (select avg(pay) from personal where p.dno=dno);
-- 18. 입사가 가장 빠른 사람의 이름, 급여, 부서명
select pname, pay, dname from personal p, division d
	where p.dno=d.dno && startdate = (select min(startdate) from personal);
-- 19. 이름, 급여, 해당부서평균
select pname, pay, (select avg(pay) from personal where p.dno=dno) avgpay from personal p;
-- 20. 이름, 급여, 부서명, 해당부서평균(반올림)
select pname, pay, dname, round((select avg(pay) from personal where p.dno=dno)) avgpay
	from personal p, division d
	where p.dno=d.dno;
    
-- Oracle에서의 단일행 함수와 MySQL 칼럼 함수의 다른 부분
select concat(pname, '은 ', job, '이다') from personal; -- 여러개 연결 가능(오라클은 2개씩만 가능)
select round(12345.67, 1); -- from 절 없이도 실행 가능(오라클은 from절 필수여서 확인용으로 from dual 이용)
select year(startdate), month(startdate), pname from personal; -- 오라클의 extract(year from 날짜) = MySQL의 year(날짜)
select monthname(startdate) from personal; -- (영문)월 이름 추출
select dayname(startdate) from personal; -- 요일 추출
-- date_format
-- %y 년도 2자리(21), %Y 년도 4자리(2021)
-- %M 월 이름(January), %m 월 2자리(01), %b 짧은 월이름(Jan), %c 월(1,2,....12)
-- %d 일 2자리(05), %e 일(5)
-- %H 24시간, %h 12시간, %p(오전, 오후), %i 분, %s 초
select date_format(now(), '%y년%m월%d일 %p%h시 %i분 %s초');
-- personal 이름, 입사일(1989년 1월 9일)
select pname, date_format(startdate, '%Y년 %c월 %e일') 입사년월일 from personal;
-- 시스템으로부터 현재 날짜, 시간
select sysdate();
select now();
-- 시스템으로부터 현재 날짜
select current_date();
select curdate();
-- 시스템으로부터 현재 시간
select current_time();
select curtime();
-- format()
select format(pay, 1) from personal; -- 숫자가 소수점 1자리까지 나오고, 3자리 마다 ,
select format(pay, 0) from personal; -- 3자리마다 , 
-- personal 이름, 급여, 급여 3000이상이면 높음, 아니면 낮음 출력
select pname, pay, if(pay>=3000, '높음', '낮음') from personal; -- if를 NVL()함수 대신 사용하기도 함; ifnull( )도 가능

-- top-N구문 다른점
select pname, pay from personal order by pay desc;
-- limit n; 1~n등까지 출력
select pname, pay from personal order by pay desc limit 5; -- 1~5등까지 출력
-- limit n1, n2; n1번째부터 n2개 출력(0번째부터 카운트, ※0번째=1등)
select pname, pay from personal order by pay desc limit 5, 5; -- 6~10등까지 출력
-- 3~5등 limit 2, 3
select pname, pay from personal order by pay desc limit 2,3;
-- 1~3등
select pname, pay from personal order by pay desc limit 3;
select pname, pay from personal order by pay desc limit 0,3;