
import graphics
import time

# Parameters of the graphics window
WIDTH  = 1200
HEIGHT = 600

# Parameters for the ball
BALL_RADIUS = 10
BALL_COLOR  = 'white'
BALL_X_VELO = -4
BALL_Y_VELO = 2
BALL_X_VDIFF = 2
BALL_Y_VDIFF = 1

# Parameters for the edge
EDGE_TOP    = 100
EDGE_BOTTOM = HEIGHT
EDGE_LEFT   = 0
EDGE_RIGHT  = WIDTH-200
EDGE_INSIDE_TOP    = EDGE_TOP    + BALL_RADIUS
EDGE_INSIDE_LEFT   = EDGE_LEFT   + BALL_RADIUS
EDGE_INSIDE_BOTTOM = EDGE_BOTTOM - BALL_RADIUS
EDGE_POINT1 = graphics.Point(EDGE_LEFT,        EDGE_TOP          )
EDGE_POINT2 = graphics.Point(EDGE_RIGHT,       EDGE_TOP          )
EDGE_POINT3 = graphics.Point(EDGE_RIGHT,       EDGE_INSIDE_TOP   )  
EDGE_POINT4 = graphics.Point(EDGE_INSIDE_LEFT, EDGE_INSIDE_TOP   )
EDGE_POINT5 = graphics.Point(EDGE_INSIDE_LEFT, EDGE_INSIDE_BOTTOM)
EDGE_POINT6 = graphics.Point(EDGE_RIGHT,       EDGE_INSIDE_BOTTOM)
EDGE_POINT7 = graphics.Point(EDGE_RIGHT,       EDGE_BOTTOM       )
EDGE_POINT8 = graphics.Point(EDGE_LEFT,        EDGE_BOTTOM       )
EDGE_COLOR = 'white'

# Parameters for the score text
SCORE_TEXT_X     = EDGE_RIGHT / 2
SCORE_TEXT_Y     = EDGE_TOP   / 2
SCORE_TEXT_FONT  = 'courier'
SCORE_TEXT_SIZE  = 36
SCORE_TEXT_COLOR = 'white'

# Parameters for the paddle
PADDLE_HEIGHT = 8*BALL_RADIUS
PADDLE_WIDTH  = BALL_RADIUS
GAP_FROM_EDGE_TO_PADDLE = 2
PADDLE_LEFT_EDGE   = EDGE_RIGHT + GAP_FROM_EDGE_TO_PADDLE + 1
PADDLE_RIGHT_EDGE  = EDGE_RIGHT + GAP_FROM_EDGE_TO_PADDLE + PADDLE_WIDTH
PADDLE_TOP_EDGE    = (EDGE_TOP + EDGE_BOTTOM - PADDLE_HEIGHT) / 2
PADDLE_BOTTOM_EDGE = (EDGE_TOP + EDGE_BOTTOM + PADDLE_HEIGHT) / 2
PADDLE_LOWER_LEFT_POINT  = graphics.Point(PADDLE_LEFT_EDGE,  PADDLE_BOTTOM_EDGE)
PADDLE_UPPER_RIGHT_POINT = graphics.Point(PADDLE_RIGHT_EDGE, PADDLE_TOP_EDGE)
PADDLE_MAX_POSITION = EDGE_BOTTOM - (PADDLE_HEIGHT / 2)
PADDLE_MIN_POSITION = EDGE_TOP    + (PADDLE_HEIGHT / 2)
PADDLE_MOVEMENT = PADDLE_HEIGHT / 4
PADDLE_COLOR = 'white'

