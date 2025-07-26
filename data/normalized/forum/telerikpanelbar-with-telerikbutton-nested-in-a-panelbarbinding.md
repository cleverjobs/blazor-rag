# TelerikPanelBar with TelerikButton nested in a PanelBarBinding...

## Question

**Pau** asked on 27 Oct 2024

Hi All, I have a TelerikButton within a PanelBarBinding element in an TelerikPanelBar, and i like to avoid the Panel to expand when i click the TelerikButton. However the Panel should expand if i click the Panel anywhere else. how can i do this ? i use Telerik UI for Blazor ? Thx

## Answer

**Hristian Stefanov** answered on 30 Oct 2024

Hi Paul, Indeed, the button affects the state of the PanelBar. To avoid that, wrap the button within a div that stops its onclick event propagation. This prevents the event from bubbling up to the parent component and resolves the expand/collapse state conflict. Here is an illustration of the approach: <div style="width: 30%;"> <TelerikPanelBar Data="@Items" @bind-ExpandedItems="@ExpandedItems"> <PanelBarBindings> <PanelBarBinding> <HeaderTemplate> @{
var item=context as PanelBarItem; <div style="font-weight: bold; text-decoration: underline"> @item.Text </div> <div @onclick:stopPropagation> <TelerikButton OnClick="@TestHandler"> Test </TelerikButton> </div> } </HeaderTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar> </div> @code {
public List <PanelBarItem> Items { get; set; }
public IEnumerable <object> ExpandedItems { get; set; }=new List <object> ();

private void TestHandler()
{
//test
}

public class PanelBarItem
{
public int Id { get; set; }
public string Text { get; set; }
public int? ParentId { get; set; }
public bool HasChildren { get; set; }
public ISvgIcon Icon { get; set; }
public string Url { get; set; }
}

private List <PanelBarItem> LoadFlatData()
{
List <PanelBarItem> items=new List <PanelBarItem> ();

items.Add(new PanelBarItem()
{
Id=1,
Text="Project",
ParentId=null,
HasChildren=false,
Icon=SvgIcon.Folder,
Url="projectURL.url"
});

items.Add(new PanelBarItem()
{
Id=2,
Text="Implementation",
ParentId=null,
HasChildren=true,
Icon=SvgIcon.Code
});

items.Add(new PanelBarItem()
{
Id=3,
Text="C#",
ParentId=2,
HasChildren=false,
Icon=SvgIcon.Cs
});

items.Add(new PanelBarItem()
{
Id=4,
Text="HTML 5",
ParentId=2,
HasChildren=false,
Icon=SvgIcon.Html5
});

items.Add(new PanelBarItem()
{
Id=5,
Text="CSS",
ParentId=2,
HasChildren=false,
Icon=SvgIcon.Css
});

return items;
}

protected override void OnInitialized()
{
Items=LoadFlatData();

ExpandedItems=new List <object> () { Items[1] };

base.OnInitialized();
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Paul** commented on 31 Oct 2024

Hi Hristian, @onclick:stopPropagation was the Key ! THX a lot for Support and Help ! Paul

### Response

**Hristian Stefanov** commented on 01 Nov 2024

Hi Paul, I'm very happy to hear that the matter is resolved. Kind Regards, Hristian
