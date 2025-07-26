# Dynamically change the Editor Template when another column's value changes

## Question

**Dav** asked on 10 Jan 2024

Hello, I have a grid with InLine editing. The first column in the grid is a dropdownlist. The second column has a switch statement that will show a different control based on the selected value of the dropdown. I have an OnChange() method on the dropdown and I call StateHasChanged() in that method, but the switch statement never gets called. How can I get the second column in the grid change based on the first column changing? Thanks, Dave

### Response

**David** commented on 11 Jan 2024

NVM. There was a bug that made it appear this was not working. It's working fine. Dave

### Response

**Hristian Stefanov** commented on 11 Jan 2024

Hi Dave, Thank you for updating us on the situation. From the provided information, it seems that everything is working fine now. I'm glad to hear that. If we can assist with more information, let me know. Kind Regards, Hristian

### Response

**Rama** commented on 23 Jan 2024

Hello, I have same exact requirement? Is there a sample available in the Telerik Wesbite? If not, I really appreciate if you post the solution. I am using Telerik Blazor Grid. In that, The first EditorTemplate column has dropdownlist (Guid and Name), when user selects a Name, OnChange event, we need to get the Guid from the selected item and find the matching Guid from another array list to get the description and update the second EditorTemplate column value (textbox) with description. Thanks in advance. Thanks Ram

### Response

**David** commented on 23 Jan 2024

Hey Rama, Here is a code snippet showing the basics of how I got this to work. I hope it helps Dave <TelerikGrid Data="@myData" TItem="MyObject" EditMode="GridEditMode.Inline" Data="@gridData">
<GridColumns>
<GridColumn Filterable="false" Title="Field 1>
<Template>
@{
if (context is MyObject myObject)
{
<span>myObject.Field1</>
} }
</Template>
<EditorTemplate>
@{
if (context is MyObject myObject)
{
<TelerikDropDownList @bind-Value=" myobject.Field1 " Data=" @DropDownData " OnChange=" Field1Changed "></TelerikDropDownList>
}
}
</EditorTemplate>
</GridColumn>
<GridColumn Field=" @nameof(MyObject.Field2) FieldType="typeof(string)" Filterable="false" Title="Field 2"></GridColumn>
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true" OnClick="GridUpdated">Update</GridCommandButton>
<GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil">Edit</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</TelerikGrid>

@{
SourceFieldChanged( object newValue)
{ if (newValue is int id)
{ // update field 2 here }
} class MyObject { int Field 1 { get; set;} string Field2 { get; set;}
}
}

### Response

**Rama** commented on 23 Jan 2024

Thanks Dave, I would look into this and let you know if there are any questions.
