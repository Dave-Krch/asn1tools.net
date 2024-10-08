using System.Collections;

namespace test_namespace.bit_string {
    public class SpecialTransportType {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        SpecialTransportType() {
            this.named_bits.Add(0, "heavyLoad");
            this.named_bits.Add(1, "excessWidth");
            this.named_bits.Add(2, "excessLength");
            this.named_bits.Add(3, "excessHeight");
        }
    }
}
