"My custom meta class."


class CustomMeta(type):

    "Meta class which adds 'custom_' to every attribute/method name (except magic methods)."

    def __new__(cls, clsname, bases, attrs):
        res_attrs = {}
        for attr, val in attrs.items():
            if attr.startswith('__') and attr.endswith('__'):
                res_attrs[attr] = val
            else:
                res_attrs['custom_' + attr] = val

        if '__init__' not in attrs:
            return super().__new__(cls, clsname, bases, res_attrs)

        def init(self, *args, **kwargs):
            attrs['__init__'](self, *args, **kwargs)
            dict_mods = {}
            for attr, val in self.__dict__.items():
                if attr.startswith('__') and attr.endswith('__'):
                    continue
                dict_mods[(attr, 'custom_' + attr)] = val
            for (old_attr, new_attr), val in dict_mods.items():
                delattr(self, old_attr)
                setattr(self, new_attr, val)

        res_attrs['__init__'] = init
        return super().__new__(cls, clsname, bases, res_attrs)
