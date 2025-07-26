# Set default value from code behind

## Question

**Joe** asked on 22 Jan 2024

I have a listbox where I feed a default value into the class in the url. I am able to populate the bound SelectedItems value but it doesn't highlight the selected value in the control. How do I do this? <TelerikListBox Data="@SessionOptionTemplates" Width="350px" SelectionMode="ListBoxSelectionMode.Single" TextField="@nameof(SessionOptionTemplate.Name)" OnReorder="@((ListBoxReorderEventArgs<SessionOptionTemplate> args)=> OnReorderSessionOptionTemplates(args))" OnRemove="@((ListBoxRemoveEventArgs<SessionOptionTemplate> args)=> OnRemoveSessionOptionTemplates(args))" SelectedItemsChanged="@((IEnumerable<SessionOptionTemplate> selectedTemplates)=> OnSelectedSessionOptionTemplate(selectedTemplates))"> <ListBoxToolBarSettings> <ListBoxToolBar Visible="true"> <ListBoxToolBarMoveUpTool /> <ListBoxToolBarMoveDownTool /> <ListBoxToolBarRemoveTool /> <ListBoxToolBarCustomTool> <TelerikButton Icon="@SvgIcon.DetailSection" Enabled="@( SelectedSessionOptionTemplate !=null )" OnClick="@ShowEditDialogSessionOptionTemplates" /> </ListBoxToolBarCustomTool> </ListBoxToolBar> </ListBoxToolBarSettings> </TelerikListBox> public async Task OnSelectedSessionOptionItem(
IEnumerable <SessionOptionItem> selectedItems)
{
if (selectedItems.Any())
{
SessionOptionItem selectedItem=selectedItems.FirstOrDefault(x=>
x.Id==selectedItems.First().Id);

if (selectedItem !=null)
{
SelectedSessionOptionItems=new List <SessionOptionItem> ()
{
selectedItem
};
}
}

await Task.CompletedTask;
} public async Task OnSelectedSessionOptionTemplate(
IEnumerable <SessionOptionTemplate> selectedItems)
{
if (selectedItems.Any())
{
SessionOptionTemplate selectedItem=selectedItems.FirstOrDefault(x=>
x.Id==selectedItems.First().Id);

if (selectedItem !=null)
{
SelectedSessionOptionTemplates=new List <SessionOptionTemplate> () { selectedItem };

SessionOptionItemClient.AccessToken=AccessToken;
SessionOptionItemClient.CustomerUniqueId=CustomerUniqueId;

var itemResponse=await SessionOptionItemClient.GetBySessionOptionTemplateIdAsync(
selectedItem.Id);

if (itemResponse !=null &&
itemResponse.IsSuccess &&
itemResponse.Result !=null)
{
SessionOptionItems=itemResponse.Result.OrderBy(x=> x.Order).ToList();

if (SessionOptionItems.Any())
{
await OnSelectedSessionOptionItem(
new List <SessionOptionItem> () { SessionOptionItems.First() });
}
}
else
{
SessionOptionItems=null;
}
}
}
}

private IEnumerable <SessionOptionTemplate> SelectedSessionOptionTemplates { get; set; }=new List <SessionOptionTemplate> ();

## Answer

**Dimo** answered on 25 Jan 2024

Hi Joel, I don't see a SelectedItems parameter in the ListBox declaration. Please set it and make sure that the corresponding variable receives a value on page load. ListBox Selection documentation and example Regards, Dimo Progress Telerik

### Response

**Joel** commented on 25 Jan 2024

Well... that was easy. Honestly, I took the SelectedItems out of there when I added the SelectedItemsChanged handler not thinking about my posted scenario. Follow-up question: How do I get it to ensure the listbox scrolls to the selected item. Right now, the selected item remains out of view but I'd like the selected item to be selected and in view.

### Response

**Joel** commented on 25 Jan 2024

Same concept as the ScrollIntoView() method provided on your other products. ScrollIntoView

### Response

**Dimo** commented on 26 Jan 2024

@Joel - please open the ListBox Selection article and check the "Related articles" in the right column. I am also curious whether the ListBox scrolling article appears at the top of Google search results if you search by telerik blazor listbox scroll to the selected item. This does happen on my side, but probably Google knows that I am biased.

### Response

**Joel** commented on 26 Jan 2024

Honestly, the "related articles" section never caught my attention. Even after you pointing it out I sat and stared at the "next steps" section looking for more information. I suggest that "related articles" be given a 1st class setting instead of being a side-bar. I'll take a look.

### Response

**Joel** commented on 26 Jan 2024

I avoid JSRuntime... thats why I use Blazor. Nonetheless, I'll add this but please reassure me that this is on the list to be added as a feature of your control. That said, can you educate me on how to pass the listbox to this method when it is saved into its own file for CSP reasons?

### Response

**Dimo** commented on 31 Jan 2024

@Joel I passed your feedback to the team who maintains the UX of our documentation sites. The current idea is to measure the number of clicks on related articles and see if there is a general problem with the visibility. Thanks for sharing! I also updated the KB to show how to target and scroll a specific ListBox component. On the other hand, a method to scroll the ListBox is questionable, because when we implement virtualization, the selected item may not be rendered. This is the reason why: We declined a similar request for the Grid. Virtual DropDownLists don't scroll to the selected item automatically, unlike non-virtual ones. It's true that JavaScript can be a bad practice in Blazor apps, but it's not the case here. The script only simulates user behavior and does not change the application state behind Blazor's back. It's hard to completely avoid using JS in web apps.

### Response

**Joel** commented on 31 Jan 2024

Seems like there is some circular logic here. The over-all request is that I be able to select an item in the ListBox from code-behind then I must scroll to it. That item better be there or I'm not going to be able to select it. So, if there is a selected item then I should be able to scroll to it... we know its there.

### Response

**Dimo** commented on 31 Jan 2024

"we know the selected item is there" is not same as "the selected item is rendered in the DOM" To show what I mean, here is a Grid Selection demo with selected items on page 1. If you go to Page 3, the selected items are "still there", but you can't scroll to them. Virtual scrolling is similar to paging, because the component renders only one "page" of items at a time.

### Response

**Joel** commented on 31 Jan 2024

I'll just mark this up as a "I don't understand virtualization" moment. It still seems that if I'm going to select a record from code behind that happens to be on page 3 of the grid that once I select it the control should move to page 3 and page 3 would then be loaded in the DOM in order to display it. If its "not there" then I'm also confused as to why the javascript can get to it. Actually, maybe I do understand this a little. Is it because the code behind runs on the server and the javascript is in the browser? If that is the case, in the wonderful world of Blazor, couldn't there be a SignalR exchange that would tell the client to "load page 3 and select my target record"?

### Response

**Dimo** commented on 31 Jan 2024

>> if I select a record on page 3 of the grid, the control should move to page 3 There is no built-in mechanism for this in any of our components. Usually, when you have item virtualization, the component has only the current page of items. In other words, if a component shows page 1 and the app selects item from another page, the component doesn't know which page that is. As I mentioned above, virtual DropDownLists don't scroll to the selected item automatically (even though it may be desirable), unlike non-virtual ones.

### Response

**Joel** commented on 31 Jan 2024

Thanks for the Dialog
