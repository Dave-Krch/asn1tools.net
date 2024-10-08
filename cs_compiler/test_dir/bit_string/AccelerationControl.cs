using System.Collections;

namespace test_namespace.bit_string {
    public class AccelerationControl {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        AccelerationControl() {
            this.named_bits.Add(0, "brakePedalEngaged");
            this.named_bits.Add(1, "gasPedalEngaged");
            this.named_bits.Add(2, "emergencyBrakeEngaged");
            this.named_bits.Add(3, "collisionWarningEngaged");
            this.named_bits.Add(4, "accEngaged");
            this.named_bits.Add(5, "cruiseControlEngaged");
            this.named_bits.Add(6, "speedLimiterEngaged");
        }
    }
}
