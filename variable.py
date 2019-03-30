# weights are trainable parameters = variables
class Variable():
  def __init__(self, initial_value=None):
    self.value = initial_value
    _default_graph.variables.append(self)