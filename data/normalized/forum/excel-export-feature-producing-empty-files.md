# Excel Export feature producing empty files

## Question

**DanDan** asked on 19 Aug 2020

Hi there, I was hoping someone could help me with the problem I am having with the Excel Export feature. I have carefully reviewed the support docs to ensure that everything is set up correctly, however, the export is producing empty .xlsx files (no data in the export, despite there being nearly 1000 records displayed in the grid). I've spent many hours troubleshooting and found that if I set the AutoGenerateColumns parameter to true, it fixes the issue. That said, I do not wish to have this option turned on. Any and all help with this would very much be appreciated. Thank you! Code Context: Code-behind for my Razor page - here's how I declared the properties to initialize the data for the grid: [Inject] public IManageChemicalService ManageChemicalService { get; set; } public Telerik.Blazor.Components.TelerikGrid<Chemical> ManageChemicalGrid; public List<Chemical> Chemicals { get; set; } protected override async Task OnInitializedAsync() { Chemicals=(await ManageChemicalService.GetAllChemicals()).ToList(); } Razor page -here's how I set up the grid: <TelerikGrid Data="@Chemicals" @ref="ManageChemicalGrid" Pageable="true" PageSize="100" Sortable="true" Resizable="true" Reorderable="true" FilterMode="@GridFilterMode.FilterRow" Groupable="true" EditMode="@GridEditMode.Popup" OnCreate="@CreateHandler" OnUpdate="@UpdateHandler" OnDelete="@DeleteHandler"> <GridToolBar> <GridCommandButton Command="Add" Icon="add">Add Chemical</GridCommandButton> <GridCommandButton OnClick="@ShowLoadingSign" Command="ExcelExport" Icon="@IconName.FileExcel">Export to Excel</GridCommandButton> <label><TelerikCheckBox @bind-Value="@ExportAllPages" />&nbsp; Export All Pages</label> </GridToolBar> <GridExport> <GridExcelExport FileName="ChemicalsExport" AllPages="@ExportAllPages" /> </GridExport> <GridColumns> <GridColumn Field="@(nameof(Chemical.Id))" Editable="false" Filterable="false" Width="4%"> </GridColumn> ...and many more defined columns, editor templates and commands

## Answer

**Svetoslav Dimitrov** answered on 20 Aug 2020

Hello Dan, I am sending a sample WASM application that has the Excel Export setup in it. Could you compare the setup against your own and if this does not help you move forward could you make some changes to that project so that the issue is reproducible and we can further investigate? Regards, Svetoslav Dimitrov

### Response

**Dan** answered on 20 Aug 2020

Hello Svetoslav, Thanks for your response! I reviewed the sample WASM application and noticed that you have set the AutoGenerateColumns property to true in the grid. Is this required to be enabled for the export to work? As I mentioned in my original post, the only way I could get the export to work is by setting the AutoGenerateColumns propery to true. Otherwise, if I don't set it to true, the export just produces an empty file. If I set it to true, it fixes it. Thank you! -Dan

### Response

**Svetoslav Dimitrov** answered on 21 Aug 2020

Hello Dan, The automatically generated columns are not required, I have modified the project so that it has explicitly declared columns and put Editor Template to one of them. Could you modify this one, so that the Export produces an empty file and we can further investigate? Regards, Svetoslav Dimitrov

### Response

**Dan** answered on 21 Aug 2020

I'm a little confused of what you're asking me to do? I've compared the code you provided in the sample with mine and other than some differences in the editor templates, I don't see anything that would cause an issue on my end.

### Response

**Dan** answered on 21 Aug 2020

Oops, meant to mention prior to submitting my reply - I've attached screenshots of my grid and corresponding base properties/methods for the grid. Would you by any chance be able to take a look?

### Response

**Svetoslav Dimitrov** answered on 25 Aug 2020

Hello Dan, Based on the screenshots we could see nothing wrong with the Excel Export. I would suggest you open a support ticket, so it is private, and send us a runnable version of your application so we can dive deeper and investigate the issue you are facing. Regards, Svetoslav Dimitrov

### Response

