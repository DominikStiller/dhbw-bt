source("input.vehicle-position", VehiclePosition.class)
   // First, key and deduplicate by vehicle
   // This selects only the most recent position
   .keyBy(new UniqueVehicleIdKeySelector())
      .window(SlidingEventTimeWindows.of(Time.seconds(30), Time.seconds(5)))
      .evictor(new MostRecentDeduplicationEvictor())
      .process(new IdentityProcessFunction<>())
   // Then, key and aggregate by geocell to count vehicles
   .keyBy(GeocellKeySelector.ofVehiclePosition())
      .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
      .aggregate(new CountVehiclesPerGeocellFunction<>(),
                 new CreateOutputMessageFunction())
      .addSink(sink("analytics.vehicle-distribution"));
