/*******************************************************************************
 The block below describes the properties of this PIP. A PIP is a short snippet
 of code that can be read by the Projucer and used to generate a JUCE project.

 BEGIN_JUCE_PIP_METADATA

  name:             LLDBTest
  version:          1.0.0
  vendor:           Paul Chana
  website:          git@github.com:PaulChana/juce-lldb.git
  description:      This is a simple test file for my LLDB scripts

  dependencies:     juce_core, juce_graphics, juce_gui_basics
  exporters:        clion, xcode_mac

  type:             Console
  mainClass:        main.cpp

 END_JUCE_PIP_METADATA

*******************************************************************************/

#pragma once


void string ()
{
    juce::String helloWorld = "Hello world";
    juce::String emptyString = "";
}

void file ()
{
    juce::File emptyFile;
    juce::File path =
        juce::File::getSpecialLocation (juce::File::SpecialLocationType::tempDirectory);
}

void uuid ()
{
    juce::Uuid nullUuid = juce::Uuid::null ();
    juce::Uuid uuid;
}

void colour ()
{
    juce::Colour emptyColour = juce::Colours::transparentBlack;
    juce::Colour red = juce::Colours::red;
    juce::Colour green = juce::Colours::green;
    juce::Colour blue = juce::Colours::blue;
    juce::Colour colour (uint8 (128), uint8 (64), uint8 (75), uint8 (200));
}

void rectangle ()
{
    juce::Rectangle<int> emptyIntRect;
    juce::Rectangle<int> filledIntRect (10, 12, 20, 25);

    juce::Rectangle<float> emptyFloatRect;
    juce::Rectangle<float> filledFloatRect (10.25f, 12.1f, 20.225f, 25.6543f);
}

void stringArray ()
{
    juce::StringArray emptyArray;
    juce::StringArray singleArray = {"foo"};
    juce::StringArray multipleArray = {"foo", "bar", "funky", "drummer"};
}

void stringPairArray ()
{
    juce::StringPairArray emptyPairs;
    juce::StringPairArray singleParameter;
    singleParameter.set ("foo", "bar");

    juce::StringPairArray multiParameter;
    multiParameter.set ("foo", "bar");
    multiParameter.set ("funky", "drummer");
}

void url ()
{
    juce::URL emptyURL;
    juce::URL url ("https://www.github.com");

    juce::StringPairArray parameters;
    parameters.set ("foo", "bar");
    parameters.set ("funky", "drummer");
    juce::URL urlWithParameters = juce::URL ("https://www.github.com").withParameters (parameters);
}

void memory ()
{
    juce::MemoryBlock emptyMemory;
    juce::MemoryBlock filledMemory;
    filledMemory.setSize (strlen ("donut-eating-programmer"), false);
    filledMemory.copyFrom ("donut-eating-programmer", 0, strlen ("donut-eating-programmer"));
}

void component ()
{
    Component component;
    Component component2;
    juce::TextButton button ("foobar");

    component.setBounds (0, 0, 100, 100);
    component2.setBounds (10, 12, 5, 8);
    button.setBounds (20, 25, 5, 10);
}

void vars ()
{
    juce::var emptyVar;
    juce::var stringVar ("foobar");
    juce::var intVar (10);
    juce::var boolVar (true);
    juce::var floatVar (20.0);
}

void point ()
{
    juce::Point<int> emptyIntPoint;
    juce::Point<int> filledIntPoint (10, 15);

    juce::Point<float> emptyFloatPoint;
    juce::Point<float> filledFloatPoint (10.f, 15.f);
}

void range ()
{
    juce::Range<int> emptyIntRange;
    juce::Range<int> filledIntRange (10, 15);

    juce::Range<float> emptyFloatRange;
    juce::Range<float> filledFloatRange (10.f, 15.f);
}

void result ()
{
    auto ok = juce::Result::ok ();
    auto failed = juce::Result::fail ("because");
}

void relativeTime ()
{
    RelativeTime emptyTime;
    RelativeTime relativeTime (50);
}

void time ()
{
    juce::Time emptyTime;
    juce::Time now = juce::Time::getCurrentTime ();
}

int main (int argc, char * argv [])
{
    string ();
    file ();
    uuid ();
    url ();
    colour ();
    rectangle ();
    memory ();
    stringArray ();
    stringPairArray ();
    component ();
    vars ();
    point ();
    range ();
    result ();
    relativeTime ();
    time ();

    return 0;
}
