# PdfViewer - start download with custom toolbar tool

## Question

**Kee** asked on 07 Oct 2022

Hello, I started using the PdfViewer component and I like it very much, very easy to use. But I have a small issue, the customer doesn't want a download button with an icon but with the text 'Download'. So I added a custom toolbar tool with a normal button, like the sample in the docs, but how do I then trigger de download action of the PdfViewer? I can of course add my own download logic, but in the component it's already there... Kind regards, Kees Alderliesten

## Answer

**Dimo** answered on 12 Oct 2022

Hello Kees, In this case, the easiest option is to inject button text with CSS: .k-pdf-viewer.k-i-download +.k-button-text::before { content: "Download"; margin-right: . 3em;
} Otherwise you will need to implement separate download logic, as the PDF Viewer does not expose a Download method at this point. Regards, Dimo
