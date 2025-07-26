# Open TelerikPopup in Grid Cell

## Question

**Chr** asked on 12 Feb 2024

I'm trying to open a popup from a button in a grid cell. The button work and opens the popup, but it opens in the top left corner of the screen, rather than anchored to the button. I would love to get it to the right of the icon, with a little space in between. In my grid column, I've added a button to open the popup <GridColumn Field="L1" Title="Level 1" FieldType="@typeof(string)"> <Template> @{
var item=(TaxonomyGrid)context;
}
@item.L1 <TelerikButton OnClick="@(()=> PopupRef.Popup_OpenAsync())" Class="popup-target" Icon="@SvgIcon.User" Title="The name of the owner" /> </Template> <FilterMenuTemplate> <div> <TelerikMultiSelect Width="300px" AutoClose=false Data="@L1List" TextField="Name" ValueField="TaxonomyId" OnChange="@(()=> FilterGrid(1, SelectedL1Ids))" @bind-Value=@SelectedL1Ids> </TelerikMultiSelect> </div> </FilterMenuTemplate> <FilterMenuButtonsTemplate /> </GridColumn> The popup itself is pretty generic and is added to the page after the grid. <TelerikPopup @ref="@PopupRef" AnchorSelector=".popup-target"> I am a Telerik Popup. </TelerikPopup> My other issue is I have none of the placement properties such as AnchorHorizontalAlign and AnchorVerticalAlign. If I try and add them to the TelerikPopup tag, it tells me it doesn't exist. It's got to be something really simple, yes? Help me please. Update: I added the popup to the column template <GridColumn Field="L2" Title="Level 2" FieldType="@typeof(string)"> <Template> @{
var item=(TaxonomyGrid)context;
}
@item.L2
@{
if (item.L2OwnerId !=null)
{ <TelerikButton OnClick="@(()=> PopupRef.Popup_OpenAsync())" Class="popup popup-target" Icon="@SvgIcon.User" Title="The name of the owner" /> <TelerikPopup Class="popup" @ref="@PopupRef" MinHeight="500px" MinWidth="300px" AnchorSelector=".popup-target"> <span> @item.L2OwnerName </span> <span> @item.L2OwnerEmail </span> </TelerikPopup> }
} </Template> <FilterMenuTemplate> <div> <TelerikMultiSelect Width="300px" AutoClose=false Data="@L2List" TextField="Name" ValueField="TaxonomyId" OnChange="@( ()=> FilterGrid(2, SelectedL2Ids))" @bind-Value=@SelectedL2Ids> </TelerikMultiSelect> </div> </FilterMenuTemplate> <FilterMenuButtonsTemplate /> </GridColumn> Now, I click on the first row with an icon and the tooltip works as expected. However, if I click on a subsequent row the tooltip appears in the wrong place. I assume this is related to the fact I can't set the horizontal/vertical relationship with the anchor because the properties are availble? Update #2 I fixed part of the anchor problem. I created a method to open the popup and I found some properties there that let me set the anchor alignment, plus I removed the min-height and set the max-height. public void Openpopup () {
PopupRef.AnchorAlign.HorizontalAlign=PopupHorizontalAlign.Right;
PopupRef.AnchorAlign.VerticalAlign=PopupVerticalAlign.Top;
PopupRef.Popup_OpenAsync();
} Now if I click down the column the popup is positioned correctly, however (LOL) if I click on the 6th row down, then click on the first row the popup appears with the 6th row. ugh.

### Response

**Chris** commented on 13 Feb 2024

deleted comment

### Response

**Chris** commented on 13 Feb 2024

deleted comment

## Answer

**Dimo** answered on 15 Feb 2024

Hello Chris, Each TelerikPopup component expects to have its own anchor with a unique AnchorSelector value. When the AnchorSelector is the same for all Popup instances, every instance will show next to the first element on the page, which matches the anchor selector. Setting the alignment settings does not seem necessary in your case. If you don't see all expected parameters of the Popup in intellisense, then delete the bin and obj folders in the app and restart Visual Studio. Here is what I recommend in terms of using Popup in a Grid: [https://blazorrepl.telerik.com/GeOwvzkM59FC1Mep41](https://blazorrepl.telerik.com/GeOwvzkM59FC1Mep41) On a side note, please ask the license holder at your company to assign you a license, so that your account is compliant with our license agreement and can receive technical assistance from us. Regards, Dimo Progress Telerik

### Response

**Chris** commented on 15 Feb 2024

Dimo, that works great. I was certain I needed a unique id to anchor the popup but I couldn't figure out how. Thanks. Regarding the license, I am a contractor at Microsoft and I requested a license and I received a link to download the software from an internal site. Since I'm a contractor they won't give me an account on Telerik.
