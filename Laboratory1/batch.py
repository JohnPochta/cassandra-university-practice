from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect("rdbms2nosqlmigration")

query = SimpleStatement("""BEGIN BATCH
	INSERT INTO operation(database, name, componentname, rules) VALUES ('mysql', 'createtable', 'datadefinition', [{operationentity: 'datatable', operationargumentsentities: [{maxAllowed: -1, entityName: 'datatableattribute'}, {entityName: 'datatableconstraint', maxAllowed: 1}]}]);
    INSERT INTO Component(database, name, listofentities) VALUES ('mysql', 'datadefinition', ['datatable', 'datatableattribute', 'datatableconstraint']);
APPLY BATCH;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query)