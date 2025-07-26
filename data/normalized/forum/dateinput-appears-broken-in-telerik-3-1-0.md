# DateInput appears broken in Telerik 3.1.0

## Question

**Dea** asked on 11 Mar 2022

Since upgrading from Telerik 3.0.1 to 3.1.0, DateInput controls no longer bind to properties for me. The following works in 3.0.1 but not 3.1.0 @page "/TestPage" <p> Message: @Message </p> <p> MyDate: @MyDate </p> <TelerikTextBox @bind-Value="Message"> </TelerikTextBox> <TelerikDateInput @bind-Value="MyDate" Format="dd/MM/yyyy"> </TelerikDateInput> @code {
public string Message { get; set; }
public DateTime MyDate { get; set; }
}

### Response

**Marin Bratanov** commented on 12 Mar 2022

Double check that the JS Interop file matches the version if you are using the CDN, and that you have no JS errors, try cleaning your build folders (bin and obj) and clearing the browser cache. If the issue persists, I recommend opening a ticket.

## Answer

**Dean** answered on 16 Mar 2022

Working now thanks
