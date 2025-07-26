# Want to get Current Selected Row in Grid with TelerikButton

## Question

**Mic** asked on 10 Feb 2022

Hello, I am wanting to use a TelerikButton outside of my TelerikGrid to get the current selected row in the Grid, I do not want to use a GridRowButton on each row, but one TelerikButton outside of the grid. For an example, we have a Grid of employees and each employee is an object in a list of EmployeeVM class objects. which has an EmployeeID for each employee. When the TelerikButton is clicked, I want to get the EmployeeID of the employee selected in the Grid in a method in the @code section that is the same as listed in the OnClick property on the Telerik Button. I spent some time searching on Google but did not find what I was looking for, I am an experienced developer but new to Telerik UI for Blazor. Thank you.

### Response

**Michael** commented on 11 Feb 2022

Hello, Thanks for the reply, but I need a solution that works only with a TelerikButton to get the currently selected row in the Grid. This is example is using TelerikNumericTextBox to set the selected item, that is not what I need. I need an example that shows a Dialog with the CompanyName for the Company Selected in the Grid. Thanks. - Michael

### Response

**Matthias** commented on 11 Feb 2022

hi Michel Look at this method, that's exactly what it does. The other options are just there to demonstrate the behavior when your values dynamically manipulate the selection via code. async Task GetSelectedItem () { if (SelectedItems.Any())
{
SelectedItem=SelectedItems.FirstOrDefault(); await Dialogs.AlertAsync( $" {SelectedItem.Name} selected" );
} else { await Dialogs.AlertAsync( "No item selected" );
}
}

### Response

**Michael** commented on 14 Feb 2022

Ok thanks, Now I can get the value, in this case the Name, out of the selected row on the grid. I was missing a bind, so now the example works. now there is a new issue. It looks like your example is getting a string out of the grid and displaying it in a dialogue. I need to get an int number, like for the Employee ID, but not as a string, I can get it as a string, but then when trying to convert to an int get the following error: Error: System.FormatException: Input string was not in a correct format. can you show me some example code that gets a C# int out of the grid? Thanks, this forum is very helpful, you and the other Telerik employees do a great job. Michael G. Workman

### Response

**Michael** commented on 17 Feb 2022

Hello Matthias, Pardon me for the confusion, but int.Parse is not needed at all, The ID field in SelectedItem is already an int and a parse is not needed. However, using int.Parse might be a good option for obfuscated code contests, LOL. - Michael

## Answer

**Matthias** answered on 15 Feb 2022

Hello Michael, so if I understand you correctly, instead of the name, you want the EmployeeId? You would only need to return this value as int. Alternatively you can define a variable that gets this value after calling the method. Here as an example a simple possibility: regards Matthias <div style="height: 50px"> <TelerikButton OnClick="@GetEmployeeGetId"> Get Selected </TelerikButton> </div> <h2> @SelectedEmployeeID </h2> <TelerikGrid Data=@Employees SelectionMode="@GridSelectionMode.Single" @bind-SelectedItems="@SelectedItems" Pageable=true PageSize="10"> <GridColumns> <GridColumn Field=@nameof(Employee.EmployeeId) Title="EmployeeId" /> <GridColumn Field=@nameof(Employee.Name) Title="Name" /> <GridColumn Field=@nameof(Employee.Street) Title="Street" /> <GridColumn Field=@nameof(Employee.Zipcode) Title="Zip" /> <GridColumn Field=@nameof(Employee.City) Title="City" /> </GridColumns> </TelerikGrid> @code{ public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Street { get; set; } public string City { get; set; } public string Zipcode { get; set; }
}

ObservableCollection<Employee> Employees=new ObservableCollection<Employee>();
IEnumerable<Employee> SelectedItems { get; set; }=new List<Employee>(); private int SelectedEmployeeID { get; set; } protected override async Task OnInitializedAsync ( ) {
Employees.Add( new Employee {EmployeeId=1, Name="John Doe", Street="123 Main Street", City="Anytown", Zipcode="12345" });
Employees.Add( new Employee {EmployeeId=2, Name="Jane Doe", Street="456 Main Street", City="Anytown", Zipcode="12345" });
Employees.Add( new Employee {EmployeeId=3, Name="Sammy Doe", Street="789 Main Street", City="Anytown", Zipcode="12345" });

SelectedItems=new List<Employee> {Employees.FirstOrDefault()};
} async Task GetEmployeeGetId ( ) {
SelectedEmployeeID=SelectedItems.Any() ? SelectedItems.FirstOrDefault().EmployeeId : 0; await InvokeAsync(StateHasChanged);
}

}

