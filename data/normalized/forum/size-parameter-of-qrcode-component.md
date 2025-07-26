# Size parameter of QRCode component

## Question

**Kee** asked on 06 Mar 2024

Is it possible to specify the QRcode size in other units than pixels? If I set Size="10vw" then the surrounding div scales correctly, but the inner div has a with and height of 10px, and the QR code is empty. It seems to me that the unit is ignored and only the numbers are used as a size in pixels. Is there a way to make the QR image scalable? Kind regards, Kees Alderliesten

## Answer

**Nadezhda Tacheva** answered on 11 Mar 2024

Hi Kees, The QRCode component uses a drawing <canvas>. Relative sizes with automatic HTML element resizing are not supported and that's why the component requires pixel dimensions. I noticed this is not explicitly listed in our documentation, so I will update it. Please accept my apologies for the inconvenience this missing information might have caused you. To achieve relative sizing for the QRCode component, you may use the same approach as the one listed here: [https://docs.telerik.com/blazor-ui/knowledge-base/signature-relative-width-height.](https://docs.telerik.com/blazor-ui/knowledge-base/signature-relative-width-height.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Kees** commented on 11 Mar 2024

Hi Nadezhda, The QR component doesn't use a drawing canvas, it is just an SVG wrapped in two divs. The SVG has a height and width of 100% and the divs get their height and width from the Size setting. But if I change the pixel sizes in the HTML using the browser's DevTools to a bigger pixel value the SVG doesn't scale with it, despite the 100% setting. It seems that the SVG has a fixed viewbox or something. I did some testing by specifying a class instead of Size/Height/Width parameters and then it becomes more strange. Specifying this CSS class seems to work: .qrcode { width: 10vw; height: 10vw;
} <TelerikQRCode Value="@QrCode" Class="qrcode" /> But if I resize the browser the outer div scales correctly, but the inner div and QR don't change. In my project, the QR changes every 30 seconds and when it refreshes then it scales to the new size. Looking at the rendered HTML it seems that the specified relative size from my CSS class is calculated to pixel values and then applied to the div and SVG. IFAIK does the 'S' in SVG stand for 'scaleable', so, why make it fixed? Kind regards, Kees Alderliesten

### Response

**Nadezhda Tacheva** commented on 14 Mar 2024

Hi Kees, Let me provide some clarification as I was not specific enough in my previous response. The QRCode does not always use <canvas> but this is one of the options it provides. One can control the rendering mode through the RenderAs parameter - the QRCode supports both SVG and Canvas. To cover both options, we accept pixels for the Size, Width and Height parameters as the width and height of the <canvas> HTML element accept pixels. I agree that in some scenarios it may be useful if one can set a relative size to the QRCode and I believe we can enhance the component in this regard. I can open a feature request on your behalf and for that purpose, I want to gather as much information as possible for the use case. Тhus we can ensure there will be no mismatch between the exact requirement and the functionality we deliver. Please share more details on the following: Description Define the user problem and what you need to solve. Use Cases Define the application scenarios that need to be covered. For example, you need to scale the QRCode size upon browser resize, when displayed on different screens or else. Describe the solution you'd like In your initial post, the first question targets the possibility of specifying the QRcode size in other units than pixels. Are you referring to the various available relative units or do you explicitly need vw and vh? If you are able to set a relative size (let's say vw/vh or percent) but we then calculate that internally and translate it to pixels, will that be an issue or it will suffice to achieve the desired behavior? When you resize the browser or the container, the QRCode is not automatically redrawn. If you are able to set relative size, would you expect the QRCode to be automatically redrawn to the respective new size or would you prefer to force it to redraw through the Refresh method (in a similar fashion to how the responsive Chart behavior is achieved here )? List any other aspects or key points to the solution you are looking for. Implementation proposal Any additional suggestions you may have for the implementation.
