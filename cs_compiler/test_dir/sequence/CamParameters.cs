using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class CamParameters {
        public BasicContainer BasicContainer { get; set; }
        public HighFrequencyContainer HighFrequencyContainer { get; set; }
        public LowFrequencyContainer? LowFrequencyContainer { get; set; }
        public SpecialVehicleContainer? SpecialVehicleContainer { get; set; }
    }
}
