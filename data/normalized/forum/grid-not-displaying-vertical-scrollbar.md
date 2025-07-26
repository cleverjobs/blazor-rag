# Grid not displaying vertical scrollbar

## Question

**Alb** asked on 22 Aug 2023

I have a simple TelerikGrid within a blazored modal: <TelerikGrid Data="this.Model" Height="400px"> <GridColumns> <GridColumn Field="Id" Width="30px" Title="Id" /> <GridColumn Field="Name" Title="Name" /> <GridColumn Field="RoleId" Width="30px" Title="SRRid" /> </GridColumns> </TelerikGrid> when I load the information I get 50 records, due to the modal size I can only see 15 records, however the vertical scrollbar is not being displayed. Am I missing something else that I need to configure?

### Response

**Hristian Stefanov** commented on 25 Aug 2023

Hi Alberto, I confirm that the provided Grid configuration is correct. I have also tested it in this REPL link, and seems that the vertical scrollbar is shown as expected. You can run and test it to see whether you get the same result. This observation leads me to think that certain additional CSS styles, originating from the Blazored modal, may be engaging in conflict with the Grid styles. In order to progress further, I recommend installing the Blazored package within the REPL platform. By sharing a functional sample encompassing your current configuration, I will be able to examine all CSS styles active on the page. Subsequently, I can pinpoint the underlying cause of the issue at hand and suggest a possible solution. I eagerly await hearing back from you. Kind Regards, Hristian
