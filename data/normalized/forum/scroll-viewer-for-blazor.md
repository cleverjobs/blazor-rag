# Scroll Viewer for Blazor

## Question

**Joe** asked on 19 May 2025

I'm using a splitter. But, my contents can go longer than the exposed area defined by the splitter (height). Do you have a scroll viewer for blazor or a similar layout control? <TelerikSplitter Orientation="SplitterOrientation.Horizontal" Height="70vh"> <SplitterPanes> <SplitterPane Size="40%" Min="30%" Max="70%" Collapsible="false">

## Answer

**Dimo** answered on 20 May 2025

Hi Joel, You can make a Splitter pane scrollable with the k-scrollable CSS class. Regards, Dimo Progress Telerik

### Response

**Joel** commented on 20 May 2025

I believe this got me there... however, it seems odd. In my opinion this should be a 1st class citizen of your control. E.g. <SplitterPane Size="40%" Min="30%" Max="70%" Collapsible="false" Scrollable="true">
