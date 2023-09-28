import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = pandas.read_csv("50_states.csv")

# def get_mouse_click_corr(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()


guest_state = []
score = 0


while len(guest_state) < 50:
    answer_state = screen.textinput(f"State correct: {len(guest_state)}/50 ", "What is another state's name").title()

    state_data = data[data.state == answer_state]

    if not state_data.empty and not guest_state.__contains__(answer_state):
        x = int(state_data["x"].to_string(index=False))
        y = int(state_data["y"].to_string(index=False))

        pen.goto(x, y)
        pen.write(answer_state)

        guest_state.append(answer_state)

    all_state = state_data["state"].to_list()

    if answer_state == "Exit"  :
        state_to_learn =[ state for state in data["state"].to_list() if state not in guest_state]



        new_data = pandas.DataFrame(state_to_learn)
        new_data.to_csv("state_to_learn.csv")
        break





screen.exitonclick()
