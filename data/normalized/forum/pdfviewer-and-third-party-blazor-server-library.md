# PDFViewer and third party blazor server library

## Question

**Djo** asked on 27 Mar 2025

I would like to use Telerik PDFViewer along with other blazor components librarly but when I incorporate PDF Viewer into my page I have problem with missing buttons and format of PDF viewer toolbar. Viewer display PDF document but toolbar does not work. What to do to activate PDF Toolbar? Obviously I missed something.

## Answer

**Dimo** answered on 28 Mar 2025

Hello Djordje, The Telerik CSS theme appears to be missing. Please revisit the links below and make sure the URL in the <link> tag is correct: Adding a CSS theme @Workflow Details Using a Telerik CSS theme Regards, Dimo

### Response

**Anislav** answered on 27 Mar 2025

Hi, It looks like the icons are not loading in the PDF Viewer toolbar. This issue might be related to missing font icons. You can check this Telerik knowledge base article for possible solution: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/font-icons-not-rendering.](https://www.telerik.com/blazor-ui/documentation/knowledge-base/font-icons-not-rendering.) Regards, Anislav Atanasov
