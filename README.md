awsstats
--------

AWS services' statistics...simplified!

##Requires

* boto3


##Example

    # Environment variables
    # AWS_ACCESS_KEY=<YOUR AWS_ACCESS_KEY>
    # AWS_ACCESS_SECRET=<YOUR AWS_ACCESS_SECRET>

    import ec2
    for timestamp, value in ec2.get_avg_cpu('i-1234ab56'):
        print('{}: {}'.format(timestamp, value))

output

    2017-03-10 16:03:00+00:00: 1.434
    2017-03-10 16:08:00+00:00: 1.276
    2017-03-10 16:13:00+00:00: 1.9460000000000002
    2017-03-10 16:18:00+00:00: 2.08
    2017-03-10 16:23:00+00:00: 1.534
    2017-03-10 16:28:00+00:00: 1.9120000000000001
    2017-03-10 16:33:00+00:00: 1.486
    2017-03-10 16:38:00+00:00: 1.8379999999999999
    2017-03-10 16:43:00+00:00: 1.6420000000000001
    2017-03-10 16:48:00+00:00: 1.288
    2017-03-10 16:53:00+00:00: 1.076


##Mini API Docs

####Some Defaults

* Time ranges: 1 hour
* Period: 60 seconds (unless restricted by service)

####ec2.py

* **get_avg_cpu(instance_id)**: The percentage of CPU utilization. (units: %)
    
    instance_id: 


####dynammodb.py

* **get_avg_read_capacity(table_name)**: The number of read capacity units consumed over the time range. (units: Count)

    table_name: DynamoDB table name

* **get_avg_write_capacity(table_name)**: The number of write capacity units consumed over the time range. (units: Count)

    table_name: DynamoDB table name

####rds.py

* **get_avg_cpu(db_instance_name)**: The percentage of CPU utilization. (units: %)
    
        db_instance_name: Database instance name

* **get_avg_read_iops(db_instance_name)**: The average number of disk I/O operations per second. (units: Count/Second)
    
        db_instance_name: Database instance name

* **get_avg_write_iops(db_instance_name)**: The average number of disk I/O operations per second. (units: Count/Second)
    
        db_instance_name: Database instance name

* **get_avg_free_memory(db_instance_name)**: The amount of available random access memory. (units: Gigabytes)
    
        db_instance_name: Database instance name

* **get_avg_free_storage(db_instance_name)**: The amount of available storage space. (units: Megabytes)
    
        db_instance_name: Database instance name

* **get_avg_swap_usage(db_instance_name)**: The amount of swap space used on the DB instance. (units: Megabytes)
    
        db_instance_name: Database instance name

* **get_avg_connections(db_instance_name)**: The number of database connections in use. (units: Count)
    
        db_instance_name: Database instance name



