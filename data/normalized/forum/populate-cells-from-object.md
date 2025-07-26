# Populate cells from object[][]

## Question

**Rém** asked on 21 May 2020

Hi, I don't know how my data are organised, I can't create a class about it (this is CSV file import, any kind of file) I want to display this is a grid. <TelerikGrid Data="@datable.rows" <GridColumns> @{ for ( int i=0; i <datable.columns.Count; i++) { <GridColumn Field="@(i.ToString())"> <Template> @(((QFLib.DataRow)context)[i].ToString()) // How to evaluate i here ? </Template> </GridColumn> } } </GridColumns> </TelerikGrid> It doens't work because the template during code generation doesn't evaluate i Is it possible ? Another way of doing this ? Sincerely, Remi

## Answer

**Svetoslav Dimitrov** answered on 22 May 2020

Hello Remi, On our Feedback Portal there is a Feature Request (link: [https://feedback.telerik.com/blazor/1418456-bind-to-datatable](https://feedback.telerik.com/blazor/1418456-bind-to-datatable) ) regarding binding the Grid to a DataTable, which is scheduled for our 2.15.0 (next) release. I have added a Vote on your behalf. You can Follow the thread to receive email notification when the release is live and the feature is available. Regards, Svetoslav Dimitrov
