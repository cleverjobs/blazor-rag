# Dynamic Change datasource for the Blazor ComboBox

## Question

**Mar** asked on 27 Aug 2021

Hi I would like to change the datasouce dynamic for a combobox. I have two radiobuttons on top of the CB. The chosen radio button should change the datasource. What are my options? Two Comboboxes stacked? mange visibility base on the radio button value?

## Answer

**Matthias** answered on 27 Aug 2021

Hello, here is one way I implement this in similar scenarios. Info: this is a possible solution, alternatively you can use css to show or hide one or the other ComboBox. <TelerikRadioGroup Data="@Choices" @bind-Value="@Choice"> </TelerikRadioGroup> @{
if (Choice=="order")
{ <TelerikComboBox Value="@SelectedOrder.OrderId" Data="OrdersList" TextField="@nameof(Order.Product)" ValueField="@nameof(Order.OrderId)"> </TelerikComboBox> }
else
{ <TelerikComboBox Value="@SelectedSales.SalesId" Data="SalesList" TextField="@nameof(Sales.Product)" ValueField="@nameof(Sales.SalesId)"> </TelerikComboBox> }
} code public List <string> Choices { get; set; }=new List<string>() { "order", "sale" }; public string? Choice { get; set; } public List<Order> OrdersList { get; set; } public List<Sales> SalesList { get; set; } public Order SelectedOrder { get; set; } public Sales SelectedSales { get; set; } protected override void OnInitialized ( ) {
Choice="order";

OrdersList=new List<Order>();
OrdersList.Add( new Order() {OrderId=1, Product="Order 1" });
OrdersList.Add( new Order() {OrderId=2, Product="Order 2" });
SelectedOrder=OrdersList.FirstOrDefault();

SalesList=new List<Sales>();
SalesList.Add( new Sales() {SalesId=1, Product="Sale 1" });
SalesList.Add( new Sales() {SalesId=2, Product="Sale 2" });
SelectedSales=SalesList.FirstOrDefault();
} public class Order { public int OrderId { get; set; } public string Product { get; set; }
} public class Sales { public int SalesId { get; set; } public string Product { get; set; }
} regards Matthias

### Response

**Marin Bratanov** answered on 28 Aug 2021

Hi, You can simply replace the Data collection with a new one, assuming the other settings need to stay the same. You can see how this works here: [https://docs.telerik.com/blazor-ui/components/combobox/refresh-data.](https://docs.telerik.com/blazor-ui/components/combobox/refresh-data.) If you also need to change settings, Mattias' approach is valid. Regards, Marin Bratanov Progress Telerik
