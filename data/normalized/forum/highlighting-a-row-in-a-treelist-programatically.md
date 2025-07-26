# Highlighting a row in a treelist programatically

## Question

**Jas** asked on 16 Jul 2021

Hi, I have a Treelist filled with items + plus another textbox control. The contents of these controls are just different views of the same list of fields. As I move my mouse over the treelist, I'd like a mousemove event to fire so I can highlight the equivalent item in my textbox. How do I get a mouseover event to call my underlying C# code with the current mouse over row? Note, I currently have a column template with mousemove event in it. That works, but requires very specific mouse locations. I'd like it to be a full row trigger (just like your current mouseover highlighting). I'd really prefer not to use a row template either as I want all the cool functionality you provide without it (expand/collapse, edit etc). Is this possible? I'm from a wpf background and love the idea of making web-based apps that can provide rich experiences to my users. I'm really hoping that Blazor grant me this opportunity. Cheers

## Answer

**Marin Bratanov** answered on 17 Jul 2021

Hello Jason, Using cell templates or the row template is the way this can be done. Exposing an event like mouseover for the rows will cause serious performance problems in Blazor - the more event handlers a component attaches to the DOM and then the more it exposes as EventCallbacks, the worse its performance gets for all users, even those who do not need or use the events. With that in mind, I can suggest a few options you can consider: adding a button in the rows to have user users use that using the SelectedItemsChanged event for when users change selection (e.g., click on a row) using JavaScript to attach a handler to a parent element of the treelist so it does not get disposed with treelist re-renders and then use information from the event to extract data. For example, find which row is hovered, go to its cells and find the one that has the record ID rendered to identify the row, and pass that to your C# code Regards, Marin Bratanov Progress Telerik

### Response

**Jason** answered on 18 Jul 2021

Hi Marin Thanks for your help. Since I'm just after the mouse over as a passive highlighter, I think your third option makes the most sense for me. So that's, use javascript to detect the mouse move anywhere on the list, then loop over all the HTML items and find the one the mouse is over and call the ID back to Blazor C#. How would the javascript know the item the mouse is over in that instance? You don't already have a script available that can detect this, do you? Not having to use Javascript was was really my major Blazor drawcard. Note: I found this in another post you made, and it finds the selected row by class (I think), but this wouldn't work for the highlighted row as the class doesn't change when mouse covering. I guess it would need a completely different method? function scrollToSelectedRow ( gridSelector ) { var gridWrapper=document.querySelector(gridSelector); if (gridWrapper) { var selectedRow=gridWrapper.querySelector( "tr.k-state-selected" ); if (selectedRow) {
selectedRow.scrollIntoView();
}
}
} Cheers, Jason

### Response

**Marin Bratanov** commented on 19 Jul 2021

You'd need an event handler rather than a method that seeks DOM elements. That mouseover event handler has various properties, including the target element that was actually hovered, so you can traverse the DOM and find what you need. It is not a very trivial task, and Blazor makes it harder by making it harder to hook to plain JS events like that. I don't have a ready-made script for that either, because Blazor does, indeed, abstract away a lot of the JS involved for the majority of cases. Thus, I'd say one of the other options will be much easier for you.

### Response

**Jason** answered on 22 Jul 2021

