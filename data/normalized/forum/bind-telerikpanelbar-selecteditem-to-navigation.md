# Bind TelerikPanelBar SelectedItem to Navigation?

## Question

**mat** asked on 08 Apr 2024

Hello, I'm using the PanelBarComponent to navigate between Pages. Right now I am facing the following problems: 1) when a page where unsaved user input is detected triggers a user prompt before the location is changed, i.e. 'are you sure ..' this breaks the selection of the panelbar. Wether the users decides to stay on the page or discarcd the changes and confirms the location change the selectedItem is set the last clicked item. 2) a page containing a link or any other means of a location change, i.e. the location change is not triggered by the clicking the corresponding item on the panelbar also breaks the selection. In this case the selectedItem is not updated at all. 3) if the user uses a bookmark to navigate to the page the panelbar doesn't show any selection

## Answer

**Nadezhda Tacheva** answered on 11 Apr 2024

Hello Matt, I see that all of the issues you listed are related to managing the selection in the PanelBar. The root cause for these issues is that at this stage, the PanelBar does not support actual selection. When the user clicks on a PanelBar, we add background to it but it is not saved as "selected". The component does not currently provide an option to preserve the selection or programmatically manage the selected state of an item. I opened a feature request for that on your behalf: Selection - ability to get and set the selected item. I added your vote there and as a creator, you are automatically subscribed to get status updates. For the time being, I can suggest two options: Simulate selection with CSS. You may save the item that the user clicked on upon navigation or promt confirmaton. Then you can handle the OnItemRender event to mark the corresponding item as "selected" with CSS similar to the approach used here: [https://blazorrepl.telerik.com/cmFmQCFY55yyPJNa37.](https://blazorrepl.telerik.com/cmFmQCFY55yyPJNa37.) Use the Drawer component for navigation as it provides selection: Drawer Selection. Regards, Nadezhda Tacheva Progress Telerik
