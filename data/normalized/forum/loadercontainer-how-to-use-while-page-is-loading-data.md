# LoaderContainer How to use while page is loading data?

## Question

**Dea** asked on 13 Sep 2022

I would like to use this control but I am not getting very far. Sad! The loading does not appear! and my app looks like tis doing nothing for a minute or so. Then the grid with the data appears. HOw do I set this up to have the loader appear before the data is done and then disappear when the grid is done? My razor page looks like this: <PageTitle>SodaTools</PageTitle> <TelerikGridLayout> <GridLayoutColumns> <GridLayoutColumn Width="5%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="5%"></GridLayoutColumn> <GridLayoutColumn Width="5%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="10%"></GridLayoutColumn> <GridLayoutColumn Width="5%"></GridLayoutColumn> </GridLayoutColumns> <GridLayoutRows> <GridLayoutRow Height="23%"></GridLayoutRow> <GridLayoutRow Height="1%"></GridLayoutRow> <GridLayoutRow Height="75%"></GridLayoutRow> <GridLayoutRow Height="1%"></GridLayoutRow> </GridLayoutRows> <GridLayoutItems> <GridLayoutItem Column="2" Row="1"> <div hidden="@blnHideMe"> <b>Message:</b> </div> </GridLayoutItem> <GridLayoutItem Column="3" Row="1" ColumnSpan="9"> <div hidden="@blnHideMe" style="align-content:center;background-color:yellow"> @* <TelerikTextBox @bind-Value="@strAppMsg" Id="AppMsg" />*@<p style="white-space: pre-line">@strAppMsg</p> </div> </GridLayoutItem> <GridLayoutItem Column="2" Row="2"> </GridLayoutItem> <GridLayoutItem Column="3" Row="2"> </GridLayoutItem> <GridLayoutItem Column="10" Row="2"> </GridLayoutItem> <GridLayoutItem Column="2" Row="3" ColumnSpan="10"> <TelerikLoaderContainer Visible="@( @GridData==null )" Text="Please wait..." /> <div hidden="@blnHideGrid"> <TelerikGrid Data="@GridData" AutoGenerateColumns="true" Pageable="true" Sortable="true" FilterMode="@GridFilterMode.FilterRow" Class="custom-row-colors"> <GridToolBar> <GridCommandButton Command="ExcelExport" Icon="file-excel">Export to Excel</GridCommandButton> <label class="k-checkbox-label"><TelerikCheckBox @bind-Value="@ExportAllPages" /> Export All Pages</label> </GridToolBar> <GridExport> <GridExcelExport FileName="telerik-grid-export" AllPages="@ExportAllPages" OnBeforeExport="@OnBeforeExcelExport" /> </GridExport> </TelerikGrid> </div> </GridLayoutItem> </GridLayoutItems> </TelerikGridLayout> Codebehind looks like this: private List<LoadStatsResult> GridData { get; set; } protected override async Task OnInitializedAsync() { base.OnInitialized(); strAppMsg="I am in Load Stats!"; getData(); } private async void getData() { strAppMsg="This be an app msg: You clicked my Load Stats Button!"; setAppMsg(); // how do I connect to my DAS cls List<LoadStatsResult> LoadStatsResults=new List<LoadStatsResult>(); LoadStatsResults=clsDataAccessService.doLoadStats(GlobalStuff.msDBEnvir); GridData=LoadStatsResults; if (GridData.Count> 0) { strAppMsg="How to Use:" + Environment.NewLine + "1) Click the [Export to Excel] button to export displayed rows." + Environment.NewLine + "2) To export all the pages, first click the [Export All Pages] button. Then the [Export to Excel] button." + Environment.NewLine + "3) Filter a column by typing value into textbox on left-handside of the beaker icons." + Environment.NewLine + "4) Filter rules can be gotten by clicking on the full beaker icon. A drop down list of available rules will appear." + Environment.NewLine + "5) Filter clearing is done by clicking on the crossed out beaker icon." + Environment.NewLine + "6) Paging is done by clicking on the Left and right paging icons at the bottom of the grid."; } else { strAppMsg="Sorry nothing found! "; }; }

## Answer

**Hristian Stefanov** answered on 16 Sep 2022

Hello Deasun, There does not seem to be anything wrong with the setup of the LoaderContainer. However, I do have a guess about what is wrong and that stems from the fact the getData() call is not awaited, thus the LoadStatsResults collection gets initialized straight away, making the loader check somehow redundant. If the call is properly awaited, then the collection/check will be executed only after the call has actually returned a value. I have prepared a rather simple example that demonstrates this: [https://blazorrepl.telerik.com/GmEjFTOM24pRHs4G03](https://blazorrepl.telerik.com/GmEjFTOM24pRHs4G03) Also, we have a demo showcasing an integration of what you are after, which can be found here: Grid - Loading Animation. Note the Grid there uses an OnRead handler, but the concept is basically the same. Regards, Hristian Stefanov Progress Telerik

### Response

**Deasun** commented on 19 Sep 2022

this helped a lot. New to this , as you might have guessed. <GridLayoutItems> <TelerikLoaderContainer Visible="@(GridData==null)" LoaderPosition="@LoaderPosition.End"></TelerikLoaderContainer> await Task.Delay(3000); getData(); private void getData(){} When I ran that it works as I expected. :) But when I did this; await getData(); private async Task getData() It did not appear. I guess I am not understanding something with this Task stuff.

### Response

**Deasun** commented on 19 Sep 2022

Found a fix! on the page init as the first line put: await Task.Delay(1); Then declare the procedure your calling as; Private Task getDate(){} And as the last line within the called task, put Return Task.TaskCompleted; Then the calling code is; await getData() This worked fine. :)

### Response

**Deasun** commented on 19 Sep 2022

One last question, how would I get this to work when a user clicks a button on the page? I tried just calling the task procedure await getData(){} under the button click but as before it doesnt show up.

### Response

**Joana** commented on 22 Sep 2022

Hi Deasun, The visibility of the LoaderContainer is controlled by its Visible property. It's initial value might be set to true if the GridData is null. However, if you need to show it later through another condition you should simply assign it. You might find useful our demos and documentation resources: [https://demos.telerik.com/blazor-ui/loadercontainer/overview](https://demos.telerik.com/blazor-ui/loadercontainer/overview) [https://docs.telerik.com/blazor-ui/components/loadercontainer/overview](https://docs.telerik.com/blazor-ui/components/loadercontainer/overview)
