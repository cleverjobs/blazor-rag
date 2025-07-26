# How to change model bind to EditContext and FluentValidator validator

## Question

**Mar** asked on 26 Jan 2023

I have a dropdownlist on my form, to select products from. When I load a new product I get the following error: Cannot validate instances of type 'ManualCertificateTrade'. This validator can only validate instances of type 'ManualTradeModel' ManualCertificateTrade is my razor view and ManualTradeModel is the model I load from my API. This is my code behind class. public partial class ManualCertificateTrade {
[ Inject ] public IManualCertificateTradeService TradeService { get; set; } private EditContext EditContext { get; set; } private ManualTradeModel ManualTradeModel { get; set; }=new (); private ManualTradeValidator TradeValidator { get; set; }=new (); private List<Product> Products { get; set; }=new (); private int SelectedProductId { get; set; } protected override async Task OnInitializedAsync ( ) {
EditContext=new EditContext(ManualTradeModel);
Products=await TradeService.GetProducts();
} private async Task ProductChangedEvent ( object id ) { if (id is int productId)
{
TradeValidator=null;
SelectedProductId=productId;
ManualTradeModel=await TradeService.GetNewManualTrade(productId);
EditContext=new EditContext(ManualTradeModel);
TradeValidator=new ();
}
}
}

### Response

**Hristian Stefanov** commented on 31 Jan 2023

Hi Martin, I confirm that the provided part of the actual code seems OK. Still, it is hard to tell where the problem comes from without the other parts of the configuration. In order to help you get this up and running, I'll need a little bit more information. Can you please send me a runnable sample, maybe a REPL that shows the other parts of the configuration as well? That will allow me to see where the validation happens and investigate further the situation with runnable code. I look forward to hearing from you. On a side note, make sure this line " TradeService.GetNewManualTrade(productId); " returns the correct model. Here is also an example you may have seen of such third-party validation that you can use as a comparison: Fluen Validation sample. Kind Regards, Hristian

## Answer

**Martin Herløv** answered on 31 Jan 2023

The dropdown are not bound to any field on the model. That was causing the error. The dropdown is a list of products. When you choose a product I load a DTO from the server and bind it to the form.
