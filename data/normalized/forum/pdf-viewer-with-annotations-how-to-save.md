# PDF Viewer with Annotations: How to save

## Question

**Joe** asked on 18 Mar 2025

My bosses like the idea of being able to add the annotations on the PDF Viewer. I pull my files from Azure and they want to mark them up. So, I'll need to save the updated copy back to Azure. How does this work? Do you have an example of how to keep the changes? Do the annotations become part of the PDF File or must I save those off separately in order to reapply them when I view? Or, can I just take the modified bytes and upload them as a new copy of the original file?

## Answer

**Nadezhda Tacheva** answered on 19 Mar 2025

Hi Joel, I see you have submitted a private ticket on the matter where I just responded. I am pasting the response here as well for visibility. The annotations become part of the document but currently, the PDFViewer does not provide an option to detect when an annotation has been added or deleted. I logged the following feature request on your behalf: Expose an annotation changed event I voted for it on your behalf and as a creator, you are automatically subscribed to get status updates. Apart from that, in order to completely achieve your desired scenario, you will also need a way to programmatically get the file with the updated annotations. This feature is tracked by the following item: Add a method to give access to the currently open PDF file. I added your vote to that as well and you may follow it to keep in track with its progress. Regards, Nadezhda Tacheva
