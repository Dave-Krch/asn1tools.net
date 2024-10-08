using test_namespace.bit_string;
using test_namespace.enumerated;

namespace test_namespace.sequence {
    public class ProtectedCommunicationZone {
        public ProtectedZoneType ProtectedZoneType { get; set; }
        public TimestampIts? ExpiryTime { get; set; }
        public Latitude ProtectedZoneLatitude { get; set; }
        public Longitude ProtectedZoneLongitude { get; set; }
        public ProtectedZoneRadius? ProtectedZoneRadius { get; set; }
        public ProtectedZoneID? ProtectedZoneID { get; set; }
    }
}
