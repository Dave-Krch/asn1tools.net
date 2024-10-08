using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class EventPoint {
        public DeltaReferencePosition EventPosition { get; set; }
        public PathDeltaTime? EventDeltaTime { get; set; }
        public InformationQuality InformationQuality { get; set; }
    }
}
