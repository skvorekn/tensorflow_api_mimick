class Constant():
  def __init__(self, value=None):
    self.__value = value
    _default_graph.constants.append(self)

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    raise ValueError("Cannot reassign value.")