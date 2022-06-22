import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add -x juce::MemoryBlock  -F juce_memory.memory_summary -w juce"
    )
    debugger.HandleCommand("type category enable juce")


def memory_summary(value_object, dictionary):
    if value_object.GetChildMemberWithName("size").GetValueAsUnsigned() == 0:
        return "<empty>"

    return (
        value_object.GetChildMemberWithName("data")
        .GetChildMemberWithName("data")
        .GetSummary()
    )
