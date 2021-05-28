BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "qnaapi_ntuhqna" (
	"qid"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(50),
	"que"	varchar(180),
	"ans"	varchar(250)
);

INSERT INTO "qnaapi_ntuhqna" ("qid","title","que","ans") VALUES 
 (1,'諮詢專線','門診業務諮詢專線？','服務時間：週一~週五 08：00~17：00  總院：(02)2356-2504、2356-2505 兒醫：(02)2312-3456 轉分機 70170、70171'),
 (2,'病症掛科','查詢病症應掛那一科？','請於週一~週五08：00~17：00洽詢健康教育中心 (02)2312-3456 分機 62114。'),
 (3,'看診時間','門診醫師之看診時間？','上午門診：09：00~12：00 下午門診：13：30~16：30');
COMMIT;


CREATE TABLE IF NOT EXISTS "myapp_ntuhqna" (
	"qid"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(50),
	"que"	varchar(180),
	"ans"	varchar(250)
);

INSERT INTO "myapp_ntuhqna" ("qid","title","que","ans") VALUES 
 (1,'諮詢專線','門診業務諮詢專線？','服務時間：週一~週五 08：00~17：00  總院：(02)2356-2504、2356-2505 兒醫：(02)2312-3456 轉分機 70170、70171'),
 (2,'病症掛科','查詢病症應掛那一科？','請於週一~週五08：00~17：00洽詢健康教育中心 (02)2312-3456 分機 62114。'),
 (3,'看診時間','門診醫師之看診時間？','上午門診：09：00~12：00 下午門診：13：30~16：30');
COMMIT;
