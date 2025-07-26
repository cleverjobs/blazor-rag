# TelerikGridLayoutRef.GridLayoutRows.Add doesn't exist

## Question

**Joe** asked on 04 Feb 2025

How do I add a new row to the GridLayout through code? Then, I'll need to add a new GridLayoutItem to the new row. Then, I need to add a custom component to that GridLayoutItem.

## Answer

**Hristian Stefanov** answered on 06 Feb 2025

Hi Joel, To dynamically add a new row and a GridLayoutItem containing custom elements to a TelerikGridLayout, you can use conditional rendering in Razor. The TelerikGridLayout does not support direct manipulation of rows or items through code-behind, but you can achieve this by managing the layout through a list of items. Use a list to store your items and iterate over them to render the rows and items dynamically. Here is a brief example that you can use as a starting point: <TelerikGridLayout> <GridLayoutColumns> <GridLayoutColumn Width="200px"> </GridLayoutColumn> <GridLayoutColumn Width="200px"> </GridLayoutColumn> <GridLayoutColumn Width="200px"> </GridLayoutColumn> </GridLayoutColumns> <GridLayoutItems> @foreach (var row in Rows)
{
@foreach (var item in row)
{ <GridLayoutItem> <div style="border: 1px gray solid; padding: 5px;"> @item </div> </GridLayoutItem> }
} </GridLayoutItems> </TelerikGridLayout> <TelerikButton OnClick="AddRow"> Add Row </TelerikButton> @code {
private List<List <string>> Rows=new()
{
new List <string> { "Item 1", "Item 2", "Item 3" }
};

private void AddRow()
{
Rows.Add(new List <string> { $"New Item {Rows.Count + 1}" });
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Joel** commented on 06 Feb 2025

I like it; its a good solution. As an old "desktop" guy I frequently forget that I can manipulate the markup right on the presentation layer.
