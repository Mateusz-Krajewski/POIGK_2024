

class Move:
    def __init__(self, position = (0, 0, 0), onlyMove = False):
        self.x:float = position[0]
        self.y:float = position[1]
        self.z:float = position[2]
        self.OnlyMove = onlyMove
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z:{self.z}, OnlyMove:{self.OnlyMove}"
    
    def GetPosition(self):
        return (self.x,self.y,self.z)
    def changeX(self, deltaX):
        self.x += deltaX
    def changeY(self, deltaY):
        self.x += deltaY
    def changeZ(self, deltaZ):
        self.x += deltaZ

class GCodeParser:
    def __init__(self) -> None:
        pass

    def readFileLines(self) -> list[str]:
        with open("test1.gcode",'r') as file:
            lines = file.readlines()
        return lines

    def filter_lines(self,lines:list[str]) -> list[str]:
        """function returns comments, end line sign and command not starts with G

        Args:
            lines (list[str]): linie wczytane z pliku

        Returns:
            list[str]: przefiltrowane dane
        """
        filtered =[]
        for line in lines:
            if line.startswith(';'):
                continue
            line = line.split("\n")[0]
            if ';' in line:
                continue
            if line.startswith("G"):
                filtered.append(line)
        return filtered



    def filter_v2(self,lines:list[str]):
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

    def GetFilteredLines(self):
        return self.filter_v2(self.filter_lines(self.readFileLines()))

    def ConvertGCodeToList(self, list):
        startX=0
        startY=0
        is_first_XY = True
        i = 0
        while (is_first_XY):
            line = list[i].split(" ")
            i+=1
            if (line[0] != "G1"):
                continue
            if (len(line) != 3):
                continue
            if (line[1].startswith("X") and line[2].startswith("Y")):
                startX = float(line[1][1:])
                startY = float(line[2][1:])
                is_first_XY = False
                print(f"X:{startX},Y:{startY}")
                continue

        out = [Move((0,0,0),True)]
        for order in list:
            move = Move()
            ord = order.split(" ")
            if ord[0] != "G1":
                continue
            if ord[1].startswith("Z"):
                move.x = out[-1].x
                move.y = out[-1].y
                move.z = float(ord[1][1:])
            elif ord[1].startswith("X"):
                if (len(ord) == 3):
                    move.OnlyMove = True
                    move.x = startX - float(ord[1][1:])
                    move.y = startY - float(ord[2][1:])
                    move.z = out[-1].z
                if (len(ord) == 4):
                    move.OnlyMove = False
                    move.z = out[-1].z
                    move.x = startX - float(ord[1][1:])
                    move.y = startY - float(ord[2][1:])
            else :
                continue
            out.append(move)
        return out



    def save_lines(self,lines:list[str]):
        with open("out.gcode",'w') as file:
            for line in lines:
                file.write(line+"\n")

if __name__ == "__main__":
    par = GCodeParser()
    lines = par.GetFilteredLines()
    out = par.ConvertGCodeToList(lines)
    for move in out[:100]:
        print(move)