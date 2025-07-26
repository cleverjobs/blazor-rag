# Populate Grid from Model

## Question

**con** asked on 15 Jun 2020

Hello, I'm having the List of <Model> which is populated by call to database: private List<OrdersModel> orders; protected override async Task OnInitializedAsync() { orders=await _db.GetOrders(); } How do I fill Grid with orders info? This is how my Model looks like: public class OrdersModel { public string OrdNo { get; set; } public string OrdStatus { get; set; } } Please advise.

## Answer

**Marin Bratanov** answered on 15 Jun 2020

Hi, You just point the Data parameter of the grid to the orders collection. You can find an example here: [https://docs.telerik.com/blazor-ui/components/grid/overview.](https://docs.telerik.com/blazor-ui/components/grid/overview.) You can also scroll a little down to the "Data Binding" section for more details, examples and links. If you don't want to define the columns yourself, you can have the grid generate them for you: [https://docs.telerik.com/blazor-ui/components/grid/columns/auto-generated.](https://docs.telerik.com/blazor-ui/components/grid/columns/auto-generated.) Regards, Marin Bratanov

### Response

**const** answered on 16 Jun 2020

Figured it out, thank you!
