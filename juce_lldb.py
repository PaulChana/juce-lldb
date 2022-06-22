import lldb


def __lldb_init_module(debugger, dict):

    debugger.HandleCommand(
        'type summary add juce::String --summary-string "${var.text.data}" -w juce'
    )
    debugger.HandleCommand(
        'type summary add juce::File --summary-string "${var.fullPath.text.data}" -w juce'
    )
    debugger.HandleCommand(
        'type summary add -x "^juce::Rectangle<.*>" --summary-string "${var.pos.x}, ${var.pos.y}, ${var.w}, ${var.h}" -w juce'
    )
    debugger.HandleCommand(
        'type summary add -x "^juce::Point<.*>" --summary-string "${var.x}, ${var.y}" -w juce'
    )
    debugger.HandleCommand(
        'type summary add -x "^juce::Range<.*>" --summary-string "${var.start}, ${var.end}" -w juce'
    )
    debugger.HandleCommand(
        'type summary add -x "juce::RelativeTime" --summary-string "seconds = ${var.numSeconds}" -w juce'
    )
    debugger.HandleCommand("type category enable juce")
