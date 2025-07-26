# How to configure autocomplete / Bind to a list of objeckt

## Question

**Jen** asked on 19 Mar 2024

Hello, i want to bind the autocomplete to a list of object. But the data in the template is empty: The code is this: Kunde: <TelerikAutoComplete Data="@DataCustomer" TItem="@Customer" ValueChanged="@((string value)=> OnComboCustomerValueChanged(value))"> <ItemTemplate> @(nameof(Customer.customerName)) </ItemTemplate> <FooterTemplate> <h6> Anzahl: @DataCustomer.Count() </h6> </FooterTemplate> <NoDataTemplate> <div class="no-data-template"> <TelerikSvgIcon Icon="@SvgIcon.FilesError" Size="@ThemeConstants.SvgIcon.Size.Large"> </TelerikSvgIcon> <p> No items available </p> </div> </NoDataTemplate> </TelerikAutoComplete> protected override async Task OnInitializedAsync () {
List<Customer> customers=new List<Customer>();
customers.Add( new Customer()
{
customerId="",
customerName="" });

DataCustomer=customers;
} private void OnComboCustomerValueChanged ( string value ) {
ComboCustomerValue=value; if ( value!=null && value.Length> 3 )
{ if (DataCustomer==null )
{
List<Customer> Data=new List<Customer>();
} if (DataCustomer.FirstOrDefault(item=> item.customerId==value.ToString())==null )
{
IO.Swagger.Api.CustomerApi customerApi=new IO.Swagger.Api.CustomerApi( "[https://server:8080"](https://server:8080") ); foreach ( var itemsFound in customerApi.ApiV1CustomerIdGet(Convert.ToInt32( value )))
{ if (DataCustomer.FirstOrDefault(item=> item.customerId==itemsFound.Id.ToString())==null )
{
DataCustomer.Add( new Customer()
{
customerId=itemsFound.Id.ToString(),
customerName=itemsFound.Name + @" (" + itemsFound.Id.ToString() + @")" });
}
}

}
}
} What have i made wrong? Kind regards Jens

## Answer

**Marco** answered on 20 Mar 2024

Hy Jens, I've had the same problem in the past too. Maybe you can try to setting the TelerikAutocomplete component's DebounceDelay property to 0. King regards, Marco

### Response

**Jens** commented on 21 Mar 2024

Hello Marco, thank you for your support. I have changed the DebounceDelay to 0, but the problem is the same. Kind regards Jens

### Response

**Nadezhda Tacheva** answered on 21 Mar 2024

Hi Jens and Marco, The issue in this case is that the value is not extracted from the context that the ItemTemplate provides. This context represents the current item and one should use it to get and display the needed field information in the template. For example: <TelerikAutoComplete Data="@Suggestions" ValueField="@( nameof(SuggestionsModel.Suggestion) )" @bind-Value="@TheValue"> <ItemTemplate> Templated content for <strong> @context.Suggestion </strong> suggestion </ItemTemplate> </TelerikAutoComplete> @code {
string TheValue { get; set; }

List <SuggestionsModel> Suggestions { get; set; }=new List <SuggestionsModel> {
new SuggestionsModel { Suggestion="first", SomeOtherField=1 },
new SuggestionsModel { Suggestion="second", SomeOtherField=2 },
new SuggestionsModel { Suggestion="third", SomeOtherField=3 }
};

public class SuggestionsModel
{
public string Suggestion { get; set; }//the auto complete needs only the string field
public int SomeOtherField { get; set; }
}
} Note: This configuration will work as you will be programmatically controlling what should be displayed in the popup through the ItemTemplate. If you decide to not use this template, you should also set ValueField of the component. Otherwise, it will not know what field data to display. See "Databind to a model" for more details. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Jens** commented on 22 Mar 2024

Hello Nadezhda, thank you for your support. I will need a bit time to test your hint. Kind regards Jens

### Response

**Jens** commented on 08 Apr 2024

Hello Nadezhda, now it looks so: This is the code: <TelerikAutoComplete Data="@dataCustomer" @bind-Value="@customerId" ValueField="@( nameof(Customer.customerId) )">
<ItemTemplate>
@( nameof (Customer.customerName))
</ItemTemplate>
<FooterTemplate>
<h6>Anzahl: @dataCustomer.Count()</h6>
</FooterTemplate>
<NoDataTemplate>
<div class="no-data-template">
<TelerikSvgIcon Icon="@SvgIcon.FilesError" Size="@ThemeConstants.SvgIcon.Size.Large"></TelerikSvgIcon>
<p>No items available</p>
</div>
</NoDataTemplate>
</TelerikAutoComplete>

@code { public MarkupString message; public MarkupString userName; public string userId; public List<Customer>? dataCustomer { get; set; } public List<Stacker> dataRepository { get; set; } public string customerId { get; set; }=""; public string repositoryId { get; set; }=""; public string repositoryValue { get; set; }=""; protected override async Task OnInitializedAsync () {
List<Customer> customers=new List<Customer>(); if (customers.Count==0 )
{
List<Models.Customer> customer=await JupiterClient.Api.V1.Customer.GetAsync(x=> x.QueryParameters=null ); foreach ( var item in customer)
{
customers.Add( new Customer()
{
customerId=item.Id.ToString(),
customerName=item.Name + @" (" + item.Id.ToString() + @")" }); if (customers.Count> 999 )
{ break;
}
}
}

}
} What have i make wrong? Kind regards Jens

### Response

**Nadezhda Tacheva** commented on 11 Apr 2024

Hi Jens, Do not use @(nameof(Customer.customerName)) in the ItemTemplate: <ItemTemplate> @(nameof(Customer.customerName)) </ItemTemplate> Use the customerName field value from the context instead: <ItemTemplate> @context.customerName </ItemTemplate>

### Response

**Jens** answered on 12 Apr 2024

Hello Nadezhda, thanks, this helps. Kind regards Jens
