class Placeholder():
  def __init__(self):
    self.value = None
    _default_graph.placeholders.append(self)