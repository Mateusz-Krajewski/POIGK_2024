"""GCode parser module."""

class GCodeParser:
    """Parser for GCode files."""

    def __init__(self) -> None:
        """Initialize the GCodeParser."""
        pass

    def read_file_lines(self) -> list[str]:
        """Read lines from a GCode file."""
        with open("resources/test1.gcode", 'r', encoding='utf-8') as file:
            lines = file.readlines()  # pylint: disable=all
        return lines

    def filter_lines(self, lines: list[str]) -> list[str]:
        """Return filtered lines that start with G.

        Args:
            lines (list[str]): Lines read from a file.

        Returns:
            list[str]: Filtered lines.
        """
        filtered = []
        for line in lines:
            if line.startswith(';'):
                continue
            line = line.split("\n")[0]
            if ';' in line:
                continue
            if line.startswith("G"):
                filtered.append(line)
        return filtered

    def filter_v2(self, lines: list[str]):
        """Further filter lines by removing lines ending with F."""
        re = []
        for line in lines:
            l = line.split(" ")
            if len(l) == 2 and l[1].startswith("F"):
                continue
            else:
                if l[-1].startswith("F"):
                    line = " ".join(l[0:-1])
            re.append(line)
        return re

    def get_filtered_lines(self):
        """Get filtered lines from a GCode file."""
        return self.filter_v2(self.filter_lines(self.read_file_lines()))

    def convert_gcode_to_list(self, gcode_list):
        """Convert GCode to a list of Move objects."""
        start_x = 0
        start_y = 0
        is_first_xy = True
        i = 0
        while is_first_xy:
            line = gcode_list[i].split(" ")
            i += 1
            if line[0] != "G1":
                continue
            if len(line) != 3:
                continue
            if line[1].startswith("X") and line[2].startswith("Y"):
                start_x = float(line[1][1:])
                start_y = float(line[2][1:])
                is_first_xy = False
                print(f"X: {start_x}, Y: {start_y}")
                continue

        out = [Move((0, 0, 0), True)]
        for order in gcode_list:
            move = Move() # pylint: disable=all
            ord_parts = order.split(" ")
            if ord_parts[0] != "G1":
                continue
            if ord_parts[1].startswith("Z"):
                move.x = out[-1].x
                move.y = out[-1].y
                move.z = float(ord_parts[1][1:])
            elif ord_parts[1].startswith("X"):
                if len(ord_parts) == 3:
                    move.only_move = True
                    move.x = start_x - float(ord_parts[1][1:])
                    move.y = start_y - float(ord_parts[2][1:])
                    move.z = out[-1].z
                if len(ord_parts) == 4:
                    move.only_move = False
                    move.z = out[-1].z
                    move.x = start_x - float(ord_parts[1][1:])
                    move.y = start_y - float(ord_parts[2][1:])
            else:
                continue
            out.append(move)
        return out

    def save_lines(self, lines: list[str]): # pylint: disable=all
        """Save lines to a GCode file."""
        with open("out.gcode", 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + "\n")


if __name__ == "__main__":
    parser = GCodeParser()
    lines = parser.get_filtered_lines()
    moves = parser.convert_gcode_to_list(lines)
    for move in moves[:100]:
        print(move)
