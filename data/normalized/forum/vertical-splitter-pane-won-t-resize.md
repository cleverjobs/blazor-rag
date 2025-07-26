# Vertical Splitter Pane won't resize

## Question

**BobBob** asked on 17 Nov 2021

I have a Vertical Splitter pane that will not resize until I first collapse it and then expand it. I am getting an error in the browser when I first try to re-size it. telerik-blazor.js:63 Uncaught TypeError: Cannot read properties of undefined (reading 'min') at e.value (telerik-blazor.js:63) at e.value (telerik-blazor.js:63) at e.value (telerik-blazor.js:63) at e.value (telerik-blazor.js:63) at Object.i.onResizableResize [as resize] (telerik-blazor.js:63) at e.value (telerik-blazor.js:1) at e.value (telerik-blazor.js:49) at Object.i.onDraggableDrag [as drag] (telerik-blazor.js:49) at e.value (telerik-blazor.js:1) at e.value (telerik-blazor.js:3) Here is the markup of the Splitter: <TelerikSplitter Orientation="SplitterOrientation.Vertical" Height="100%" Class="accountWorkscopeSplitter"> <SplitterPanes> <SplitterPane Class="scrollablePane"> <LeftNav WorkspaceId="@WorkspaceId.Value" NavigationWorkspace="Account" OnNavItemSelected="NavItemSelected" /> </SplitterPane> @if (showExpenditureCenter || showRevenueCenter)
{ <SplitterPane Collapsible="true" Resizable="true" Size="50%" Max="50%" Class="scrollablePane"> @if (showExpenditureCenter)
{ <div id="ExpenditureCenterDiv"> <AccountCenter Type="AccountType.Expenditures"> </AccountCenter> </div> }
@if (showRevenueCenter)
{ <div id="RevenueCenterDiv"> <AccountCenter Type="AccountType.Revenues"> </AccountCenter> </div> } </SplitterPane> } </SplitterPanes> </TelerikSplitter> One thing I will note is this splitter inside a pane of a Horizontal splitter.

### Response

**Hristian Stefanov** commented on 22 Nov 2021

Hi Bob, The shown markup of the Splitter seems correct. I made an improvised example with the configuration of the provided code snippet to try to reproduce the error. However, the resize functionality works as expected on my end, without exceptions. Can you please modify the attached project to reproduce the problem you are facing and send it? This will allow me to see the error on my machine and debug it. On a side note, we have an article for Javascript Errors that shows troubleshooting of common js errors. You can take a look at it for additional helpful information. Thank you, and I look forward to your reply. Regards, Hristian Stefanov Progress Telerik

## Answer

**Dimo** answered on 09 Feb 2022

I have to admit we reproduced the issue and logged it. Here is the public item for status tracking. Regards, Dimo
