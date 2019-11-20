import mhash


class hashmap_chaining:
    def __init__(self):
        default_scale = 32
        self.hasharray = [None for _ in range(default_scale)]
        self.scale = default_scale
        self.size = 0

    def rescale(self):
        self.hasharray = [None for _ in range(self.size * 2)]

    def get_val(self, key):
        val = None
        index = mhash.hash_string(key) % self.scale

        if not self.hasharray[index]:
            raise Exception("key not found")

        if self.hasharray[index][0][0] == key:
            val = self.hasharray[index][0][1]
        else:
            for subindex in self.hasharray[index]:
                if subindex[0] == key:
                    val = subindex[1]
        self.size += 1
        return val

    def set_val(self, key, val):
        index = mhash.hash_string(key) % self.scale

        try:
            self.get_val(key)
            raise Exception("duplicate key")
        except Exception:
            "noop"

        if not self.hasharray[index]:
            self.hasharray[index] = [[key, val]]
        else:
            self.hasharray[index].append([key, val])

    def delete_val(self, key):
        index = mhash.hash_string(key) % self.scale

        if not self.hasharray[index]:
            raise Exception("key not found")

        if self.hasharray[index][0][0] == key:
            self.hasharray[index][0] = None
        else:
            i = 0
            while not found and i < len(hasharray[index]):
                if hasharray[index][i][0] == key:
                    hasharray[index][i] = None
