# Splitter order not correct

## Question

**Rém** asked on 01 Mar 2021

Hi, Version 2.14.1 I want to display 2 or 3 panes in a splitter. With the code below middle pane is on the right. What is the best way to keep pane order ? Remi @page "/" <div style="width: 500px; height: 300px; border: 1px solid red;"> <TelerikSplitter @ref="ts" Width="100%" Height="100%" Orientation="@SplitterOrientation.Horizontal"> <SplitterPanes> <SplitterPane Size="20%" Collapsible="true"> <div>left</div> </SplitterPane> @if (bunique) { <SplitterPane Size="10%" Collapsible="true"> <div>middle</div> </SplitterPane> } <SplitterPane> <div>right</div> </SplitterPane> </SplitterPanes> </TelerikSplitter> </div> @code{ bool bunique=false; Telerik.Blazor.Components.TelerikSplitter ts; protected override void OnAfterRender( bool firstRender) { if (firstRender) { if (!bunique) { bunique=true; StateHasChanged(); } } } }

## Answer

**Nadezhda Tacheva** answered on 02 Mar 2021

Hi Remi, Indeed, when hiding a pane and then showing it again, the Splitter ignores the initial position of the Pane and displays it in the end. The reason behind this behavior is that the component (the Splitter) is initialized first and then its child components (the panes) are rendered. When you are hiding a pane it is removed from the collection of child elements (panes) that the Splitter has to display. Then when you show it again it is added to that collection and as per standard it is added in the end. I have created a bug report in our public
