using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class ItsPduHeader {
        public long ProtocolVersion { get; set; }
        public long MessageID { get; set; }
        public StationID StationID { get; set; }
    }
}
