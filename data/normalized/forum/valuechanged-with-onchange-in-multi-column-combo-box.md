# ValueChanged with OnChange in multi column combo box

## Question

**Dou** asked on 31 May 2023

My goal is to have a multi column combo box such that the list changes as the user types in the combo box (by hitting an API) and then when the user clicks one of the items in the drop down I'd like to show the value from one of the columns. I've gotten the first part working but the issue arises when the user clicks on an item. With the code below what I'm observing is that when the user types in the combo box, the ValueChanged handler fires and gets sent the text the user has typed which allows me to call the API with that value. The drop down displays the data as I expect. So far so good. Then when the user clicks on an item in the drop down, the ValueChanged handler fires not with the text but with the Id from my model since the ValueField is set to the Id. But I'm also getting an invalid cast error in the browser console. If I change the ValueField to a string, say OrderNumber, the ValueChanged and OnChange handlers fire with the OrderNumber value and I no longer get the error, but the problem is that OrderNumber is not unique so I can't find the distinct item in the collection. So the question is, how do I send the typed text into the ValueChanged handler and send the Id into the OnChange handler? Thanks in advance for your help. <TelerikMultiColumnComboBox Data="_orders" AllowCustom="true" Value="_selectedOrder" ValueExpression="(()=> _selectedOrder)" ValueChanged="@(async (string order)=> await OrderValueChangedAsync(order))" OnChange="OrderChangedHandler" ValueField="@nameof(OrderDto.Id)" TextField="@nameof(OrderDto.OrderNumber)"> <MultiColumnComboBoxColumns> <MultiColumnComboBoxColumn Field="@nameof(OrderDto.Source)" Title="Source"> </MultiColumnComboBoxColumn> <MultiColumnComboBoxColumn Field="@nameof(OrderDto.DeliverOn)" Title="Deliver On"> </MultiColumnComboBoxColumn> <MultiColumnComboBoxColumn Field="@nameof(OrderDto.OrderNumber)" Title="Order Number"> </MultiColumnComboBoxColumn> <MultiColumnComboBoxColumn Field="@nameof(OrderDto.Suffix)" Title="Suffix"> </MultiColumnComboBoxColumn> </MultiColumnComboBoxColumns> <MultiColumnComboBoxSettings> <MultiColumnComboBoxPopupSettings Width="600px" /> </MultiColumnComboBoxSettings> </TelerikMultiColumnComboBox> private string _selectedOrder; private async Task OrderValueChangedAsync ( string orderNumber ) { try {
Console.WriteLine( $"ValueChanged fired with value {orderNumber} " ); if (orderNumber==null || orderNumber.Length <5 )
{
_orders=new (); // Don't load orders until the user has typed in at least 4 characters so we don't bring back too many orders return;
} if (_activity.Type=="C" )
{
_orders=await APIService.CallAPIAsync<List<OrderDto>>( $"RMOActivity/GetSalesOrders?orgCode={AppState.SelectedDivision.OrgCode} &orderNumber={orderNumber} ", null, HttpMethod.Get);
} else {
_orders=await APIService.CallAPIAsync<List<OrderDto>>( $"RMOActivity/GetPurchaseOrders?orgCode={AppState.SelectedDivision.OrgCode} &purchaseOrderNumber={orderNumber} ", null, HttpMethod.Get);
}
} catch (Exception e)
{
LogError( "Error loading orders", e);
} finally {
Console.WriteLine( $"ValueChanged finished with value {orderNumber} " );
}
} private void OrderChangedHandler ( object order ) { try {
Console.WriteLine( $"OnChange fired with value {(order==null? "null": order.ToString())} " ); if (order !=null )
{
_selectedOrder=( string )order;
}
Console.WriteLine( $"OnChange finished with value {(order==null? "null": order.ToString())} " );
} catch (Exception e)
{
LogError( "Error loading order", e);
}
} public class OrderDto { public int Id { get; set; } public string Source { get; set; } public DateOnly? DeliverOn { get; set; } public string OrderNumber { get; set; } public string Suffix { get; set; } public string CustomerOrVendorNumber { get; set; } public string ShipToOrVendorCode { get; set; }
}

## Answer

**Dimo** answered on 01 Jun 2023

Doug, do you really need custom values that do not exist in the data source? If not, then use the built-in filtering instead of the current custom logic in ValueChanged. If you have too many orders, then bind the component with OnRead and still use the built-in filtering. Here is a relevant example with ComboBox filtering and OnRead. If yes, then adjust the logic in ValueChanged and OnChange, so that you know if the current value is custom or not.

### Response

**Doug** commented on 01 Jun 2023

Thanks Dimo. In the meantime I did get this working by changing my Id property to a string and tacking on a character sequence that a user is unlikely to type and so in the ValueChanged handler I can distinguish between the user typing in the combo box vs selecting an item in the list. Your solution using OnRead seems more elegant and I will play with that but maybe you can help me understand something. Why does the ValueChanged handler get sent two different data fields? Sometimes it gets sent the text the user types and sometimes it gets sent an Id. That seems strange to me and makes me think I may have something set wrong in the parameters for the combo box.

### Response

**Dimo** commented on 01 Jun 2023

>> "Why does the ValueChanged handler get sent two different data fields? Sometimes it gets sent the text the user types and sometimes it gets sent an Id." This is because AllowCustom="true". Sometimes you get a custom value and sometimes you get the ID of a selected predefined item. My idea was to disable custom values and use only filtering instead.
