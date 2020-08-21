class Connector:
   def __init__(self, config, processor):
      # Set up connector

   def start(self):
      # Start the ingestion of events
      # Example:
      for raw_event in external_source:
         if topic, event_timestamp, details
               := processor.process(raw_event):
            self._ingest(topic, build_event(event_timestamp, details)

   @final
   def _ingest(self, topic, event):
      produce_to_kafka(topic, serialize(event))


class Processor:
   def __init__(self, config):
      # Set up processor

   def process(self, raw_event) -> Optional[topic, event_timestamp, details]:
      # Extract timestamp and event details
      # Return None if event should be filtered out
