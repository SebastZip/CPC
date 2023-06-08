class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cliente = value  # Agregar el atributo cliente
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance_factor = self._get_balance_factor(node)
        
        if balance_factor > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance_factor < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        x = z.left
        if x is None:
            return z

        T3 = x.right

        x.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x



    
    def actualizar_cliente(self, cliente, ticket):
        if self.root is None:
            return False
        else:
            return self._actualizar_cliente_recursivo(self.root, cliente, ticket)

    def _actualizar_cliente_recursivo(self, nodo, cliente, ticket):
        if nodo is None:
            return False
        elif nodo.cliente.get_idCliente() == cliente.get_idCliente():
            nodo.cliente = cliente
            nodo.cliente.get_tickets().append(ticket)
            nodo.cliente.get_vehiculos().append(cliente.get_vehiculos()[0])
            return True
        elif nodo.cliente.get_idCliente() > cliente.get_idCliente():
            return self._actualizar_cliente_recursivo(nodo.left, cliente, ticket)
        else:
            return self._actualizar_cliente_recursivo(nodo.right, cliente, ticket)