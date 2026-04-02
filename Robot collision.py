class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        
        # Step 1: combine all data
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # Step 2: sort by position
        robots.sort()
        
        stack = []  # will store indices of robots moving right
        
        # Step 3: process robots
        for i in range(len(robots)):
            pos, health, direction, idx = robots[i]
            
            if direction == 'R':
                stack.append(i)
            
            else:  # direction == 'L'
                # collision happens
                while stack and robots[i][1] > 0:
                    j = stack[-1]  # last right-moving robot
                    
                    # Case 1: right robot weaker
                    if robots[j][1] < robots[i][1]:
                        robots[i][1] -= 1   # lose 1 health
                        robots[j][1] = 0    # right robot dies
                        stack.pop()
                    
                    # Case 2: left robot weaker
                    elif robots[j][1] > robots[i][1]:
                        robots[j][1] -= 1
                        robots[i][1] = 0
                        break
                    
                    # Case 3: equal
                    else:
                        robots[j][1] = 0
                        robots[i][1] = 0
                        stack.pop()
                        break
        
        # Step 4: return result in original order
        robots.sort(key=lambda x: x[3])
        
        result = []
        for robot in robots:
            if robot[1] > 0:
                result.append(robot[1])
        
        return result
