# Row click event fires on second click when EditMode = Incell

## Question

**Jef** asked on 01 Dec 2020

Grid is using Incell edit mode. Clicking on a cell brings the cell into focus but it's only on the second click that the OnRowClick event is firing. i.e. when the cell entered edit mode. Is this expected behavior?

## Answer

**Jeffrey** answered on 01 Dec 2020

I figured it out. I had Navigable=true. Switching it to false results in a single click firing the OnRowClick event. Still not sure if that's the intended behavior though.

### Response

**Bozhidar** answered on 03 Dec 2020

Hi, Thank you for reporting this to us. This is indeed a bug in the component - when navigable is true, clicking on a cell should not only focus it, but also raise the event and open the Incell editor. I've fixed the issue in our code, and the fix will be available in our next release, which is expected in the second half of January. Regards, Bozhidar
