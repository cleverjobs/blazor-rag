# TelerikGrid - Click on GridCommandButton does not set selected row

## Question

**Mar** asked on 23 May 2024

I have a GridCommandButton with a custom action. If I click directly on the button, the select row is not set. How can I get the content of the row when I click the button? <GridCommandButton Command="SyncWithAD" Icon="@FontIcon.Lock" Title="Sync to Azure" Enabled="CanEdit" OnClick="@ShowSyncUserWithAdDialog"> </GridCommandButton> Use the GridCommandEventArgs.Item private async Task ShowSyncUserWithAdDialog ( GridCommandEventArgs args ) { if (args.Item is not JasminExternalUser user) return;

Progress.Visible=true; var props=new JasminUserAdProperties { Email=user.Email, Name=user.Name, Groups=[] };
AdProperties=await UserService.GetUserAdProperties(props);
Progress.Visible=false;
}

## Answer

**Nansi** answered on 28 May 2024

Hello Martin, Thank you for the provided code example. To access the data of the clicked model item, you need to explicitly cast the item to the model. JasminExternalUser user=(JasminExternalUser)args.Item; I have prepared a REPL example that displays some properties of the model when you click the custom command button. Regards, Nansi Progress Telerik
