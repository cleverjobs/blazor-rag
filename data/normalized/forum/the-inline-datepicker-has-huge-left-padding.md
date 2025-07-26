# The inline DatePicker has huge left padding

## Question

**Rol** asked on 03 Aug 2020

See the attached image. How do I suppress the padding/margin/whatever? I can't see the classes used because the picker disapperas as soon as you click outside the cell.

## Answer

**Svetoslav Dimitrov** answered on 04 Aug 2020

Hello Roland, From what I can see you probably have some custom CSS rules in your project which might override the ones we have set up and thus the unwanted UI behavior. Could you provide a runnable sample project so we can investigate the origin of the issue? To isolate the issue easier you can read this article. Also, you can check out this article regarding ways to improve the debugging skill with Chrome DevTools. Regards, Svetoslav Dimitrov

### Response

**Roland** answered on 04 Aug 2020

>you probably have some custom CSS rules in your project No, I think it is the combined 32px left padding of your k-picker-wrap and k-dateinput-wrap styles that I somehow cannot override.

### Response

**Svetoslav Dimitrov** answered on 05 Aug 2020

Hello Roland, As attached file you can a demo project which has a Grid with Inline Editing and a DateTime field, which by default will be edited with DatePicker. It seems that locally, for me, there is no padding so could you compare that project against yours and see if any difference cause the issue. If that does not help, could you modify the project so that the padding is reproduced and we can further investigate the issue? Regards, Svetoslav Dimitrov

### Response

**Roland** answered on 05 Aug 2020

I will have to put this on the backburner. Too busy with deadlines :). I switched to DateInput instead of DatePicker for simple inline dates, so at the moment this extra padding is not a problem for me. But when I have more time available I will dive into this. I do want to know what is going on behind the scenes. The probable outcome will be that my CSS is a mess...
