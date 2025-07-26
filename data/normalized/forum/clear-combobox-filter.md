# Clear Combobox Filter

## Question

**Eug** asked on 01 Jun 2020

Is there a way to reset filter for combo box? I have two comboboxes with filters. I want to reset filter for second combobox when value in first combo box is changed.

## Answer

**Svetoslav Dimitrov** answered on 02 Jun 2020

Hello Eugene, You could use the OnChange event (more information here: [https://docs.telerik.com/blazor-ui/components/combobox/events#onchange](https://docs.telerik.com/blazor-ui/components/combobox/events#onchange) ) for the ComboBox which resets the value for the second ComboBox. In its event handler you can set the property to which the Value or @bind-Value is bound to null. I have created a short code snippet to illustrate that. You can find more examples of the core concept here: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-cascading](https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-cascading) Selected value: @selectedValue
<br />

<TelerikComboBox Data="@myComboData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue" OnChange="@OnChangeHandler" Placeholder="Select an item..." ClearButton="true" Filterable="true">
</TelerikComboBox>

<br />

@SelectedValue
<br />

<TelerikComboBox Data="@Data" Filterable="true" Placeholder="Find product by typing part of its name" @bind-Value="@SelectedValue" TextField="ProductName" ValueField="ProductId">
</TelerikComboBox>

@code { void OnChangeHandler ( object input ) { int userInput=( int )input;

SelectedValue=null;
} IEnumerable<MyDdlModel> myComboData=Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x }); int selectedValue { get; set; }=3; //usually the current value should come from the model data //in a real case, the model is usually in a separate file //the model type and value field type must be provided to the dropdpownlist public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
} //second combo public List<Product> Data { get; set; } public int? SelectedValue { get; set; } protected override void OnInitialized ( ) {
List<Product> products=new List<Product>(); for ( int i=0; i <20; i++)
{
products.Add( new Product()
{
ProductId=i,
ProductName=$"Product {i} " });
}

Data=products; base.OnInitialized();
} public class Product { public int ProductId { get; set; } public string ProductName { get; set; }
}
} Regards, Svetoslav Dimitrov

### Response

**Eugene** answered on 02 Jun 2020

In this example filter doesn't show how to reset the filter. Let me give you more details. let's modify your example a little bit, just method OnChangeHandler void OnChangeHandler( object input) { int userInput=( int )input; //select "related" item in products //simplified logic how to find related item (match by id) SelectedValue=userInput; StateHasChanged(); } So when user select any value in first combobox it will select related product in second combobox. Works good. Then do next: type "product 5" in second combobox (it will filter the list to one value) - pick value from the list. (now combobox2 filter is active) Then try to change first combobox to any value - "select related product" logic is not working any more for any product that doesn't match filter criteria "product 5". Looks like combobox2 filter is still active and filtering out data source. Even if user click "clear filter" button on second combobox - filter is still active. The only way to make this example works - type something in second combobox and erase what you typed to see unfiltered "combo list" - then filter is gone and example works. I attached animated gif that shows what I just described. What I am looking is - when user change value in first combobox - "clear filter" in second combobox and select related product. Please advice, Thanks Eugene

### Response

**Svetoslav Dimitrov** answered on 10 Jun 2020

Hello Eugene, After discussions with our Dev team we have discovered this to be a bug. What happens is that when Data and Value are populated, firstly our logic for clearing the Value is applied for example selectedValue is 0, than the Value is set and selectedValue=2, the ComboBox displays that successfully, but the value printed on the view remains 0. That being said, I have created a Bug Report on our Feedback Portal (link here: [https://feedback.telerik.com/blazor/1471160-selection-should-not-reset-value-on-data-change](https://feedback.telerik.com/blazor/1471160-selection-should-not-reset-value-on-data-change) ). I have given a Vote on your behalf and you can Follow it for email notifications. As attached file, you can see two examples on how this should work when the bug is fixed. Regards, Svetoslav Dimitrov
