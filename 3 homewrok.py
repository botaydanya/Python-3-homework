def hasPathSum(vertices, targetSum, node=0, current_path=[]):
    if node >= len(vertices) or vertices[node] is None:
        return False
    
    current_path.append(vertices[node])
    
    if (not node * 2 + 1 < len(vertices)) and (not (node * 2 + 2 < len(vertices))): 
        if sum(current_path) == targetSum:
            return current_path
        else:
            current_path.pop()
            return False
    
    left = hasPathSum(vertices, targetSum, node * 2 + 1, current_path)
    right = hasPathSum(vertices, targetSum, node * 2 + 2, current_path)
    
    if left:
        return left
    elif right:
        return right
    else:
        current_path.pop()
        return False


vertex_input = input("Введите значения вершин деревьев через пробел: ")
vertices = [int(val) if val != "None" else None for val in vertex_input.split()]

targetSum = int(input("Введите сумму, которую необходимо получить: "))

path = hasPathSum(vertices, targetSum)

if path:
    path_str = ' -> '.join(map(str, path))
    print("Путь с необходимой суммой следующий:", path_str)
else:
    print("Не существует путя с необходимой суммой")
