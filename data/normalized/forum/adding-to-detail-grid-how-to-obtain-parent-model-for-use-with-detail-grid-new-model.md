# Adding to detail grid ... how to obtain Parent model for use with detail grid new model?

## Question

**RobRob** asked on 24 Dec 2024

Couple of questions: 1. When working Add command for a detail templated grid, the args parameter doesn't provide for the parent model so there is no way to quickly determine values needed from the parent that will populate the child/detail (like primary key values on a composite key). I guess I can manually track "current parent row" via OnRowClick but that seems a bit tedious? Surely there is an easier approach? I was expecting the OnCreate for detail grid to provide parent object/model as part of the event parameters, but that doesn't seem to be the case. 2. When working EditMode=InCell on a detail grid, my expectations was that when I click on an empty grid it would automatically put me into EditMode (Add) for a new detail row, but that doesn't seem to be the case? I have to go thru the OnCreate (which doesn't provide for parent model). I was reading thru your documentation here and here but they weren't useful for is a real world scenario as none of the examples show "Add" case on a detail item that relies on a parent key value to build a composite key when the data is actually saved to a database. Any clean suggestions other than tracking "current parent row" via OnRowClick? Rob.

## Answer

**Hristian Stefanov** answered on 25 Dec 2024

Hi Rob, Accessing Parent Model in Detail Grid The following article shows how you can use data from the parent grid while editing a child grid: Hierarchy Editing. Automatically Entering EditMode in Empty Detail Grid For EditMode=InCell, where you want the grid to automatically enter edit mode when it's empty, you can achieve this by programmatically adding a new row when the grid is detected to be empty. Detect when the detail grid is empty and trigger the addition of a new row. You can handle this logic in the OnRead event or when rendering the grid. Here's a basic example: @code { private bool IsDetailGridEmpty=true; // Flag to check if the grid is empty private void OnReadHandler ( ) { if (IsDetailGridEmpty)
{ // Logic to add a new row AddNewDetailRow();
}
} private void AddNewDetailRow ( ) { // Add a new row to the detail grid's data source }
} This method provides control over when a new row is added, facilitating automatic entry into edit mode. Regards, Hristian Stefanov Progress Telerik

### Response

**Rob** commented on 31 Dec 2024

Hi Hristian, Worked perfectly, thank you! Rob
