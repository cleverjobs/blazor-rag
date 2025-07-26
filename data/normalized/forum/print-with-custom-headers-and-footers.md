# Print with custom headers and footers

## Question

**Val** asked on 26 Jul 2023

Hello, The PDF Viewer provides a Print method. Is it possible to print with custom headers and footers? Kind regards,

### Response

**Nadezhda Tacheva** commented on 31 Jul 2023

Hi Valeriy, By design, the print method will target the document that is visualized in the PDF component. Generally speaking, it is possible to create a custom tool that you can use to invoke the browser print and target the desired elements from the DOM for printing. Similar to this approach for printing the whole Grid, for example: [https://github.com/telerik/blazor-ui/blob/8892d4f84331246bc2086be9806265a5b50eb6eb/grid/print/Pages/PrintWholeGrid.razor.](https://github.com/telerik/blazor-ui/blob/8892d4f84331246bc2086be9806265a5b50eb6eb/grid/print/Pages/PrintWholeGrid.razor.) At this stage, however, it is not clear what kind of custom headers and footers you are referring to, so it will be useful if you can share some more details on the specific use case. Are these elements part of the document? How are they added?

### Response

**Valeriy** commented on 31 Jul 2023

Hi Nadezhda, Currently, the text ‘about:blank’ appears in both the header and footer. Can any text be passed programmatically?

### Response

**Nadezhda Tacheva** commented on 03 Aug 2023

Hi Valeriy, Thank you for getting back to me! I now understand your concern. The print method of the PDFViewer opens the browser print dialog and these header and footer are controlled from there. Based on my research, it looks like this "about:blank" text is set to the URL of the page being printed. So, when the page you are printing does not have a URL, this text is displayed. The browser window offers an option to hide the headers and footers. In Chrome, for example, you can find it under the "More settings" menu: However, I was not able to find an option to customize this text.
