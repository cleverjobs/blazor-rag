# Component similar to the "Properties" window in Visual Studio.

## Question

**Kri** asked on 17 Nov 2022

I need a component that allows the user to enter multiple key-values. Similar to the "properties" window in Visual Studio. The challenge is that "value" is object type because values ​​can be of different types. I wanted to implement this using a Grid component with the InCell editing option. The problem, however, is the unspecified "value" type... The edit cell would have to render a different edit component depending on the "value" type. Do you have any idea how to accomplish this? My test code: <TelerikGrid Data=@MyData EditMode="@GridEditMode.Incell"> <GridColumns> <GridColumn Field=@nameof(TextValue.Text) Title="Text" Editable="false" /> <GridColumn Field=@nameof(TextValue.Value) Title="Value" Editable="true" /> </GridColumns> </TelerikGrid> @code { TextValue[] MyData=new TextValue[] { new TextValue { Text="test1", Value="test" }, new TextValue { Text="test2", Value=false }, new TextValue { Text="test3", Value=3 } }; public class TextValue { public string Text { get; set; } public object Value { get; set; } } }
