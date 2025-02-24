from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from collections import deque

@csrf_exempt
def find_shortest_path(request):
    data = json.loads(request.body)
    start = data.get('start')
    end = data.get('end')


    if not start or not end:
        return  JsonResponse({"error": "Start and end is not provided."})
    path = find_path_algorithm(start, end)
    if path:
        return JsonResponse({'result': path})
    else:
        return JsonResponse({"sucess" : False})

def find_path_algorithm(start, end):

    visited = {(start[0], start[1]) : None}
    found = False
    # Initializing a queur with the start
    queue = deque([(start[0], start[1])])

    # All neighours directions = top, right, bottom and left.
    directions = [(-1,  0), (1,0), (0,-1), (0,1)]
    # directions = [(-1,  0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (1,1), (-1,1)]

    
    # Iterating queue and adding neighbouring grid to the queue.
    while queue:
        current = queue.popleft()
        # If current matches with end. Taget is found and returned.
        if current == (end[0], end[1]):
            found = True
            break

        # Adding neighbouring grids to the queue
        for dx, dy in directions:
            x,y = current[0] + dx, current[1] + dy
            if 0 <= x <= 20 and 0 <= y <= 20 and (x,y) not in visited:
                visited[(x,y)] = current
                queue.append((x,y))
        
        # Handle Not found situation

        # Reconstruct path from end to start
    path = []
    current = (end[0], end[1])
    while current:
        path.append([current[0], current[1]])
        current = visited[current]
    
    # Reversing the path from [end to start] to [start to end]
    path.reverse()
    return path 


