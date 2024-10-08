using System.Collections;

namespace test_namespace.bit_string {
    public class EmergencyPriority {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        EmergencyPriority() {
            this.named_bits.Add(0, "requestForRightOfWay");
            this.named_bits.Add(1, "requestForFreeCrossingAtATrafficLight");
        }
    }
}
