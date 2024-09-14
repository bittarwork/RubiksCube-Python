class RubiksCube:
    """
    Class to represent a 3x3 Rubik's Cube and handle basic operations such as face rotations.
    """

    def __init__(self):
        """
        Initializes the cube with six faces, each with 9 squares (3x3 grid) filled with a single color.
        """
        self.faces = {
            'F': ['G'] * 9,  # Green (Front)
            'B': ['B'] * 9,  # Blue (Back)
            'U': ['W'] * 9,  # White (Up)
            'D': ['Y'] * 9,  # Yellow (Down)
            'L': ['O'] * 9,  # Orange (Left)
            'R': ['R'] * 9   # Red (Right)
        }

    def rotate_face_clockwise(self, face):
        """
        Rotates the specified face of the cube 90 degrees clockwise.
        
        Input:
            face (str): The face to rotate, should be one of 'F', 'B', 'U', 'D', 'L', or 'R'.
            
        Output:
            None. The method directly modifies the face's color arrangement in the cube.
        
        How it works:
            - The 3x3 grid of a face is represented as a list of 9 squares.
            - The method reorders the list to simulate a 90-degree clockwise rotation.
        """
        new_face = self.faces[face][6:] + self.faces[face][:6]  # Rotate the 9 squares
        self.faces[face] = [
            new_face[6], new_face[3], new_face[0],
            new_face[7], new_face[4], new_face[1],
            new_face[8], new_face[5], new_face[2]
        ]

    def print_cube(self):
        """
        Prints the current state of the cube for inspection. Outputs each face as a 3x3 grid.
        """
        for face, colors in self.faces.items():
            print(f"{face}: {colors[:3]}\n   {colors[3:6]}\n   {colors[6:]}")

# Test rotating the front face
cube = RubiksCube()
cube.rotate_face_clockwise('F')
cube.print_cube()
