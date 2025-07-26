# Hide 'Start' and 'End' labels

## Question

**Doo** asked on 31 Jan 2021

Hi! Is there a way to disable/hide the labels for start and end? I'm having issues fitting this control in another vendor's Form Layout.

## Answer

**Nadezhda Tacheva** answered on 03 Feb 2021

Hi Hassan, You can hide the Start and End labels of the DateRangePicker with some custom CSS. The labels have .k-label class which you can use to access and hide them. To better illustrate how to achieve that, I've created this knowledge base article for hiding the DateRangePicker labels. Speaking of finding elements in the DOM, you might find helpful this article for improving your debugging skills. Regards, Nadezhda Tacheva

### Response

**Hassan** answered on 12 Feb 2021

Thanks for the reply and the dedicated article. I was not able to have the labels hidden though. Is this workaround theme dependent?

### Response

**Nadezhda Tacheva** answered on 15 Feb 2021

Hi Hassan, Generally speaking the theme you are using should not affect the styles that you are additionally applying. One possible reason for the described behavior could be if you are using some other styling that overrides the one responsible for hiding the labels (that could be for example due to a stronger selector). You could try checking what styles are computed on the .k-label element through the debugger tools and investigate where do they come from. If this does not help, you can send us a runnable example where the issue is reproduced, so we can look further and provide a solution. Regards, Nadezhda Tacheva
