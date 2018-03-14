import json
import boto3


def lambda_handler(event, context):

    client = boto3.client('ssm')
    
    response = client.send_command(
        InstanceIds=['i-0ddf7ca3a0af32d0f'],
        DocumentName='AWS-RunShellScript',
        Comment='Flush IPTables',
        Parameters={'commands': ['sudo iptables -F']})

    response = client.send_command(
        InstanceIds=['i-0ddf7ca3a0af32d0f'],
        DocumentName='AWS-RunShellScript',
        Comment='Drop connection on Port 80',
        Parameters={'commands': ['sudo iptables -A INPUT -p tcp --dport 80 -j DROP']})
