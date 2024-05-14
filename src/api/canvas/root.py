import json
from fastapi import APIRouter
from pyjsoncanvas import (
    Canvas,
    TextNode,
    FileNode,
    Edge,
    Color,
)
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

canvas_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@canvas_router.get("/", response_class=HTMLResponse)
def get_canvas(request: Request):
    with open("/workspace/src/sample.canvas") as f:
        canvas_json = json.load(f)
    canvas_json = json.dumps(canvas_json)
    canvas_json = Canvas.from_json(canvas_json)
    print(canvas_json)
    return templates.TemplateResponse("canvas.html", {"request": request})

@canvas_router.get("/create")
def create_canvas():
    # Create a new canvas
    canvas = Canvas(nodes=[], edges=[])
    print(Canvas)
    # Add some nodes
    text_node = TextNode(x=100, y=100, width=200, height=100, text="Hello, world!")
    canvas.add_node(text_node)
    print(text_node)
    file_node = FileNode(x=300, y=100, width=100, height=100, file="/path/to/file.png")
    canvas.add_node(file_node)

    # Add an edge
    edge = Edge(
        fromNode=text_node.id,
        fromSide="bottom",
        toNode=file_node.id,
        toSide="top",
        color=Color("#FF0000"),
        label="Edge 1",
    )
    canvas.add_edge(edge)
    print(edge)
    # Save the canvas as JSON
    json_str = canvas.to_json()
    print(json_str)
    # Load the canvas from JSON
    loaded_canvas = Canvas.from_json(json_str)
    print(loaded_canvas)
    # Get a node
    node = loaded_canvas.get_node(text_node.id)
    print(node)
    # Get connections for a node
    connections = loaded_canvas.get_connections(text_node.id)
    
    print(connections)