PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE taginfo(
release_primary_key text not null primary key,
client_name text default none,
client_jiva text default none,
jiva_version text default none,
last_updated text default none);
COMMIT;
