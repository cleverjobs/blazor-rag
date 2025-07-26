# How to conditionally display grid cell data based upon the row context?

## Question

**Dav** asked on 21 Jun 2022

Situation: I have an EF table being displayed in a Telerik Grid. There is a command field which when clicked goes to a page to an action page that consumes the the record for that row. I want the button to display in rows that meet a condition in that row's data. Status (an enum) is the field that will if a certain value the condition is true. So I guess I need access to row's context. ??? <GridColumn Field="@(nameof(RecordResult.Status))" Title="Status" Width="80px" /> <GridCommandColumn Title="Update" Width="80px"> <GridCommandButton Command="MyOwnCommand" Icon="Information" OnClick="@MyCustomCommandHandler"> Claim </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid>

### Response

**David** commented on 22 Jun 2022

I have tried using context as per Blazor Grid - Overview <GridColumn Field="@nameof(ProductDto.Discontinued)" Width="135px" Title="Discontinued" Editable="false" TextAlign="@ColumnTextAlign.Center"> <Template> @{
var product=context as ProductDto;

if (product.Discontinued.GetValueOrDefault())
{ <span class="k-badge k-badge-md k-badge-solid k-badge-rounded k-badge-error"> Discontinued </span> }
else
{ <span class="k-badge k-badge-md k-badge-solid k-badge-rounded k-badge-success"> Available </span> }
} </Template> </GridColumn My code: <GridColumn Field="@(nameof(RecordResult.Status))" Title="Claims"> <template> @{
var product=context as RecordResult;
if (product.Status==recordStatus.current)
{ <GridCommandButton Command="MyOwnCommand" Icon="Information" OnClick="@MyCustomCommandHandler"> Claim </GridCommandButton> }
else
{ <span class="k-badge k-badge-md k-badge-solid k-badge-rounded k-badge-success"> &nbsp; </span> }
} </template> </GridColumn> But compiler doesn't like the context entity. The name 'context' does not exist in the current context

### Response

**David** commented on 23 Jun 2022

Did an upgrade to V3.4.0 . The following now works. <GridColumn Field="@(nameof(RecordResult.Status))" Title="Status" Width="80px" /> <GridColumn Field="@(nameof(RecordResult.Status))" Title="Claim" Width="80px"> <Template> @{
var recordResult=context as RecordResult;
if (recordResult.Status==recordStatus.current)
{ <TelerikButton Icon="Information" @onclick="()=> MyCustomCommandHandler(recordResult)"> Claim </TelerikButton> }
else
{

}
} </Template> </GridColumn> Ps: Could put conditional in Template in a CommandField.

## Answer

**David** answered on 23 Jun 2022

As per my last comment.