### Response

**Michael** commented on 16 Feb 2022

Hello Matthias, Thanks for all your help! My code is now working correctly after your suggested changes. The reason it would not work at first was I left out the BIND attribute from the TelerikGrid tag. Then the issue with getting the ID was my own fault, I was trying to convert the string $"{SelectedItem.EmployeeID} selected" to an integer using int.Parse, but I had a brain fart and was trying to convert "12345 selected" to an integer, instead of just the string $"{SelectedItem.EmployeeID}" which for example would be "12345" . But now that is corrected after removing the word SELECTED from the string and now I have a proper integer. Telerik UI for Blazor really is a top notch software product and is well worth the money. Support is excellent also, you made quick, timely responses to my inquiries that were very helpful with me getting my job done. Have a great day! Michael G. Workman

### Response

**Matthias** answered on 11 Feb 2022

Hi MIchael, Try this. This is a "quick & dirty" solution. But your question, as I understood it, should be answered. Greetings Matthias razor @page "/"

@using System.Collections.ObjectModel <div style="width: 200px;height: 50px;"> <TelerikNumericTextBox ValueChanged="@((int v)=> SetAndShowItemWithId(v))" Min="1"> </TelerikNumericTextBox> </div> <div style="height: 50px"> <TelerikButton OnClick="()=> SetAndShowItemWithId(3)"> Set Selected to 3 </TelerikButton> <TelerikButton OnClick="GetSelectedItem"> Get Selected </TelerikButton> </div> <TelerikGrid Data=@Customers SelectionMode="@GridSelectionMode.Single" @bind-SelectedItems="@SelectedItems" Pageable=true PageSize="10"> <GridColumns> <GridColumn Field=@nameof(Customer.id) Title="id" /> <GridColumn Field=@nameof(Customer.Name) Title="Name" /> <GridColumn Field=@nameof(Customer.street) Title="Street" /> <GridColumn Field=@nameof(Customer.zipcode) Title="Zip" /> <GridColumn Field=@nameof(Customer.city) Title="City" /> </GridColumns> </TelerikGrid> code @code{

[ CascadingParameter ] public DialogFactory Dialogs { get; set; } public class Customer { public int id { get; set; } public string Name { get; set; } public string street { get; set; } public string city { get; set; } public string zipcode { get; set; }
}

ObservableCollection<Customer> Customers=new ObservableCollection<Customer>();
IEnumerable<Customer> SelectedItems { get; set; }=new List<Customer>();
Customer SelectedItem { get; set; } private int IntValue=1; protected override async Task OnInitializedAsync () {
Customers.Add( new Customer {id=1, Name="John Doe", street="123 Main Street", city="Anytown", zipcode="12345" });
Customers.Add( new Customer {id=2, Name="Jane Doe", street="456 Main Street", city="Anytown", zipcode="12345" });
Customers.Add( new Customer {id=3, Name="Sammy Doe", street="789 Main Street", city="Anytown", zipcode="12345" });
SelectedItem=Customers.FirstOrDefault();

SelectedItems=new List<Customer> {SelectedItem};
} async Task GetSelectedItem () { if (SelectedItems.Any())
{
SelectedItem=SelectedItems.FirstOrDefault(); await Dialogs.AlertAsync( $" {SelectedItem.Name} selected" );
} else { await Dialogs.AlertAsync( "No item selected" );
}
} async Task SetAndShowItemWithId ( int id ) { if (Customers.Any())
{
SelectedItem=Customers.FirstOrDefault(x=> x.id==id); if (SelectedItem is not null )
{
SelectedItems=new List<Customer> {SelectedItem}; await Dialogs.AlertAsync( $" {SelectedItem.Name} selected" );
} else { await Dialogs.AlertAsync( "No item selected" );
}
}
}

}

### Response

**Phyllis** commented on 27 Aug 2022

Thank you :)
