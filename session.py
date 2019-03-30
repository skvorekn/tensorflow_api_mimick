class Session():
  def run(self, operation, feed_dict={}):
    nodes_sorted = topology_sort(operation)

    for node in nodes_sorted:
      if type(node) == Placeholder:
        node.output = feed_dict[node]
      elif type(node) == Variable or type(node) == Constant:
        node.output = node.value
      else:
        inputs = [node.output for node in node.input_nodes]
        node.output = node.forward(*inputs)

    return operation.output