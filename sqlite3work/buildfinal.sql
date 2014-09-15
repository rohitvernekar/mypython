PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE releaseinfo(
Id text not null primary key,
Client_name text default none,
Module text default none,
Release_id text default none,
Build_no int default 0,
Artifact_name text default none);
INSERT INTO "releaseinfo" VALUES('1','bcbsma','app','r5',1,'buildapp.tar');
COMMIT;
