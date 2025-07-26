# Style <GridCommandColumn> title

## Question

**Noa** asked on 23 Aug 2023

How can I style the Title of the GridCommandColumn? I jsut want to make the text bold. I've tried using <HeaderTemplate> and <GridCommandColumn.TItleTemplate> neither have worked. And I can't seem to find anything in the docs about styling the title. <GridCommandColumn Width="50px" Title="Actions"> <GridCommandButton Command="Edit" Icon="@FontIcon.Pencil"> </GridCommandButton> <GridCommandButton Command="Delete" Icon="@FontIcon.Trash" ThemeColor="error"> </GridCommandButton> </GridCommandColumn> <GridColumn Title="First Name" Field="@(nameof(SecurityAdminDto.firstName))" Width="100px"> <HeaderTemplate> <div class="column-title"> First Name </div> </HeaderTemplate> </GridColumn> <GridColumn Title="Last Name" Field="@(nameof(SecurityAdminDto.lastName))" Width="100px"> <HeaderTemplate> <div class="column-title"> Last Name </div> </HeaderTemplate> </GridColumn> <GridColumn Title="Email" Field="@(nameof(SecurityAdminDto.email))" Width="100px"> <HeaderTemplate> <div class="column-title"> Email </div> </HeaderTemplate> </GridColumn> <GridColumn Title="EmployeeId" Field="@(nameof(SecurityAdminDto.employeeId))" Width="100px"> <HeaderTemplate> <div class="column-title"> EmployeeId </div> </HeaderTemplate> </GridColumn> <GridColumn Title="NetworkId" Field="@(nameof(SecurityAdminDto.networkId))" Width="100px"> <HeaderTemplate> <div class="column-title"> NetworkId </div> </HeaderTemplate> </GridColumn> <GridColumn Title="Security Admin" Field="@(nameof(SecurityAdminDto.isSecurityAdmin))" Width="100px"> <HeaderTemplate> <div class="column-title"> Security Admin </div> </HeaderTemplate> </GridColumn> <GridColumn Title="FSO" Field="@(nameof(SecurityAdminDto.fsoCodes))" Width="100px"> <HeaderTemplate> <div class="column-title"> FSO </div> </HeaderTemplate> <Template> @{
var cellValue=((SecurityAdminDto)context).fsoCodes;
int i=0;
@foreach(var fsoCode in cellValue)
{
if (i !=0)
{ <span>, </span> } <span> @fsoCode </span> i++;
}
} </Template> </GridColumn> <GridColumn Title="FTC" Field="@(nameof(SecurityAdminDto.isFTC))" Width="100px"> <HeaderTemplate> <div class="column-title"> FTC </div> </HeaderTemplate> </GridColumn> <GridColumn Title="HR" Field="@(nameof(SecurityAdminDto.hrCodes))" Width="100px"> <HeaderTemplate> <div class="column-title"> HR </div> </HeaderTemplate> <Template> @{
var cellValue=((SecurityAdminDto)context).fsoCodes;
int i=0;
@foreach (var hrCode in cellValue)
{
if (i !=0)
{ <span>, </span> } <span> @hrCode </span> i++;
}
} </Template> </GridColumn> <GridColumn Title="Contracts" Field="@(nameof(SecurityAdminDto.contractsCodes))" Width="100px"> <HeaderTemplate> <div class="column-title"> Contracts </div> </HeaderTemplate> <Template> @{
var cellValue=((SecurityAdminDto)context).contractsCodes;
int i=0;
@foreach (var contractCode in cellValue)
{
if (i !=0)
{ <span>, </span> } <span> @contractCode </span> i++;
}
} </Template> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Georgi** answered on 28 Aug 2023

Hello, Noah, You can style the Title of the GridCommandColumn by using custom CSS e.g.: <style>.k-grid th.customTitle { font-weight: bold;
}
</style> The HeaderClass parameter can be used to style specific columns as follows: <TelerikGrid Data=@GridData EditMode="@GridEditMode.Inline" OnUpdate="@MyOnUpdateHandler" Pageable="true" PageSize="15" Height="500px"> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Editable="false" Title="Employee ID" /> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> <GridCommandColumn Title="Command Title" HeaderClass="customTitle"> <GridCommandButton Command="Edit" Icon="@FontIcon.Pencil"> Edit </GridCommandButton> <GridCommandButton Command="Save" Icon="@FontIcon.Save" ShowInEdit="true" OnClick="@CustomSaveOnClickHandler"> Update </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@FontIcon.Cancel" ShowInEdit="true"> Cancel </GridCommandButton> <GridCommandButton Command="MyOwnCommand" Icon="@FontIcon.InfoCircle" ShowInEdit="false" OnClick="@MyCustomCommandOnClickHandler"> My Command </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> You can find additional information about column styling in this knowledge-base article. You can see the final result in this REPL example. Let me know if additional questions arise. Regards, Georgi Progress Telerik
