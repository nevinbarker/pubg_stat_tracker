import matplotlib.pyplot as plt
from io import BytesIO
import base64


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, x_label, y_label, title):
    plt.switch_backend('AGG')

    plt.plot(x, y)
    plt.title(title)
    plt.tight_layout()
    plt.style.use('fivethirtyeight')
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    graph = get_graph()
    return graph
