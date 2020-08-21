#Thanks for watching this video, Please like this video and subscribe my youtube channel. I appreciate your support.
#I will see you in next video!!~
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def Convert(t):
    D = t % 10
    B = (t // 100) % 6
    C = (t // 10) % 10
    A = t // 100
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

def start():
    global timer,color
    color = "white"
    if not timer.is_running():
        timer.start()

def stop():
    global timer, color
    timer.stop()
    color = "red"

def Clear():
    global t, timer, color
    timer.stop()
    t = 0
    color = "white"

def timerHandler():
    global t
    t += 1

def drawHandler(canvas):
    t_convert = Convert(t)
    canvas.draw_text(t_convert, (15 ,120), 60, color, 'serif')

def main():
    global t, color
    t = 0
    color = "white"
    frame = simplegui.create_frame('Timer', 200, 200, 150)
    global timer
    timer = simplegui.create_timer(100, timerHandler)
    frame.set_draw_handler(drawHandler)
    button_start = frame.add_button("Start", start, 150)
    button_stop = frame.add_button("Stop", stop, 150)
    button_clear = frame.add_button("Clear", Clear, 150)
    frame.start()


if __name__ == '__main__':
    main()
