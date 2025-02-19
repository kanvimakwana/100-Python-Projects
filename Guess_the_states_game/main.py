import turtle
import pandas

# Load Data
data = pandas.read_csv(r"d:/Udemy python/india game/states_data.csv")

# Setup Screen
screen = turtle.Screen()
screen.title("India")
image = r"d:/Udemy python/india game/blank_map.gif"
screen.addshape(image)  
turtle.shape(image)  

# Game Variables
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    
    if answer_state is None:  # If user closes input box
        break
    
    answer_state = answer_state.title()
    

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        # Create Turtle for Writing State Name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        # Get State Data
        state_data = data[data.state == answer_state]
        x, y = float(state_data.x.item()), float(state_data.y.item())  # Convert to float
        
        print(type(x), type(y))  # Debugging output
        
        t.goto(x, y)
        t.write(answer_state)
