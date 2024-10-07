using System.Collections;

namespace test_namespace.bit_string {
    public class ExteriorLights {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        ExteriorLights() {
            this.named_bits.Add(0, "lowBeamHeadlightsOn");
            this.named_bits.Add(1, "highBeamHeadlightsOn");
            this.named_bits.Add(2, "leftTurnSignalOn");
            this.named_bits.Add(3, "rightTurnSignalOn");
            this.named_bits.Add(4, "daytimeRunningLightsOn");
            this.named_bits.Add(5, "reverseLightOn");
            this.named_bits.Add(6, "fogLightOn");
            this.named_bits.Add(7, "parkingLightsOn");
        }
    }
}
