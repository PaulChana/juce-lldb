import lldb
import datetime


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add juce::Time -F juce_time.time_summary -w juce"
    )

    debugger.HandleCommand("type category enable juce")


def time_summary(value_object, dictionary):
    return datetime.datetime.fromtimestamp(
        value_object.GetChildMemberWithName("millisSinceEpoch").GetValueAsUnsigned()
        / 1000.0
    ).strftime("%d-%m-%Y %H:%M:%S.%f")
