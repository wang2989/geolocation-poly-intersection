from PIL import Image

graph1 = Image.open('test/graphs/poly_intersection_v1_graph.png')
graph2 = Image.open('test/graphs/pip_graph.png')

finalImage = Image.new('RGB', (graph1.width, graph1.height + graph2.height))
finalImage.paste(graph1, (0,0))
finalImage.paste(graph2, (0,graph1.height))

finalImage.save('test/graphs/concat_graphs.png')