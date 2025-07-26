# Tabstrips for Blazor

## Question

**Gar** asked on 27 Feb 2025

I'm using a collection of tabs to display PDF files. For example, I have two tabs open and the current document is scrolled to about mid document. Now I add a new document in a new tab. The new document and all others will scroll to the same spot as the previously active tab. I'd like to retain the position of documents in any open tabs while having the document in the new tab open to the top of the first page. If I have multiple tabs open and documents scrolled to various positions they do not change simply switching from tab to tab. The change only occurs when adding a new tab.

### Response

**Anislav** commented on 28 Feb 2025

Could you please provide more details about your setup? Do you have a separate PDF Viewer for each tab, like this? <TelerikTabStrip>
@foreach ( var doc in Documents)
{
<TabStripTab Title="@doc.Title">
<TelerikPdfViewer @key="doc.Id" Data="@doc.Data" />
</TabStripTab>
}
</TelerikTabStrip>

### Response

**Gary** commented on 28 Feb 2025

Yes very similar to that, but we're using PDFSharp instead of the TelerikPdfViewer. Telerik does not support some PDF features we need.

### Response

**Anislav** commented on 28 Feb 2025

I am not very familiar with PDFSharp, so I looked it up. It seems that it does not provide a native Blazor component. Achieving what you want might not be straightforward. You will likely need to store the scroll position of each PDF document before switching tabs. Then, when navigating back to a tab, you would retrieve and apply the saved scroll position to the PDFSharp viewer. These interactions may require using Blazor JavaScript Interoperability (JS interop) to track and restore the scroll positions effectively.

### Response

**Gary** commented on 28 Feb 2025

Just switching tabs it is fine. It's only when you add a new tab with a new document it makes all others scroll to position of last active tab. I believe this is because the tabstrip re-renders everything when a new tab is created.

## Answer

**Anislav** answered on 28 Feb 2025

The TabStrip loads a tab's content only when activated and removes it when deactivated. To keep content in the DOM even when inactive, set the PersistContent parameter to true. This hides inactive content with CSS instead of disposing of it, resolving your issue with dynamically added tabs. I prepared an example with a viewer component that logs to the console on initialization: [https://blazorrepl.telerik.com/czaQGCwG11ODPAWx42.](https://blazorrepl.telerik.com/czaQGCwG11ODPAWx42.) It demonstrates how PersistContent ensures dynamically added tabs retain their content without re-initialization. Regards, Anislav Atanasov

### Response

**Anislav** commented on 24 Mar 2025

@Gary, did the suggested solution resolve your issue?

### Response

**Gary** commented on 24 Mar 2025

No, we were already using the persist option. It appears when a new tab is created a refresh is executed for all of the tabs and that was the root of the issue. We resolved it by using bootstrap tabs instead of the Telerik Tabstrip.
