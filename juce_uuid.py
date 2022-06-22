import lldb
import uuid


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add juce::Uuid -F juce_uuid.uuid_summary -w juce"
    )

    debugger.HandleCommand("type category enable juce")


def uuid_summary(value_object, dictionary):
    juceUuid = value_object.GetChildMemberWithName("uuid")

    bytes = []
    for i in range(0, 16):
        bytes.append(
            format(juceUuid.GetChildAtIndex(i).GetValueAsUnsigned(), "#04x")[2:]
        )

    uid = "".join(map(str, bytes))
    result = uuid.UUID(uid)
    return result
