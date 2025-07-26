# Telerik Panel Bar: Has default use for spaces which prevents users from adding space to content

## Question

**Noa** asked on 07 Aug 2021

I have a situation where I a storing the names of dashboards inside of a Telerik panel bar. The problem is that according to the documentation "space and enter" are both used to expand the panel ( Documentation ). This prevents that ability for a user to enter in a space in their desired dashboard name. Is there a work around that would allow me to get the intended functionality or should I look at other options?

## Answer

**Dimo** answered on 11 Aug 2021

Hi Noah, Indeed, this is a bug and we already have a public item for it. I have voted on your behalf to bump up the popularity and priority. You can also follow the item to receive status updates. Here is a possible workaround. It's rather old school, but I hope it is feasible for you: <TelerikPanelBar Data="@Items"> <PanelBarBindings> <PanelBarBinding> <ContentTemplate> @{
var item=context as PanelBarItem; <div onkeydown="stopPropagation(event)"> <TelerikTextBox @bind-Value="item.Text"> </TelerikTextBox> </div> } </ContentTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar> JavaScript window.stopPropagation=( e )=> {
e.stopPropagation();
} Regards, Dimo Progress Telerik

### Response

**Noah** commented on 16 Aug 2021

Thank you for your response. Unfortunately, this does not seem to solve the issue for me. I have attached some code to show my current setup below. <TelerikPanelBar Data="@_sortedTabs" Class="dash-settings-accordion" OnItemClick="@onItemClickHandler"> <PanelBarBindings> <PanelBarBinding> <HeaderTemplate> @{
string sName=context as string; <div class="d-flex flex-rev w-40"> <div class=""> <AppOneInPlaceEditor DisplayText="@sName" OnSave="onRename" ReturnVals="@(new object[] { sName })"> <input type="text" @onclick:stopPropagation="true" @bind-value="@_sNewTabName" /> </AppOneInPlaceEditor> </div> </div> } </HeaderTemplate> </PanelBarBinding> </PanelBarBindings> </TelerikPanelBar>

### Response

**Dimo** commented on 16 Aug 2021

Hello Noah, There is a difference between client-side attributes (such as onclick="..." ) and server-side directives (such as @onclick ). In this case, you need to stop propagation of an event, which is fired and handled client-side. That is why the server directive does not work. Please use only HTML/JavaScript code, as suggested previously.

### Response

**Chris** commented on 17 Nov 2023

Thank you for this answer, Dimo. It works great for me, even two years later.
