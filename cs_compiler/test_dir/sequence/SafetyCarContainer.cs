using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class SafetyCarContainer {
        public LightBarSirenInUse LightBarSirenInUse { get; set; }
        public CauseCode? IncidentIndication { get; set; }
        public TrafficRule? TrafficRule { get; set; }
        public SpeedLimit? SpeedLimit { get; set; }
    }
}
