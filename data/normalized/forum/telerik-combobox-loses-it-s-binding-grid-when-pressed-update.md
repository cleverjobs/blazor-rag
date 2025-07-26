# Telerik Combobox loses it's binding grid when pressed update

## Question

**ASI** asked on 29 Apr 2021

Hello, I want to use a combobox in a telerik grid, I'm succesfully able to bind and display the data in the combobox as well. however when I select a value from the combobox and press the update button, I get out of the edit mode and the combobox value goes back to null. (placeholder) here is a simplified version of my models public class PageControlsM
{

[Key, DatabaseGenerated(DatabaseGeneratedOption.Identity)]
public int Id { get; set; }

public string ControlCode { get; set; }

[ForeignKey("ControlCode")]
public ControlTypes ControlTypes { get; set; }

} public class ControlTypes
{
[Key]
public string Code { get; set; }

public string ControlName { get; set; }

public string HtmlCode { get; set; }
} and this is my grid implementation: <TelerikGrid Data="@PageControlList" Height="auto" Pageable="true" Sortable="true" Reorderable="true" Resizable="true" PageSize="5" EditMode="GridEditMode.Popup"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Yeni Kontrol Ekle </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field=@nameof(PageControlsM.ControlCode) Width="100%" Title="Kontrol Turu"> <EditorTemplate Context="controlMContext"> @{
if (controlMContext is PageControlsM controlM)
{ <TelerikComboBox Data="@ControlTypesList" TextField="ControlName" ValueField="Code" Width="90%" @bind-Value="controlM.ControlCode" Placeholder="<Seciniz>" ClearButton="true" Filterable="false"> </TelerikComboBox> }
} </EditorTemplate> </GridColumn> <GridCommandColumn Width="100%"> <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="delete"> Delete </GridCommandButton> <GridCommandButton Command="Update" Icon="update" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Save" Icon="cancel" ShowInEdit="true"> Save </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hi Asim, Please try storing the reference to the currently edited row in a field in the view-model like shown in the documentation: [https://docs.telerik.com/blazor-ui/components/grid/templates/editor.](https://docs.telerik.com/blazor-ui/components/grid/templates/editor.) The current code will create a new reference every time the editor template re-renders, and that can happen many times for many reasons, and can thus affect the code in the editor template. Regards, Marin Bratanov
