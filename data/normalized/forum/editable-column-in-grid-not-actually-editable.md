# Editable Column in Grid not actually editable

## Question

**Tan** asked on 04 Jan 2023

I have created a Grid to display a list of rows from a database. I want to have two columns more than the table gives me - one for a text box and one for a submit button. I need the button's OnClick method to be able to access the entire row. Here's what I've got (simplified) and the final text column is not editable: @page "/pathto/page" @using Solution.Shared.Models;
@inject HttpClient Http

<TelerikLoader Visible="@(Results==null)" Size="@ThemeConstants.Loader.Size.Medium" />
@if (Results is not null )
{
<TelerikGrid Data="@Results" TItem="@Result" @ref="@Grid" EditMode="@GridEditMode.Inline" OnCreate="@Submit" Class="auto-table" Resizable="true" Sortable="true" Pageable="true" PageSize="15" Height="auto">
<GridToolBar>
<GridCommandButton Command="ExcelExport" Icon="file-excel">Export to Excel</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field="@nameof(Result.Username)" Width="8%" Editable="false" Groupable="true">
<Template>
@{ string? username=(context as Result)?.username;
<LinkToAnotherPage Username="@username" Link />
}
</Template>
</GridColumn>
<GridColumn Field="@nameof(Result.display_name)" Title="Name" Width="8%" Editable="false" />
<GridColumn Field="@nameof(Result.Date)" Title="Date" Width="4%" Editable="false" DisplayFormat="{0:MM/dd/yyyy}" />
<GridColumn Field="@nameof(Result.EditableColumn)" Title="Save This Value" Editable="true" Width="18%" />
<GridCommandColumn Title="Approve" Width="3%">
<GridCommandButton Command="Add" Icon="checkmark" ShowInEdit="true" />
</GridCommandColumn>
</GridColumns>
</TelerikGrid>
}

@code {
List<Result>? Results; private TelerikGrid<Result>? Grid; protected override async Task OnInitializedAsync ( ) {
Results=await Http.GetFromJsonAsync<List<Result>>( "Controller/Action" );
} private async Task Submit ( GridCommandEventArgs args ) { var ex=args.Value; // this should be the edited column Result res=(Result)args.Item; // do stuff with res and ex variables }
} Can I bind to the value of the editable column's content when the row is clicked? Is there a better way to do this?

## Answer

**Yanislav** answered on 06 Jan 2023

Hello Tanner, Thank you for the provided information and code snippet! I've reviewed the requirement and I'd like to first verify if I understand it correctly. Feel free to correct me, but if I properly understand, the Grid should render two additional cells for each record, one with a text box and one with a button. When the button is clicked, you need the data item of the row and the value of the text box. As I imagine, the value of the text box should be saved as a comment to a field of the corresponding item. Am I correct? If that's the case, you can declare a Column Template that contains a TextBox component. Then, through the ` context ` object of the Template, you can bind the input to a property of the row. <GridColumn Context="dataItem" Title="Save This Value" Editable="true" Width="18%">
<Template>
@{ var item=dataItem as WeatherForecast;
<TelerikTextBox @bind-Value="item.Comment "></TelerikTextBox>
}
</Template>
</GridColumn> Now, when the input is bound to the model, in order to access it when a button is clicked, you can declare a Custom Command button. <GridCommandColumn Title="Approve" Width="3%">
<GridCommandButton Command="AddComment" OnClick="@AddComment" Icon="checkmark" ShowInEdit="false" />
</GridCommandColumn> Hook up for its OnClick event and through the `Item` property of the event argument s you can access the item and save the inserted comment by the user. private async Task AddComment ( GridCommandEventArgs args ) {
WeatherForecast res=(WeatherForecast)args.Item; // row data Console.WriteLine(res.Id); // row Id Console.WriteLine(res.Comment); // Inserted data in the textbox // submit value logic here res.Comment=""; // clear the textbox } For your convenience, I've prepared an example so you can review and test the approach: [https://blazorrepl.telerik.com/GHkFaKvg58N2wf2t12.](https://blazorrepl.telerik.com/GHkFaKvg58N2wf2t12.) The information that I am currently missing is what should happen with that comment after it is submitted. Should it be displayed in the Grid or should the TextBox value be cleared after that? In the above sample, the value is cleared, however, you may handle it as needed to match the specific application requirements. Please try the approach and let me know if it meets your requirement or if further assistance is needed. Regards, Yanislav Progress Telerik

### Response

**Tanner** commented on 09 Jan 2023

Thank you so much for this solution! It seems to have worked in this scenario. The information that I am currently missing is what should happen with that comment after it is submitted. Should it be displayed in the Grid or should the TextBox value be cleared after that? I actually want the row to disappear from this grid and be shown with the comment in a different grid. I do what I need to do with the submit, which prevents it appearing in the Grid's list the next time, and I call await OnInitializedAsync() at the end to rerender the grid without the row that was just commented on. A new issue I'm having is with the next grid. I want to show the comment, allow it to be editable, and have buttons to update the comment if necessary and trigger some more logic. The same solution with the other grid does not seem to be working. Does the @bind-Value attribute in the comment column not support the two-way binding that I need here?

### Response

**Yanislav** commented on 10 Jan 2023

Hello Tanner, Based on the provided information, I understand that the new Grid that contains the records with comments should have the same functionality as the first Grid. I've modified the example from my previous reply and tried to reproduce the problem: [https://blazorrepl.telerik.com/QxkvbObr01FlGSnV15](https://blazorrepl.telerik.com/QxkvbObr01FlGSnV15) Testing the example above on my end, the approach seems to be working correctly. Can you spot something different from the scenario you have? If the sample is not useful, may I ask you to try reproducing the problem and send it back to me so I can review the implementation in detail? Thus, I can try to find the reason for the problem and further troubleshoot it.

### Response

**Tanner** commented on 10 Jan 2023

The issue was that the values of the Context attribute inside the GridColumn were the same. The second grid is in a child component of the page where the first grid is, so I did not expect that to be a problem. I have much to learn... Your replies have been very much appreciated! If there is anything else that comes up relating to these grids, I'll post here again. Thanks again for your help :)

### Response

**Yanislav** commented on 12 Jan 2023

Hello Tanner, You're welcome! I'm glad I was able to assist you. Since the issue seems to be resolved now, I'll mark the ticket as closed, but in case you run into any issues or have any questions, please don't hesitate to contact us.
