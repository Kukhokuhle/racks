import turtle

myPen = turtle.Pen()

l = 2500 #length of rack (mm)
h = 1650 #height of rack (mm)
w = 850   #width of rack (mm)

#height of rack levels from bottom(level1) to top(level4) (mm) 
level1 = 300
level2 = 300
level3 = 400
level4 = 500 

#CONSTANTS
level0 = 70             #this level is almost always ~70 mm from base
angle  = 40             #how much higher back levels are than front levels (in mm!!!!!!!!!!!!!)

################################################################################
sc=turtle.Screen() 
#myPen=turtle.Turtle() 
myPen.speed(0)

#myPen.penup()
side_x_start = (-1*l)
rear_x_start = side_x_start + ( (-1*w) - 500 )
grid_x_start = rear_x_start - 500
myPen.goto(grid_x_start/10, 0)

#myPen.pendown()

# method to draw y-axis lines 
def drawy(val): 
	
	# line 
	myPen.forward(300) 
	
	# set position 
	myPen.up() 
	myPen.setpos(val,300) 
	myPen.down() 
	
	# another line 
	myPen.backward(300) 
	
	# set position again 
	myPen.up() 
	myPen.setpos(val+10,0) 
	myPen.down() 
	
# method to draw x-axis lines 
def drawx(val): 
	
	# line 
	myPen.forward(600) 
	
	# set position 
	myPen.up() 
	myPen.setpos(600,val) 
	myPen.down() 
	
	# another line 
	myPen.backward(600) 
	
	# set position again 
	myPen.up() 
	myPen.setpos(grid_x_start/10,val+10) 
	myPen.down() 
	
# Main Section 
# set screen 
sc.setup(800,800)	 

# set turtle features 
#myPen.speed(1) 
myPen.left(90) 
myPen.color('lightgreen') 

# y lines 
for i in range(90): 
	drawy(10*-1*(i+1-50)) 

# set position for x lines 
myPen.right(90) 
myPen.up() 
#myPen.setpos(grid_x_start/10,0) 
myPen.down() 

# x lines 
for i in range(30): 
	drawx((10*(i+1-1))) 

################################################################################

#setworldcoordinates(-2200, -100, 5200, 2100)

myPen.color('black') 
#################################
#pick up the pen and move to start drawing the side view
myPen.penup()

side_x_start = (-1*l)
myPen.goto(side_x_start/10, 0 )

myPen.pendown()
#################################

#################################
#draw the side view
for i in range(2):
	myPen.forward(l/10)
	myPen.left(90)
	myPen.forward(h/10)
	myPen.left(90)

#pick up the pen and move to start drawing strut 1
myPen.penup()
 
#start drawing strut 1 150 mm from base
strut_y_start = 150

myPen.goto(side_x_start/10, strut_y_start/10)
    
myPen.pendown()

#strut 1 goes 1/3 of the length from the rear
myPen.goto( (side_x_start + l/3)/10, h/10 )

#draw side column 1
myPen.goto( (side_x_start + l/3)/10, 0 )

#draw side column 2
myPen.goto( (side_x_start + (2/3)*l)/10, 0 )
myPen.goto( (side_x_start + (2/3)*l)/10, h/10 )

#draw strut 2
myPen.goto( (side_x_start + l/3)/10, h/10 )
myPen.goto( (side_x_start + (2/3)*l)/10, strut_y_start/10)

#draw level 0 of side view 
side_level0_y = level0 + angle

myPen.penup()
myPen.color('red') #draw rollers in red 
myPen.goto(side_x_start/10, side_level0_y/10 )
myPen.pendown()
myPen.goto( (side_x_start+l)/10, (side_level0_y-angle)/10 )

#draw level 1 of side view 
side_level1_y = side_level0_y + level1

myPen.penup()
#myPen.color('red')
myPen.goto(side_x_start/10, side_level1_y/10 )
myPen.pendown()
myPen.goto( (side_x_start+l)/10, (side_level1_y-angle)/10 )

