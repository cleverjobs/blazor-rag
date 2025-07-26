# Fill Splitter with Grid

## Question

**Joe** asked on 23 May 2025

Can you tell me how I can define the Grid to fill the entire splitter area without trying to guess? <TelerikGrid Data=@Sessions SelectedItems="SelectedSessions" Pageable=true PageSize="20" Height="80%" SelectionMode=GridSelectionMode.Single SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Session> m)=> OnSessionSelected(m))"> <GridColumns> <GridColumn Field=@nameof(Session.TimestampDisplayName) Title="Timestamp" /> <GridColumn Field=@nameof(Session.TimeZoneOffset) Title="Time Zone Offset" /> </GridColumns> </TelerikGrid> <TelerikSplitter Orientation="SplitterOrientation.Horizontal" Height="75vh"> <SplitterPanes> <SplitterPane Size="50%" Min="30%" Max="70%" Collapsible="false" Class="k-scrollable"> </SplitterPane> <SplitterPane Min="30%" Max="70%" Collapsible="false" Class="k-sc </SplitterPane>
</SplitterPanes>
</TelerikSplitter>

## Answer

**Nadezhda Tacheva** answered on 28 May 2025

Hi Joel, If you don't set an explicit height to the Grid, it will by design, expand to fill its container. Here is a runnable sample using your Splitter configuration: [https://blazorrepl.telerik.com/cfaJciPu45B6B3il24.](https://blazorrepl.telerik.com/cfaJciPu45B6B3il24.) Another option is to set the Grid height to 100% instead of 80% as outlined in your initial post. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Joel** commented on 28 May 2025

<h3> Session Files </h3> <TelerikGrid Data=@StorageFiles SelectedItems="@SelectedStorageFiles" Pageable=true PageSize="20" SelectionMode=GridSelectionMode.Single SelectedItemsChanged="@((IEnumerable<StorageFile> m)=> OnFileSelected(m))"> <GridColumns> <GridColumn Field=@nameof(StorageFile.Name) Title="Name" /> <GridColumn Field=@nameof(StorageFile.CreationTimeDisplayName) Title="Timestamp" /> <GridColumn Field=@nameof(StorageFile.TimeZoneOffsetName) Title="Time Zone Offset" /> </GridColumns> </TelerikGrid> Okay, so. I removed the setting and it constricts the grid all the way at the top. I need it to fill the area because this just feels crowded:

### Response

**Nadezhda Tacheva** commented on 29 May 2025

Hi Joel, If you have so little items, the Grid cannot expand to fill the pane and you must explicitly set Height="100%" to force it to. Note that you will still have an empty area as there are not enough items to fill the space but this empty area will be inside the Grid. Here is the updated sample: [https://blazorrepl.telerik.com/GzOzcXbT455n49TZ58.](https://blazorrepl.telerik.com/GzOzcXbT455n49TZ58.)

### Response

**Joel** commented on 30 May 2025

This definition does fill the area: <TelerikGrid Data=@Patients SelectedItems="SelectedPatients" Pageable=true PageSize="20" Height="100%" SelectionMode=GridSelectionMode.Single SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Person> m)=> OnPatientSelected(m))"> <GridColumns> <GridColumn Field=@nameof(Person.FirstName) Title="First Name" /> <GridColumn Field=@nameof(Person.LastName) Title="Last Name" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.DateOfBirthDisplay )}") Title="Date of Birth" Width="125px" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.GenderDisplay )}") Title="Sex" Width="100px" /> <GridColumn Field=@nameof(Person.LastSessionTimestampDisplay) Title="Last Session" /> </GridColumns> </TelerikGrid> However, if I add one thing to the top of the splitter area the grid does not calculate the height correctly. Do you have another layout control that will fill the area 100% and allow me to dock these controls without having to specify their height? I tried the LayoutGrid but didn't have any success because it seems to always need the height specified. I'll post a similar question but using the LayoutGrid. <TelerikButton OnClick="@OnCreate" Class="gsi-width-100pct"> Create New </TelerikButton>

### Response

**Dimo** commented on 03 Jun 2025

Joel - If two or more elements should fill a container, you either need to adjust all heights (e.g. see Adjust Grid Height to fill a container ), or use an additional layout like flexbox. [https://blazorrepl.telerik.com/GJEUknlk16W7hBIk02](https://blazorrepl.telerik.com/GJEUknlk16W7hBIk02)