Hi Marin I'm pretty close on this now. I'm stretching my content to 100% on each cell and having an event on every cell (yuck, but works). The only problem is the first cell on each row as it adds x number of spans for the expand/collapse buttons and indentation. Putting it to 100% forces it to wrap down to another line. I wish there was a CSS way to make my inline div fill the remaining space of a td without wrapping, but I can't find it. (if you know, then please tell me and I'll be forever grateful). I think though that I'm at the point of giving up on avoiding row templates and just accepting my fate... However, I really want the ability to expand, collapse, and show hierarchy with indention (all the cool features that I purchased Telerik for). Do you have a sample row template that includes that functionality so I don't need to start from scratch? The sample one is rather functionless. [https://docs.telerik.com/blazor-ui/components/treelist/templates/row](https://docs.telerik.com/blazor-ui/components/treelist/templates/row) I also note that the blazor row template doesn't expose the TR, while your ASP.net one does. Is there a way to get to the TR from the template so I can add a row MouseOver event? Cheers, Jason

### Response

**Marin Bratanov** commented on 23 Jul 2021

Maybe some CSS similar to this [https://docs.telerik.com/blazor-ui/knowledge-base/treelist-longer-text-starts-from-root-level,](https://docs.telerik.com/blazor-ui/knowledge-base/treelist-longer-text-starts-from-root-level,) or maybe you can change the overflow of the td with CSS to something like "ellipsis": [https://stackoverflow.com/questions/9789723/css-text-overflow-in-a-table-cell](https://stackoverflow.com/questions/9789723/css-text-overflow-in-a-table-cell) The templates in blazor function quite differently than the older asp.net incarnations (especially those based on direct JS DOM manipulations), and we can't expose control over the <tr> in blazor simply because we need to keep an element in our control to provide at the very least some core functionality and rendering (say, data manipulations like sorting).

### Response

**Jason** answered on 26 Jul 2021

Hi Marin Thanks for your continued support. I managed to use your links to product the required stretching to the right. Fiddly stuff, but made it. It's not perfect because the mousover doesn't work to the left of the text e.g. the indentation, but I will live with that for now. I could make it 100% if I could build a row template, but then I lose the indentation and expansion. Do you have a template or something that can be used in a row template that brings it back? How about inheritance, can I somehow inherit teleriks row object and update the tr? I kinda feel something here should be possible? To help others, here is the code that allows the div to strect to 100% width <style>.MyTreeList.defaultHeight { height: 50px;
}.MyTreeList td { max-width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}.MyTreeList.defaultHeight.k-icon { float: left; height: 100%;
} </style> <TelerikTreeList Data="@Data" IdField="EmployeeId" ParentIdField="ReportsTo" Pageable="true" Class="MyTreeList"> <TreeListColumns> <TreeListColumn OnCellRender="@( (TreeListCellRenderEventArgs e)=> e.Class=" defaultHeight " )" Field="FirstName" Expandable="true"> <Template Context="item"> @{
var field=item as Employee; <div style="height: 100%; background-color: #CBA; display: inline-grid; width:100%"> <span style="padding: 4px 8px;"> @field.FirstName </span> </div> } </Template> </TreeListColumn> <TreeListColumn Field="EmployeeId"> </TreeListColumn> </TreeListColumns> </TelerikTreeList> @code {
public List <Employee> Data { get; set; }

public class Employee
{
public int EmployeeId { get; set; }
public string FirstName { get; set; }
public int? ReportsTo { get; set; }
}

protected override void OnInitialized()
{
Data=new List <Employee> ();
var rand=new Random();
int currentId=1;

for (int i=1; i <3; i++)
{
Data.Add(new Employee()
{
EmployeeId=currentId,
ReportsTo=null,
FirstName="Employee " + i.ToString()
});

currentId++;
}
for (int i=1; i <3; i++)
{
for (int j=0; j <2; j++)
{
Data.Add(new Employee()
{
EmployeeId=currentId,
ReportsTo=i,
FirstName="Employee " + j.ToString() + " : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
});
currentId++;
}
}
}
}

### Response

**Marin Bratanov** commented on 27 Jul 2021

You can use the State feature of the component to set the ExpandedItems collection. This can let you put your own button/arrow/element to expand/collapse rows. You can read more about the state in the following article, and there is an example about the expanded items in the "Set TreeList Options Through State" section: [https://docs.telerik.com/blazor-ui/components/treelist/state](https://docs.telerik.com/blazor-ui/components/treelist/state)

### Response

**Jason** commented on 27 Jul 2021

Thanks Marin. Yeah, I'm using the state. I don't see any why that the state can provide the layout for a row template, but that's ok, I've got the columns working okish now. I will read that state stuff thoroughly as it looks pretty helpful. Cheers

### Response

**Marin Bratanov** commented on 28 Jul 2021

The State feature is just an API surface so you can tell the component to do things that usually happen on user interaction with its elements. So, if you customzie the UI or use templates, you can use the state to invoke functionality similar to what the templates may be taking away. For example, to expand/collapse the current row by altering the expanded rows collection in the state. The UI is up to you (say, an icon, button or something else whos @onclick you handle).
