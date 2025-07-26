# Filter For GridColumn using <Template>

## Question

**Tim** asked on 28 May 2021

We have a grid as the snippet below. I can't figure out how to put a FilterMenu on the Template(d) columns. The Filter shows up for the "Id" column, which is just a field. Is it possible to have a filter menu for the columns which are Template? <TelerikGrid Data="@_vehicleParts" Pageable="true" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Resizable="true" Reorderable="true" PageSize="20" Navigable="true" OnRead=@OnVehiclePartsRead TotalCount="@TotalCount"> <GridColumns> <GridColumn Width="10%" Field="Id" /> <GridColumn Width="10%" Title="Year"> <Template Context="vehiclePartCtx"> @{
if (vehiclePartCtx is VehiclePart { BaseVehicle: { } } vehiclePart)
{ <span> @vehiclePart.BaseVehicle.YearId </span> }
else
{ <span>??? </span> }
} </Template> </GridColumn>

### Response

**Paul Wood** commented on 11 Jan 2022

I have a very similar scenario where I'd like to search by a field in a ForeignKey related model. <GridColumn Title="Client Name" Field="@nameof(WebInvoice.Booking.Client.ClientName)"> <Template> @{
var item=context as WebInvoice;
@(item.Booking.Client.ClientName)
} </Template> </GridColumn> The data is available from the database in the query that populates the model (as it shows in the Template) so I would have thought I should be able to search by it as well but instead I get an error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Common.Filters.FilterList.TelerikFilterList.GetFilterOperators() which suggests it can't find the data in the model. Changing the top level model to incorporate this related field is of course theoretically possible, but would be a complete pain and wrecks how the EF Core data layer works. Surely this would be a very common requirement? Is there no other workaround?

### Response

**Timothy J** commented on 11 Jan 2022

I think I can help you, but I've had a few drinks. Can you provide more details? What is your controller expecting and returning?

## Answer

**Dimo** answered on 28 May 2021

Hello Timothy, Column filtering, sorting and editing depends on the column Field. Without it, the Grid doesn't know which data to use for these data operations and what is the data type (i.e. what filtering component and operators to use). The Field property for template columns is set in the same way as for non-templated columns. Afterwards, you can still use any other field in the template. [https://demos.telerik.com/blazor-ui/grid/templates](https://demos.telerik.com/blazor-ui/grid/templates) [https://docs.telerik.com/blazor-ui/components/grid/templates/column](https://docs.telerik.com/blazor-ui/components/grid/templates/column) Regards, Dimo Progress Telerik

### Response

**Timothy J** commented on 28 May 2021

>>column Field. Without it, the Grid doesn't know which data to use <<Sure, I was hoping there was some event where we could handle the filtering if not using a field.

### Response

**Dimo** commented on 28 May 2021

Well, I am afraid there is no such event. Even the filter template for the column requires a Field, otherwise it will not render. Out of curiosity, can you describe your use case and why you prefer not to define a Field for the template column?

### Response

**Timothy J** commented on 28 May 2021

Sure, I am trying to filter on a property that is off of the main model, for example Year in the above code

### Response

**Dimo** commented on 31 May 2021

I see. Well, I can only suggest that you create a grid model that includes the base vehicle's year and then you will be able to set it as a field and filter by it. I assume you have already considered that and I hope it is an acceptable.

### Response

**Kevin** commented on 25 May 2022

Is there any reason the filter can't just use the data in the cell itself to filter by? Especially in the case of templates where you'd think that would be the expectation.

### Response

**Dimo** commented on 30 May 2022

@Kevin - Grid data operations rely on strongly-typed model properties. This approach allows a non-ambiguous method for filtering and sorting. Column templates add some important challenges - the data type of the content becomes ambiguous the template content may not be suitable for filtering at all (e.g. an image, a child component, etc.) Even if the above two limitations are resolved by additional column properties, the Grid will still have to extract the template content from the UI, and generate a new data collection to work with it in the business layer. Last but not least, filtering itself is not done by the Grid component (even when it's databound via the Data parameter). The desired functionality will require tight coupling between parts of our product, which are detached as a fundamental software design decision. Custom filtering is possible and easier to implement by the developer via the OnRead event, the Grid State and/or filter templates. Here is a related Grid search example that shows how to create custom filter descriptors in the Grid state.
