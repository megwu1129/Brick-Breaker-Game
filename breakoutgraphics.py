"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=PADDLE_WIDTH, height=PADDLE_HEIGHT, x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.paddle_width = PADDLE_WIDTH
        self.paddle_height = PADDLE_HEIGHT
        self.paddle_offset = PADDLE_OFFSET
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width-ball_radius*2)/2, y=(self.window.height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball_radius = BALL_RADIUS
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners.
        onmouseclicked(self.mouse_click)
        onmousemoved(self.mouse_move)
        # Draw bricks.
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset+j*(brick_height+brick_spacing))
                if j == 0 or j == 1:
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                    self.window.add(self.brick)

                elif j == 2 or j == 3:
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                    self.window.add(self.brick)

                elif j == 4 or j == 5:
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                    self.window.add(self.brick)
                elif j == 6 or j == 7:
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                    self.window.add(self.brick)
                elif j == 8 or j == 9:
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                    self.window.add(self.brick)

    def mouse_move(self, event):
        '''
        :param event: mouse
        When the mouse moves, the paddle moves.
        '''
        self.paddle.x = event.x - self.paddle_width/2
        self.paddle.y = self.window.height - self.paddle_offset
        if event.x+self.paddle_width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle_width
        if event.x-self.paddle_width/2 <= 0:
            self.paddle.x = 0

    def mouse_click(self, event):
        '''
        :param event: mouse
        If the ball is at the start location, set velocity for the ball.
        '''
        if self.ball.x == (self.window.width-self.ball_radius*2)/2:
            self.set_ball_velocity()

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_ball_velocity(self):
        '''
        Set velocity for the ball.
        '''
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def zero(self):
        '''
        Turn the velocity of __.dx and __.dy to zero.
        '''
        self.__dx = 0
        self.__dy = 0
