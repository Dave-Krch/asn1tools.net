using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class BasicVehicleContainerHighFrequency {
        public Heading Heading { get; set; }
        public Speed Speed { get; set; }
        public DriveDirection DriveDirection { get; set; }
        public VehicleLength VehicleLength { get; set; }
        public VehicleWidth VehicleWidth { get; set; }
        public LongitudinalAcceleration LongitudinalAcceleration { get; set; }
        public Curvature Curvature { get; set; }
        public CurvatureCalculationMode CurvatureCalculationMode { get; set; }
        public YawRate YawRate { get; set; }
        public AccelerationControl? AccelerationControl { get; set; }
        public LanePosition? LanePosition { get; set; }
        public SteeringWheelAngle? SteeringWheelAngle { get; set; }
        public LateralAcceleration? LateralAcceleration { get; set; }
        public VerticalAcceleration? VerticalAcceleration { get; set; }
        public PerformanceClass? PerformanceClass { get; set; }
        public CenDsrcTollingZone? CenDsrcTollingZone { get; set; }
    }
}
