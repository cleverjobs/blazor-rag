# support for dynamic editor template for grid column based on object type

## Question

**Har** asked on 10 May 2022

Is there a way to support editing an object (key/value pair) where the value field is an object and can be of a different type for each record? Current issue is error in editor saying: Argument 1: cannot convert from object to string public class KeyValue { public string Key { get; set; } public object Value { get; set; } } <div> <div> <div> <TelerikGrid Data="@KeyValues" @ref="@Grid" EditMode="GridEditMode.Incell" OnStateInit="@((GridStateEventArgs<LabelEntry> args)=> OnStateInitHandler(args))"> <GridColumns> <GridColumn Field="Key" Editable="false" /> <GridColumn Field="Value" Editable="true"> <EditorTemplate> @{ CurrentEntry=context as KeyValue; if (CurrentEntry.Value.GetType().ToString().Equals("System.String", StringComparison.CurrentCultureIgnoreCase)) { <TelerikTextBox @bind-Value=" @CurrentEntry.Value " /> } else if(CurrentEntry.Value.GetType().ToString().Equals("System.Int32", StringComparison.CurrentCultureIgnoreCase)) { <TelerikNumericTextBox @bind-Value="@CurrentEntry.Value"/> } } </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid> </div> </div> </div>

### Response

**Harold** commented on 10 May 2022

I got further with this. I realized that each editor has a specific type it needs to bind with. The TelerikTextBox uses a string and the TelerikNumericTextBox uses numeric type. I added the 2 types to my model and bound to them. I load the appropriate field when receiving the data in the parameter method and move data from the specific type to the normal object field during UpdateHandler. The remaining issue is with the TelerikNumericTextBox that it is not picking up the new value. The editor shows the correct value, but when leaving the editor the grid does not show the new value. The model does have the correct value in both Value and ValueInt fields. The TelerikTextBox works. public class KeyValue
{
public string Key { get; set; }
public object Value { get; set; }
public string ValueString { get; set; }
public int ValueInt { get; set; }
} <div> <div> <div> <TelerikGrid Data="@LabelEntries" @ref="@Grid" ScrollMode="GridScrollMode.Scrollable" Groupable="true" SelectionMode="GridSelectionMode.None" ShowColumnMenu="true" EditMode="GridEditMode.Incell" OnStateInit="@((GridStateEventArgs<LabelEntry> args)=> OnStateInitHandler(args))" OnUpdate="@UpdateHandler"> <GridColumns> <GridColumn Field="DataGroup" Visible="false" Editable="false" /> <GridColumn Field="Name" Editable="false" /> <GridColumn Field="ValueString" Editable="true"> <EditorTemplate> @{ CurrentEntry=context as LabelEntry; if (CurrentEntry.DataType.Equals("string", StringComparison.CurrentCultureIgnoreCase)) { <TelerikTextBox @bind-Value="@CurrentEntry.ValueString" /> } else if (CurrentEntry.DataType.Equals("integer", StringComparison.CurrentCultureIgnoreCase)) { <TelerikNumericTextBox @bind-Value="@CurrentEntry.ValueInt" Format="G"/> } else { <span>@CurrentEntry.DataType not supported</span> } } </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid> </div> </div> </div>

## Answer

**Marin Bratanov** answered on 11 May 2022

Hello Harold, I see you are on the right track with adding checks and appropriate fields. Perhaps you need some logic in the getters and setters of the new fields to have them integrate with the "object" field in a manner suitable for your case. What I would say is that when you have the appropriate typed field, the grid will automatically set the correct editor so you don't have to go through all this (see a live example in this demo ). If nothing else, then you have dedicated fields so you can declare their own columns and the different fields won't be jumbled in the same template if you still do need to use templates. If you truly have to have dynamic objects, I suggest you take a look at these examples about using ExpandoObject type. Regards, Marin Bratanov Progress Telerik

### Response

**Harold** commented on 11 May 2022

I think you are missing a key point of my issue. I only have 2 columns. The key is of type string and does not change between rows. The value field is defined as object because it does change between rows. One row could be a string, another an integer and another a datetime. I'm only showing 2 columns in the grid and the value column needs to have the appropriate editor for the row it is on. If the row has the value as a string then the TextBox editor template is used. For integer the NumericTextBox is used and DatePicker for datetime. The editor template will be mapped to a different field than what is being used to display the data ValueString. When integer the ValueInt field is used and for datetime the ValueDateTime is used (not currently showing this in the above code). Both examples you referenced are using a separate column for the different data types. Not something that would work for my scenario.

### Response

**Marin Bratanov** commented on 12 May 2022

I think you might actually be in need of a so-called Property Grid component: [https://feedback.telerik.com/blazor/1468343-propertygrid-property-grid-vertical-oriented-grid-with-cell-labels-in-column-1](https://feedback.telerik.com/blazor/1468343-propertygrid-property-grid-vertical-oriented-grid-with-cell-labels-in-column-1) If you want to keep using a grid, you have to implement a lot of code in the template. I'd suggest you separate it out into a new component, pass the row model as a parameter, and when it gets updated, fire an event that the parent component where the grid is can handle and update the actual data source. The grid is not designed for a setup like yours, it is designed for repeating rows of the same model (strongly typed) where each column has the same type of values in each row.

### Response

**Harold** commented on 12 May 2022

This sounded promising until I read this: Using the row template takes functionality away from the grid because it no longer controls its own rendering. For example, InCell and Inline editing could not render editors, detail templates will not be available, column resizing, locking, visibility and reordering cannot change the data cells anymore, only the headers, and row selection must be implemented by the app ( example ). What I currently have seems to be working as I need it. I'm able to support the 3 different field types (string, int and datetime) with the appropriate editors. Hopefully, I won't run into other issues.
