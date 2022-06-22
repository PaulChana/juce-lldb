import lldb
import uuid


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
        "type summary add -x juce::URL -F juce_lldb.urlSummary -w juce"
    )
    debugger.HandleCommand(
        "type summary add juce::Uuid -F juce_lldb.uuidSummary -w juce"
    )
    debugger.HandleCommand(
        "type summary add juce::Colour -F juce_lldb.colourSummary -w juce"
    )

    debugger.HandleCommand("type category enable juce")


# -------------------------------------------------------------------------------------
# UUID definition
# Displays the uuid in the dash encoded format (00000000-0000-0000-0000-000000000000)
# -------------------------------------------------------------------------------------
def uuidSummary(valueObject, dictionary):
    juceUuid = valueObject.GetChildMemberWithName("uuid")

    bytes = []
    for i in range(0, 16):
        bytes.append(
            format(juceUuid.GetChildAtIndex(i).GetValueAsUnsigned(), "#04x")[2:]
        )

    uid = "".join(map(str, bytes))
    result = uuid.UUID(uid)
    return result


# -------------------------------------------------------------------------------------
# Colour definition
# Displays the colour as both a rgba value and the hex ARGB version
# -------------------------------------------------------------------------------------
def colourSummary(valueObject, dictionary):
    return "0x{a:02X}{r:02X}{g:02X}{b:02X}".format(
        a=valueObject.GetChildMemberWithName("argb")
        .GetChildMemberWithName("components")
        .GetChildMemberWithName("a")
        .GetValueAsUnsigned(),
        r=valueObject.GetChildMemberWithName("argb")
        .GetChildMemberWithName("components")
        .GetChildMemberWithName("r")
        .GetValueAsUnsigned(),
        g=valueObject.GetChildMemberWithName("argb")
        .GetChildMemberWithName("components")
        .GetChildMemberWithName("g")
        .GetValueAsUnsigned(),
        b=valueObject.GetChildMemberWithName("argb")
        .GetChildMemberWithName("components")
        .GetChildMemberWithName("b")
        .GetValueAsUnsigned(),
    )


def generateParameterDescription(
    paramIndex, paramNames, paramValues, dataType, dataSize
):
    return (
        paramNames.CreateChildAtOffset("", paramIndex * dataSize, dataType)
        .GetSummary()
        .replace('"', "")
        + "="
        + paramValues.CreateChildAtOffset("", paramIndex * dataSize, dataType)
        .GetSummary()
        .replace('"', "")
    )


def getParameterAppendString(index):
    if index == 0:
        return ""

    return "&"


def generateURLParameters(valueObject):
    numParameters = (
        valueObject.GetChildMemberWithName("parameterNames")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("numUsed")
        .GetValueAsUnsigned()
    )

    if numParameters == 0:
        return ""

    paramNames = (
        valueObject.GetChildMemberWithName("parameterNames")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("elements")
        .GetChildMemberWithName("data")
    )

    paramValues = (
        valueObject.GetChildMemberWithName("parameterValues")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("elements")
        .GetChildMemberWithName("data")
    )

    dataType = paramNames.GetType().GetPointeeType()
    dataSize = dataType.GetByteSize()

    parameters = "?"

    for index in range(0, numParameters):
        parameters += getParameterAppendString(index) + generateParameterDescription(
            index, paramNames, paramValues, dataType, dataSize
        )

    return parameters


def urlSummary(valueObject, dictionary):
    return (
        '"'
        + (
            valueObject.GetChildMemberWithName("url")
            .GetChildMemberWithName("text")
            .GetChildMemberWithName("data")
            .GetSummary()
            .replace('"', "")
        )
        + generateURLParameters(valueObject)
        + '"'
    )
