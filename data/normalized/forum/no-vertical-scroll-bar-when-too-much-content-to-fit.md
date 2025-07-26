# No vertical scroll bar when too much content to fit

## Question

**ran** asked on 01 Nov 2020

We have 2 different instances of Window: Editor Details Editor always has too much content to show and Windows automatically adds a vertical scroll bar. Editor's content is a number of Telerik controls "statically" defined in the Razor. We also define a height and width. Details is mostly a <table> with rows built from a foreach loop. We don't specify a Height or Width. Sometimes there's too many rows to fit in the dialog given the browser or screen size. Details does not display a vertical scroll bar when there is too much content so much of it is hidden. How can we get the vertical scroll bar on the Details instance described above?

## Answer

**Lachezar Georgiev** answered on 02 Nov 2020

Hello Randy, As far as I understand there is a problem with a vertical scroll bar not showing. Can you send me a project, so I can investigate the issue and provide you further information? Regards, Lachezar Georgiev

### Response

**randy** answered on 03 Nov 2020

Solved. Specify Height (and Width?) and you get the scroll bar.

### Response

**Lachezar Georgiev** answered on 03 Nov 2020

Hi Randy, I'm glad you resolved the issue. Regards, Lachezar Georgiev

### Response

**Ted** commented on 31 Oct 2023

So how was this fixed exactly? We want the Telerik Form to show a vertical scroll bar if the content in the form overflows the form height.

### Response

**Radko** answered on 01 Nov 2023

Hello Ted, To achieve what you are after, you should set such a height to the form which is not large enough to fit all the editors within it. For the vertical scroll bar to appear, you can set the overflow-y property to scroll. Lastly, this should be practically valid for any block elements, not just our form. Please have a look at the following example: [https://blazorrepl.telerik.com/GxlPubkh43PpeyWQ03](https://blazorrepl.telerik.com/GxlPubkh43PpeyWQ03) Regards, Radko Progress Telerik
