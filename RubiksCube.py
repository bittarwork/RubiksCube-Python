# Rubik's Cube representation in memory
class RubiksCube:
    """
    Class to represent a 3x3 Rubik's Cube.
    
    The cube is represented by six faces: Front (F), Back (B), Up (U), Down (D), Left (L), Right (R).
    Each face contains 9 squares (3x3 grid), and each square has a color.
    
    Attributes:
        faces (dict): A dictionary containing the cube's faces with their corresponding colors.
    """

    def __init__(self):
        """
        Initializes a Rubik's Cube with all faces set to their respective color.
        
        Faces are:
        - 'F' (Front) with green squares
        - 'B' (Back) with blue squares
        - 'U' (Up) with white squares
        - 'D' (Down) with yellow squares
        - 'L' (Left) with orange squares
        - 'R' (Right) with red squares
        """
        self.faces = {
            'F': ['G'] * 9,  # Green (Front)
            'B': ['B'] * 9,  # Blue (Back)
            'U': ['W'] * 9,  # White (Up)
            'D': ['Y'] * 9,  # Yellow (Down)
            'L': ['O'] * 9,  # Orange (Left)
            'R': ['R'] * 9   # Red (Right)
        }

    def print_cube(self):
        """
        Prints the current state of the cube's faces.
        
        This function outputs the 3x3 grids of each face to the command line for visual inspection.
        """
        for face, colors in self.faces.items():
            print(f"{face}: {colors[:3]}\n   {colors[3:6]}\n   {colors[6:]}")

# Test the cube representation
cube = RubiksCube()
cube.print_cube()