**Dan** answered on 28 Sep 2020

Prior to opening a ticket, I did have one last-minute thought in regards to this issue. In the grid, one of the columns that I am displaying is actually a property located on a separate (virtual) object that I am returning with the grid data (using .Include in my repository to return) . This is the only other thing I can think of that could possibly cause the export file to be empty? Here is the model for the grid data that I am displaying: LabChemical.cs [NotMapped] private string _selectedChemicalName; [NotMapped] public string SelectedChemicalName ( This is one of the properties that I bound to the grid to display its associated chemical name) { get { if (this._selectedChemicalName==null) { if (this.Chemical !=null) { _selectedChemicalName=this.GetChemicalName; return _selectedChemicalName; } } return _selectedChemicalName; } set { _selectedChemicalName=value; } } [Required] public int ChemicalId { get; set; } public virtual Chemical Chemical { get; set; }

### Response

**Svetoslav Dimitrov** answered on 29 Sep 2020

Hello Dan, I have spoken to our Dev team regarding the issue you are facing. The lazy loading of the Chemical that you are doing probably does not get the data in time for the start of the export. What we do when exporting is to take only the collection of data provided in the Data parameter of the Grid and we do not make any calls to the database to get all the data. What we could suggest from what you have provided is to make sure that all data you would like to export is available by the time the export starts. Alternatively, you can build your own export in a fashion similar to the sample from this page: [https://feedback.telerik.com/blazor/1485764-customize-the-excel-file-before-it-gets-to-the-client](https://feedback.telerik.com/blazor/1485764-customize-the-excel-file-before-it-gets-to-the-client) Regards, Svetoslav Dimitrov

### Response

**Dan** answered on 05 Nov 2020

Hi Svetoslav, Is there a way to delay the export for a ~second to allow the data to be gathered first prior to starting the export? Maybe a hook somewhere to insert something like: await Task.Delay(50); Thank you, Dan

### Response

**Svetoslav Dimitrov** answered on 10 Nov 2020

Hello Dan, When Exporting data to Excel you should prepare the data beforehand so that the export feature should not wait for the data to be present. The expected workflow of the application would be: The data is present in the grid Press the Export button Export it to excel If you are using the OnRead event it would be the place to prepare the data for the current page you are exporting. Regards, Svetoslav Dimitrov

### Response

**Dan** answered on 10 Nov 2020

Hi Svetoslav, I meant to add that the data is already loaded in the grid prior to clicking the export button - yet the excel file is still empty. Would you by any chance be available for a quick screenshare meeting? Thank you! -Dan

### Response

**Marin Bratanov** answered on 13 Nov 2020

Hello Dan, The way we could investigate such problems is by having a sample reproducible that we can then proceed to debug. To do that, we need you to modify one of our examples (like the one from the documentation ) and send it back to us (just please keep it runnable and clear of any business logic and dependencies). The following blog post can guide you in creating such a reproducible example Isolating a problem in a sample project. Having that will let us investigate in detail with all the resources we have at our disposal as a team, and dedicate the necessary time to it. To attach a project, you should open a private support ticket (direct link for Blazor tickets here ), so you can attach the .zip archive with the reproducible. The forums (this here is a public forum thread) do not allow archives as attachments, only images. In the private ticket, we could also discuss your available support options (such as the potential for a screen sharing session which is available to DevCraft Ultimate license holders, and which, in my experience, is rarely helpful in investigating such complex issues in the deep logic of the code). Regards, Marin Bratanov

### Response

**Ben** answered on 05 Oct 2022

Don't know if this is the same root cause or not, but we observed the GridReadEventArgs.Request.PageSize value was set to 0 during the Read request for the Excel export (even though the grid PageSize property was set to 50). We worked around this by setting PageSize on the request to int.MaxValue.

### Response

**Svetoslav Dimitrov** commented on 10 Oct 2022

Hello Ben, If the Grid is using OnRead and is exporting all pages, it will fire an additional OnRead event at the time of exporting, with a request PageSize of 0. This will enable the component to obtain all data. You can see the Export to Excel documentation article (Notes section) for more information.