# Parameters for 'move paddle up' box
UP_BOX_HEIGHT = 2 * PADDLE_HEIGHT
UP_BOX_WIDTH  = 2 * PADDLE_HEIGHT
UP_BOX_RIGHT_EDGE  = WIDTH - 2
UP_BOX_LEFT_EDGE   = WIDTH - 1 - UP_BOX_WIDTH
UP_BOX_BOTTOM_EDGE = ((EDGE_TOP + EDGE_BOTTOM) / 2) - 1
UP_BOX_TOP_EDGE    = ((EDGE_TOP + EDGE_BOTTOM) / 2) - UP_BOX_HEIGHT
UP_BOX_LOWER_LEFT_POINT  = graphics.Point(UP_BOX_LEFT_EDGE,  UP_BOX_BOTTOM_EDGE)
UP_BOX_UPPER_RIGHT_POINT = graphics.Point(UP_BOX_RIGHT_EDGE, UP_BOX_TOP_EDGE)
UP_BOX_COLOR = 'white'
UP_BOX_TEXT = 'Click here\nto move\npaddle Up'
UP_BOX_TEXT_SIZE = 16
UP_BOX_TEXT_FONT = 'courier'
UP_BOX_TEXT_COLOR = 'black'
UP_BOX_TEXT_X = (UP_BOX_RIGHT_EDGE + UP_BOX_LEFT_EDGE) / 2
UP_BOX_TEXT_Y = (UP_BOX_TOP_EDGE + UP_BOX_BOTTOM_EDGE) / 2

# Parameters for 'move paddle down' box
DOWN_BOX_HEIGHT = 2 * PADDLE_HEIGHT
DOWN_BOX_WIDTH  = 2 * PADDLE_HEIGHT
DOWN_BOX_RIGHT_EDGE  = WIDTH - 2
DOWN_BOX_LEFT_EDGE   = WIDTH - 1 - DOWN_BOX_WIDTH
DOWN_BOX_TOP_EDGE    = ((EDGE_TOP + EDGE_BOTTOM) / 2) + 1
DOWN_BOX_BOTTOM_EDGE = ((EDGE_TOP + EDGE_BOTTOM) / 2) + DOWN_BOX_HEIGHT
DOWN_BOX_LOWER_LEFT_POINT  = graphics.Point(DOWN_BOX_LEFT_EDGE,
                                            DOWN_BOX_BOTTOM_EDGE)
DOWN_BOX_UPPER_RIGHT_POINT = graphics.Point(DOWN_BOX_RIGHT_EDGE,
                                            DOWN_BOX_TOP_EDGE)
DOWN_BOX_COLOR = 'white'
DOWN_BOX_TEXT = 'Click here\nto move\npaddle Down'
DOWN_BOX_TEXT_SIZE = 16
DOWN_BOX_TEXT_FONT = 'courier'
DOWN_BOX_TEXT_COLOR = 'black'
DOWN_BOX_TEXT_X = (DOWN_BOX_RIGHT_EDGE + DOWN_BOX_LEFT_EDGE) / 2
DOWN_BOX_TEXT_Y = (DOWN_BOX_TOP_EDGE + DOWN_BOX_BOTTOM_EDGE) / 2

# Parameters for 'start game' text
GAME_START_TEXT = 'Click to Start Game'
GAME_START_TEXT_SIZE = 36
GAME_START_TEXT_FONT = 'courier'
GAME_START_TEXT_COLOR = 'white'
GAME_START_TEXT_X = (EDGE_RIGHT + EDGE_LEFT  ) / 2
GAME_START_TEXT_Y = (EDGE_TOP   + EDGE_BOTTOM) / 2

# Parameters for 'game over' text
GAME_OVER_TEXT = 'GAME OVER!\nClick to EXIT'
GAME_OVER_TEXT_SIZE = 36
GAME_OVER_TEXT_FONT = 'courier'
GAME_OVER_TEXT_COLOR = 'white'
GAME_OVER_TEXT_X = (EDGE_RIGHT + EDGE_LEFT  ) / 2
GAME_OVER_TEXT_Y = (EDGE_TOP   + EDGE_BOTTOM) / 2

SPEED = 0.02 # seconds between movements

