# Color code dropdownlist item

## Question

**Kev** asked on 19 Sep 2023

Is there a way to have a dropdownlist item be a color based on some criteria?

## Answer

**Tino** answered on 20 Sep 2023

Hello Kevin, for sure it is possible. an appropriate css should you then still compile in this case here colorIndicatorDropDownListClass with appropriate values... dropdownList like this: <TelerikDropDownList Data="_enumList" ValueField="Key" TextField="Value" @bind-Value="@Value" ScrollMode="DropDownScrollMode.Virtual" Filterable="@IsFilterAble" FilterOperator="StringFilterOperator.Contains" ItemHeight="35" PageSize="10" Enabled="@(!IsReadOnly)" Class="colorIndicatorDropDown">
<DropDownListSettings>
<DropDownListPopupSettings Class="colorIndicatorDropDownListClass" />
</DropDownListSettings>
<ItemTemplate>
@{ var itemSelection=context.Key;
<span class="colorIndicator">
<i class="fa-solid fa-circle @itemSelection"></i>
<label>@context.Value</label>
</span>

}
</ItemTemplate>
<ValueTemplate>
@{ var i=context.Key;
<span class="colorIndicator @i">
<i class="fa-solid fa-circle @i"></i>
<label class="@i">@context.Value</label>
</span>
}
</ValueTemplate>
</TelerikDropDownList>

### Response

**Hristian Stefanov** answered on 20 Sep 2023

Hello, I confirm that Tino's approach is indeed valid. On a related note, there's an alternative method that eliminates the need for using an ItemTemplate – you can leverage the OnItemRender event. Feel free to check out our documentation for more details and a practical example: OnItemRender Docs. Regards, Hristian Stefanov Progress Telerik

### Response

**Kevin** commented on 25 Sep 2023

I tried both Tino's and your approach using OnItemRender and the only problem is that the items initially look good, however when I select an item the list then looks like it resets itself without the criteria style being applied. Basically it does not retain the style.

### Response

**Tino** commented on 26 Sep 2023

Hello Kevin, i have created a small repo. Here you find the way how I solved it with the colored dropdown. May it will help you a bit. ColoredDropdown Repo

### Response

**Rob** commented on 27 Jan 2025

Tino, I was unable to get this to work per link to OnItemRenderDocs. The link to the Repo shows 404. What I get is a blue background on every entry in the list (no idea where that came from?) The code is take from your sample doc: <style>.customized-inactive { font-weight: lighter; color: gray;
} </style> <TelerikDropDownList Id="@Id" Width="@Width" Data="@_bookerList" OnItemRender="@OnItemRenderHandler" Enabled="@Enabled" TextField="Name" DefaultText="Select Shipper" ValueField="ShipperId" Filterable="true" FilterOperator="@_filterOperator" Value="@Value" ValueExpression="@( ()=> Value )" ValueChanged="@( (int? newValue)=> OnSelectionChanged(newValue) )"> </TelerikDropDownList> and the code: private void OnItemRenderHandler ( DropDownListItemRenderEventArgs<BookerModel> args ) { if (args.Item !=null )
{
BookerModel booker=args.Item; if (booker.IsActive==false )
{
args.Class="customized-inactive";
}
}
} What I expected from this is the dropdown list would show lighter text that is gray for those items that are set as Inactive (booker.IsActive==false). As you can see, I didn't get that, not even close? Rob.

### Response

**Tino** commented on 28 Jan 2025

Hi Rob, the repo is accessible and available again. Hope it helps you move forward. much success! Tino

### Response

**Rob** commented on 28 Jan 2025

Hi Tino, Unfortunately your code sample doesn't work when I adapt to my project. It also doesn't use OnItemRenderHandler as provided in your documentation. In addition the following documentation will crash with a reload when I try to execute the example. To add to my confusion. When I remove all the List item color change based on value code, I still get the same odd dropdownlist with every item having a blue background? I have 100's of other dropdownlist that don't exhibit this behavior and I've gone over every aspect I can think of to try to figure out why this (and only this) dropdownlist renders differently? I'm beginning to think that "IsActive" property of my model/class definition is somehow a reserved word that you folks use during rendering of a dropdownlist?? Rob.

### Response

**Rob** commented on 29 Jan 2025

Hi Tino, Got it working per your original documentation here... this approach is actually very easy and preferred. Contractors I was working with were referencing the wrong model property for ValueField in the dropdownlist. It's interesting that this didn't cause an exception, instead it rendered the TextField from the datasource but the ValueField there was no underlying model property so as a side affect, all list items where "selected" (hence the blue background as in above image). Not sure if this is how you folks want to handle and error like this, the side affect seem unintentional, triggering an exception would be my expectation. Rob.
