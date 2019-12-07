Insert into databaseentity (database, name, allowedoperationslist) VALUES ('mysql', 'datatable', ['createtable', 'altertable', 'droptable']);
Insert into databaseentity (database, name, allowedoperationslist) VALUES ('cassandra', 'datatable', ['createtable', 'droptable']);
Insert into databaseentity (database, name, allowedoperationslist) VALUES ('oracle', 'datatable', ['createtable', 'droptable']);
Select * from databaseentity ;

insert into datatype (database, name, bytesize, numbercharachetistic) values ('mysql', 'int', 4, {isfloat: false, isunsigned: false, numericalsystem: 10});
insert into datatype (database, name, bytesize, numbercharachetistic) values ('cassandra', 'int', 4, {isfloat: false, isunsigned: false, numericalsystem: 10});
insert into datatype (database, name, bytesize, numbercharachetistic) values ('Oracle', 'NumberInt', 4, {isfloat: false, isunsigned: false, numericalsystem: 10}); 
Select * from datatype ;

INSERT INTO operation(database, name, componentname, rules) VALUES ('mysql', 'createtable', 'datadefinition', [{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}]);
INSERT INTO operation(database, name, componentname, rules) VALUES ('oracle', 'createtable', 'datadefinition', [{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}]);
INSERT INTO operation(database, name, componentname, rules) VALUES ('cassandra', 'createtable', 'datadefinition', [{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}]);
SELECT * FROM operation;


INSERT INTO Component(database, name, listofentities) VALUES ('mysql', 'datadefinition', ['datatable', 'datatableattribute', 'datatableconstraint']);
INSERT INTO Component(database, name, listofentities) VALUES ('oracle', 'datadefinition', ['datatable', 'datatableattribute', 'datatableconstraint']);
INSERT INTO Component(database, name, listofentities) VALUES ('cassandra', 'datadefinition', ['datatable', 'datatableattribute', 'datatableconstraint']);
SELECT * from Component;

INSERT INTO syntax (database , regex , operation ) VALUES ( 'mysql', 'CREATE TABLE(\s+|)(.*)\);', 'createtable' );
INSERT INTO syntax (database , regex , operation ) VALUES ( 'oracle', 'CREATE TABLE(\s+|)(.*)\);', 'createtable' );
INSERT INTO syntax (database , regex , operation ) VALUES ( 'cassandra', 'CREATE TABLE(\s+|)(.*)\);', 'createtable' );
SELECT * from syntax;

Update Component set listofentities=['datatable', 'datatableattribute', 'datatableconstraint'] where database='mysql' and name='datadefinition' ;
Update Component set listofentities=['datatable', 'datatableattribute', 'datatableconstraint'] where database='oracle' and name='datadefinition';
Update Component set listofentities=['datatable', 'datatableattribute', 'datatableconstraint'] where database='cassandra' and name='datadefinition' ; 
Select * from Component;

UPDATE operation set rules=[{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}]}] WHERE database='mysql' and name='createtable';
UPDATE operation set rules=[{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}]}] WHERE database='oracle' and name='createtable';
Update operation set rules=[{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}] where database='cassandra' and name='createtable';
SELECT * FROM operation;

Update databaseentity SET allowedoperationslist=['createtable', 'droptable'] where database='oracle' and name='datatable';
Update databaseentity SET allowedoperationslist=['createtable', 'droptable'] where database='cassandra' and name='datatable';
Update databaseentity SET allowedoperationslist=['createtable', 'droptable'] where database='mysql' and name='datatable';
Select * from databaseentity ;

update datatype SET bytesize=4 where database='mysql' and name='int';
update datatype SET bytesize=4 where database='cassandra' and name='int';
update datatype SET bytesize=4 where database='oracle' and name='NumberInt';
SELECT * FROM datatype;

DELETE FROM Component where database='mysql' and name='datadefinition' ;
DELETE FROM Component where database='oracle' and name='datadefinition' ;
DELETE FROM Component where database='cassandra' and name='datadefinition' ;
SELECT * FROM Component;

DELETE FROM operation WHERE database='mysql' and name='createtable';
DELETE FROM operation WHERE database='oracle' and name='createtable';
DELETE FROM operation WHERE database='cassandra' and name='createtable';
SELECT * FROM operation;

DELETE FROM databaseentity where database='oracle' and name='datatable';
DELETE FROM databaseentity where database='cassandra' and name='datatable';
DELETE FROM databaseentity where database='mysql' and name='datatable';
Select * from databaseentity ;

DELETE FROM datatype where database='mysql' and name='int';
DELETE FROM datatype where database='cassandra' and name='int';
DELETE FROM datatype where database='oracle' and name='int';
Select * from datatype ;

DELETE FROM syntax where database= 'mysql' and operation='createtable';
DELETE FROM syntax where database= 'oracle' and operation='createtable';
DELETE FROM syntax where database= 'cassandra' and operation='createtable';
SELECT * FROM syntax;

SELECT regex from syntax where operation = 'createtable' and database = 'mysql' ;
SELECT database, name from component where listofentities contains 'datatable' ALLOW FILTERING;
SELECT database, name from operation where componentname='datadefinition' ALLOW FILTERING;
SELECT database, name from datatype where numbercharachetistic = { isfloat: False, isunsigned: False, maxprecission: null, numericalsystem: 10 } ALLOW FILTERING;
