# Grid export of hidden columns

## Question

**Mar** asked on 04 Oct 2021

I have hidden some columns using the code <GridColumn Field="@nameof(DataEntryExternalUser.Name)" Editable="true" Visible="@IsVisible" /> So when I edit in a pop-up form I set IsVisible=true; The problem I have now is with exporting data. Only the visible columns is exported. Can I somehow set IsVisible=true before triggering the export command? Have tried setting it in the OnClick handler. Not working. <GridCommandButton OnClick="@ShowLoadingSign" Command="ExcelExport" Icon="file-excel"> Export to Excel </GridCommandButton>

## Answer

**Marin Bratanov** answered on 06 Oct 2021

Hello Martin, You can Follow the implementation of such functionality here: [https://feedback.telerik.com/blazor/1479440-blazor-grid-export-columns-only-visible-for-export.](https://feedback.telerik.com/blazor/1479440-blazor-grid-export-columns-only-visible-for-export.) P.S.: I've also fixed the typo in the thread title and removed that bit from your post. Regards, Marin Bratanov

### Response

**Martin Herløv** commented on 07 Oct 2021

Good morning. Thanks for fixing my typos. I have been thinking! What about adding an overload of the export command. Giving it a collection of ColumnDescriptors?

### Response

**Marin Bratanov** commented on 07 Oct 2021

Feel free to post that as a comment in the portal for everyone's review. At this point I can't say exactly how this will be implemented, a proper research needs to be done first.
