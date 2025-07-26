# Keyboard Navigation

## Question

**TDTD** asked on 28 May 2020

Do not use keyboard navigation in Window,Thank you for your help!

## Answer

**Svetoslav Dimitrov** answered on 28 May 2020

Hello, Thank you for using our components! Could you elaborate on how can we help you using our components and in this case the TelerikWindow? Regards, Svetoslav Dimitrov

### Response

**ian** commented on 05 Jul 2021

It seems that disabling keyboard navigation on the TelerikWindow is what is desired. Concrete examples: TelerikWindow with Modal=true can be navigated away from to another Modal TelerikWindow via TAB, OR the TelerikWindow can be closed via ESC (there is a workaround for ESC, but not for TAB) in my situation.

### Response

**Svetoslav Dimitrov** answered on 08 Jul 2021

Hello Ian, If I understand your question correctly you would not like to allow your users to close the Modal window by clicking on the Esc keyboard key or by navigating to the Close (x) built-in button by using the Tab key. If indeed this is the case, this behavior is shown in the Keyboard Navigation demo for the Window and this is the expected result. In case you are using the Modal Window to create notifications in your application, I would like to suggest the Notification component. You can create an automatically closing notification that the user will not be able to close by clicking a close button. Alternatively, if you would like to stop the user from being able to close the window by clicking the built-in Close button you can remove the definition of the button from the markup: <TelerikWindow Visible="true"> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> @* remove this line from the definition *@</WindowActions> <WindowTitle> Optional title </WindowTitle> <WindowContent> I have action buttons. Try using them, but if you close me, you can't reopen me without a few lines of code, so try that last. <br /> The title bar will now render even if you don't define a title, because it will show the action buttons. </WindowContent> </TelerikWindow> If neither of these approaches helps you get the desired behavior could you provide some additional information so that I can further evaluate the scenario. Regards, Svetoslav Dimitrov Progress Telerik
