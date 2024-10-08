using System.Collections;

namespace test_namespace.bit_string {
    public class LightBarSirenInUse {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        LightBarSirenInUse() {
            this.named_bits.Add(0, "lightBarActivated");
            this.named_bits.Add(1, "sirenActivated");
        }
    }
}
