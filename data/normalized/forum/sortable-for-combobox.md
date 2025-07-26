# sortable for combobox

## Question

**kha** asked on 03 Feb 2020

Hello, i wanted to know if you are planning to add sortable to combobox in ui for blazor ?

## Answer

**Marin Bratanov** answered on 03 Feb 2020

Hi Khashayar, We haven't had such requests and you can simply .OrderBy() the data source. The feature that helps users find what they are looking for in a combobox is generally the filtering: [https://demos.telerik.com/blazor-ui/combobox/filtering.](https://demos.telerik.com/blazor-ui/combobox/filtering.) How would you expect a built-in feature to work? Would it require some UI to let the user sort and if so - how do you imagine it in the component? If it doesn't, would simply sorting the data source suffice for your needs? Regards, Marin Bratanov

### Response

**khashayar** answered on 04 Feb 2020

let's think of a scenario i as a client might want to sort the datas as i prefer or when i add new item to combo box list before making request it gets right where it has to be because of client side sorting and there is a scenario with less value which there wont be any burden on server because for server side sorting i don't have a specific UI in my mind but maybe something to let user choose options like "asc" , "desc" , ...

### Response

**Marin Bratanov** answered on 04 Feb 2020

Hello Khashayar, The combo box (or Blazor, for that matter) does not have the concept of local and remote data - all the data is in the view model, and this is what the combo box displays. This data may be generated, or fetched from a service, in all cases it ends up as a local variable in the view model. Thus, to sort the items in the combo box according to your desired logic, you must sort its data source. This is also applicable for cases where you have added/removed items dynamically. If there is a lot of data so the user may benefit from sorting, I can suggest the following alternatives: enable filtering: [https://demos.telerik.com/blazor-ui/combobox/filtering](https://demos.telerik.com/blazor-ui/combobox/filtering) if there is too much data to store all of it in the view model, implement custom filtering: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) if you need a lot of UI for filtering, sorting and to display alot of data, consider using a grid with selection enabled: [https://demos.telerik.com/blazor-ui/grid/selection.](https://demos.telerik.com/blazor-ui/grid/selection.) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 04 Feb 2020

Hello, I made an example for you that showcases how you can: use observable collections to update the dropdown data in real time use our DataSourceRequest to add custom sorting use the OnRead event to apply the custom sorting, and a separate button click to add items to the data source @using Telerik.DataSource.Extensions
@using System.Collections.ObjectModel

@SelectedValue
<br />
<TelerikComboBox Data="@CurrentOptions" OnRead=@ReadItems
Filterable="true" FilterOperator="@StringFilterOperator.Contains" Placeholder="Find a car by typing part of its make" @bind-Value="@SelectedValue" ValueField="Id" TextField="Make">
</TelerikComboBox>

<TelerikButton OnClick="@AddCar">Add Car</TelerikButton>

@code { public int? SelectedValue { get; set; }
ObservableCollection<Car> AllOptions { get; set; }

ObservableCollection<Car> CurrentOptions { get; set; } void AddCar ( ) { //add data to the main list of data AllOptions.Add( new Car { Id=AllOptions.Count + 1, Make="ZZ My Car " + ( AllOptions.Count + 1 ) }); //use observable collections so the component can pick up the data //we also move this to the current collection for the case when the user has not opened the dropdown yet //in this case the current data source is already defined and it does not otherwise know about the new item CurrentOptions.Add(AllOptions[AllOptions.Count - 1 ]);
} protected async Task ReadItems ( ComboBoxReadEventArgs args ) {
Console.WriteLine( "aa" ); //generate the big data source that we want to narrow down for the user //in a real case you would probably have fetched it in OnInitializedAsync if (AllOptions==null )
{
AllOptions=new ObservableCollection<Car>
{ new Car { Id=1, Make="Honda" }, new Car { Id=2, Make="Opel" }, new Car { Id=3, Make="Audi" }, new Car { Id=4, Make="Lancia" }, new Car { Id=5, Make="BMW" }, new Car { Id=6, Make="Mercedes" }, new Car { Id=7, Make="Tesla" }, new Car { Id=8, Make="Vw" }, new Car { Id=9, Make="Alpha Romeo" }, new Car { Id=10, Make="Chevrolet" }, new Car { Id=11, Make="Ford" }, new Car { Id=12, Make="Cadillac" }, new Car { Id=13, Make="Dodge" }, new Car { Id=14, Make="Jeep" }, new Car { Id=15, Make="Chrysler" }, new Car { Id=16, Make="Lincoln" }
};
} //add a sort operator to the request. In a more copmlex model this can be another field that is not directly shown if (args.Request.Sorts.Count==0 )
{
args.Request.Sorts.Add( new Telerik.DataSource.SortDescriptor
{
Member="Make",
SortDirection=Telerik.DataSource.ListSortDirection.Descending
});
} //use Telerik extension methods to filter the data source based on the request from the component var datasourceResult=AllOptions.ToDataSourceResult(args.Request);
CurrentOptions=new ObservableCollection<Car>((datasourceResult.Data as IEnumerable<Car>));
} public class Car { public int Id { get; set; } public string Make { get; set; }
}
} Regards, Marin Bratanov
