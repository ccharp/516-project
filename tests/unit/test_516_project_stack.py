import aws_cdk as core
import aws_cdk.assertions as assertions

from 516_project.516_project_stack import 516ProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 516_project/516_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 516ProjectStack(app, "516-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
