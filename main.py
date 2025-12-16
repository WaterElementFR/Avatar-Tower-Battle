import pygame
import math

class Character:
    def __init__(self, x, y, orientation, body_points):
        """
        Initialize a character with position, orientation, and body points.
        
        Args:
            x (float): X coordinate of character position
            y (float): Y coordinate of character position
            orientation (float): Orientation angle in degrees
            body_points (list): List of 11 tuples representing:
                [0] left shoulder
                [1] left elbow
                [2] left hand
                [3] right shoulder
                [4] right elbow
                [5] right hand
                [6] waist
                [7] left knee
                [8] left feet
                [9] right knee
                [10] right feet
        """
        self.x = x
        self.y = y
        self.orientation = orientation
        self.body_points = body_points
    
    def move(self, dx, dy):
        """Move character by delta x and y."""
        self.x += dx
        self.y += dy
    
    def rotate(self, angle):
        """Rotate character by given angle in degrees."""
        self.orientation = (self.orientation + angle) % 360
    
    def get_position(self):
        """Return current 2D position."""
        return (self.x, self.y)
    
    def draw(self, surface, color=(255, 255, 255), line_width=2, point_radius=4):
        """
        Draw the stick man on the pygame surface.
        
        Args:
            surface (pygame.Surface): The surface to draw on
            color (tuple): RGB color for drawing
            line_width (int): Width of lines
            point_radius (int): Radius of joint points
        """
        if not self.body_points or len(self.body_points) < 11:
            return
        
        # Extract points with offset for positioning
        points = [
            (self.body_points[i][0] + self.x, self.body_points[i][1] + self.y)
            for i in range(11)
        ]
        
        # Points: 0=left shoulder, 1=left elbow, 2=left hand
        #         3=right shoulder, 4=right elbow, 5=right hand
        #         6=waist, 7=left knee, 8=left feet, 9=right knee, 10=right feet
        
        # Draw body segments
        # Left arm: shoulder -> elbow -> hand
        pygame.draw.line(surface, color, points[0], points[1], line_width)
        pygame.draw.line(surface, color, points[1], points[2], line_width)
        
        # Right arm: shoulder -> elbow -> hand
        pygame.draw.line(surface, color, points[3], points[4], line_width)
        pygame.draw.line(surface, color, points[4], points[5], line_width)
        
        # Torso: shoulders to waist
        pygame.draw.line(surface, color, points[0], points[6], line_width)
        pygame.draw.line(surface, color, points[3], points[6], line_width)
        
        # Left leg: waist -> knee -> feet
        pygame.draw.line(surface, color, points[6], points[7], line_width)
        pygame.draw.line(surface, color, points[7], points[8], line_width)
        
        # Right leg: waist -> knee -> feet
        pygame.draw.line(surface, color, points[6], points[9], line_width)
        pygame.draw.line(surface, color, points[9], points[10], line_width)
        
        # Draw joints as circles
        for point in points:
            pygame.draw.circle(surface, color, point, point_radius)
    
    def __repr__(self):
        return f"Character(x={self.x}, y={self.y}, orientation={self.orientation})"



def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Character Display")
    clock = pygame.time.Clock()
    
    # Create example character with stick man body points
    body_points = [
        (-10, -30),  # left shoulder
        (-20, -10),  # left elbow
        (-30, 5),    # left hand
        (10, -30),   # right shoulder
        (20, -10),   # right elbow
        (30, 5),     # right hand
        (0, 0),      # waist
        (-5, 20),    # left knee
        (-5, 40),    # left feet
        (5, 20),     # right knee
        (5, 40),     # right feet
    ]
    
    character = Character(width // 2, height // 2, 0, body_points)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        character.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()
