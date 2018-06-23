class State():
    def __init__(self, westCannibal, westMissionary, eastCannibal, eastMissionary, boatPosition):
        self.westCannibal = westCannibal
        self.eastCannibal = eastCannibal
        self.westMissionary = westMissionary
        self.eastMissionary = eastMissionary
        self.boatPosition = boatPosition

    def isFinalState(self):
        if self.westCannibal == 0 and self.westMissionary == 0:
            return True
        else:
            return False

    def checkStateValidity(self):
        if self.westMissionary >= 0 and self.eastMissionary >= 0 and self.westCannibal >= 0 and self.eastCannibal >= 0 and (self.eastMissionary == 0 or self.eastMissionary >= self.eastCannibal) and (self.westMissionary == 0 or self.westMissionary >= self.westCannibal):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.westCannibal == other.westCannibal and self.westMissionary == other.westMissionary and self.boatPosition == other.boatPosition and self.eastCannibal == other.eastCannibal and self.eastMissionary == other.eastMissionary

    def __hash__(self):
        return hash((self.westCannibal, self.westMissionary, self.eastCannibal, self.eastMissionary, self.boatPosition))


def movements(curr_state):
    allStates = [];
    if curr_state.boatPosition == "west":

        new_state = State(curr_state.westCannibal, curr_state.westMissionary - 2, curr_state.eastCannibal, curr_state.eastMissionary + 2, "east")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal - 2, curr_state.westMissionary, curr_state.eastCannibal + 2, curr_state.eastMissionary, "east")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal - 1, curr_state.westMissionary - 1, curr_state.eastCannibal + 1, curr_state.eastMissionary + 1, "east")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal, curr_state.westMissionary - 1, curr_state.eastCannibal, curr_state.eastMissionary + 1, "east")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal - 1, curr_state.westMissionary, curr_state.eastCannibal + 1, curr_state.eastMissionary, "east")
        if new_state.checkStateValidity():
            allStates.append(new_state)

    else:

        new_state = State(curr_state.westCannibal, curr_state.westMissionary + 2, curr_state.eastCannibal, curr_state.eastMissionary - 2, "west")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal + 2, curr_state.westMissionary, curr_state.eastCannibal - 2, curr_state.eastMissionary, "west")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal + 1, curr_state.westMissionary + 1, curr_state.eastCannibal - 1, curr_state.eastMissionary - 1, "west")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal, curr_state.westMissionary + 1, curr_state.eastCannibal, curr_state.eastMissionary - 1, "west")
        if new_state.checkStateValidity():
            allStates.append(new_state)

        new_state = State(curr_state.westCannibal + 1, curr_state.westMissionary, curr_state.eastCannibal - 1, curr_state.eastMissionary, "west")
        if new_state.checkStateValidity():
            allStates.append(new_state)

    return allStates


movement_graph = {
    State(3, 3, 0, 0, "west"): movements(State(3, 3, 0, 0, "west")),
    State(3, 2, 0, 1, "west"): movements(State(3, 2, 0, 1, "west")),
    State(3, 1, 0, 2, "west"): movements(State(3, 1, 0, 2, "west")),
    State(3, 0, 0, 3, "west"): movements(State(3, 0, 0, 3, "west")),
    State(2, 3, 1, 0, "west"): movements(State(2, 3, 1, 0, "west")),
    State(2, 2, 1, 1, "west"): movements(State(2, 2, 1, 1, "west")),
    State(2, 1, 1, 2, "west"): movements(State(2, 1, 1, 2, "west")),
    State(2, 0, 1, 3, "west"): movements(State(2, 0, 1, 3, "west")),
    State(1, 3, 2, 0, "west"): movements(State(1, 3, 2, 0, "west")),
    State(1, 2, 2, 1, "west"): movements(State(1, 2, 2, 1, "west")),
    State(1, 1, 2, 2, "west"): movements(State(1, 1, 2, 2, "west")),
    State(1, 0, 2, 3, "west"): movements(State(1, 0, 2, 3, "west")),
    State(0, 3, 3, 0, "west"): movements(State(0, 3, 3, 0, "west")),
    State(0, 2, 3, 1, "west"): movements(State(0, 2, 3, 1, "west")),
    State(0, 1, 3, 2, "west"): movements(State(0, 1, 3, 2, "west")),
    State(0, 0, 3, 3, "west"): movements(State(0, 0, 3, 3, "west")),

    State(3, 3, 0, 0, "east"): movements(State(3, 3, 0, 0, "east")),
    State(3, 2, 0, 1, "east"): movements(State(3, 2, 0, 1, "east")),
    State(3, 1, 0, 2, "east"): movements(State(3, 1, 0, 2, "east")),
    State(3, 0, 0, 3, "east"): movements(State(3, 0, 0, 3, "east")),
    State(2, 3, 1, 0, "east"): movements(State(2, 3, 1, 0, "east")),
    State(2, 2, 1, 1, "east"): movements(State(2, 2, 1, 1, "east")),
    State(2, 1, 1, 2, "east"): movements(State(2, 1, 1, 2, "east")),
    State(2, 0, 1, 3, "east"): movements(State(2, 0, 1, 3, "east")),
    State(1, 3, 2, 0, "east"): movements(State(1, 3, 2, 0, "east")),
    State(1, 2, 2, 1, "east"): movements(State(1, 2, 2, 1, "east")),
    State(1, 1, 2, 2, "east"): movements(State(1, 1, 2, 2, "east")),
    State(1, 0, 2, 3, "east"): movements(State(1, 0, 2, 3, "east")),
    State(0, 3, 3, 0, "east"): movements(State(0, 3, 3, 0, "east")),
    State(0, 2, 3, 1, "east"): movements(State(0, 2, 3, 1, "east")),
    State(0, 1, 3, 2, "east"): movements(State(0, 1, 3, 2, "east")),
    State(0, 0, 3, 3, "east"): movements(State(0, 0, 3, 3, "east"))
}


def depth_first_backtrack(graph, state, visited):
    if state not in visited:
        visited.append(state)
        for n in graph[state]:
            depth_first_backtrack(graph, n, visited)
    return visited


def main():
    start_state = State(3, 3, 0, 0, "west")
    visited = depth_first_backtrack(movement_graph, start_state, [])
    print ("Format : (West Cannibals, West Missionaries) <<<< Boat Position >>>>  (East Cannibals, East Missionaries)")
    while visited:
    	state = visited.pop(0)
    	print ("(" + str(state.westCannibal) + ", " + str(state.westMissionary) + ")" + "  << " + state.boatPosition + " >>  " + "(" + str(state.eastCannibal) + ", " + str(state.eastMissionary) + ")")
    	if state.isFinalState():
    		break


if __name__ == "__main__":
    main()
