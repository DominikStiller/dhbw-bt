class Connector(AbstractBaseClass):
   def __init__(self, config, processor):
      # Set up connector

   def start(self):
      # Start the ingestion of events
      # Example:
      for raw_event in external_source:
         if topic, event_timestamp, details
               := processor.process(raw_event):
            self._ingest(topic, build_base_event(event_timestamp, details)

   @final
   def _ingest(self, topic, base_event):
      produce_to_kafka(topic, serialize(base_event))


class Processor(AbstractBaseClass):
   def __init__(self, config):
      # Set up processor

   def process(self, raw_event) -> Optional[topic, event_timestamp, details]:
      # Extract timestamp and event details
      # Return None if event should be filtered out
