# Telerik Blazor grid style

## Question

**VHA** asked on 14 Aug 2022

I am looking for more help/demos on styling the Telerikgrid. I would like to know: How do I change the background color of rows? '.k-grid tr.k-alt' changes the alternate row, but setting '.k-grid tr' isn't applied when ran. When ran '.k-grid tr' is set to inherit. I can change the style within the master theme, but the master row background stays white, even though the debugger shows that it should be a different color. How do I change the background color dependent on row data? For example, perhaps I want future transactions to be shades of blue. How do I hide gridcommandbuttons based on the current row's data? I have set the gridcommandbutton size to "small" to decrease the row height. I have tried changing the font size using the styling below, but this only affects the display rows and not the new/edit row. How do I change the size of the new/edit row? @page "/GeneralLedgerGridEntry" <style> div.smallerFont, div.smallerFont.k-filtercell *
{ font-size: 10px;
} div.smallerFont.k-dropdown.k-header.k-dropdown-operator { width: calc ( 8px + 2em )!important;
} div.smallerFont.k-grid-edit-cell.k-grid-content input { font-size: 10px; line-height: 0.05; padding: 0.25rem 0.25rem;
} div.smallerFont.k-grid-container { font-size: 10px; line-height: 0.05; padding: 0.25rem 0.25rem;
} div.smallerFont.k-grid.k-grid-content.k-grid-content { font-size: 10px; line-height: 0.05; padding: 0.25rem 0.25rem;
}.k-grid tr { border-color: rgba ( 84, 122, 218, 0.39 );
}.k-grid tr.k-alt { background-color: rgba ( 84, 122, 218, 0.8 );
} </style> <div class="row"> <div class="sm-col-4"> <h3> Select Account: </h3> </div> <div class="sm-col-8"> <TelerikComboBox Data="@AccountList" @bind-Value="chosenAccountID" ValueField="@nameof(VM_AccountsGridEntry.AccountID)" TextField="@nameof(VM_AccountsGridEntry.AccountDescription)" Id="cmbAccountSelect" OnChange="ChangeSelectionChoice"> </TelerikComboBox> </div> </div> @if (ShowGrid)
{ <EditForm EditContext="@_formDataContext" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit"> <h5 class="card-title"> @FormTitle </h5> <div class="p-2"> <DataAnnotationsValidator /> <ValidationSummary /> </div> </EditForm> <TelerikGrid Data=@Griddata Class="smallerFont" EditMode="@GridEditMode.Inline" Pageable="true" OnCreate="@CreateItem" OnUpdate="@UpdateItem" OnDelete="@DeleteItem" RowHeight="1"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add Transaction </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.TransactionID)) Title="TransactionID" Visible="false" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.TransactionDate)) Editable=true width="15em" DisplayFormat="{0:dd MMM yyyy}" Title="Transaction Date" Visible="true" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.CheckNumber)) Editable=true Title="Check #" width="10em" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.PayeeDescription)) Title="Payee Description" width="28em" Visible="true"> <Template> @{
ProductToEdit=context as VM_GeneralLedgerGridEntry ?? new VM_GeneralLedgerGridEntry(); <TelerikTextBox Size="small" Enabled="false" @bind-Value="@ProductToEdit.PayeeDescription" /> if ((ProductToEdit.CategoriesID==1) && (ProductToEdit.PayeeID==1))
{
//Hide gridcommandbuttons
}
} </Template> <EditorTemplate> @{
ProductToEdit=context as VM_GeneralLedgerGridEntry ?? new VM_GeneralLedgerGridEntry(); <TelerikDropDownList Size="Small" Data="@PayeeList" @bind-Value="@ProductToEdit.PayeeID" Width="100%" TextField="PayeeDescription" ValueField="PayeeID" Filterable="true" FilterOperator="StringFilterOperator.Contains"> </TelerikDropDownList> <TelerikValidationMessage For="@(()=> ProductToEdit.PayeeID)" /> } </EditorTemplate> </GridColumn> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.Memo)) Title="Memo" Visible="true" width="20em" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.CategoryDisplayDescription)) Editable=true Title="Category" width="28em" Visible="true"> <EditorTemplate> @{
ProductToEdit=context as VM_GeneralLedgerGridEntry ?? new VM_GeneralLedgerGridEntry(); <TelerikDropDownList Size="Small" Data="@CategoryList" @bind-Value="@ProductToEdit.CategoriesID" Width="100%" TextField="CategoryDisplayDescription" ValueField="CategoriesID" Filterable="true" FilterOperator="StringFilterOperator.Contains"> </TelerikDropDownList> <TelerikValidationMessage Class="smallerFont" For="@(()=> ProductToEdit.CategoriesID)" /> } </EditorTemplate> </GridColumn> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.Payment)) Editable=true Title="Payment" DisplayFormat="{0:C}" width="15em" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.Deposit)) Title="Deposit" Visible="true" DisplayFormat="{0:C}" width="15em" /> <GridColumn Field=@(nameof(VM_GeneralLedgerGridEntry.Current_Balance)) Title="Account Balance" Editable="false" Visible="true" DisplayFormat="{0:C}" width="13em" /> <GridCommandColumn Width="15em"> <GridCommandButton Id="btnEdit" Command="Edit" Icon="edit" Size="Small"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="delete" Size="Small"> Delete </GridCommandButton> <GridCommandButton Command="Save" Icon="save" Size="Small" ShowInEdit="true" OnClick="@CreateItem"> Save </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true" Size="Small"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> }
else
{ <LoadingAnimation LoadingText="Loading Data"> </LoadingAnimation> }

## Answer

**Dimo** answered on 17 Aug 2022

Hello Scott, Here are some pointers on your questions:.k-grid tr should work for row background, but is too general combinator and will affect more rows than it should (for example, header rows). Use something more specific like.k-grid .k-grid-content .k-master-row To change the row background conditionally, use the OnRowRender event to apply custom row CSS classes To hide command buttons, use conditional statements inside the GridCommandColumn RenderFragment - see how the Delete buttons are hidden on some rows To style edit rows, use the.k-grid-edit-row class selector As always in such scenarios, the browser's DOM inspector and knowledge about CSS specificity are your best friends. Regards, Dimo

### Response

**VHAHTMInfrastructure** commented on 23 Aug 2022

Thank you, Dimo! Those resources were very helpful!
