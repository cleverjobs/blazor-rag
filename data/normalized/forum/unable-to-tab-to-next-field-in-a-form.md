# Unable to tab to next field in a form

## Question

**Mar** asked on 30 Jan 2023

After I select a product I tab to get to the Trade date field. The cursor get's there, but then move back to the product field, why? @page "/ManualCertificateTrade"
@attribute [Authorize]
@using Ibex.Shared.Domain <h3> Manual Certificate Trade </h3> <TelerikForm Model="@TradeModel" OnValidSubmit="TradeModelValidSubmit" Columns="1" ColumnSpacing="15px" Width="800px"> <FormValidation> <FluentValidationValidator /> </FormValidation> <FormItems> <FormGroup LabelText="Product" Columns="2" ColumnSpacing="15px"> <FormItem> <Template> <label for="Products"> Product </label> <TelerikDropDownList TValue="int" TItem="Product" Id="Products" Data="@Products" TextField="Name" ValueField="Id" OnChange="@ProductChangedEvent" Value="@SelectedProductId" ValueExpression="@(()=> SelectedProductId)" Filterable="true" DefaultText="Select a product" FilterOperator="StringFilterOperator.Contains" /> @* <TelerikValidationMessage For="@(()=> TradeModel.ProductId)" /> *@</Template> </FormItem> <FormItem LabelText="Nav" Field="@nameof(TradeModel.NavSellPrice)" Enabled="false" /> <FormItem LabelText="Issue price" Field="@nameof(TradeModel.StandardBuyPrice)" Enabled="false" /> <FormItem LabelText="Redemption price" Field="@nameof(TradeModel.StandardSellPrice)" Enabled="false" /> <FormItem LabelText="Other Issue price" Field="@nameof(TradeModel.OtherBuyPrice)" Enabled="false" /> <FormItem LabelText="Other Redemption price" Field="@nameof(TradeModel.OtherSellPrice)" Enabled="false" /> </FormGroup> <FormGroup LabelText="Dates" Columns="2" ColumnSpacing="15px"> <FormItem> <Template> <label for="TradeDate"> Trade date </label> <TelerikDatePicker Id="TradeDate" @bind-Value="TradeModel.TradeDate" Format="dd-MM-yyyy" /> <TelerikValidationMessage For="@(()=> TradeModel.TradeDate)" /> </Template> </FormItem> <FormItem> <Template> <label for="SettlementDate"> Settle date </label> <TelerikDatePicker Id="SettlementDate" @bind-Value="TradeModel.SettlementDate" Format="dd-MM-yyyy" /> <TelerikValidationMessage For="@(()=> TradeModel.SettlementDate)" /> </Template> </FormItem> </FormGroup> <FormGroup LabelText="Price" Columns="2" ColumnSpacing="15px"> <FormItem Hint="Negative quantity is client sell (redemption)"> <Template> <label for="Quantity"> Quantity </label> <TelerikNumericTextBox Id="Quantity" @bind-Value="TradeModel.Quantity" /> <div class="k-form-hint"> Negative quantity is client sell (redemption) </div> <TelerikValidationMessage For="@(()=> TradeModel.Quantity)" /> </Template> </FormItem> @* <FormItem LabelText="Quantity" Field="@nameof(ManualTrade.Quantity)" Hint="Negative quantity is client sell (redemption)" /> *@<FormItem LabelText="Nav override (Invision)" Field="@nameof(TradeModel.NavOverride)" /> <FormItem LabelText="Buy price" Field="@nameof(TradeModel.ManualBuyPrice)" Enabled="@(TradeModel.Quantity> 0)" /> <FormItem LabelText="Other Buy Cost %" Field="@nameof(TradeModel.OtherBuyCost)" Enabled="@(TradeModel.Quantity> 0)" /> <FormItem LabelText="Sell price" Field="@nameof(TradeModel.ManualSellPrice)" Enabled="@(TradeModel.Quantity <0)" /> <FormItem LabelText="Other Sell Cost %" Field="@nameof(TradeModel.OtherSellCost)" Enabled="@(TradeModel.Quantity <0)" /> </FormGroup> <FormGroup LabelText="Customer information for account-holding fund" Columns="2" ColumnSpacing="15px"> <FormItem LabelText="Customer" Field="@nameof(TradeModel.Customer)" Hint="Ask FundAccounting" /> <FormItem LabelText="Customer account" Field="@nameof(TradeModel.CustomerAccount)" Hint="Ask FundAccounting" /> </FormGroup> </FormItems> </TelerikForm> using Blazored.LocalStorage; using Ibex.Client.Services; using Ibex.Shared.Domain; using Ibex.Shared.DTO; using Microsoft.AspNetCore.Components; namespace Ibex.Client.Pages; public partial class ManualCertificateTrade {
[ Inject ] public IManualCertificateTradeService TradeService { get; set; }
[ Inject ] public ILocalStorageService LocalStorageService { get; set; } private ManualTradeModel TradeModel { get; set; }=new (); private List<Product> Products { get; set; }=new (); private int SelectedProductId { get; set; } private string SelectedProductName { get; set; } private bool IsModalVisible { get; set; } private decimal OtherBuyCost { get; set; } private decimal OtherSellCost { get; set; } protected override async Task OnInitializedAsync ( ) {
Products=await TradeService.GetProducts();
} private async Task ProductChangedEvent ( object id ) { if (id is int productId)
{
SelectedProductId=productId;
SelectedProductName=Products.FirstOrDefault(x=> x.Id==productId)?.Name;
TradeModel=await TradeService.GetNewManualTrade(productId);
OtherBuyCost=TradeModel.OtherBuyCost;
OtherSellCost=TradeModel.OtherSellCost;
}
} private void TradeModelValidSubmit ( ) {
IsModalVisible=true;
} private async Task CreateTrade ( ) { var success=await TradeService.CreateManualTrade(TradeModel);
Console.WriteLine( $"Trade Created {success} " );
}

}

