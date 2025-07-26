# DialogFactory with custom content

## Question

**Mar** asked on 12 Dec 2024

I urgently need an awaitable dialog with custom content. I am working with a DataGrid, and in the on-save event, I need to validate some data. In certain cases, I must display a dialog that allows the user to decide whether to save or cancel the update, based on data retrieved from the API. Is it possible to "hack" the DialogFactory to achieve this? Radzen can do it? [https://blazor.radzen.com/dialog?theme=material3](https://blazor.radzen.com/dialog?theme=material3)

## Answer

**Dimo** answered on 12 Dec 2024

Hi Martin, I can suggest an approach without DialogFactory and with a custom Grid Save command. In terms of UX it should be the same. Custom confirmation Dialog during Grid editing Regards, Dimo Progress Telerik

### Response

**Martin Herløv** commented on 13 Dec 2024

I thank you for the solution, I will use it, but it isn't nice. Lots of moving parts, and code all over. var res=await DialogFactory.ShowDialog<MyDialogComponent>(); So, so much nicer
