import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add -x juce::Component -F juce_component.component_summary -w juce"
    )


def component_summary(value_object, dictionary):

    name = (
        value_object.GetChildMemberWithName("componentName")
        .GetSummary()
        .replace('"', "")
    )
    bounds = (
        value_object.GetChildMemberWithName("boundsRelativeToParent")
        .GetSummary()
        .replace('"', "")
    )
    visible = (
        value_object.GetChildMemberWithName("flags")
        .GetChildMemberWithName("visibleFlag")
        .GetValue()
    )
    parent = (
        value_object.GetChildMemberWithName("parentComponent").GetValueAsUnsigned() != 0
    )
    return (
        name
        + " bounds = "
        + bounds
        + " parent = "
        + str(parent)
        + " visible = "
        + str(visible)
    )
