# Is there a way to filter a column based on how the data is rendered by a template?

## Question

**Jas** asked on 17 Nov 2023

I am using a Telerik DataGrid in Blazor to display entity data. In this grid, one column's Field represents a one-many data relationship. The Field type is an int, however in this column we use both a <Template> and a <EditorTemplate> to display string values associated with the backing Ints, which serves as an ID for this data. This string data is not stored in this application, but rather retrieved via a webAPI from another application that manages it. Is it possible to filter the column based on how the data is rendered in the display Template, which is a string? At present, any filtering at all Below is the code for the data grid. The column on which we would like to filter based on the string rendered in the template is bolded: <TelerikGrid Data="@BranchList" FilterMode="@GridFilterMode.FilterMenu" EditMode="GridEditMode.Inline" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler" Resizable="true" Sortable="true" SortMode="SortMode.Single"> <GridToolBar> <GridCommandButton Command="Add" Icon="add">Add New OB Branch</GridCommandButton> </GridToolBar> <GridColumns> <GridCommandColumn Width="100px"> <GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Save</GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn> <GridColumn Field="Id" FieldType="@typeof(int)" Editable="false" Visible="false" /> <GridColumn Field="Name" FieldType="@typeof(string)" Editable="true" Title="Branch Name" Width="200px"/> <GridColumn Field="GroupId" FieldType="@typeof(int)" Editable="true" Visible="true" Title="Group" Sortable="true" Filterable="true" Context="context" Width="100px"> <Template Context="ctx"> @{ var b=ctx as OptimalBlueBranch; <span>@(Groups.Where(g=>g.Id==b.GroupId).Select(g=>g.Name).FirstOrDefault())</span> } </Template> <EditorTemplate Context="ctx"> @{ var b=ctx as OptimalBlueBranch; <TelerikComboBox Data="@Groups" TextField="Name" ValueField="Id" @bind-Value="@b.GroupId" Placeholder="Add a group" ClearButton="true" Filterable="true"> </TelerikComboBox> } </EditorTemplate> </GridColumn> <GridColumn Field="Active" Title="Active" FieldType="@typeof(bool)" Editable="true" Width="100px"> <Template Context="ctx"> @{ var b=ctx as OptimalBlueBranch; <input type="checkbox" checked="@b.Active" disabled /> } </Template> </GridColumn> <GridColumn Field="Mappings" Title="Oasys Branch Mappings" Filterable="true" Width="250px"> <Template Context="ctx"> @{ var b=(ctx as OptimalBlueBranch).Mappings; var mapped=b.Any(); var styleClass=SetBranchBlockStyle(b); <span class="@styleClass fill-cell"> @if (b !=null && b.Count> 0) { foreach (var mapping in b) { <span>@GetOasysBranchName(mapping),&nbsp;</span> } } else { <span>No Oasys branches mapped</span> } </span> } </Template> <EditorTemplate Context="ctx"> @{ var b=ctx as OptimalBlueBranch; <TelerikMultiSelect Data="@OasysBranches" @bind-Value="@b.Mappings" TextField="Name" ValueField="Code" Placeholder="Add relevant branches" AutoClose="false"> </TelerikMultiSelect> } </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Hristian Stefanov** answered on 21 Nov 2023

Hi Jason, We've got a knowledge base article with a runnable sample showcasing how to filter a column with a 'Field' type of 'int' based on its string value presented in the template. Dive into the details with this example: Grid Foreign Key Column. Take a moment to run and test the sample, paying attention to the second column, 'Category'. Use it as a reference point for your needs. I hope the above information proves helpful. If there's anything I might have missed in addressing your question, do let me know. Regards, Hristian Stefanov Progress Telerik

### Response

**Jason** commented on 21 Nov 2023

Hristian- When I try to either "Edit" or "Preview" on the example you pointed to, I see this: Is there anything special I should do in order to get this to run? I would like to examine it as it is to see if on the surface it can be a starting point for the issue I am attempting to solve.

### Response

**Hristian Stefanov** commented on 22 Nov 2023

Hi Jason, I have tested the preview mode from the documentation on my machine, and it seems to work as expected. This leads me to think that the issue with loading it on your side is related to a browser cache. To verify this, you can open the documentation in incognito browser mode. I recommend clearing the browser cache and retrying. Let me know whether you are still facing difficulties with running it. Kind Regards, Hristian

### Response

**Jason** commented on 22 Nov 2023

Hey Hristian- I have tried in an incognito window, as well as in 3 different browsers (Edge, Chrome, and Firefox- which i just installed anew to test this) all with the same result as what I posted above. Do you have any other suggestions?

### Response

**Hristian Stefanov** commented on 23 Nov 2023

Hi Jason, I appreciate the ongoing updates on the progress. I additionally tested across multiple machines, including those of my colleagues, and the preview mode on this documentation page continues to display as expected. Another potential cause for the issue could be related to networking problems, such as REPL resources not loading correctly due to environmental settings. As a next step, right-click on the docs page and select ' Inspect,' then navigate to the ' Network ' tab to confirm if the REPL resources are loading correctly. You may also consider running various REPL samples in preview mode on different documentation pages for comparison. As a last resort, you can copy the code and paste it into an actual Visual Studio project to examine the sample firsthand. Kind Regards, Hristian
