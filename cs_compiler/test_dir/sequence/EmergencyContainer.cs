using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class EmergencyContainer {
        public LightBarSirenInUse LightBarSirenInUse { get; set; }
        public CauseCode? IncidentIndication { get; set; }
        public EmergencyPriority? EmergencyPriority { get; set; }
    }
}
