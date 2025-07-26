# Intermittently - Tooltip sometimes doesn't show on Click

## Question

**Vin** asked on 22 Nov 2022

Hi Team, Currently I am using Telerik UI Blazor with 3.7.0 version, few cases and intermittently TooltipShowEvent.Click is not working and tooltip is not getting displayed and unable to find root cause for it. Could you please assist what is causing for this behavior and feasible solution? Below is sample code snippet where we use 3 tabs <TelerikTabStrip Class="tmGraphTabStrip" ActiveTabIndex="@ActiveTab" ActiveTabIndexChanged="@ActiveTabChanged" @ref="@TabRef"> @for (var i=0; i <4; i++) { <TabStripTab Title="@TabName" Class="tmTabHeaderCellStyle"> <TelerikGridLayout RowSpacing="20px" ColumnSpacing="1px" Class="grid-CardlayoutNew"> @* display data in gridlayout structure for each row/column along with tooltip, we are able to see div selector and target selector Ids from Dev Tools browser *@</TelerikGridLayout> </TabStripTab> } </TelerikTabStrip> Ex: <TelerikTooltip TargetSelector="@ToolTipCurselector" ShowOn="@TooltipShowEvent.Click" Position="TooltipPosition.Top"> </TelerikTooltip>

### Response

**Dimo** commented on 25 Nov 2022

Duplicate of this public feedback item.
