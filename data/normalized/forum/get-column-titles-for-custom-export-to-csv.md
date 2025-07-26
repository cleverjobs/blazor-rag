# Get column titles for custom export to CSV

## Question

**Adr** asked on 06 Sep 2021

Hi, I am trying to implement a custom CSV export for a Telerik Blazor Grid. I want to be able to build up my CSV file manually so can't use the out of the box exporting solutions that the grids currently have. I want to be able to generate the CSV header row and I want to be able to use the column header titles as they are displayed to the user. This information doesn't appear to be exposed in the grid API. I have found this article: [https://docs.telerik.com/blazor-ui/components/grid/state?_ga=2.72679824.2042974694.1630916775-1170839967.1533657392#get-current-columns-visibility-order-field](https://docs.telerik.com/blazor-ui/components/grid/state?_ga=2.72679824.2042974694.1630916775-1170839967.1533657392#get-current-columns-visibility-order-field) which shows that you can get a list of current column states but it doesn't look like you can get the properties of the column e.g. fieldName, columnHeaderTitle etc. The linked article seems to suggest that: This example also shows a workaround for getting the Field of the column that will be availale in a future release as part of the column state Are there any updates on what release this will be available in and whether it will include more column properties like Title ? Thanks.

## Answer

**Marin Bratanov** answered on 06 Sep 2021

Hello Adrian, First things first, please give the built-in CSV export a chance, as it literally requires 1 line of markup from you: [https://docs.telerik.com/blazor-ui/components/grid/export/csv.](https://docs.telerik.com/blazor-ui/components/grid/export/csv.) To know when extra features (Field and Id) get added to the state, click the Follow button here: [https://feedback.telerik.com/blazor/1489571-add-field-and-id-property-in-grid-s-columnstate.](https://feedback.telerik.com/blazor/1489571-add-field-and-id-property-in-grid-s-columnstate.) The feedback portal is the place to get such notifications. I've added your Vote to this request on your behalf too, and you can also do this on your own by clicking the Vote button on items that interest you or you need. Our management tracks this interest when prioritizing and planning. As for the Title - this is not going to be part of the state. It is not something the end user can control and as such it does not belong in the grid state. It is a string the developer configures, and it can be localizable, and it can depend on a great many things. It can also change from one page load to the next if a new version of the app is deployed, even if nothing else changes. This is one more reason why such volatile content cannot be added there. That said, other option for generating things on your own are: Use the approach from this thread: [https://feedback.telerik.com/blazor/1485764-customize-the-excel-file-before-it-gets-to-the-client.](https://feedback.telerik.com/blazor/1485764-customize-the-excel-file-before-it-gets-to-the-client.) You can use the same approach to generate any desired format. You may also want to Vote for and Follow this feature, as it would let you get the file we generate so you can use it as base for your manipulations, thereby reducing work you have to do. Consider mapping columns to their titles in a fashion similar to the article you found - you can maintain some form of relationship for them in your own code to use for the file generation. You can even generate the columns in a loop based on a descriptor class of yours that you can give the backend together with the data to generate the columns over (basically, add the sample from the docs to the thread in the previous bullet). You can find a similar loop here: [https://feedback.telerik.com/blazor/1450105-column-chooser](https://feedback.telerik.com/blazor/1450105-column-chooser) Regards, Marin Bratanov Progress Telerik

### Response

**Aleksandr** commented on 06 May 2023

basically we need access to title, we mostly use jquery & have ability to namage grid layout as a checkbox list of all fields, unfortunately i cant create the same control using blazor because i cant show to the user the title instead of the field, would be great to have it

### Response

**Nadezhda Tacheva** commented on 10 May 2023

Hi Aleksandr, Even though the Title is not part of the state (due to the key points my colleague listed in the above post), you still have a couple of options to set the needed titles to the headers in the custom exported file. Were you able to try the suggestions? Did you face any difficulties while testing them? Apart from that, I'd like to check with you about why it is needed to implement a custom export. Is there any missing functionality of the built-in Grid export that you need? Currently, it is possible to customize the exported file before it reaches the client by handling the exposed export events. You may use our SpreadProcessing or SpreadStreamProcessing libraries to make various modifications.

### Response

**Aleksandr** commented on 10 May 2023

Hello Nadezhda, thx a lot for reply, i dont need it for export, but i need it to implement the functionality similar columns management you have, basically we have it custom for telerik jquery grid & wanted to re-create the same control (UI/UX) for blazor, the part of this control is a columns list, this is where i need titile to show to the user to select visible/hidden for each

### Response

**Nadezhda Tacheva** commented on 11 May 2023

Hi Aleksandr, Thank you for providing details on the use case! In this regard, you may follow this feature request: Standalone ColumnChooser component. Once available, you may use this component in the custom popup. I added your vote to the request to bump its popularity. We prioritize the component enhancements based on the demand and we track the gathered votes to evaluate that. For the time being, you may proceed with one of the approaches Marin suggested.
