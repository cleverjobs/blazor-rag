# Is it possible to disable the entire TelerikWizard stepper?

## Question

**Ste** asked on 20 Oct 2021

The title is self explanatory. We don't require a stepper. Our wizard could also potentially consist of up to 10 steps, which would make the stepper too chaotic. Is it possible to disable and/or hide the entire stepper somehow? Thanks in advance!

### Response

**Marin Bratanov** commented on 23 Oct 2021

The typical way to hide something is to wrap it in an @if(condition) { <Component> } block so it renders only when you want it to. You can also disable each individual step as well, but I am not sure how good a UX that would provide.

## Answer

**Blazorist** answered on 31 May 2022

It's been a while but maybe it will help someone looking in this forum. /* override telerik styles to hide the stepper and the pager (legend "Step X of Y")*/ .k-wizard-pager { display: none !important; } .k-stepper { display: none !important; } Bye.