## Answer

**Yanislav** answered on 02 Feb 2023

Hello Martin, Thank you for the provided code snippets. I've reviewed the configuration you've shared and it looks OK. To test the behavior, I created a REPL example in which a similar scenario is implemented but I was not able to reproduce the issue. On my side, the form keyboard navigation seems to be working correctly. May I ask you to create an example or edit the REPL sample I've shared above so the problem is reproducible and send it back to me for additional review? Thus, I will be able to investigate the problem and try to find a possible solution. Regards, Yanislav

### Response

**Martin Herløv** commented on 02 Feb 2023

Thanks for creating the REPL. The only difference is that you are binding the dropdown to a field on the model. I don't I will start with modifying your example to see if I can reproduce the problem

### Response

**Indra** commented on 03 Feb 2023

I can reproduce the issue using Yanislav REPL [https://blazorrepl.telerik.com/cnOQamar412jo3mR32](https://blazorrepl.telerik.com/cnOQamar412jo3mR32) probably related to this DropDownList lost focus too ( [https://www.telerik.com/forums/bug-dropdownlist-tab-key-issue-when-using-mouse-to-select-item](https://www.telerik.com/forums/bug-dropdownlist-tab-key-issue-when-using-mouse-to-select-item) ). This is the step to reproduce the DateTimePicker lost focus

### Response

**Martin Herløv** commented on 03 Feb 2023

Thanks for proving that I am not crazy 😊

### Response

**Yanislav** commented on 07 Feb 2023

Hello, Thank you for the additional information. I was able to reproduce the issue. It seems like the issue stems from the DateTimePicker component regardless of whether or not it is placed in a Form. When you just click on the "NOW" button, the focus is lost from thе component. However, the problem seems to arise occasionally. Therefore I have logged a bug report on your behalf: [https://feedback.telerik.com/blazor/1596645-datetimepicker-loses-focus-when-the-now-button-is-clicked](https://feedback.telerik.com/blazor/1596645-datetimepicker-loses-focus-when-the-now-button-is-clicked) I added your votes there to increase its popularity as we are prioritizing the fixes based on the community demand along with their severity. In the meantime, if we can find a possible workaround, we will post it immediately as a comment in the public post. Please accept our apologies for the inconvenience caused.
