# Signature line doesn't draw correctly when TelerikSignature dimensions are larger

## Question

**Dou** asked on 05 Oct 2023

If you use the Blazor repl link below and make the dimensions of the signature pad relatively large and you draw two lines in quick succession it sometimes doesn't draw the second line correctly. For example, if I make the width 1000px and the height 400px (or more) and attempt to use my mouse to write my own name which starts with a D, I can draw the vertical line first and if I draw the curved line to complete the D too quickly it will sometimes draw a straight line from start to finish rather than following the curve that I made with the mouse. It's like there's some sort of lag occurring before you can draw a second line. If I wait a couple seconds before drawing the second line it works. The larger you make the signature pad the more pronounced this issue is. You can also see this if you use your mouse to draw several random lines in quick succession. When the dimensions are smaller, say 500px x 200px it mostly works okay, but if I have a user running a big ipad pro then having to limit the signature pad size like that isn't going to work very well. Is there any way to resolve this? [https://blazorrepl.telerik.com/QnYKEGvE34EIrAdC04?_ga=2.93311705.595058249.1696447250-1661447875.1621547203&_gl=1*1yfgby6*_ga*MTY2MTQ0Nzg3NS4xNjIxNTQ3MjAz*_ga_9JSNBCSF54*MTY5NjU0MTk5Ni4yOTQuMC4xNjk2NTQxOTk2LjYwLjAuMA..](https://blazorrepl.telerik.com/QnYKEGvE34EIrAdC04?_ga=2.93311705.595058249.1696447250-1661447875.1621547203&_gl=1*1yfgby6*_ga*MTY2MTQ0Nzg3NS4xNjIxNTQ3MjAz*_ga_9JSNBCSF54*MTY5NjU0MTk5Ni4yOTQuMC4xNjk2NTQxOTk2LjYwLjAuMA..)

## Answer

**Dimo** answered on 10 Oct 2023

Hi Doug, The Signature Value is a base64 string, which will become very large when the component dimensions are large too. As a result, it takes more time for this string to be sent from the client to the .NET runtime, especially in server apps. Set a larger DebounceDelay value to make client-server requests less frequent. This should mitigate the problem. Regards, Dimo Progress Telerik

### Response

**Doug** commented on 16 Oct 2023

Dimo, Thanks for your response. I'm using Blazor Wasm so no trips to the server but I've continued to play around with this and while increasing the debounce delay does help (tried 500ms, 1000ms, 5000ms), it doesn't completely solve the problem. If you draw a second line at just the right time it will still show a straight line from start to end rather than the curved line you made with the mouse or your finger. I've been evaluating another signature control which I will have to pay for if we can't find a solution with the Telerik signature, but based on your comments above I confirmed that they are also returning a base64 string and when I evaluate the size of the strings between the two controls for similar signatures, their string is less than half the size of the Telerik signature string. So my question is, why is the Telerik signature image string so large? Seems like that may be the crux of the issue here.

### Response

**Dimo** commented on 17 Oct 2023

Our Signature component sets ExportScale to 2 by default. Apart from the component Width and Height, the export scale is the other significant parameter, which affects the Value size. If you don't need high precision and large dimensions of the saved signature image, reduce the ExportScale to 1 or even less than 1. REPL example: Comparing the effect of Signature ExportScale

### Response

**Doug** answered on 17 Oct 2023

Thanks for your suggestions, Dimo. I think I've got it working now. I'm going to write this as an answer for the benefit of someone else who might come across this in the future. For ExportScale, I'm shrinking it down after the user signs so I don't need it to be high resolution and I've got it set to 0.2. That drastically shrinks the size of the image string. For DebounceDelay, rather than setting that to a larger value, I've found that setting it to a smaller value (like 50ms) works best as long as I've also got ExportScale set to a small value. With both of those properties set to small values the issue seems to be resolved. The issue seems to occur when you have the debounce delay set to a time long enough to where the user could start drawing a new line at about the time when the debounce delay hits. So for example if the debounce delay is set to 1000ms, if you complete a line and then wait one second and start drawing a new line, then you hit this issue. With a debounce delay of only 50ms along with a small image size, the user can't start a new line quick enough to beat the image string update. So that works for my use case but if someone were to need a higher resolution signature with relatively large height and width then another solution will be necessary. But I'm moving forward so thanks again for your help.

### Response

**Dimo** commented on 17 Oct 2023

Thanks for the follow-up, Doug! I am happy to find out the component performance meets your requirements now.
