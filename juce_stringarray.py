import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        'type summary add juce::StringArray --summary-string "size = ${var.strings.values.numUsed}" -w juce'
    )
    debugger.HandleCommand(
        'type synthetic add -x "juce::StringArray" --python-class juce_stringarray.StringArrayChildrenProvider -w juce'
    )

    debugger.HandleCommand("type category enable juce")


class StringArrayChildrenProvider:
    def __init__(self, value_object, dictionary):
        self.value_object = value_object
        self.count = 0
        self.update()

    def num_children(self):
        return self.count

    def get_child_index(self, name):
        return int(name.lstrip("[").rstrip("]"))

    def get_child_at_index(self, index):
        return self.values.CreateChildAtOffset(
            "[" + str(index) + "]", index * self.data_size, self.data_type
        )

    def update(self):
        self.values = (
            self.value_object.GetChildMemberWithName("strings")
            .GetChildMemberWithName("values")
            .GetChildMemberWithName("elements")
            .GetChildMemberWithName("data")
        )
        self.data_type = self.values.GetType().GetPointeeType()
        self.data_size = self.data_type.GetByteSize()
        self.count = (
            self.value_object.GetChildMemberWithName("strings")
            .GetChildMemberWithName("values")
            .GetChildMemberWithName("numUsed")
            .GetValueAsUnsigned()
        )

    def has_children(self):
        return self.count > 0
