        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num-1].xcor()
            new_y = self.turtles[turt_num-1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)    
        self.head.forward(move_distance)