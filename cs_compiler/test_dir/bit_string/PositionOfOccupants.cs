using System.Collections;

namespace test_namespace.bit_string {
    public class PositionOfOccupants {
        BitArray Data { get; set; }
        Dictionary<int, string> named_bits = new Dictionary<int, string>();
        PositionOfOccupants() {
            this.named_bits.Add(0, "row1LeftOccupied");
            this.named_bits.Add(1, "row1RightOccupied");
            this.named_bits.Add(2, "row1MidOccupied");
            this.named_bits.Add(3, "row1NotDetectable");
            this.named_bits.Add(4, "row1NotPresent");
            this.named_bits.Add(5, "row2LeftOccupied");
            this.named_bits.Add(6, "row2RightOccupied");
            this.named_bits.Add(7, "row2MidOccupied");
            this.named_bits.Add(8, "row2NotDetectable");
            this.named_bits.Add(9, "row2NotPresent");
            this.named_bits.Add(10, "row3LeftOccupied");
            this.named_bits.Add(11, "row3RightOccupied");
            this.named_bits.Add(12, "row3MidOccupied");
            this.named_bits.Add(13, "row3NotDetectable");
            this.named_bits.Add(14, "row3NotPresent");
            this.named_bits.Add(15, "row4LeftOccupied");
            this.named_bits.Add(16, "row4RightOccupied");
            this.named_bits.Add(17, "row4MidOccupied");
            this.named_bits.Add(18, "row4NotDetectable");
            this.named_bits.Add(19, "row4NotPresent");
        }
    }
}
