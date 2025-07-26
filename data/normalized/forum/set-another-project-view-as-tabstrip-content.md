# Set another Project View as TabStrip Content

## Question

**Mar** asked on 09 Apr 2021

Hello, Is it possible to define a view (razor-class) as the content of a TabStripTab, as is possible in the Telerik WPF TabItem? Something like this: <Tabcontrol> <TabItem> <TabItem.Content> <view:AnotherProjectView x:Name="AnotherProjectView "/> </TabItem.Content> </TabItem> </Tabcontrol>

## Answer

**Mario** answered on 09 Apr 2021

Got it! <TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Top" @ref="mainTabStrip"> <TabStripTab Title="MyTab"> <AnotherProjectView></AnotherProjectView> </TabStripTab> </TelerikTabStrip>
