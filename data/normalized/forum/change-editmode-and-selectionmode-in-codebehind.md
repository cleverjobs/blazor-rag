# Change EditMode and SelectionMode in CodeBehind

## Question

**Mic** asked on 21 May 2022

Is it possible to change the EditMode during Runtime in C#? please see the following code - MyGrid stays in Incell Editmode. <Toolbar> <ToggleButton OnClick=@StartEditMode/> <ToggleButton OnClick=@StartSelectionMode/> </Toolbar> <Grid @ref="_myGrid" EditMode=Incell>... columns.... </Grid> </> Grid

StartEditMode()
{
_myGrid.EditMode=GridEditMode.Incell;
_myGrid.SelectionMode=GridSelectionMode.None;
_myGrid.SelectedItemsChanged=EventCallback<IEnumerable <DataItem>>.Empty;
}

StartSelectionMode()
{
_myGrid.EditMode=GridEditMode.None;
_myGrid.SelectionMode=GridSelectionMode.Multiple;
_myGrid.SelectedItemsChanged=Microsoft.AspNetCore.Components.EventCallback.Factory.Create(this, (IEnumerable <DataItem> items)=> OnSelectionChanged(items.ToArray()));
}

OnSelectionChanged(DataItem[] items)
{
... do something here
}

## Answer

**Marin Bratanov** answered on 22 May 2022

Hello Michael, In Blazor, you should change the value of the field that the component parameter uses. Typically, references are used for calling methods and setting properties via them is not the way to alter the component settings - using the view-model is the way to do that. Here is a basic example I made for you, based off on one of the editing snippets in the docs: [https://blazorrepl.telerik.com/mGOJcwPc50qT6CWJ15,](https://blazorrepl.telerik.com/mGOJcwPc50qT6CWJ15,) and that's the key parts only: <TelerikGrid Data=@MyData EditMode="@editMode". . . .
</TelerikGrid>

<TelerikButton OnClick="@ToggleEditMode">ToggleEditMode</TelerikButton>

@code{ GridEditMode editMode { get; set;}=GridEditMode.Inline; void ToggleEditMode ( ) { switch (editMode)
{ case GridEditMode.Inline:
editMode=GridEditMode.Incell; break; case GridEditMode.Incell:
editMode=GridEditMode.Inline; break;
}
}
} Regards, Marin Bratanov Progress Telerik
