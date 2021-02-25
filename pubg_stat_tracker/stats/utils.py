import matplotlib.pyplot as plt
from matplotlib import rcParams
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
    plt.style.use('fivethirtyeight')
    rcParams.update({'figure.autolayout': True})

    plt.plot(x, y)
    plt.title(title)
    plt.tight_layout()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(x)
    plt.ylim(bottom=0)

    graph = get_graph()
    return graph
