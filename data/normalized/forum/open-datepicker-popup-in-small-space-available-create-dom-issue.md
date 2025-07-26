# Open DatePicker popup in small space available create dom issue

## Question

**Cla** asked on 07 May 2025

Hi i have a DatePicker in a module form. If i resize the browser window in order to have low visible space below the datepicker, then i open the datepicker popup, it create a strange effect on the page. For example i have this page with a datepicker (highligted in red): if i open the datepicker popup the dom change adding white space on bottom of the page: closing the popup, the white space disappear. How to solve? Thanks

## Answer

**Dimo** answered on 09 May 2025

Hello Claudio, By default, the DatePicker opens downwards. If there is not enough space downwards, the component will open upwards. If there is not enough space upwards either, then the component will open downwards. In all cases, the Calendar popup receives focus, which triggers the browser to perform the so-called scroll into view automatically. I am not aware of a way to prevent this and I also don't think we should prevent scroll into view, because it will create accessibility and usability issues. If you really need to support users with such small screens, then consider these options: Adjust the adaptive breakpoints, so that the adaptive (full-screen) Calendar popup appears on wider screens. Use a Telerik DateInput or a native <input type="date" /> instead of a Telerik DatePicker. Another option is to consider global page scrolling instead of separate container scrolling for the left and right parts. This will make the page layout simpler and allow the page to grow in a better way. Regards, Dimo Progress Telerik
