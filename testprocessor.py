from nifiapi.flowfiletransform import FlowFileTransform, FlowFileTransformResult

class WriteHelloWorld(FlowFileTransform):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']
    class ProcessorDetails:
        version = '0.0.1-SNAPSHOT'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def transform(self, context, flowfile):
        # Import Python dependencies
        input = flowFile.getContentsAsBytes().decode()
        # Do something with the input
        output = input
        return FlowFileTransformResult(
            relationship = "success",
            contents = output,
            attributes = {"greeting", "hello"}
        )