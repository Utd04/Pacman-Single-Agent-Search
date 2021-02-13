# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    REVERSE_PUSH = False

    @staticmethod
    def reverse_push():
        SearchProblem.REVERSE_PUSH = not SearchProblem.REVERSE_PUSH

    @staticmethod
    def print_push():
        print(SearchProblem.REVERSE_PUSH)

    @staticmethod
    def get_push():
        return SearchProblem.REVERSE_PUSH

    def get_expanded(self):
        return self.__expanded

    def inc_expanded(self):
        self.__expanded+=1

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    # return [s,s,s]

def dir(direction):
    if(direction=='North'):
        return 'n'
    if(direction=='South'):
        return 's'
    if(direction=='East'):
        return 'e'
    if(direction=='West'):
        return 'w'

def check(state, visited):
    for i in range(len(visited)):
        if(visited[i]==state):
            return True
    return False

def dfshelper(problem, state, path, visited):
    if(problem.isGoalState(state)):
        return True
    visited.append(state)
    successors=problem.getSuccessors(state)
    for i in range(len(successors)):
        if(successors[i][0] not in visited):
            path.append(successors[i][1])
            if(dfshelper(problem, successors[i][0], path, visited)):
                return True
            del path[-1]
    return False


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # print ("Start:", problem.getStartState())
    # print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors((5,5)))
    path=[]
    visited=[]
    dfshelper(problem,problem.getStartState(),path,visited)
    return path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import Queue
    q=Queue()
    q2=Queue()
    q2.push([])
    q.push([problem.getStartState()])
    visited = []
    visited.append(problem.getStartState())
    if(problem.isGoalState(problem.getStartState())):
        return []
    x=1
    while(q.isEmpty()==False):
        path=q.pop()
        path2=q2.pop()
        top=path[-1]
        if(problem.isGoalState(top)):
            return path2
        successors=problem.getSuccessors(top)
        for i in range(len(successors)):
            if(successors[i][0] not in visited):
                # path.append(successors[i][1])
                addpath=list(path)
                addpath.append(successors[i][0])
                addpath2=list(path2)
                addpath2.append(successors[i][1])
                q.push(addpath)
                q2.push(addpath2)
                visited.append(successors[i][0])
                # if(problem.isGoalState(successors[i][0])):
                #     return addpath2
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import PriorityQueue
    pq= PriorityQueue()
    pq.push((problem.getStartState(),0,[]),0)
    # pq2= PriorityQueue()
    # pq2.push(problem.getStartState())
    visited= []
    frontier = []
    while(pq.isEmpty()==False):
        top=pq.pop()
        if(top[0] not in visited):
            visited.append(top[0])
            if(problem.isGoalState(top[0])):
                return top[2]
            path=top[2]
            successors=problem.getSuccessors(top[0])
            for i in range(len(successors)):
                if(successors[i][0] not in visited):
                    addpath=list(path)
                    addpath.append(successors[i][1])
                    pq.update((successors[i][0],top[1]+successors[i][2],addpath),top[1]+successors[i][2])
                


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    from util import PriorityQueue
    pq= PriorityQueue()
    pq.push((problem.getStartState(),heuristic(problem.getStartState(),problem),[],0),heuristic(problem.getStartState(),problem))
    # pq2= PriorityQueue()
    # pq2.push(problem.getStartState())
    visited= []
    while(pq.isEmpty()==False):
        top=pq.pop()
        if(top[0] not in visited):
            visited.append(top[0])
            if(problem.isGoalState(top[0])):
                return top[2]
            path=top[2]
            successors=problem.getSuccessors(top[0])
            for i in range(len(successors)):
                if(successors[i][0] not in visited):
                    addpath=list(path)
                    addpath.append(successors[i][1])
                    pq.update((successors[i][0],top[3]+successors[i][2]+heuristic(successors[i][0],problem),addpath,top[3]+successors[i][2]),top[3]+successors[i][2]+heuristic(successors[i][0],problem)    )
                


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
reverse_push=SearchProblem.reverse_push
print_push=SearchProblem.print_push
