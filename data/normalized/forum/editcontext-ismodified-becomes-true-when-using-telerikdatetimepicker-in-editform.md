# EditContext.IsModified() becomes true when using TelerikDateTimePicker in EditForm

## Question

**Joe** asked on 11 Apr 2024

I have a Telerik Grid and EditForm side-by-side on a page. The EditForm displays the selected object upon clicking a grid row. Below is an excerpt of my custom form component. @typeparam TEntity where TEntity : class, IEntity, new() <div> <TelerikGrid @ref="GridRef" Pageable="true" Sortable="true" Resizable="true" ShowColumnMenu="true" Reorderable="true" PageSize="50" SelectionMode="@GridSelectionMode.Single" SelectedItems="@_selectedItems" SelectedItemsChanged="@((IEnumerable<TEntity> list)=> OnGridSelectedItemsChanged(list))" OnRowClick="@OnGridRowClick" OnRead="GetGridData" EnableLoaderContainer="true"> @* toolbar, columns, etc. *@</TelerikGrid> <EditForm EditContext="@_editContext" OnSubmit="OnSubmitAsync"> <TelerikDateTimePicker Placeholder=" " Value="(DateTime?)PropertyValue" ValueExpression="ValueExpression<DateTime?>()" ValueChanged="(DateTime? val)=> OnValueChanged(val)" Readonly="true"> </TelerikDateTimePicker> </EditForm> </div> @code {
private EditContext? _editContext;
private IEnumerable <TEntity> _selectedItems=Enumerable.Empty <TEntity> ();
private TEntity? _selectedItem;

[CascadingParameter] public TEntity? Entity { get; set; }

protected override void OnInitialized()
{
_editContext=new(Entity);
_editContext.OnFieldChanged +=OnFieldChanged!;
}

// Override the grid's built-in row selection by handling the SelectedItemsChanged event. Do not execute any logic in it to let the OnGridRowClick handle the selection.
// [https://docs.telerik.com/blazor-ui/knowledge-base/grid-select-or-deselect-item-on-row-click](https://docs.telerik.com/blazor-ui/knowledge-base/grid-select-or-deselect-item-on-row-click)
private void OnGridSelectedItemsChanged(IEnumerable <TEntity> selectedList)
{
}

private async Task OnGridRowClick(GridRowClickEventArgs args)
{
var currItem=args.Item as TEntity;

if (currItem?.Id==_selectedItem?.Id) return;

var discardChanges=await ConfirmDiscardFormChangesAsync();

if (!discardChanges) return;

_selectedItems=new[] { currItem };
_selectedItem=_selectedItems.First();
}

private async Task OnValueChanged(object? value)
{
// not getting fired when grid's selected item is changed, which is good
}

private void OnFieldChanged(object sender, FieldChangedEventArgs args)
{
// gets fired when grid's selected item is changed
// _editContext.IsModified() is true here
}
} Whenever the form displays an item upon clicking a different row with DateTime field value different from the previously selected one, the EditContext's IsModified() becomes true. This is not the case when I replace the TelerikDateTimePicker with Blazor's InputDate component.
