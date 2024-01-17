import time
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

trace.set_tracer_provider(TracerProvider())

# Set up the OTLP exporter to send traces to an OTLP collector
exporter = OTLPSpanExporter(
    endpoint="localhost:4317",
)

# Configure the tracer with the exporter
trace.get_tracer_provider().add_span_processor(BatchExportSpanProcessor(exporter))

# Create a tracer
tracer = trace.get_tracer(__name__)

def sample_function():
    with tracer.start_as_current_span("sample-span"):
        # Your application logic goes here
        print("Application logic goes here.")
        time.sleep(1)

if __name__ == "__main__":
    sample_function()
