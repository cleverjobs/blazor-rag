# Tooltip on the grid header

## Question

**Pet** asked on 05 Feb 2021

Hi, how can I show a Tooltip on the grid headers to replace short column title with a long description? In Kendo UI I use this Javascript code: grid.thead.kendoTooltip({ filter: "th", content: function (e: any) { var text=e.target.text().trim(); switch (text) { case "Länge": return "Zuglänge"; case "Kateg.": return "Zugkategorie"; case "Dauer": return "Expositionsdauer T<sub>TEL</sub>"; case "Geschw.": return "Geschwindigkeit"; case "LAmax": case "LAFmax": return "Maximalpegel"; case "LAeq": case "TEL": case "Vorbeifahrtpegel": return "Vorbeifahrtexpositionspegel"; default: return text; } } }); Best regards, Peter

## Answer

**Marin Bratanov** answered on 05 Feb 2021

Hi Peter, You can use the column header template to add a node that has the title attribute (and style as desired, such as bold) and then you can point the tooltip to that element - it uses css selectors. Then, in the tooltip template you can define the text based on the metadata you get for the target (you can see examples in the Tooltip Template article ). Regards, Marin Bratanov

### Response

**Peter** answered on 06 Feb 2021

Hi Marin, thank you. The column header template is required: <GridColumn Field="ImageId"> <HeaderTemplate> <div title="The Id in table image">Id</div> </HeaderTemplate> </GridColumn> Then a small Tooltip is shown on mouse hover: [https://pasteboard.co/JN5ejKO.png](https://pasteboard.co/JN5ejKO.png) Regards, Peter

### Response

**Peter** answered on 06 Feb 2021

with TelerikTooltip it looks better and can customized: <TelerikTooltip TargetSelector=".k-column-title div"> <Template> @context.Title </Template> </TelerikTooltip> <TelerikGrid Data=@GridData <GridColumns> <GridColumn Field="ImageId"> <HeaderTemplate> <div title="The Id in table image">Id</div> </HeaderTemplate> </GridColumn> [https://pasteboard.co/JN5gPCe.png](https://pasteboard.co/JN5gPCe.png)

### Response

**Marin Bratanov** answered on 06 Feb 2021

Indeed, Peter, that's the way to do this. I've marked your posts as answer to this thread too. Regards, Marin Bratanov

### Response

**Peter** answered on 07 Feb 2021

Hi Marin, For a model with many fields I inherit GridColumn: GridColTooltip.razor @inherits GridColumn @code{ [Parameter] override public string Title { get; set; } [Parameter] public string Tooltip { get; set; } protected override void OnParametersSet() { base.OnParametersSet(); var title=Title ?? base.Field; // if empty use fieldname var tooltip=Tooltip ?? title; // if empty use Title as Tooltip base.HeaderTemplate=@<div title="@tooltip">@title</div>; } } And now I can use: <GridColumns> <GridColTooltip Field=@nameof(ViewModel.ImageId) Width="20px" Title="Id" Tooltip="The Id in table image" /> <GridColTooltip Field=@nameof(ViewModel.ImageNumber) Width="20px" /> The width 20px is enough for the numbers (<1000) but to short for the Header Title. But now I get the tooltip to show the full text. It is safe to inherit a Telerik component? Events from the base component (GridColumn) should be avaliable in the derived component (GridColTooltip). Best regards, Peter

### Response

**Marin Bratanov** answered on 07 Feb 2021

Hello Peter, Inheriting our components is not something we support because it can lead to various behavior issues depending on what is done in the inheriting class and we can't influence this. Ultimately, razor components boil down to a C# class, so inheritance is as safe as any other inheritance in C# - as long as you don't break or override anything the base class uses things should work. Regards, Marin Bratanov

### Response

**Paul** commented on 08 Sep 2022

Hi Can you supply a small demo showing tooltip on eacht grid column? Eric

### Response

**Nadezhda Tacheva** commented on 13 Sep 2022

Hi Eric, You may try the approach that Peter proposed. The solution suggests using ".k-column-title div" for the target selector of the Tooltip. You may as well add your custom class to the column header and use that as a selector. HeaderClass feature of the Grid is available as of UI for Blazor 3.4. Here is a basic sample demonstrating the solution: [https://blazorrepl.telerik.com/ccYNlxuA22DnqJov13.](https://blazorrepl.telerik.com/ccYNlxuA22DnqJov13.) I hope you will find it useful to move forward with your application.
