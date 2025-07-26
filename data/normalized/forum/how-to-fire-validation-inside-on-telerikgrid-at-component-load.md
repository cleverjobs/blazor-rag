# How to fire Validation inside on TelerikGrid at component load?

## Question

**Arn** asked on 01 Dec 2023

Hi, I use a TelerikGrid relying on FluentValidator. Validation works fine when users manually edit a grid value. But I do not manage to trigger it after the grid loads (so users can view possible incorrect values after DB loading). I have tried 2 different ways, both without success. 1) using validation at Grid level. Well I basically replicated your demo: [https://docs.telerik.com/blazor-ui/components/grid/editing/validation](https://docs.telerik.com/blazor-ui/components/grid/editing/validation) 2) using a TelerikForm inside the (only cell) that needs to be validated. Something like this: <TelerikGrid @ref="@_gridRef" TItem="MyDto" Data="@MyItems"> <GridSettings> <GridValidationSettings> <ValidatorTemplate> <FluentValidationValidator Validator=@_validator /> </ValidatorTemplate> </GridValidationSettings> </GridSettings> <GridColumns> [...] <GridColumn Field="@nameof(MyDto.MyProp)" Title="My Prop" Context="ctx"> <Template> <EditForm Model="@ctx"> <FluentValidationValidator Validator=@_validator/> <TelerikTextBox @bind-Value="@((ctx as MyDto).MyProp)" /> </EditForm> </Template> </GridColumn> </GridColumns> </TelerikGrid> In both cases, the Textbox turns red if the users types an incorrect value. But it does not if the grid load an incorrect value from the DB and display it. Any suggestion to make this work?

## Answer

**Svetoslav Dimitrov** answered on 06 Dec 2023

Hello Arnaud, We have an open feature request to trigger the Grid's validation from code. I have added your Vote for it and you can click the Follow button to receive email updates when the status changes. Out of curiosity, why would you save incorrect values to the database? Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Arnaud** answered on 06 Dec 2023

Hi Svetoslav, Thx, let's hope you ll be able to fix it. As per your question, well, we have improved the the validation rules over the past years. IE some email regex are stronger now, or some fileds that used to be optional are now compulsory. So some old records in the DB are not up to date wit the new standards. I want the user to see what is now wrong when he loads such an old record. Have a gd day. A

### Response

**Svetoslav Dimitrov** commented on 11 Dec 2023

Hello Arnaud, I might have misunderstood your initial question, is it that you want to validate the entire Grid at the same time? If that is the case, I am sorry to report that this will not be possible. The Telerik Grid for Blazor is a UI component and is not able to serve as a "batch validator" of the database. The Grid's validation can ensure that the user input passes your validation logic, but cannot validate the entire dataset.

### Response

**Arnaud** answered on 11 Dec 2023

Hello Svetoslav, No, not the whole grid. Rather a line based validation. Well in my very case, I actually only need to validate a single field per row. If we manage to validate once the user leaves the cell, there must be a way to validate the cells on load? Have a gd day A

### Response

**Svetoslav Dimitrov** commented on 14 Dec 2023

Hello Arnaud, Let me ask one more question so that I make sure we are on the same page. Lets say that you have a Grid with 200 rows (which are essentially 200 forms). in 15 rows you have a field that does not meet the validation rules. What is the UX that you want to see in the Grid for editing?

### Response

**Arnaud** commented on 14 Dec 2023

Hi Stevoslav, In this case, the DB loads the 200 records from the DB. The page attempts to render them into the telerik grid. I would like that the validation process detects that row 15 is invalid and displays it in red . In my case, only one cell is concerned by the validator so there should be only one cell to display in red, but if you offer me a solution that displays in red the whole line, that will be faire enough. Have a gd day A

### Response

**Svetoslav Dimitrov** commented on 18 Dec 2023

Hello Arnaud, The Grid exposes the OnRowRender and OnCellRender events. These events fire when the rows and columns render. You can use them to attach a custom CSS class to a specific row/cell. In your case, you can Write some custom logic to validate the entire collection Extract the IDs of the DTOs that have invalid values Store the IDs in a collection Use the events to add custom formatting Here is a code snippet where you can see the concept. I have hardcoded 4 rows as invalid. <style>.row-invalid-value.k-master-row { background-color: red;
}.row-invalid-value.k-table-alt-row.k-master-row { background-color: red;
} </style> <TelerikGrid Data="@MyData" Height="446px" Pageable="true" OnRowRender="@OnRowRenderHandler"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Width="200px" Title="Employee Name" /> <GridColumn Field="@(nameof(SampleData.Team))" Width="200px" Title="Team" /> </GridColumns> </TelerikGrid> @code {
//Use some custom logic to populate this list with the Ids of the DTO that have invalid values
private List <int> InvalidRowsId { get; set; }=new List <int> {
1, 4, 9, 10
};

void OnRowRenderHandler(GridRowRenderEventArgs args)
{
var item=args.Item as SampleData;

if(InvalidRowsId.Contains(item.Id))
{
args.Class="row-invalid-value";
}
}

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5
});

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
}
}

### Response

**Arnaud** answered on 18 Dec 2023

Hi Svetoslav, I did try that too. Did you manage to have it to work? When I tried, it did not work as the error css class was applied to te GridColumn and not to the inner TelerikTextBox inside the GridColumn. I could see the error class name when using my browser debug tools, but it did not apply. I gave up looking further into this solution. However, we managed to find a hack that somehow solves the issue. In the TelerikGrid, we have wrapped a template containing an EditForm (associated with a Validator) in all of the GridColumns concerned with validation. We store the references of all these EditForms that need to be validated at startup (by associating them a @Ref in the razor code). Then, at startup, we can iterate the EditForms collections and for each EditForm we can perform a "EditForm.EditContext.Validate()". Doing this was, we get the expected bahaviour. Have a good day. A

### Response

**Svetoslav Dimitrov** commented on 21 Dec 2023

Hello Arnaud, I am happy to read that you have managed to achieve the desired behavior!
