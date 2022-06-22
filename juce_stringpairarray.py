import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        'type summary add -x juce::StringPairArray --summary-string "size = ${var.keys.strings.values.numUsed}" -w juce'
    )
    debugger.HandleCommand(
        'type synthetic add -x "juce::StringPairArray" --python-class juce_stringpairarray.StringPairArrayChildrenProvider -w juce'
    )

    debugger.HandleCommand("type category enable juce")


class StringPairArrayChildrenProvider:
    def __init__(self, value_object, dictionary):
        self.value_object = value_object
        self.count = 0
        self.update()

    def num_children(self):
        return self.count

    def get_child_index(self, name):
        key = name.lstrip("[ ").split("]")[0]
        for index in range(0, self.count):
            key = (
                self.keys.CreateChildAtOffset(
                    "", index * self.data_size, self.data_type
                )
                .GetSummary()
                .replace('"', "")
            )
            if key == name:
                return index

        return -1

    def get_child_at_index(self, index):
        key = (
            self.keys.CreateChildAtOffset("", index * self.data_size, self.data_type)
            .GetSummary()
            .replace('"', "")
        )

        return self.values.CreateChildAtOffset(
            "[" + key + "]",
            index * self.data_size,
            self.data_type,
        )

    def update(self):
        self.keys = (
            self.value_object.GetChildMemberWithName("keys")
            .GetChildMemberWithName("strings")
            .GetChildMemberWithName("values")
            .GetChildMemberWithName("elements")
            .GetChildMemberWithName("data")
        )
        self.values = (
            self.value_object.GetChildMemberWithName("values")
            .GetChildMemberWithName("strings")
            .GetChildMemberWithName("values")
            .GetChildMemberWithName("elements")
            .GetChildMemberWithName("data")
        )
        self.data_type = self.values.GetType().GetPointeeType()
        self.data_size = self.data_type.GetByteSize()
        self.count = (
            self.value_object.GetChildMemberWithName("keys")
            .GetChildMemberWithName("strings")
            .GetChildMemberWithName("values")
            .GetChildMemberWithName("numUsed")
            .GetValueAsUnsigned()
        )

    def has_children(self):
        return self.count > 0
