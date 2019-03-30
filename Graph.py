class Graph():
  def __init__(self):
    self.operations = []
    self.placeholders = []
    self.variables = []
    self.constants = []

  def as_default(self):
    global _default_graph
    _default_graph = self