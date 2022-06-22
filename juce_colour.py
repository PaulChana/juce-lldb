import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add juce::Colour -F juce_colour.colour_summary -w juce"
    )

    debugger.HandleCommand("type category enable juce")


def colour_component_value(value_object, component_name):
    return (
        value_object.GetChildMemberWithName("argb")
        .GetChildMemberWithName("components")
        .GetChildMemberWithName(component_name)
        .GetValueAsUnsigned()
    )


def colour_summary(value_object, dictionary):
    return "0x{a:02X}{r:02X}{g:02X}{b:02X}".format(
        a=colour_component_value(value_object, "a"),
        r=colour_component_value(value_object, "r"),
        g=colour_component_value(value_object, "g"),
        b=colour_component_value(value_object, "b"),
    )
