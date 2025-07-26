# GridSearchBox bug

## Question

**Gle** asked on 23 Dec 2024

When enabling a GridSearchBox in my Grid, while I'm typing or deleting letters from the search box, I get spammed in my Ouput from Debug with "Exception thrown: 'System.Threading.Tasks.TaskCanceledExceptuion' in System.Private.CoreLib.dll" Here is my code: <TelerikGrid Data=@TestItemsList FilterMode="GridFilterMode.FilterRow" Sortable="true" EditMode="GridEditMode.Inline" Height="2000px" FilterRowDebounceDelay="300"> <GridToolBarTemplate> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus" Enabled="@UserModel.CanEdit()"> Add Item </GridCommandButton> <GridSearchBox Fields="@SearchableFields" Placeholder="Search..." Width="300px" /> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@nameof(TestModel.FileName)" Title="File Name" Editable="false" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true" Enabled="@UserModel.CanEdit()" OnClick="@OnUpdate"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil" Enabled="@UserModel.CanEdit()"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="@SvgIcon.Trash" Enabled="@UserModel.CanEdit()" OnClick="@OnDelete"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true" Enabled="@UserModel.CanEdit()"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @* Only showing relevent code here *@@code {

private List <string> SearchableFields=new List <string> { nameof(SDSModel.Title), nameof(SDSModel.FileName) };

} Details: System.Threading.Tasks.TaskCanceledException
HResult=0x8013153B
Message=A task was canceled. Call Stack:

## Answer

**Tsvetomir** answered on 24 Dec 2024

Hi Glenn, Thank you for sharing the error message with us. To investigate the issue further, I've tried to recreate the described behavior. However, on my end, I have been unable to reproduce the error. This suggests that there are some details that I am missing from the actual project configuration, which will help me accurately reproduce the issue. Therefore, as the next step, can you please provide me with a small runnable sample that demonstrates the actual configuration you are testing with and allows me to reproduce the error? To make it more convenient for you, you can utilize REPL instead of attaching a project. This approach will enable me to conduct a more comprehensive investigation using a configuration that closely resembles your actual environment. Additionally, could you share more details about your application's setup? Specifically, which .NET version you are using and the version of the Telerik UI for Blazor product. I look forward to your response. Regards, Tsvetomir Progress Telerik
