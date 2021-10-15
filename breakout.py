"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel


FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

score = 0   # start the score with 0
score_label = GLabel('Score: '+str(score))
score_label.font = '-20'


def main():
    graphics = BreakoutGraphics()
    graphics.window.add(score_label, 0, score_label.height+10)  # add the score in the window
    lives = NUM_LIVES
    # Add animation loop here!
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        global score
        pause(FRAME_RATE)
        # find 4 coordinates around the ball
        a = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        b = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y)
        c = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius * 2)
        d = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y + graphics.ball_radius * 2)
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        # move the ball
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            dx = -dx
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.zero()     # if the ball falls under the window height, turn the velocity to 0
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # add the ball on the window again
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball_radius*2)/2, y=(graphics.window.height-graphics.ball_radius*2)/2)
        if graphics.ball.y <= 0:
            dy = -dy

        if a is not None and a is not score_label:
            if a == graphics.paddle:
                if dy > 0:
                    dy = -dy
            else:
                dy = -dy
                graphics.window.remove(a)
                score += 1
                score_label.text = 'Score: ' + str(score)

        elif b is not None and b is not score_label:
            if b == graphics.paddle:
                if dy > 0:
                    dy = -dy
            else:
                dy = -dy
                graphics.window.remove(b)
                score += 1
                score_label.text = 'Score: ' + str(score)
        elif c is not None and c is not score_label:
            if c == graphics.paddle:
                if dy > 0:
                    dy = -dy
            else:
                dy = -dy
                graphics.window.remove(c)
                score += 1
                score_label.text = 'Score: ' + str(score)

        elif d is not None and c is not score_label:
            if d == graphics.paddle:
                if dy > 0:
                    dx = dx
                    dy = -dy
            else:
                dx = -dx
                dy = -dy
                graphics.window.remove(d)
                score += 1
                score_label.text = 'Score: ' + str(score)

        if lives == 0:
            break
    lose_label = GLabel('You lost:( ')
    lose_label.font = '-40'
    graphics.window.add(lose_label, 150, 500)




if __name__ == '__main__':
    main()
