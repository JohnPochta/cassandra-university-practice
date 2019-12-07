 
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect("rdbms2nosqlmigration")

query = SimpleStatement("""INSERT INTO databaseentity (database, name, allowedoperationslist)
VALUES (%s, %s, [%s, %s, %s]);""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datatable', 'createtable', 'altertable', 'droptable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datatable', 'createtable', 'altertable', 'droptable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datatable', 'createtable', 'altertable', 'droptable'))
rows = session.execute("SELECT * FROM databaseentity;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO datatype (database, name, bytesize, numbercharachetistic)
VALUES (%s, %s, %s, { isfloat: False, isunsigned: False, maxprecission: null, numericalsystem: 10});""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'int', 4))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'int', 4))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'NumberInt', 4))
rows = session.execute("SELECT * FROM datatype;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO operation(database, name, componentname, rules) VALUES (%s, %s, %s, [{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}]);""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'createtable', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'createtable', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'createtable', 'datadefinition'))
rows = session.execute("SELECT * FROM operation;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO Component(database, name, listofentities) VALUES ( %s, %s, ['datatable', 'datatableattribute', 'datatableconstraint']);""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datadefinition'))
rows = session.execute("SELECT * FROM component;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO syntax(database , regex , operation ) VALUES ( %s, 'CREATE TABLE(\s+|)(.*)\);', %s );""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'createtable'))
rows = session.execute("SELECT * FROM syntax;")
for row in rows:
    print(row)

query = SimpleStatement("""Update Component set listofentities=['datatable', 'datatableattribute', 'datatableconstraint'] where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datadefinition'))
rows = session.execute("SELECT * FROM component;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE operation set rules=[{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}]}] WHERE database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'createtable'))
rows = session.execute("SELECT * FROM operation;")
for row in rows:
    print(row)


query = SimpleStatement("""Update databaseentity SET allowedoperationslist=['createtable', 'droptable'] where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datatable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datatable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datatable'))
rows = session.execute("SELECT * FROM databaseentity;")
for row in rows:
    print(row)

query = SimpleStatement("""update datatype SET bytesize=4 where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'int'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'int'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'NumberInt'))
rows = session.execute("SELECT * FROM datatype;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE FROM Component where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datadefinition'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datadefinition'))
rows = session.execute("SELECT * FROM Component;")
for row in rows:
    print(row)


query = SimpleStatement("""DELETE FROM operation WHERE database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'createtable'))
rows = session.execute("SELECT * FROM operation;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE FROM databaseentity where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'datatable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'datatable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'datatable'))
rows = session.execute("SELECT * FROM databaseentity;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE FROM datatype where database=%s and name=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'int'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'NumberInt'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'int'))
rows = session.execute("SELECT * FROM datatype;")
for row in rows:
    print(row)

query = SimpleStatement("""DELETE FROM syntax where database=%s and operation=%s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('mysql', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('oracle', 'createtable'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('cassandra', 'createtable'))
rows = session.execute("SELECT * FROM syntax;")
for row in rows:
    print(row)

query = SimpleStatement("""SELECT regex from syntax where operation = %s and database = %s;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, ('createtable', 'mysql'))

query = SimpleStatement("""SELECT database, name from component where listofentities contains 'datatable' ALLOW FILTERING;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)

query = SimpleStatement("""SELECT database, name from operation where componentname='datadefinition' ALLOW FILTERING;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)

query = SimpleStatement("""SELECT database, name from datatype where numbercharachetistic = { isfloat: False, isunsigned: False, maxprecission: null, numericalsystem: 10 } ALLOW FILTERING;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
