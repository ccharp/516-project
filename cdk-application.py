from aws_cdk import App, Aws, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_emr as emr
from aws_cdk import aws_iam as iam

from constructs import Construct

from . import EMRClusterStack

app = App()
EMRClusterStack(
    app,
    "emr-cluster",
    s3_log_bucket="s3_bucket_logs",
    s3_script_bucket="s3_bucket_scripts",
    spark_script="pyspark_script.py",
)

app.synth()