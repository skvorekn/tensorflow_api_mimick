def topology_sort(operation):
    ordering = []
    visited_nodes = set()

    def recursive_helper(node):
      if isinstance(node, Operation):
        for input_node in node.input_nodes:
          if input_node not in visited_nodes:
            recursive_helper(input_node)

      visited_nodes.add(node)
      ordering.append(node)

    # start recursive depth-first search
    recursive_helper(operation)

    return ordering