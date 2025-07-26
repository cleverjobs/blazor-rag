# Fill area for Grid Layout

## Question

**Joe** asked on 30 May 2025

How do I fill the 2nd row to the bottom with my data grid? The top row filled as expected in using enough space for the button. However, I expected the bottom row to then use the rest of the area and dock the data grid. Is there a height setting that says fill the rest of the area? <TelerikGridLayout Class="grid-layout"> <GridLayoutRows> <GridLayoutRow /> <GridLayoutRow /> </GridLayoutRows> <GridLayoutItems> <GridLayoutItem Row="1"> <TelerikButton OnClick="@OnCreate" Class="gsi-width-100pct gsi-height-32px"> Create New </TelerikButton> </GridLayoutItem> <GridLayoutItem Row="2"> <TelerikGrid Data=@Patients SelectedItems="SelectedPatients" Pageable=true PageSize="20" Height="100%" SelectionMode=GridSelectionMode.Single SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Person> m)=> OnPatientSelected(m))"> <GridColumns> <GridColumn Field=@nameof(Person.FirstName) Title="First Name" /> <GridColumn Field=@nameof(Person.LastName) Title="Last Name" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.DateOfBirthDisplay )}") Title="Date of Birth" Width="125px" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.GenderDisplay )}") Title="Sex" Width="100px" /> <GridColumn Field=@nameof(Person.LastSessionTimestampDisplay) Title="Last Session" /> </GridColumns> </TelerikGrid> </GridLayoutItem> </GridLayoutItems> </TelerikGridLayout>

### Response

**Ivan Danchev** commented on 02 Jun 2025

Hello Joel, I've tried reproducing the empty space visible after the Grid in the screenshot you attached, but to no avail. Here's a REPL example that uses the same TelerikGridLayout configuration and the height of the Grid nested in it is 100%: [https://blazorrepl.telerik.com/QzYAOmlq44ScWT7P06](https://blazorrepl.telerik.com/QzYAOmlq44ScWT7P06) I've added dotted borders to the TelerikGridLayout, so that the dimensions of the containers are clearly visible. .k-grid-layout> div { border: 2px dotted;
} No empty space after the Grid appears. I suspect that additional custom CSS is involved and it could be causing the unexpected behavior. Could you please modify the example I linked accordingly and demonstrate the issue?
