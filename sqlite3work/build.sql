PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE clients (
client_name text not null primary key);
INSERT INTO "clients" VALUES('bcbsma');
INSERT INTO "clients" VALUES('bcbsma2');
INSERT INTO "clients" VALUES('amfc');
INSERT INTO "clients" VALUES('bcbsfl');
CREATE TABLE releases (
r_id text not null primary key,
release text,
client_name text references clients);
INSERT INTO "releases" VALUES('bcbsmar5','r5','bcbsma');
INSERT INTO "releases" VALUES('bcbsma2r5','r5','bcbsma2');
INSERT INTO "releases" VALUES('bcbsmar5.1','r5.1','bcbsma');
INSERT INTO "releases" VALUES('amfcr10','r10','amfc');
CREATE TABLE buildconfig(
r_id text references releases(r_id),
build_no int,
build_artifact text);
INSERT INTO "buildconfig" VALUES('bcbsmar5',1,'buildartifactname.tar');
INSERT INTO "buildconfig" VALUES('amfcr10',1,'buildartifactname.tar');
INSERT INTO "buildconfig" VALUES('bcbsmar5',2,'buildartifactname.tar');
COMMIT;
