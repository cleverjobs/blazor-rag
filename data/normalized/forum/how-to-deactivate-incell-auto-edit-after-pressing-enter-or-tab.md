# How to deactivate Incell auto edit after pressing ENTER or TAB

## Question

**Est** asked on 22 Feb 2024

After editing a cell, if I press ENTER it automatically starts editing the cell below; if I press TAB it automatically starts editing the cell at the right: After pressing TAB: I need to deactivate that behavior: Press ENTER or TAB should update the target cell and stop editing any other cell: I tried using Navigable="false" with no results. How can I achieve this? This is the example code: <TelerikGrid Data="Items" Navigable="false" EditMode="GridEditMode.Incell" Width="400px">
<GridColumns>
<GridColumn Field="Name" Title="Name" />
<GridColumn Field="Phone" Title="Phone" />
<GridColumn Field="Address" Title="Address" />
</GridColumns>
</TelerikGrid>

@code { private List<Item> Items=new ()
{ new Item {Name="User1", Phone="1111111", Address="Address1" }, new Item {Name="User2", Phone="2222222", Address="Address2" }, new Item {Name="User3", Phone="3333333", Address="Address3" }
}; private class Item { public string Name { get; set; } public string Phone { get; set; } public string Address { get; set; }
}
}

## Answer

**Dimo** answered on 23 Feb 2024

Hello Esteban, The observed behavior is identical to Excel. It is possible to prevent it with custom coding like this: Use an EditorTemplate that uses @onkeydown and stops its propagation. Exit edit mode programmatically in the custom @onkeydown handler. Example: [https://blazorrepl.telerik.com/GyYwQxbc31HIEllb30](https://blazorrepl.telerik.com/GyYwQxbc31HIEllb30) Razor <GridColumn Field="@nameof(SampleModel.Name)"> <EditorTemplate> @{ var editItem=(SampleModel)context; } <div @onkeydown:stopPropagation @onkeydown="@( (KeyboardEventArgs args)=> OnEditorKeyDown(args, editItem) )"> <TelerikTextBox @bind-Value="@editItem.Name" /> </div> </EditorTemplate> </GridColumn> C# private async Task OnEditorKeyDown ( KeyboardEventArgs args, SampleModel editItem ) { if (args.Key=="Enter" ) { var gridState=GridRef!.GetState();

OnGridUpdate( new GridCommandEventArgs() { Field=nameof (SampleModel.Name), Item=editItem });

gridState.EditField=null;
gridState.EditItem=null!;
gridState.OriginalEditItem=null!; await GridRef.SetStateAsync(gridState);
}
} Regards, Dimo Progress Telerik
