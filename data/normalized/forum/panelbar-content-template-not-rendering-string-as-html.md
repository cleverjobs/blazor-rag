# PanelBar Content Template not rendering string as html.

## Question

**Sar** asked on 29 Feb 2024

Hello, I have a TelerikPanelBar and I am getting the content from the database. the text from item.Text is a string, that includes HTML. Instead of rendering the HTML, it is still just rendering it as a string, even though I am converting it to a Markup String/using Markdig. How can I get the text to display as HTML, instead of a string?

## Answer

**Hristian Stefanov** answered on 01 Mar 2024

Hi Sarah, To render the HTML elements from the item.Text, use HeaderTemplate and convert the string to a MarkupString within it. I have prepared an example for you: <div style="width: 30%;"> <TelerikPanelBar Data="@Items" @bind-ExpandedItems="@ExpandedItems"> <PanelBarBindings> <PanelBarBinding> <HeaderTemplate> @{
var item=context as PanelBarItem; @(new MarkupString($"{(@item.Text)}")) } </HeaderTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar> </div> @code {
public List <PanelBarItem> Items { get; set; }
public IEnumerable <object> ExpandedItems { get; set; }=new List <object> ();

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
Text=" <strong> Project </strong> ",
ParentId=null,
HasChildren=false,
Icon=SvgIcon.Folder,
Url="projectURL.url"
});

items.Add(new PanelBarItem()
{
Id=2,
Text=" <strong style=\ " color: blue \"> Implementation </strong> ",
ParentId=null,
HasChildren=true,
Icon=SvgIcon.Code
});

items.Add(new PanelBarItem()
{
Id=3,
Text="C# <br /> test <br /> test",
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
