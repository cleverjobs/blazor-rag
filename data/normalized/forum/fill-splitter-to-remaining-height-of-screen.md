# Fill Splitter to remaining height of screen

## Question

**Ram** asked on 12 Aug 2021

Hi. I'm trying to make a TelerikSplitter control fill the remaining height of the screen, but I'm struggling with making it work as expected. Index.razor @page "/" <TelerikSplitter Orientation="SplitterOrientation.Horizontal"> <SplitterPanes> <SplitterPane Resizable="true" Collapsible="false"> Left </SplitterPane> <SplitterPane Resizable="true" Collapsible="false"> Right </SplitterPane> </SplitterPanes> </TelerikSplitter> Any ideas? Thank you.

## Answer

**Matthias** answered on 12 Aug 2021

HI I had the same problem and was able to solve it with BlazorSize. Documentation: [https://github.com/EdCharbeneau/BlazorSize/wiki](https://github.com/EdCharbeneau/BlazorSize/wiki) <SplitterPane Size="@PaneSize"> async void WindowResized ( object _, BrowserWindowSize window ) {
_browser=window; // calculate size StateHasChanged();
} The size can be easily calculated in the method. Since the splitter unfortunately does not yet handle all necessary events and methods, I had to add the following event: SplitterResizeEventArgs args=new SplitterResizeEventArgs();
args.Size=your_calculated_size;
args.Index=0;
args.ShouldRender=true; await OnResizeHandler(args); and the event in the splitter: <TelerikSplitter Width="100%" Height="100%" Orientation="@SplitterOrientation.Vertical" OnResize="@OnResizeHandler"> I hope this helps you. At least I was able to solve all problems with it. Regards Matthias

### Response

**Rami Abughazaleh** commented on 13 Aug 2021

Hi Matthias. Thank you for your reply. However, I'm not sure the solution you provided will solve my issue. With the code snippet you provided, I'm able to get the browser window height and width but this doesn't allow me to set the height of the splitter. My splitter is oriented horizontally, not vertically, and so the Size property doesn't seem to be the right property to set in this case. It also depends on manually having to perform the calculation which I'd like to avoid. I've attached an updated sample app that includes a navigation placeholder at the top of the page and a footer on the bottom of the page which is more like my actual use case. Any other ideas? Thank you.

### Response

**Marin Bratanov** answered on 14 Aug 2021

Hi all, There is an easier way to do this - use plain CSS with 100% dimensions and ensure that the parent elements of the splitter have height set to 100% as well. I made a public sample project that you can preview here in its PR, and I am also attaching it to this post so you can take a look. There is no need to use additional packages, event handlers and dynamic values - the CSS features browsers offer are sufficient. Regards, Marin Bratanov Progress Telerik

### Response

**Matthias** commented on 16 Aug 2021

Hi Marin, for this scenario certainly the best and easiest solution. Thanks for the advice!

### Response

**Matthias** answered on 13 Aug 2021

Hi Rami, with BlazorSize you could also change the height of the splitter. But if it's only about the adjustment, it's even easier: <TelerikSplitter Orientation="SplitterOrientation.Horizontal" Height="80vh"> <SplitterPanes> <SplitterPane Resizable="true" Collapsible="false"> Left </SplitterPane> <SplitterPane Resizable="true" Collapsible="false"> Right </SplitterPane> </SplitterPanes> </TelerikSplitter> If header and footer change in their height, however, a calculation would be necessary again. 80vh ... is an example, depending on header or footer the value must be adjusted. At least that's how I understood your question.

### Response

**Rami Abughazaleh** commented on 13 Aug 2021

Hi Matthias. Thank you for your reply. With your help and BlazorSize, I was able to adjust the height of the splitter when it's oriented horizontally after all as follows: <TelerikSplitter Orientation="SplitterOrientation.Horizontal" Width="100%" Height="@splitterHeight"> <SplitterPanes> <SplitterPane Resizable="true" Collapsible="false"> Left </SplitterPane> <SplitterPane Resizable="true" Collapsible="false"> Right </SplitterPane> </SplitterPanes> </TelerikSplitter> private string splitterHeight; private async void WindowResized ( object _, BrowserWindowSize window ) { this.browser=window; // calculate size splitterHeight=this.browser.Height - 230 + "px"; this.StateHasChanged();
} Thank you so much!
