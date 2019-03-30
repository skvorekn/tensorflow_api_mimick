class add(BinaryOperation):
  """
  Computes a + b, element-wise
  """
  def forward(self, a, b):
    return a + b

  def backward(self, upstream_grad):
    raise NotImplementedError

class multiply(BinaryOperation):
  """
  Computes a * b, element-wise
  """
  def forward(self, a, b):
    return a * b

  def backward(self, upstream_grad):
    raise NotImplementedError

class divide(BinaryOperation):
  """
  Returns the true division of the inputs, element-wise
  """
  def forward(self, a, b):
    return np.true_divide(a, b)

  def backward(self, upstream_grad):
    raise NotImplementedError

class matmul(BinaryOperation):
  """
  Multiplies matrix a by matrix b, producing a * b
  """
  def forward(self, a, b):
    return a.dot(b)

  def backward(self, upstream_grad):
    raise NotImplementedError