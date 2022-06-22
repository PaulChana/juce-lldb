import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add juce::Result -F juce_result.result_summary -w juce"
    )

    debugger.HandleCommand("type category enable juce")


def result_summary(value_object, dictionary):
    if (
        value_object.GetChildMemberWithName("errorMessage")
        .GetSummary()
        .replace('"', "")
        == ""
    ):
        return "ok"

    return "failed"