#draw level 2 of side view 
side_level2_y = side_level1_y + level2

myPen.penup()
#myPen.color('red')
myPen.goto(side_x_start/10, side_level2_y/10 )
myPen.pendown()
myPen.goto( (side_x_start+l)/10, (side_level2_y-angle)/10 )

#draw level 3 of side view 
side_level3_y = side_level2_y + level3

myPen.penup()
#myPen.color('red')
myPen.goto(side_x_start/10, side_level3_y/10 )
myPen.pendown()
myPen.goto( (side_x_start+l)/10, (side_level3_y-angle)/10 )

#draw level 4 of side view 
side_level4_y = side_level3_y + level4 - 80 #return level slopes backwards! (hence the -80mm)

myPen.penup()
#myPen.color('red')
myPen.goto(side_x_start/10, side_level4_y/10 )
myPen.pendown()
myPen.goto( (side_x_start+l)/10, (side_level4_y+angle)/10 )
#################################

myPen.color('black')
#################################
#pick up the pen and move to start drawing the rear view
myPen.penup()

rear_x_start = side_x_start + ( (-1*w) - 500 )
myPen.goto(rear_x_start/10, 0 )

myPen.pendown()

#################################
#draw the rear view
for i in range(2):
	myPen.forward(w/10)
	myPen.left(90)
	myPen.forward(h/10)
	myPen.left(90)
	
#draw level 0 of rear view
rear_level0_y = level0 + angle                    #standardise this to 110 mm (70mm+40mm) from base 
myPen.goto(rear_x_start/10, rear_level0_y/10 )
myPen.forward(w/10)

#draw level 1 of rear view
rear_level1_y = rear_level0_y + level1 

myPen.penup() 
myPen.goto(rear_x_start/10, rear_level1_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 2 of rear view
rear_level2_y = rear_level0_y + level1 + level2

myPen.penup() 
myPen.goto(rear_x_start/10, rear_level2_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 3 of rear view
rear_level3_y = rear_level0_y + level1 + level2 + level3

myPen.penup() 
myPen.goto(rear_x_start/10, rear_level3_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 4 of rear view
#one of the rear levels has to be smaller/shorter than the front one otherwise
#we cannot get a return level that slopes backwards! (hence the -80mm below)
rear_level4_y = rear_level0_y + level1 + level2 + level3 + level4 - 80 

myPen.penup() 
myPen.goto(rear_x_start/10, rear_level4_y/10 )
myPen.pendown()
myPen.forward(w/10)
#################################
#################################
    
#################################
#pick up the pen and move to start drawing the front view
myPen.penup()
    
front_x_start = 500
myPen.goto(front_x_start/10, 0 )
    
myPen.pendown()
#################################
    
#################################
#draw the front view
for i in range(2):
	myPen.forward(w/10)
	myPen.left(90)
	myPen.forward(h/10)
	myPen.left(90)

#draw level 0 of front view 
front_level0_y = level0                          
myPen.goto(front_x_start/10, front_level0_y/10 )
myPen.forward(w/10)

#draw level 1 of front view
front_level1_y = level0 + level1

myPen.penup()                 
myPen.goto(front_x_start/10, front_level1_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 2 of front view
front_level2_y = level0 + level1 + level2 

myPen.penup()                 
myPen.goto(front_x_start/10, front_level2_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 3 of front view
front_level3_y = level0 + level1 + level2 + level3

myPen.penup()                 
myPen.goto(front_x_start/10, front_level3_y/10 )
myPen.pendown()
myPen.forward(w/10)

#draw level 4 of front view
front_level4_y = level0 + level1 + level2 + level3 + level4

myPen.penup()                 
myPen.goto(front_x_start/10, front_level4_y/10 )
myPen.pendown()
myPen.forward(w/10)
#################################
myPen.hideturtle()
turtle.getscreen().getcanvas().postscript(file='rack.ps')

turtle.done()