def main():
    # Initialize the graphics window
    win = graphics.GraphWin('Pong', WIDTH, HEIGHT)
    win.setBackground('red')

    # Initialize the edge of the court
    edge = graphics.Polygon(EDGE_POINT1, EDGE_POINT2, EDGE_POINT3, EDGE_POINT4,
                            EDGE_POINT5, EDGE_POINT6, EDGE_POINT7, EDGE_POINT8)
    edge.setFill(EDGE_COLOR)
    edge.draw(win)

    # Initialize and display the score
    score = 0
    score_text = graphics.Text(graphics.Point(EDGE_RIGHT/2, EDGE_TOP/2), '')
    score_text.setFace(SCORE_TEXT_FONT)
    score_text.setSize(SCORE_TEXT_SIZE)
    score_text.setTextColor(SCORE_TEXT_COLOR)
    score_text.setText('Score:  0')
    score_text.draw(win)

    # Initialize the paddle
    paddle = graphics.Rectangle(PADDLE_LOWER_LEFT_POINT,
                                PADDLE_UPPER_RIGHT_POINT)
    paddle.setFill(PADDLE_COLOR)
    paddle.draw(win)

    # Initialize the 'move paddle up' box
    move_up = graphics.Rectangle(UP_BOX_LOWER_LEFT_POINT,
                                 UP_BOX_UPPER_RIGHT_POINT)
    move_up.setFill(UP_BOX_COLOR)
    move_up.draw(win)
    move_up_text = graphics.Text(graphics.Point(UP_BOX_TEXT_X, UP_BOX_TEXT_Y),
                                 UP_BOX_TEXT)
    move_up_text.setFace(UP_BOX_TEXT_FONT)
    move_up_text.setSize(UP_BOX_TEXT_SIZE)
    move_up_text.setTextColor(UP_BOX_TEXT_COLOR)
    move_up_text.draw(win)

    # Initialize the 'move paddle down' box
    move_down = graphics.Rectangle(DOWN_BOX_LOWER_LEFT_POINT,
                                   DOWN_BOX_UPPER_RIGHT_POINT)
    move_down.setFill(DOWN_BOX_COLOR)
    move_down.draw(win)
    move_down_text = graphics.Text(graphics.Point(DOWN_BOX_TEXT_X,
                                                  DOWN_BOX_TEXT_Y),
                                   DOWN_BOX_TEXT)
    move_down_text.setFace(DOWN_BOX_TEXT_FONT)
    move_down_text.setSize(DOWN_BOX_TEXT_SIZE)
    move_down_text.setTextColor(DOWN_BOX_TEXT_COLOR)
    move_down_text.draw(win)
    
    # Initialize the 'start game' text
    start_game_text = graphics.Text(graphics.Point(GAME_START_TEXT_X,
                                                   GAME_START_TEXT_Y),
                                    GAME_START_TEXT)
    start_game_text.setFace(GAME_START_TEXT_FONT)
    start_game_text.setSize(GAME_START_TEXT_SIZE)
    start_game_text.setTextColor(GAME_START_TEXT_COLOR)
    start_game_text.draw(win)

    # Wait for mouse click to start game
    win.getMouse()

    # Erase the 'start game' text
    start_game_text.undraw()
    
    # Initialize the ball
    ball = graphics.Circle(graphics.Point((EDGE_RIGHT+EDGE_LEFT)/2,
                                          (EDGE_TOP+EDGE_BOTTOM)/2),
                           BALL_RADIUS)
    ball.setFill(BALL_COLOR)
    ball.draw(win)
    vx = BALL_X_VELO
    vy = BALL_Y_VELO
    base_vy = BALL_Y_VELO

    while True:
        ball.move(vx, vy)
        time.sleep(SPEED)

        # Get the current position of the ball
        center = ball.getCenter()
        x = center.getX()
        y = center.getY()

        # Get the current position of the paddle
        paddleY = paddle.getCenter().getY()

        # Check whether the paddle should be moved
        mousePoint = win.checkMouse()
        if mousePoint != None:
            mousePointX = mousePoint.getX()
            mousePointY = mousePoint.getY()

            # Check whether mouse clicked in 'move paddle up' box
            if (UP_BOX_LEFT_EDGE <= mousePointX <= UP_BOX_RIGHT_EDGE) and \
               (UP_BOX_TOP_EDGE  <= mousePointY <= UP_BOX_BOTTOM_EDGE):
                # Move paddle up
                if paddleY - PADDLE_MOVEMENT >= PADDLE_MIN_POSITION:
                    paddle.move(0, -PADDLE_MOVEMENT)
                else:
                    paddle.move(0, PADDLE_MIN_POSITION - paddleY)

            # Check whether mouse clicked in 'move paddle down' box
            if (DOWN_BOX_LEFT_EDGE <= mousePointX <= DOWN_BOX_RIGHT_EDGE) and \
               (DOWN_BOX_TOP_EDGE  <= mousePointY <= DOWN_BOX_BOTTOM_EDGE):
                # Move paddle down
                if paddleY + PADDLE_MOVEMENT <= PADDLE_MAX_POSITION:
                    paddle.move(0, PADDLE_MOVEMENT)
                else:
                    paddle.move(0, PADDLE_MAX_POSITION - paddleY)
                
        # Check for collisions with the edges
        if x <= EDGE_INSIDE_LEFT + BALL_RADIUS:
            # Collision with left edge
            vx = -vx
        if y <= EDGE_INSIDE_TOP + BALL_RADIUS:
            # Collision with top edge
            vy = -vy
        elif y >= EDGE_INSIDE_BOTTOM - BALL_RADIUS:
            # Collision with bottom edge
            vy = -vy

        # Check for ball hitting paddle
        if (x >= PADDLE_LEFT_EDGE - BALL_RADIUS) and (vx > 0):
            PaddleY = paddle.getCenter().getY()
            if PaddleY - (PADDLE_HEIGHT/2) <= y <= PaddleY + (PADDLE_HEIGHT/2):
                # Collision with paddle
                vx = -vx
                score += 1
                score_text.setText('Score:  %d' % score)
            
                # If the score is a multiple of 10, increase the ball speed
                if (score // 10)*10 == score:
                    vx -= BALL_X_VDIFF
                    base_vy += BALL_Y_VDIFF

                # Set the y-velocity depending on which part of the paddle hits
                # the ball
                if y < PaddleY - (PADDLE_HEIGHT/4):
                    # Hit with top quarter of paddle, so ball goes up at twice
                    # base velocity
                    vy = -(2 * base_vy)
                elif y < PaddleY:
                    # Hit just above center, so ball goes up at base velocity
                    vy = -base_vy
                elif y > PaddleY + (PADDLE_HEIGHT/4):
                    # Hit with bottom quarter, so ball goes down at twice base
                    # velocity
                    vy = 2 * base_vy
                else:
                    # Hit just below cener, so ball goes down at base velocity
                    vy = base_vy
                    
            else:
                # Missed paddle - Game Over
                end_game_text = graphics.Text(graphics.Point(GAME_OVER_TEXT_X,
                                                             GAME_OVER_TEXT_Y),
                                             GAME_OVER_TEXT)
                end_game_text.setFace(GAME_OVER_TEXT_FONT)
                end_game_text.setSize(GAME_OVER_TEXT_SIZE)
                end_game_text.setTextColor(GAME_OVER_TEXT_COLOR)
                end_game_text.draw(win)

                # flush out any extra clicks
                time.sleep(2.0)
                while win.checkMouse() != None:
                    dummy = 0
                    
                # click the mouse to close the graphics window and end the game
                win.getMouse()
                break
        
    win.close()

if __name__ == '__main__':
    main()
