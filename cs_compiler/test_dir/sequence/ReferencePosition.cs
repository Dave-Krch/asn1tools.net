using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class ReferencePosition {
        public Latitude Latitude { get; set; }
        public Longitude Longitude { get; set; }
        public PosConfidenceEllipse PositionConfidenceEllipse { get; set; }
        public Altitude Altitude { get; set; }
    }
}
