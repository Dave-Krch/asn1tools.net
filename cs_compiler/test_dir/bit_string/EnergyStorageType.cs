using System.Collections;

namespace test_namespace.bit_string {
    public class EnergyStorageType {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        EnergyStorageType() {
            this.named_bits.Add(0, "hydrogenStorage");
            this.named_bits.Add(1, "electricEnergyStorage");
            this.named_bits.Add(2, "liquidPropaneGas");
            this.named_bits.Add(3, "compressedNaturalGas");
            this.named_bits.Add(4, "diesel");
            this.named_bits.Add(5, "gasoline");
            this.named_bits.Add(6, "ammonia");
        }
    }
}
