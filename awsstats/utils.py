import boto3
import operator
import os

from datetime import datetime
from datetime import timedelta


__all__ = ('EC2_NAMESPACE',
           'DDB_NAMESPACE',
           'RDS_NAMESPACE',
           'get_client',
           'get_ec2_servers',
           'get_instance_name',
           'get_metric_stats_args',
           'fetch_stats',)

EC2_NAMESPACE = 'AWS/EC2'
DDB_NAMESPACE = 'AWS/DynamoDB'
RDS_NAMESPACE = 'AWS/RDS'


def get_client(service, region='us-west-2', aws_key=None, aws_secret=None):
    aws_key = aws_key or os.environ.get('AWS_ACCESS_KEY')
    aws_secret = aws_secret or os.environ.get('AWS_ACCESS_SECRET')

    return boto3.client(service, aws_access_key_id=aws_key,
                        aws_secret_access_key=aws_secret,
                        region_name=region)


def get_ec2_servers():
    client = get_client('ec2')
    response = client.describe_instances()
    instances = {}
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances[instance['InstanceId']] = instance

    return instances


def get_instance_name(instance):
    for tag in v['Tags']:
        if tag['Key'] == 'Name':
            return tag['Value']

    return None


def get_time_range():
    now = datetime.utcnow()
    past = now - timedelta(minutes=60)

    return past, now


def get_metric_stats_args(ns, metric, dimension, stats=['Average'], period=60):
    s, e = get_time_range()

    return dict(
        Namespace=ns,
        MetricName=metric,
        Dimensions=[{
            'Name': dimension[0],
            'Value': dimension[1]
        }],
        StartTime=s,
        EndTime=e,
        Period=period,
        Statistics=stats)


def fetch_stats(metric_args):
    client = get_client('cloudwatch')
    resp = client.get_metric_statistics(**metric_args)
    data = [(str(r['Timestamp']), r['Average']) for r in resp['Datapoints']]
    data.sort(key=operator.itemgetter(0))

    return data
