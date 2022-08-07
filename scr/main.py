from fastapi import FastAPI
from scr.models import Request
from scr.finder_path import BFS
from scr.node import MazeNode

app = FastAPI(description='Small API to find minimal way from labyrinth, labyrinth is represented by graph.')


def get_result(graph, start, finish):
    mazes = MazeNode(graph, start)
    bfs = BFS(mazes, finish)
    result = bfs()
    return result


@app.post('/all_data')
async def all_data(request: Request):
    graph = request.graph
    start, finish = request.start, request.finish
    return get_result(graph, start, finish)


@app.post('/steps')
async def steps(request: Request):
    graph = request.graph
    start, finish = request.start, request.finish
    return get_result(graph, start, finish)[0]


@app.post('path')
async def path(request: Request):
    graph = request.graph
    start, finish = request.start, request.finish
    return get_result(graph, start, finish)[1]
