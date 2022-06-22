import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand("type summary add juce::var -F juce_var.var_summary -w juce")

    debugger.HandleCommand("type category enable juce")


def var_summary(value_object, dictionary):
    type = value_object.GetChildMemberWithName("type")
    value = value_object.GetChildMemberWithName("value")
    if type.GetChildMemberWithName("isString").GetValue() == "true":
        return (
            "string = "
            + value.GetChildMemberWithName("stringValue")
            .Cast(value_object.GetFrame().GetModule().FindFirstType("juce::String"))
            .GetSummary()
        )
    if type.GetChildMemberWithName("isInt").GetValue() == "true":
        return "int = " + value.GetChildMemberWithName("intValue").GetValue()
    if type.GetChildMemberWithName("isInt64").GetValue() == "true":
        return "int64 = " + value.GetChildMemberWithName("int64Value").GetValue()
    if type.GetChildMemberWithName("isDouble").GetValue() == "true":
        return "double = " + value.GetChildMemberWithName("doubleValue").GetValue()
    if type.GetChildMemberWithName("isBool").GetValue() == "true":
        return "bool = " + value.GetChildMemberWithName("boolValue").GetValue()
    if type.GetChildMemberWithName("isVoid").GetValue() == "true":
        return "<void>"
    if type.GetChildMemberWithName("isUndefined").GetValue() == "true":
        return "<undefined>"
    if type.GetChildMemberWithName("isObject").GetValue() == "true":
        return "<object>"
    if type.GetChildMemberWithName("isArray").GetValue() == "true":
        return "<array>"
    if type.GetChildMemberWithName("isBinaryData").GetValue() == "true":
        return "<data>"
    if type.GetChildMemberWithName("isMethod").GetValue() == "true":
        return "<function>"

    return ""
