# Dynamically change Editor Type based on type passed at runtime

## Question

**Lor** asked on 04 Jun 2024

Hi, I would like to know if the ability of Telerik Form components have the ability to change based on the passed type also at runtime. Ideally, I would like to have an editable field inside a Telerik Grid that is declared as object/dynamic and populated at runtime with values of different primitive types. Visually translating bool values into checkboxes, int values into spinboxes and string values into textboxes. Would that be possible? here the specific piece of code I'm working on: <TelerikGrid Data="PGEManagementUtility.GetPGEPropertyValues()" EditMode="GridEditMode.Incell" OnUpdate="OnPropertyValueSet">
<GridColumns>
<GridColumn Field="@nameof(PGEPropertyValue.PropertyName)" Title="Name" Editable="false" />
<GridColumn Field="@nameof(PGEPropertyValue.DataType)" Title="Data Type" Editable="false" />
<GridColumn Field="@nameof(PGEPropertyValue.Value)" Title="Value" />
</GridColumns>
</TelerikGrid> PGEPropertyValue.Value would be declared as object or dynamic based on what works best in this case. Kind Regards, Lorenzo

## Answer

**Nansi** answered on 07 Jun 2024

Hello Lorenzo, I can propose the following options to handle the EditorType depending on the type of a dynamic field: Set a runtime EditorType 1. Create a nullable GridEditorType variable GridEditorType? EditorTypeVar { get; set; } 2. Set the variable as EditorType parameter of the dynamic column <GridColumn Field=@nameof(PGEPropertyValue.Value) Title="Value" EditorType="@EditorTypeVar" /> 3. Set the value of the EditorType depending on the field type, for example in the OnEdit event handler async Task EditHandler ( GridCommandEventArgs args ) { var field=args.Field; var dynamicObjectCellType=field.GetType(); //set the EditorType if (dynamicObjectCellType==typeof ( bool ))
{
EditorTypeVar=GridEditorType.CheckBox;
}
} Bind the Grid to an expando object and dynamically set the FieldType You can review our knowledge base article on how to bind the Grid to an expando object. With this approach, you won't need to handle the EditorType. It depends on the type of the dynamic object. However, if the PGEPropertyValue.Value property is nullable you need to note the section related to the editing. Regards, Nansi Progress Telerik

### Response

**Lorenzo** answered on 07 Jun 2024

Hi @Nansi, I've tried both approaches but they seems to be tied to a single column value. Do you think it would be possible to have different editor types row by row? This is because in this specific piece of code we are assigning property values, so we could have one property that accepts a boolean value, while the next one will accept string or int. Would it be possible? Best Regards, Lorenzo

### Response

**Lorenzo** commented on 11 Jun 2024

I've changed the grid to be like the following: <TelerikGrid Data="PGEManagementUtility.GetPGEPropertyValues()"> <GridColumns> <GridColumn Field="@nameof(PGEPropertyValue.PropertyName)" Title="Name" Editable="false" /> <GridColumn Field="@nameof(PGEPropertyValue.DataType)" Title="Data Type" Editable="false" /> <GridColumn Field="@nameof(PGEPropertyValue.Value)" Title="Value"> <Template> @{
var item=context as PGEPropertyValue;

switch (item?.Value)
{
case bool b: <TelerikCheckBox Value="b" ValueChanged="@((bool value)=> OnBoolPropertyValueSet(item.PropertyName, value))"> </TelerikCheckBox> break;
case double d: <TelerikNumericTextBox Value="d" ValueChanged="@((double value)=> OnDoublePropertyValueSet(item.PropertyName, value))"> </TelerikNumericTextBox> break;
case int i: <TelerikNumericTextBox Value="i" ValueChanged="@((int value)=> OnIntPropertyValueSet(item.PropertyName, value))"> </TelerikNumericTextBox> break;
case string s: <TelerikTextBox Value="s" ValueChanged="@((string value)=> OnStringPropertyValueSet(item.PropertyName, value))"> </TelerikTextBox> break;
default:
break;
}
} </Template> </GridColumn> </GridColumns> </TelerikGrid> Using the template gives me more granular control over the Grid items. Do you see any cons using this approach?

### Response

**Nansi** answered on 12 Jun 2024

Hi Lorenzo, I apologize if I misunderstood your initial request. If you are searching for a solution to render the Grid cells differently for each cell, you are on the right track with the column template. With this approach, the CRUD operations depend on the component used in the template and not on the Grid. While this seems to be a valid implementation, it is not expected for the Grid to work with different types of values on each row. With this approach, issues can occur when filtering and sorting the Grid data in this column. Regards, Nansi Progress Telerik
