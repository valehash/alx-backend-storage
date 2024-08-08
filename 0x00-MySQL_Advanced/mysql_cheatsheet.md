
# MySQL Cheatsheet

=====================

## Browsing

-----------

### Show databases, tables, and fields

```sql
SHOW DATABASES;

SHOW TABLES;

SHOW FIELDS FROM table / DESCRIBE table;

SHOW CREATE TABLE table;

SHOW PROCESSLIST;

KILL process_number;
```

## Select

### Basic select statements

```sql
SELECT * FROM table;

SELECT * FROM table1, table2;

SELECT field1, field2 FROM table1, table2;

SELECT ... FROM ... WHERE condition;

SELECT ... FROM ... WHERE condition GROUP BY field;

SELECT ... FROM ... WHERE condition GROUP BY field HAVING condition2;

SELECT ... FROM ... WHERE condition ORDER BY field1, field2;

SELECT ... FROM ... WHERE condition ORDER BY field1, field2 DESC;

SELECT ... FROM ... WHERE condition LIMIT 10;

SELECT DISTINCT field1 FROM ...;

SELECT DISTINCT field1, field2 FROM ...;
```

### Joining tables

```sql
SELECT ... FROM t1 JOIN t2 ON t1.id1 = t2.id2 WHERE condition;

SELECT ... FROM t1 LEFT JOIN t2 ON t1.id1 = t2.id2 WHERE condition;

SELECT ... FROM t1 JOIN (t2 JOIN t3 ON ...) ON ...;
```

## Conditions

### Basic conditions

```sql
field1 = value1;

field1 <> value1;

field1 LIKE 'value _ %';

field1 IS NULL;

field1 IS NOT NULL;

field1 IS IN (value1, value2);

field1 IS NOT IN (value1, value2);

condition1 AND condition2;

condition1 OR condition2;
```

## Create / Open / Delete Database

### Create database

```sql
CREATE DATABASE DatabaseName;

CREATE DATABASE DatabaseName CHARACTER SET utf8;
```

### Use database

```sql
USE DatabaseName;
```

### Drop database

```sql
DROP DATABASE DatabaseName;
```

### Alter database

```sql
ALTER DATABASE DatabaseName CHARACTER SET utf8;
```

## Backup and Restore

### Backup database to SQL file

```bash
mysqldump -u Username -p dbNameYouWant > databasename_backup.sql;
```

### Restore from backup SQL file

```bash
mysql -u Username -p dbNameYouWant < databasename_backup.sql;
```

## Repair Tables

### Repair tables after unclean shutdown

```bash
mysqlcheck --all-databases;

mysqlcheck --all-databases --fast;
```

## Insert

### Basic insert statement

```sql
INSERT INTO table1 (field1, field2) VALUES (value1, value2);
```

## Delete

### Basic delete statement

```sql
DELETE FROM table1 / TRUNCATE table1;

DELETE FROM table1 WHERE condition;

DELETE FROM table1, table2 WHERE table1.id1 = table2.id2 AND condition;
```

## Update

### Basic update statement

```sql
UPDATE table1 SET field1=new_value1 WHERE condition;

UPDATE table1, table2 SET field1=new_value1, field2=new_value2, ... WHERE table1.id1 = table2.id2 AND condition;
```

## Create / Delete / Modify Table

### Create table

```sql
CREATE TABLE table (field1 type1, field2 type2);

CREATE TABLE table (field1 type1, field2 type2, INDEX (field));

CREATE TABLE table (field1 type1, field2 type2, PRIMARY KEY (field1));

CREATE TABLE table (field1 type1, field2 type2, PRIMARY KEY (field1,field2));
```

### Create table with foreign key

```sql
CREATE TABLE table1 (fk_field1 type1, field2 type2, ...,
  FOREIGN KEY (fk_field1) REFERENCES table2 (t2_fieldA)) 
    [ON UPDATE|ON DELETE] [CASCADE|SET NULL];
```

### Create table with multiple foreign keys

```sql
CREATE TABLE table1 (fk_field1 type1, fk_field2 type2, ...,
  FOREIGN KEY (fk_field1, fk_field2) REFERENCES table2 (t2_fieldA, t2_fieldB));
```

### Create temporary table

```sql
CREATE TEMPORARY TABLE table;
```

### Drop table

```sql
DROP TABLE table;

DROP TABLE IF EXISTS table;

DROP TABLE table1, table2, ...;
```

### Alter table

```sql
ALTER TABLE table MODIFY field1 type1;

ALTER TABLE table MODIFY field1 type1 NOT NULL ...;

ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1;

ALTER TABLE table CHANGE old_name_field1 new_name_field1 type1 NOT NULL ...;

ALTER TABLE table ALTER field1 SET DEFAULT ...;

ALTER TABLE table ALTER field1 DROP DEFAULT;

ALTER TABLE table ADD new_field type1;
```

