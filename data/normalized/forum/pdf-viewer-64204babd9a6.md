# Pdf Viewer

## Question

**Gra** asked on 09 Sep 2019

Hi, Is a PDf Viewer on the roadmap for the Blazor SDK? If so will a thumbnail viewer be included? Regards, Graham

## Answer

**Marin Bratanov** answered on 09 Sep 2019

Hi Graham, You can Follow the following page for a PDF viewer and processing tools (I believe you have already found it, but I have to make sure): [https://feedback.telerik.com/blazor/1404008-my-staff-loved-your-radpdfviewer-and-radpdfprocessing-for-silverlight-i-m-hoping-to-see-these-controls-or-the-same-feature-sets-become-available-for-client-side-blazor.](https://feedback.telerik.com/blazor/1404008-my-staff-loved-your-radpdfviewer-and-radpdfprocessing-for-silverlight-i-m-hoping-to-see-these-controls-or-the-same-feature-sets-become-available-for-client-side-blazor.) The PDF viewer itself is not yet on the roadmap, but we do take community feedback actively in our plans, so it may soon show up there. At the moment, we are focusing the gird features, and the next big step is a scheduler. In the meantime, you can consider adding Kendo widgets to fill in such gaps: [https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor.](https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor.) As for a thumbnail viewer - could you provide some more details on what you would want from such a component? Would a listview suffice so you can add whatever content you wish in its items? We do not have another such component in our web suites, so I would need to get a better understanding of what you envision from it. Regards, Marin Bratanov

### Response

**Graham** answered on 09 Sep 2019

Hi, Thanks for the feedback. Viewer/Thumb nails of pages within a document, like the adobe reader viewer. The thumbnails are related to the pages within a document. A viewer displays the active page, the thumbs show the other available pages. Eg. [http://atalasoft-viewer-demo.azurewebsites.net/](http://atalasoft-viewer-demo.azurewebsites.net/) Regards, Graham

### Response

**Marin Bratanov** answered on 09 Sep 2019

Hello Graham, Thank you for clarifying this for me, I had thought that is a separate component, while it is a feature of the pdf viewer. At this point, it's too early to say what features will be available, especially for v1. I would suggest you follow the

### Response

**Michael** answered on 04 Oct 2019

Anyone as a clear tutorial on how to include a PDFViewer in a Blazor app until they come up with a built-in solution?

### Response

**Marin Bratanov** answered on 06 Oct 2019

Hello Michael, You can try using the Kendo UI jQuery widgets as explained here: [https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor.](https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor.) The sample may be a bit dated, but the concepts remain the same. Regards, Marin Bratanov

### Response

**Laura** commented on 30 Apr 2021

Can the jquery-kendo-in-blazor be updated to show how to add a file stream (byte array) contents to the file : data property of the PDF Viewer sample code?

### Response

**Marin Bratanov** commented on 30 Apr 2021

The easiest way to do that right now is to have a controller endpoint that returns the file, and change the URL the pdf viewer uses. If you would like something else to happen, you're more than welcome to open a pull request and ad such an example.
