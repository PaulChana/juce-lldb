import lldb


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        "type summary add -x juce::URL -F juce_url.url_summary -w juce"
    )


def generate_parameter_description(
    paramIndex, parameter_names, parameter_values, data_type, data_size
):
    return (
        parameter_names.CreateChildAtOffset("", paramIndex * data_size, data_type)
        .GetSummary()
        .replace('"', "")
        + "="
        + parameter_values.CreateChildAtOffset("", paramIndex * data_size, data_type)
        .GetSummary()
        .replace('"', "")
    )


def get_parameter_append_string(index):
    if index == 0:
        return ""

    return "&"


def url_parameter_parts(value_object):
    num_parameters = (
        value_object.GetNonSyntheticValue()
        .GetChildMemberWithName("parameterNames")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("numUsed")
        .GetValueAsUnsigned()
    )

    parameter_names = (
        value_object.GetNonSyntheticValue()
        .GetChildMemberWithName("parameterNames")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("elements")
        .GetChildMemberWithName("data")
    )

    parameter_values = (
        value_object.GetNonSyntheticValue()
        .GetChildMemberWithName("parameterValues")
        .GetChildMemberWithName("strings")
        .GetChildMemberWithName("values")
        .GetChildMemberWithName("elements")
        .GetChildMemberWithName("data")
    )

    data_type = parameter_names.GetType().GetPointeeType()
    data_size = data_type.GetByteSize()

    return num_parameters, parameter_names, parameter_values, data_type, data_size


def generate_url_parameters(value_object):
    (
        num_parameters,
        parameter_names,
        parameter_values,
        data_type,
        data_size,
    ) = url_parameter_parts(value_object)

    if num_parameters == 0:
        return ""

    parameters = "?"

    for index in range(0, num_parameters):
        parameters += get_parameter_append_string(
            index
        ) + generate_parameter_description(
            index, parameter_names, parameter_values, data_type, data_size
        )

    return parameters


def url_summary(value_object, dictionary):
    return (
        '"'
        + (
            value_object.GetChildMemberWithName("url")
            .GetChildMemberWithName("text")
            .GetChildMemberWithName("data")
            .GetSummary()
            .replace('"', "")
        )
        + generate_url_parameters(value_object)
        + '"'
    )
