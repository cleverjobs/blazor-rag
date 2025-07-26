# Tabstrip Scrollable not work when tab count is dynamic

## Question

**Bra** asked on 21 Nov 2022

Hi there, I use the sample code in here and I can see the scrollable icon. But when I try to add tabs by button click , the scrollable icon is not shown. How to fix it? <TelerikTabStrip Scrollable="true" Width="300px" TabPosition="Telerik.Blazor.TabPosition.Top"> @{
for (int i=0; i <tabCount; i++)
{
var title="long long long-" + @i.ToString(); <TabStripTab Title="@title" @key="@i"> Tab content. </TabStripTab> }
} </TelerikTabStrip> <TelerikButton OnClick="AddTab"> add tab </TelerikButton> @code {
int tabCount=0;

void AddTab()
{
tabCount++;
StateHasChanged();
}
}

### Response

**Brandon** commented on 23 Nov 2022

I just found it fixed in version 3.7

## Answer

**Brandon** answered on 23 Nov 2022

I just found it fixed in version 3.7
