# Encapsulating TelerikGrid and its components and context

## Question

**Nik** asked on 27 Oct 2023

Hello, I have a custom razor component called MyGrid.razor which encapsulates the TelerikGrid component. The goal of my doing is to achieve a result which looks like the following: <MyGrid> <MyGridColumn Title="Id" Width="200px" Field=@(nameof(MyDTO.Id))> @{ @(MarkupString)MyService.FormatTitle(context.Title) } <MyGridColumn> <MyGridColumn Title="Status" Width="200px" Field=@(nameof(MyDTO.Status))> @{ @(MarkupString)MyService.FormatStatus(context.Status) } <MyGridColumn> </MyGrid> The component MyGridColumn should represent the GridColumn which is a Telerik component. So ultimately my goal is to encapsulate the TelerikGrid and also its components like the GridColums, GridColumn, so I do not have to copy-paste the same component with its settings from one razor page to another. Is there any way I could achieve this without the need of using the RowTemplate and is this actually even possible? Best regards, Nikita

## Answer

**Hristian Stefanov** answered on 25 Jan 2024

Hi Nikita, I confirm that it is possible to encapsulate the Grid component in your own custom one, making it easy to reuse without using the RowTemplate. I have prepared an example for you in this REPL link. Please run and test it to see the result. This seems to cover the desired configuration. Regards, Hristian Stefanov Progress Telerik

### Response

**Nikita** commented on 26 Jan 2024

Hello Hristian, I took a look at the example and that seems to be the solution I was looking for. Thank you very much! I will check it out and let you know if it works! Thanks for the great support. Best Regards, Nikita

### Response

**Hristian Stefanov** commented on 26 Jan 2024

Hi Nikita, I'm glad to hear that the example looks good to you. Take your time to test it. If you face problems with it, I stand ready to provide further assistance. Kind Regards, Hristian
