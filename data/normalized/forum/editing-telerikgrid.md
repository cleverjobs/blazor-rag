# Editing TelerikGrid

## Question

**Tes** asked on 31 Mar 2023

Is there a way to do in form editing in Telerik Grid for Blazor(TelerikGrid) like the one shown here for Telerik RadGrid? [https://demos.telerik.com/aspnet-ajax/grid/examples/data-editing/edit-form-types/defaultcs.aspx](https://demos.telerik.com/aspnet-ajax/grid/examples/data-editing/edit-form-types/defaultcs.aspx)

### Response

**Dimo** commented on 04 Apr 2023

If the edit form should appear between table rows, it is possible to implement an edit form like this: Use a custom edit form Render it inside the Grid <DetailTemplate> Expand and collapse the edit form (DetailTemplate) via the Grid State.

## Answer

**swathi** answered on 11 Apr 2023

<DetailTemplate> @{ EmpData emp=context as EmpData; <div class="row"> //Add your form </div> } </DetailTemplate> TelerikGrid<EmpData> empGrid { get; set; } private async Task OnEdit(bool value, EmpData empData) { GridState<EmpData> desiredState=new GridState<EmpData>(); isEdit=true; if (isEdit) { desiredState.ExpandedItems=new List<EmpData> { empData }; } else { desiredState.ExpandedItems=null; } await empGrid.SetState(desiredState); }
