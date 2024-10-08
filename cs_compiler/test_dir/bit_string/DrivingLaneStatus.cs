using System.Collections;

namespace test_namespace.bit_string {
    public class DrivingLaneStatus {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        DrivingLaneStatus() {
        }
    }
}
