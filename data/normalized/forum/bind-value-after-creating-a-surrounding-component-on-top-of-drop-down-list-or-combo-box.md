# Bind Value After Creating a surrounding component on top of drop down list or combo box

## Question

**joh** asked on 22 Apr 2021

I am trying to create a reusable component which binds to a data service where I pass the binded value to the parent and get the data from the Telerik Drop List / Combo box, etc. What am I missing in regards to getting this data back up the the parent model? When I submit, it provides a value of null. #StillLearning Code example concept: Razor: @inherits ActiveProviderTypeDropDownListBase <TelerikComboBox Data="@ProviderTypes" OnRead="@OnReadAsync" TValue="string" TItem="string" AllowCustom="true" @bind-Value="@BindValue" Width="100%" /> Base: public class ActiveProviderTypeDropDownListBase : ComponentBase { [Inject] ProviderDataService ProviderDataService { get; set; } [Parameter] public string Width { get; set; } [Parameter] public string BindValue { get;set; } public List<string> ProviderTypes { get; set; } public async Task OnReadAsync() { ProviderTypes=await ProviderDataService.GetActiveProviderTypesAsync(); } } Reusable Component For Elsewhere Elsewhere: <ActiveProviderTypeDropDownList Width="100%" BindValue="DialogBaseService.ValueToCreate.ProviderTypeName"

## Answer

**Marin Bratanov** answered on 22 Apr 2021

Hello John, I recommend you start by reviewing this article on the core concepts of value and data binding: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding.](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding.) What the provided snippet is missing is the two-way binding of values. Put shortly, you need something like this in the dropdown component [Parameter] public string BindValue { get;set; } [Parameter] public EventCallback<string> BindValueChanged { get;set; } and so you can use the following in the parent component <ActiveProviderTypeDropDownList Width="100%" @bind- BindValue="DialogBaseService.ValueToCreate.ProviderTypeName" /> And the last bit is that you will need to raise the BindValueChanged as needed, when the value in the child component changes, or at another event suitable for your case. You can find more details and examples in the MSDN documentation - the Binding with component parameters section of the ASP.NET Core Blazor data binding article provides the core information. Regards, Marin Bratanov

### Response

**johnbolt** answered on 23 Apr 2021

Thanks for guidance.
