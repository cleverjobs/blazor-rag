# binding inside contextmenu does not work

## Question

**Cla** asked on 29 Mar 2023

Hi, i show in a specific position a context menu with some fields. If i try to update a binding field (using @bind-Value), for example with a TelerikTextBox it does not work. You can see this simple example, press Reset button does not update the textbox content. What's wrong? Thanks [https://blazorrepl.telerik.com/QxkRwDbe51q1XmYf53](https://blazorrepl.telerik.com/QxkRwDbe51q1XmYf53) <TelerikContextMenu @ref="ContextMenu" TItem="object"> <Template> <div> Input name </div> <TelerikTextBox @bind -Value="Value" /> <br /> <TelerikButton OnClick="@(()=> Value="")"> Reset </TelerikButton> <TelerikButton OnClick="@(()=> ContextMenu.HideAsync())"> Close </TelerikButton> </Template> </TelerikContextMenu> <TelerikButton OnClick="()=> ContextMenu.ShowAsync(100,100)"> Open context menu </TelerikButton> @code { private TelerikContextMenu <object> ContextMenu {get;set;} private string Value {get;set;} }

## Answer

**Hristian Stefanov** answered on 03 Apr 2023

Hi Claudio, Thank you for sending a runnable sample. I'm reproducing the described behavior with it. The problem in this scenario is due to a missing Refresh method in the ContextMenu. Thus, I opened a feature request on your behalf for that method: Refresh Method. As implementing the Refresh method is a quick enhancement, I will personally engage to include this feature in our next release 4.2 expected to come out on the 26th of April. You are automatically subscribed as a creator to receive email notifications for status updates. Regards, Hristian Stefanov
