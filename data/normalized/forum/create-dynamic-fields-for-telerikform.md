# Create Dynamic Fields For TelerikForm

## Question

**bil** asked on 16 Sep 2021

I have a need to create FormItems dynamically according to an collection of selected paramter types. Example, we have a collection of objects (Abbreviated example below), and each item in the collection represents an input (FormItem in TelerikForm). public class Parameter { public string Label { get; set;} public ParameterTypeEnum ParameterType { get; set } public bool IsRequired { get; set;}
} These types can be string, DateTime, List (ComboBox), int, etc. Then when the Blazor App receives the response from API, it will receive this collection. From that response, I need to create TelerikForm -> FormItems for each item in the collection. Is there a way to pass a collection of "things" into the TelerikForm that it can interpolate into the corresponding FormItems? If not, how can this be accomplished? Thx, B
