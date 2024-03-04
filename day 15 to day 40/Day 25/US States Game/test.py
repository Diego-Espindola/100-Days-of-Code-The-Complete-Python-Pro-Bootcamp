class AttrDict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(f"'AttrDict' object has no attribute '{name}'")


# Example usage:
my_dict = AttrDict({'a': 1, 'b': 2, 'c': 3})

print(my_dict.a)  # Output: 1
print(my_dict.b)  # Output: 2

# Accessing non-existent attribute
# This will raise an AttributeError
# print(my_dict.d)
